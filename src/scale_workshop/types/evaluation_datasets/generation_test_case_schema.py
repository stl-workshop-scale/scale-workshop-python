# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.string_extra_info_schema import StringExtraInfoSchema

__all__ = ["GenerationTestCaseSchema"]


class GenerationTestCaseSchema(BaseModel):
    input: str

    expected_extra_info: Optional[StringExtraInfoSchema] = None

    expected_output: Optional[str] = None
