# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.chat_message import ChatMessage
from ..shared_params.flexible_chunk import FlexibleChunk
from ..shared_params.string_extra_info_schema import StringExtraInfoSchema

__all__ = ["FlexibleTestCaseSchemaParam"]


class FlexibleTestCaseSchemaParam(TypedDict, total=False):
    input: Required[Union[str, Dict[str, Union[str, float, Iterable[FlexibleChunk], Iterable[ChatMessage]]]]]

    expected_extra_info: StringExtraInfoSchema

    expected_output: Union[str, Dict[str, Union[str, float, Iterable[FlexibleChunk], Iterable[ChatMessage]]]]
