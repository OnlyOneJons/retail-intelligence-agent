import React, { useState } from 'react';
import { Bot, ShoppingBag, CreditCard, Radio, Layers, Sparkles } from 'lucide-react';
import { AgentChat } from './components/AgentChat';
import { FleetTelemetryWidget } from './components/FleetTelemetryWidget';

export const App: React.FC = () => {
  const [selectedDomain, setSelectedDomain] = useState<'general' | 'omnicore' | 'clearsettle' | 'edgepulse'>('general');

  return (
    <div className="app-container">
      {/* Left Navigation & Domain Switcher */}
      <nav className="nav-sidebar">
        <div className="brand-header">
          <div className="brand-icon">
            <Bot size={20} />
          </div>
          <div>
            <h1 className="brand-title">Retail Intelligence</h1>
            <span className="brand-badge">FastAPI + LangGraph</span>
          </div>
        </div>

        <div>
          <div className="domain-section-title">Operations Copilots</div>
          <button
            className={`preset-btn ${selectedDomain === 'general' ? 'active' : ''}`}
            onClick={() => setSelectedDomain('general')}
          >
            <Layers size={16} />
            Unified Enterprise Sentinel
          </button>
          <button
            className={`preset-btn ${selectedDomain === 'omnicore' ? 'active' : ''}`}
            onClick={() => setSelectedDomain('omnicore')}
          >
            <ShoppingBag size={16} color="#06b6d4" />
            OmniCore Stock Copilot
          </button>
          <button
            className={`preset-btn ${selectedDomain === 'clearsettle' ? 'active' : ''}`}
            onClick={() => setSelectedDomain('clearsettle')}
          >
            <CreditCard size={16} color="#f59e0b" />
            ClearSettle LCR Advisor
          </button>
          <button
            className={`preset-btn ${selectedDomain === 'edgepulse' ? 'active' : ''}`}
            onClick={() => setSelectedDomain('edgepulse')}
          >
            <Radio size={16} color="#10b981" />
            EdgePulse Fleet Triage
          </button>
        </div>

        <div style={{ marginTop: 'auto', padding: 12, borderRadius: 8, background: 'var(--bg-surface-elevated)', border: '1px solid var(--border-subtle)', fontSize: 11, color: '#64748b' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6, color: '#c4b5fd', fontWeight: 600, marginBottom: 4 }}>
            <Sparkles size={12} />
            Production Template
          </div>
          Stateful LangGraph checkpointer with wire-compatible multi-LLM endpoints & Langfuse tracing.
        </div>
      </nav>

      {/* Main Agent Reasoning & Chat Panel */}
      <AgentChat selectedDomain={selectedDomain} />

      {/* Right Monorepo Telemetry Sidebar */}
      <FleetTelemetryWidget />
    </div>
  );
};

export default App;
