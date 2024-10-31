# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .user_message import UserMessage
from .system_message import SystemMessage
from .assistant_message import AssistantMessage

__all__ = ["ChatMessage"]

ChatMessage: TypeAlias = Union[UserMessage, AssistantMessage, SystemMessage]
