from enum import Enum
from typing import List

from pydantic import BaseModel


class MessageType(Enum):
    user = "user"
    assistant = "assistant"
    system = "system"


class HistoryRecord(BaseModel):
    type: MessageType
    text: str


class EngineInput(BaseModel):
    history: List[HistoryRecord]
