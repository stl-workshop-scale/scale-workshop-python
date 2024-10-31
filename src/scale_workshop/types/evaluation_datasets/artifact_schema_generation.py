# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.string_extra_info_schema import StringExtraInfoSchema

__all__ = ["ArtifactSchemaGeneration"]


class ArtifactSchemaGeneration(BaseModel):
    artifact_ids_filter: List[str]

    input: str

    expected_extra_info: Optional[StringExtraInfoSchema] = None

    expected_output: Optional[str] = None
