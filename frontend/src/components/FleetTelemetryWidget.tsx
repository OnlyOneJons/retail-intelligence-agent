import React from 'react';
import { Activity, Server, Zap, Database } from 'lucide-react';

export const FleetTelemetryWidget: React.FC = () => {
  return (
    <aside className="telemetry-sidebar">
      <div className="telemetry-card">
        <div className="telemetry-card-title">
          <Activity size={14} color="#8b5cf6" />
          LangGraph Agent Runtime
        </div>
        <div className="metric-row">
          <span className="metric-label">Graph State</span>
          <span className="metric-value" style={{ color: '#10b981' }}>COMPILED</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Checkpointer</span>
          <span className="metric-value">MemorySaver</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">LLM Provider</span>
          <span className="metric-value" style={{ color: '#06b6d4' }}>Atlas / OpenAI</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Langfuse Tracing</span>
          <span className="metric-value" style={{ color: '#10b981' }}>ACTIVE</span>
        </div>
      </div>

      <div className="telemetry-card">
        <div className="telemetry-card-title">
          <Database size={14} color="#06b6d4" />
          OmniCore Stock Signal
        </div>
        <div className="metric-row">
          <span className="metric-label">Reserved SKU Qty</span>
          <span className="metric-value">1,420 units</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Velocity / Min</span>
          <span className="metric-value" style={{ color: '#f59e0b' }}>15 orders/m</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">RLS Security</span>
          <span className="metric-value" style={{ color: '#10b981' }}>ENFORCED</span>
        </div>
      </div>

      <div className="telemetry-card">
        <div className="telemetry-card-title">
          <Zap size={14} color="#f59e0b" />
          ClearSettle Payments
        </div>
        <div className="metric-row">
          <span className="metric-label">Live Settled GMV</span>
          <span className="metric-value" style={{ color: '#10b981' }}>£4.89M</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">LCR BPS Saved</span>
          <span className="metric-value">+42 bps</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Primary Gateway</span>
          <span className="metric-value">Adyen (98 bps)</span>
        </div>
      </div>

      <div className="telemetry-card">
        <div className="telemetry-card-title">
          <Server size={14} color="#10b981" />
          EdgePulse 500-Store Fleet
        </div>
        <div className="metric-row">
          <span className="metric-label">Fleet Status</span>
          <span className="metric-value">487 / 500 Online</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Vector Clock Drift</span>
          <span className="metric-value" style={{ color: '#10b981' }}>0 ms (CAUSAL)</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">TPM Hardware Enc</span>
          <span className="metric-value">AES-256</span>
        </div>
      </div>
    </aside>
  );
};
