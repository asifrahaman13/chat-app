export interface Interactions {
  question: string;
  answer: string;
}

type SessionData = {
  question: string;
  answer: string;
};

export type Session = {
  session_data: SessionData[];
  id: string;
  session_id: string;
};


export interface SessionStorage {
  id: string;
  session_id: string;
}

export interface CurrentSessionButtonProps {
  onClick: () => void;
}

export interface SessionButtonProps {
  session: SessionStorage;
  onClick: (sessionId: string) => void;
}