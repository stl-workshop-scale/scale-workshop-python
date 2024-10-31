# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .flexible_test_case_schema_param import FlexibleTestCaseSchemaParam
from .artifact_schema_generation_param import ArtifactSchemaGenerationParam
from .generation_test_case_schema_param import GenerationTestCaseSchemaParam

__all__ = [
    "TestCaseUpdateParams",
    "PartialTestCaseVersionRequest",
    "PartialTestCaseVersionRequestTestCaseData",
    "RestoreRequest",
]


class PartialTestCaseVersionRequest(TypedDict, total=False):
    restore: Required[Literal[False]]
    """Set to true to restore the entity from the database."""

    evaluation_dataset_id: str

    account_id: str

    test_case_data: PartialTestCaseVersionRequestTestCaseData


PartialTestCaseVersionRequestTestCaseData: TypeAlias = Union[
    ArtifactSchemaGenerationParam, GenerationTestCaseSchemaParam, FlexibleTestCaseSchemaParam
]


class RestoreRequest(TypedDict, total=False):
    restore: Required[Literal[True]]
    """Set to true to restore the entity from the database."""

    evaluation_dataset_id: str


TestCaseUpdateParams: TypeAlias = Union[PartialTestCaseVersionRequest, RestoreRequest]
