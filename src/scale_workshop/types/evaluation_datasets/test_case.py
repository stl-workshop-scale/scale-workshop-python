# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .flexible_test_case_version import FlexibleTestCaseVersion
from .generation_test_case_version import GenerationTestCaseVersion

__all__ = ["TestCase"]

TestCase: TypeAlias = Annotated[
    Union[GenerationTestCaseVersion, FlexibleTestCaseVersion], PropertyInfo(discriminator="kind_schema")
]
