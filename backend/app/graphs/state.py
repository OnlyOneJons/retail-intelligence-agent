from typing import Annotated, Sequence, TypedDict, Optional, List, Dict, Any
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    """The state payload shared across all nodes in the LangGraph workflow."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    domain: Optional[str]  # omnicore | clearsettle | edgepulse | general
    tenant_id: Optional[str]
    actions_taken: List[Dict[str, Any]]
    requires_human_approval: bool
    evaluation_score: Optional[float]
