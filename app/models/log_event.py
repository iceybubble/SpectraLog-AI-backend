from datetime import datetime
from typing import Dict, Literal
from pydantic import BaseModel, Field


class LogEvent(BaseModel):
    device_type: Literal["android"]  # for now only android; we’ll add more later
    device_id: str                   # e.g. "Pixel-6", "Samsung-A52"
    event_type: str                  # e.g. "android_logcat"
    severity: str = Field(default="info")
    message: str                     # the log line
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    details: Dict[str, object] = Field(default_factory=dict)
