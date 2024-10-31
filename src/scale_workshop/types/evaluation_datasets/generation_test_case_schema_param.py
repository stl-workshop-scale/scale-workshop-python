# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..shared_params.string_extra_info_schema import StringExtraInfoSchema

__all__ = ["GenerationTestCaseSchemaParam"]


class GenerationTestCaseSchemaParam(TypedDict, total=False):
    input: Required[str]

    expected_extra_info: StringExtraInfoSchema

    expected_output: str
