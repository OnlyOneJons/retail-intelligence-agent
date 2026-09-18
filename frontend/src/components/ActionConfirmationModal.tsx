import React from 'react';
import { AlertTriangle, Check, X } from 'lucide-react';

interface ModalProps {
  isOpen: boolean;
  actionTitle: string;
  actionDetails: string;
  onConfirm: () => void;
  onCancel: () => void;
}

export const ActionConfirmationModal: React.FC<ModalProps> = ({
  isOpen,
  actionTitle,
  actionDetails,
  onConfirm,
  onCancel
}) => {
  if (!isOpen) return null;

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.75)',
      backdropFilter: 'blur(6px)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 1000
    }}>
      <div style={{
        background: '#0f1422',
        border: '1px solid rgba(245, 158, 11, 0.4)',
        borderRadius: 14,
        padding: 24,
        maxWidth: 480,
        width: '90%',
        boxShadow: '0 0 30px rgba(245, 158, 11, 0.2)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, color: '#f59e0b', marginBottom: 12 }}>
          <AlertTriangle size={20} />
          <h3 style={{ fontSize: 16, fontWeight: 700 }}>Human-in-the-Loop Approval Required</h3>
        </div>

        <p style={{ fontSize: 14, color: '#f8fafc', fontWeight: 600, marginBottom: 8 }}>
          {actionTitle}
        </p>
        <p style={{ fontSize: 13, color: '#94a3b8', lineHeight: 1.5, marginBottom: 20 }}>
          {actionDetails}
        </p>

        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 10 }}>
          <button
            onClick={onCancel}
            style={{
              padding: '8px 16px',
              borderRadius: 8,
              border: '1px solid rgba(255,255,255,0.1)',
              background: 'transparent',
              color: '#94a3b8',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: 6
            }}
          >
            <X size={14} /> Cancel
          </button>
          <button
            onClick={onConfirm}
            style={{
              padding: '8px 16px',
              borderRadius: 8,
              border: 'none',
              background: 'linear-gradient(135deg, #10b981, #06b6d4)',
              color: '#ffffff',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: 6
            }}
          >
            <Check size={14} /> Authorize Action
          </button>
        </div>
      </div>
    </div>
  );
};
