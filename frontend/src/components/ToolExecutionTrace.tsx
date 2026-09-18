import React, { useState } from 'react';
import { Terminal, ChevronDown, ChevronRight, CheckCircle2 } from 'lucide-react';

interface ToolTraceProps {
  toolName: string;
  result: any;
}

export const ToolExecutionTrace: React.FC<ToolTraceProps> = ({ toolName, result }) => {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="tool-trace-container">
      <div className="tool-trace-header" onClick={() => setExpanded(!expanded)}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <Terminal size={13} color="#06b6d4" />
          <span>Executed Tool: <strong style={{ color: '#ffffff' }}>{toolName}</strong></span>
          <CheckCircle2 size={12} color="#10b981" />
        </div>
        {expanded ? <ChevronDown size={14} /> : <ChevronRight size={14} />}
      </div>

      {expanded && (
        <div style={{ marginTop: 8, paddingTop: 8, borderTop: '1px dashed var(--border-subtle)' }}>
          <pre style={{ color: '#94a3b8', fontSize: 11, overflowX: 'auto' }}>
            {typeof result === 'object' ? JSON.stringify(result, null, 2) : result}
          </pre>
        </div>
      )}
    </div>
  );
};
