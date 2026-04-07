from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class LogSource(str, Enum):
    WINDOWS = "windows"
    ANDROID = "android"
    SERVER = "server"
    IOT = "iot"
    CLOUD = "cloud"


class LogSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class Log(BaseModel):
    id: str
    timestamp: str
    source: LogSource
    severity: LogSeverity
    event_type: str
    message: str
    device_id: Optional[str] = None
    user: Optional[str] = None
    ip_address: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class LogSearchBody(BaseModel):
    query: Optional[str] = None
    filters: Optional[Dict[str, Any]] = None
    limit: int = Field(default=20, ge=1, le=1000)
    offset: int = Field(default=0, ge=0)


class AlertSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AlertStatus(str, Enum):
    OPEN = "open"
    ACKNOWLEDGED = "acknowledged"
    INVESTIGATING = "investigating"
    RESOLVED = "resolved"


# Response Models
class PaginatedResponse(BaseModel):
    items: List[Any]
    total: int
    page: int
    size: int
    pages: int


class TimelineEvent(BaseModel):
    timestamp: str
    device: str
    event: str
    severity: int = Field(ge=1, le=4)
    source: str
    details: Optional[str] = None


class XAIFeature(BaseModel):
    name: str
    value: Any
    impact: float = Field(ge=-1.0, le=1.0)
    explanation: str


class XAIExplanation(BaseModel):
    alert_id: str
    model: str
    features: List[XAIFeature]
    confidence: float = Field(ge=0.0, le=1.0)
    reasoning: str


class CorrelationNode(BaseModel):
    id: str
    type: str
    label: str
    risk_score: Optional[float] = None


class CorrelationEdge(BaseModel):
    source: str
    target: str
    relationship: str
    weight: Optional[float] = None


class CorrelationGraph(BaseModel):
    nodes: List[CorrelationNode]
    edges: List[CorrelationEdge]


class DashboardMetrics(BaseModel):
    total_logs: int
    total_alerts: int
    critical_alerts: int
    open_investigations: int
    devices_monitored: int
    threat_score: float


class Alert(BaseModel):
    id: str
    timestamp: str
    title: str
    description: str
    severity: AlertSeverity
    status: AlertStatus
    source: str
    related_logs: List[str] = []
    mitre_tactics: Optional[List[str]] = None
    confidence: Optional[float] = None


class AlertUpdate(BaseModel):
    status: AlertStatus