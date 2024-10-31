# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..shared_params.string_extra_info_schema import StringExtraInfoSchema

__all__ = ["ArtifactSchemaGenerationParam"]


class ArtifactSchemaGenerationParam(TypedDict, total=False):
    artifact_ids_filter: Required[List[str]]

    input: Required[str]

    expected_extra_info: StringExtraInfoSchema

    expected_output: str
