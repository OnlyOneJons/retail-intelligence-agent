import json
import asyncio
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

from app.graphs.retail_copilot_graph import retail_copilot_app

router = APIRouter(prefix="/chat", tags=["AI Copilot Chat"])

class ChatMessage(BaseModel):
    role: str = Field(..., description="Role of the sender (user, assistant, tool)")
    content: str = Field(..., description="Message content")

class ChatRequest(BaseModel):
    message: str = Field(..., description="User prompt or query for the AI Copilot")
    thread_id: str = Field(default="default-thread", description="Unique session thread ID for checkpointing")
    tenant_id: Optional[str] = Field(default="tenant-omnicore-01", description="Tenant ID context")
    domain: Optional[str] = Field(default="general", description="Target domain: omnicore | clearsettle | edgepulse | general")

class ToolExecutionInfo(BaseModel):
    tool_name: str
    arguments: Dict[str, Any]
    output: Any

class ChatResponse(BaseModel):
    thread_id: str
    response: str
    tools_executed: List[ToolExecutionInfo] = []
    status: str = "success"

@router.post("", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Execute a multi-turn turn in the LangGraph agent state graph."""
    config = {"configurable": {"thread_id": request.thread_id}}
    
    inputs = {
        "messages": [HumanMessage(content=request.message)],
        "domain": request.domain,
        "tenant_id": request.tenant_id,
        "actions_taken": [],
        "requires_human_approval": False,
        "evaluation_score": 0.95
    }

    try:
        final_state = await asyncio.to_thread(retail_copilot_app.invoke, inputs, config=config)
        
        messages = final_state.get("messages", [])
        last_message = messages[-1] if messages else None
        response_text = last_message.content if last_message else "No response generated."
        
        tools_executed = []
        for msg in messages:
            if isinstance(msg, ToolMessage):
                tools_executed.append(ToolExecutionInfo(
                    tool_name=msg.name if hasattr(msg, "name") else "tool",
                    arguments={},
                    output=msg.content
                ))

        return ChatResponse(
            thread_id=request.thread_id,
            response=response_text if isinstance(response_text, str) else str(response_text),
            tools_executed=tools_executed,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent Graph Execution Error: {str(e)}")

@router.post("/stream")
async def chat_stream_endpoint(request: ChatRequest):
    """Stream token chunks and state updates from the LangGraph workflow via SSE."""
    config = {"configurable": {"thread_id": request.thread_id}}
    
    inputs = {
        "messages": [HumanMessage(content=request.message)],
        "domain": request.domain,
        "tenant_id": request.tenant_id,
        "actions_taken": [],
        "requires_human_approval": False,
        "evaluation_score": 0.95
    }

    async def event_generator():
        try:
            # Send initial event
            yield f"data: {json.dumps({'type': 'start', 'thread_id': request.thread_id})}\n\n"
            
            # Stream updates from the compiled graph
            for event in retail_copilot_app.stream(inputs, config=config, stream_mode="values"):
                if "messages" in event and len(event["messages"]) > 0:
                    latest_msg = event["messages"][-1]
                    if isinstance(latest_msg, AIMessage) and latest_msg.content:
                        payload = {
                            "type": "content",
                            "delta": latest_msg.content,
                            "role": "assistant"
                        }
                        yield f"data: {json.dumps(payload)}\n\n"
                    elif isinstance(latest_msg, ToolMessage):
                        payload = {
                            "type": "tool",
                            "tool_name": getattr(latest_msg, "name", "tool"),
                            "result": latest_msg.content
                        }
                        yield f"data: {json.dumps(payload)}\n\n"
            
            yield f"data: {json.dumps({'type': 'done'})}\n\n"
        except Exception as err:
            yield f"data: {json.dumps({'type': 'error', 'message': str(err)})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
