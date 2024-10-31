# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "EvaluationDatasetsTestCaseListResponse",
    "Item",
    "ItemGenerationTestCaseVersionResponse",
    "ItemGenerationTestCaseVersionResponseTestCaseData",
    "ItemGenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGeneration",
    "ItemGenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGenerationExpectedExtraInfo",
    "ItemGenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBase",
    "ItemGenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBaseExpectedExtraInfo",
    "ItemFlexibleTestCaseVersionResponse",
    "ItemFlexibleTestCaseVersionResponseTestCaseData",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember2",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3UserMessage",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3AssistantMessage",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3SystemMessage",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedExtraInfo",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember2",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3UserMessage",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3AssistantMessage",
    "ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3SystemMessage",
]


class ItemGenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGenerationExpectedExtraInfo(BaseModel):
    info: str

    schema_type: Optional[Literal["STRING"]] = None


class ItemGenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGeneration(BaseModel):
    artifact_ids_filter: List[str]

    input: str

    expected_extra_info: Optional[
        ItemGenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGenerationExpectedExtraInfo
    ] = None

    expected_output: Optional[str] = None


class ItemGenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBaseExpectedExtraInfo(BaseModel):
    info: str

    schema_type: Optional[Literal["STRING"]] = None


class ItemGenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBase(BaseModel):
    input: str

    expected_extra_info: Optional[
        ItemGenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBaseExpectedExtraInfo
    ] = None

    expected_output: Optional[str] = None


ItemGenerationTestCaseVersionResponseTestCaseData: TypeAlias = Union[
    ItemGenerationTestCaseVersionResponseTestCaseDataArtifactSchemaGeneration,
    ItemGenerationTestCaseVersionResponseTestCaseDataSchemaGenerationBase,
]


class ItemGenerationTestCaseVersionResponse(BaseModel):
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

    test_case_data: ItemGenerationTestCaseVersionResponseTestCaseData

    archived_at: Optional[datetime] = None
    """The date and time when the entity was archived in ISO format."""

    schema_type: Optional[Literal["GENERATION"]] = None


class ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember2(
    BaseModel
):
    text: str

    metadata: Optional[Dict[str, object]] = None


class ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3UserMessage(
    BaseModel
):
    content: List[str]

    role: Literal["user"]


class ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3AssistantMessage(
    BaseModel
):
    content: List[str]

    role: Literal["assistant"]


class ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3SystemMessage(
    BaseModel
):
    content: List[str]

    role: Literal["system"]


ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3: TypeAlias = Annotated[
    Union[
        ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3UserMessage,
        ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3AssistantMessage,
        ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3SystemMessage,
    ],
    PropertyInfo(discriminator="role"),
]


class ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedExtraInfo(BaseModel):
    info: str

    schema_type: Optional[Literal["STRING"]] = None


class ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember2(
    BaseModel
):
    text: str

    metadata: Optional[Dict[str, object]] = None


class ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3UserMessage(
    BaseModel
):
    content: List[str]

    role: Literal["user"]


class ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3AssistantMessage(
    BaseModel
):
    content: List[str]

    role: Literal["assistant"]


class ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3SystemMessage(
    BaseModel
):
    content: List[str]

    role: Literal["system"]


ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3: TypeAlias = Annotated[
    Union[
        ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3UserMessage,
        ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3AssistantMessage,
        ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3SystemMessage,
    ],
    PropertyInfo(discriminator="role"),
]


class ItemFlexibleTestCaseVersionResponseTestCaseData(BaseModel):
    input: Union[
        str,
        Dict[
            str,
            Union[
                str,
                float,
                List[
                    ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember2
                ],
                List[
                    ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataInputUnionMember1ItemUnionMember3
                ],
            ],
        ],
    ]

    expected_extra_info: Optional[ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedExtraInfo] = None

    expected_output: Union[
        str,
        Dict[
            str,
            Union[
                str,
                float,
                List[
                    ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember2
                ],
                List[
                    ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemFlexibleTestCaseVersionResponseTestCaseDataExpectedOutputUnionMember1ItemUnionMember3
                ],
            ],
        ],
        None,
    ] = None


class ItemFlexibleTestCaseVersionResponse(BaseModel):
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

    test_case_data: ItemFlexibleTestCaseVersionResponseTestCaseData

    archived_at: Optional[datetime] = None
    """The date and time when the entity was archived in ISO format."""

    schema_type: Optional[Literal["FLEXIBLE"]] = None


Item: TypeAlias = Annotated[
    Union[ItemGenerationTestCaseVersionResponse, ItemFlexibleTestCaseVersionResponse],
    PropertyInfo(discriminator="schema_type"),
]


class EvaluationDatasetsTestCaseListResponse(BaseModel):
    current_page: int
    """The current page number."""

    items: List[Item]
    """The data returned for the current page."""

    items_per_page: int
    """The number of items per page."""

    total_item_count: int
    """The total number of items of the query"""