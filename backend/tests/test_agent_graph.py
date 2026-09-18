import pytest
from langchain_core.messages import HumanMessage
from app.graphs.retail_copilot_graph import retail_copilot_app
from app.tools.omnicore_tools import get_omnicore_stock_inventory
from app.tools.clearsettle_tools import get_clearsettle_gateway_metrics
from app.tools.edgepulse_tools import get_edgepulse_fleet_health

def test_omnicore_tool():
    res = get_omnicore_stock_inventory.invoke({"tenant_id": "tenant-1", "sku": "SKU-TEST"})
    assert res["status"] == "HEALTHY"
    assert res["available_stock"] > 0

def test_clearsettle_tool():
    res = get_clearsettle_gateway_metrics.invoke({})
    assert "active_acquirers" in res
    assert res["least_cost_routing_active"] is True

def test_edgepulse_tool():
    res = get_edgepulse_fleet_health.invoke({})
    assert res["fleet_total_stores"] == 500
    assert res["online_stores"] >= 400

def test_langgraph_invocation():
    thread_id = "test-thread-01"
    config = {"configurable": {"thread_id": thread_id}}
    inputs = {
        "messages": [HumanMessage(content="Check OmniCore inventory for SKU-PROMO-12")],
        "domain": "omnicore",
        "tenant_id": "tenant-01",
        "actions_taken": [],
        "requires_human_approval": False,
        "evaluation_score": 1.0
    }
    
    state = retail_copilot_app.invoke(inputs, config=config)
    assert "messages" in state
    assert len(state["messages"]) > 0
