from enum import Enum
from typing import List

from pydantic import BaseModel


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"


class EngineInput(BaseModel):
    message: str
