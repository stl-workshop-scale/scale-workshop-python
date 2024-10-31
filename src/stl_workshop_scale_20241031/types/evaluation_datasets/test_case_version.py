# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "TestCaseVersion",
    "GenerationTestCaseVersionResponse",
    "GenerationTestCaseVersionResponseTestCaseData",
    "GenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGeneration",
    "GenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGenerationExpectedExtraInfo",
    "GenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBase",
    "GenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBaseExpectedExtraInfo",
    "FlexibleTestCaseVersionResponse",
    "FlexibleTestCaseVersionResponseTestCaseData",
    "FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember2",
    "FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3",
    "FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3UserMessage",
    "FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3AssistantMessage",
    "FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3SystemMessage",
    "FlexibleTestCaseVersionResponseTestCaseDataExpectedExtraInfo",
    "FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember2",
    "FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3",
    "FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3UserMessage",
    "FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3AssistantMessage",
    "FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3SystemMessage",
]


class GenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGenerationExpectedExtraInfo(BaseModel):
    info: str

    schema_type: Optional[Literal["STRING"]] = None


class GenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGeneration(BaseModel):
    artifact_ids_filter: List[str]

    input: str

    expected_extra_info: Optional[
        GenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGenerationExpectedExtraInfo
    ] = None

    expected_output: Optional[str] = None


class GenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBaseExpectedExtraInfo(BaseModel):
    info: str

    schema_type: Optional[Literal["STRING"]] = None


class GenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBase(BaseModel):
    input: str

    expected_extra_info: Optional[
        GenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBaseExpectedExtraInfo
    ] = None

    expected_output: Optional[str] = None


GenerationTestCaseVersionResponseTestCaseData: TypeAlias = Union[
    GenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGeneration,
    GenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBase,
]


class GenerationTestCaseVersionResponse(BaseModel):
    id: str
    """The unique identifier of the entity."""

    account_id: str
    """The ID of the account that owns the given entity."""

    autogenerated: bool
    """Boolean to track whether or not the test case is autogenerated"""

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    created_by_user_id: str
    """The user who originally created the entity."""

    evaluation_dataset_id: str
    """The ID of the associated evaluation dataset."""

    test_case_data: GenerationTestCaseVersionResponseTestCaseData

    archived_at: Optional[datetime] = None
    """The date and time when the entity was archived in ISO format."""

    schema_type: Optional[Literal["GENERATION"]] = None


class FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember2(
    BaseModel
):
    text: str

    metadata: Optional[Dict[str, object]] = None


class FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3UserMessage(
    BaseModel
):
    content: List[str]

    role: Literal["user"]


class FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3AssistantMessage(
    BaseModel
):
    content: List[str]

    role: Literal["assistant"]


class FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3SystemMessage(
    BaseModel
):
    content: List[str]

    role: Literal["system"]


FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3: TypeAlias = Annotated[
    Union[
        FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3UserMessage,
        FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3AssistantMessage,
        FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3SystemMessage,
    ],
    PropertyInfo(discriminator="role"),
]


class FlexibleTestCaseVersionResponseTestCaseDataExpectedExtraInfo(BaseModel):
    info: str

    schema_type: Optional[Literal["STRING"]] = None


class FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember2(
    BaseModel
):
    text: str

    metadata: Optional[Dict[str, object]] = None


class FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3UserMessage(
    BaseModel
):
    content: List[str]

    role: Literal["user"]


class FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3AssistantMessage(
    BaseModel
):
    content: List[str]

    role: Literal["assistant"]


class FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3SystemMessage(
    BaseModel
):
    content: List[str]

    role: Literal["system"]


FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3: TypeAlias = Annotated[
    Union[
        FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3UserMessage,
        FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3AssistantMessage,
        FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3SystemMessage,
    ],
    PropertyInfo(discriminator="role"),
]


class FlexibleTestCaseVersionResponseTestCaseData(BaseModel):
    input: Union[
        str,
        Dict[
            str,
            Union[
                str,
                float,
                List[
                    FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember2
                ],
                List[
                    FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3
                ],
            ],
        ],
    ]

    expected_extra_info: Optional[FlexibleTestCaseVersionResponseTestCaseDataExpectedExtraInfo] = None

    expected_output: Union[
        str,
        Dict[
            str,
            Union[
                str,
                float,
                List[
                    FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember2
                ],
                List[
                    FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1FlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3
                ],
            ],
        ],
        None,
    ] = None


class FlexibleTestCaseVersionResponse(BaseModel):
    id: str
    """The unique identifier of the entity."""

    account_id: str
    """The ID of the account that owns the given entity."""

    autogenerated: bool
    """Boolean to track whether or not the test case is autogenerated"""

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    created_by_user_id: str
    """The user who originally created the entity."""

    evaluation_dataset_id: str
    """The ID of the associated evaluation dataset."""

    test_case_data: FlexibleTestCaseVersionResponseTestCaseData

    archived_at: Optional[datetime] = None
    """The date and time when the entity was archived in ISO format."""

    schema_type: Optional[Literal["FLEXIBLE"]] = None


TestCaseVersion: TypeAlias = Annotated[
    Union[GenerationTestCaseVersionResponse, FlexibleTestCaseVersionResponse], PropertyInfo(discriminator="schema_type")
]