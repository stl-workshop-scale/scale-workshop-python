# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .user_message import UserMessage
from .system_message import SystemMessage
from .assistant_message import AssistantMessage

__all__ = ["ChatMessage"]

ChatMessage: TypeAlias = Annotated[
    Union[UserMessage, AssistantMessage, SystemMessage], PropertyInfo(discriminator="role")
]
