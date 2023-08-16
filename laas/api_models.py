from enum import Enum
from typing import List

from pydantic import BaseModel


class MessageType(str, Enum):
    user = "user"
    assistant = "assistant"
    system = "system"


class HistoryRecord(BaseModel):
    role: MessageType
    content: str


class EngineInput(BaseModel):
    history: List[HistoryRecord]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "history": [
                        {"role": "system", "content": "You are nice assistant. Be nice."},
                        {"role": "user", "content": "How are you"},
                    ]
                }
            ]
        }
    }
