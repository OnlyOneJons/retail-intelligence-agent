from langchain_core.tools import tool

@tool
def get_clearsettle_gateway_metrics() -> dict:
    """Retrieve live processing volume, current interchange fee basis points (bps), and gateway health from ClearSettle."""
    return {
        "active_acquirers": {
            "Stripe": {"status": "HEALTHY", "latency_ms": 110, "fee_bps": 140, "success_rate": 99.8},
            "Adyen": {"status": "HEALTHY", "latency_ms": 95, "fee_bps": 98, "success_rate": 99.9},
            "Worldpay": {"status": "DEGRADED", "latency_ms": 420, "fee_bps": 115, "success_rate": 94.2},
            "Chase": {"status": "HEALTHY", "latency_ms": 130, "fee_bps": 105, "success_rate": 99.5}
        },
        "total_settled_gmv_gbp": 4892400.00,
        "least_cost_routing_active": True,
        "estimated_bps_saved": 42
    }

@tool
def adjust_least_cost_routing(primary_gateway: str, fallback_gateway: str) -> dict:
    """Adjust dynamic smart payment routing priorities in ClearSettle to optimize fees or handle gateway outages."""
    return {
        "action": "LCR_ADJUSTMENT",
        "primary_gateway": primary_gateway,
        "fallback_gateway": fallback_gateway,
        "routing_policy_id": "POL-2026-LCR-EU",
        "status": "APPLIED_EFFECTIVE_IMMEDIATELY"
    }
