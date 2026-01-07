# app/models/case.py

from datetime import datetime
from typing import List, Dict, Any
import uuid


class Case:
    """
    Represents a forensic investigation case.
    """

    def __init__(
        self,
        title: str,
        description: str = "",
        created_by: str = "system",
    ):
        self.case_id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.created_by = created_by

        self.status = "open"  # open | closed
        self.created_at = datetime.utcnow().isoformat()

        # List of linked event_ids
        self.events: List[str] = []

    def attach_event(self, event_id: str):
        if event_id not in self.events:
            self.events.append(event_id)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "case_id": self.case_id,
            "title": self.title,
            "description": self.description,
            "created_by": self.created_by,
            "status": self.status,
            "created_at": self.created_at,
            "events": self.events,
        }
