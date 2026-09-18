from fastapi import APIRouter, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

router = APIRouter(prefix="/metrics", tags=["Observability Metrics"])

AGENT_REQUESTS = Counter("ai_agent_requests_total", "Total AI agent invocations", ["domain", "status"])
AGENT_LATENCY = Histogram("ai_agent_latency_seconds", "Latency of AI agent reasoning loops", ["domain"])

@router.get("")
def prometheus_metrics():
    """Export Prometheus telemetry for Grafana monitoring dashboards."""
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
