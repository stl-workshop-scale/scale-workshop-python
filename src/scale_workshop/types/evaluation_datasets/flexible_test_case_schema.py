# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from ..._models import BaseModel
from ..shared.chat_message import ChatMessage
from ..shared.flexible_chunk import FlexibleChunk
from ..shared.string_extra_info_schema import StringExtraInfoSchema

__all__ = ["FlexibleTestCaseSchema"]


class FlexibleTestCaseSchema(BaseModel):
    input: Union[str, Dict[str, Union[str, float, List[FlexibleChunk], List[ChatMessage]]]]

    expected_extra_info: Optional[StringExtraInfoSchema] = None

    expected_output: Union[str, Dict[str, Union[str, float, List[FlexibleChunk], List[ChatMessage]]], None] = None
