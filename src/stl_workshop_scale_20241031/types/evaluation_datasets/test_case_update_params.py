# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TestCaseUpdateParams",
    "PartialTestCaseVersionRequest",
    "PartialTestCaseVersionRequestTestCaseData",
    "PartialTestCaseVersionRequestTestCaseDataArtifactSchemaGeneration",
    "PartialTestCaseVersionRequestTestCaseDataArtifactSchemaGenerationExpectedExtraInfo",
    "PartialTestCaseVersionRequestTestCaseDataSchemaGenerationBase",
    "PartialTestCaseVersionRequestTestCaseDataSchemaGenerationBaseExpectedExtraInfo",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexible",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember2",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3UserMessage",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3AssistantMessage",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3SystemMessage",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedExtraInfo",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember2",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3UserMessage",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3AssistantMessage",
    "PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3SystemMessage",
    "RestoreRequest",
]


class PartialTestCaseVersionRequest(TypedDict, total=False):
    restore: Required[Literal[False]]
    """Set to true to restore the entity from the database."""

    evaluation_dataset_id: str

    account_id: str

    test_case_data: PartialTestCaseVersionRequestTestCaseData


class PartialTestCaseVersionRequestTestCaseDataArtifactSchemaGenerationExpectedExtraInfo(TypedDict, total=False):
    info: Required[str]

    schema_type: Literal["STRING"]


class PartialTestCaseVersionRequestTestCaseDataArtifactSchemaGeneration(TypedDict, total=False):
    artifact_ids_filter: Required[List[str]]

    input: Required[str]

    expected_extra_info: PartialTestCaseVersionRequestTestCaseDataArtifactSchemaGenerationExpectedExtraInfo

    expected_output: str


class PartialTestCaseVersionRequestTestCaseDataSchemaGenerationBaseExpectedExtraInfo(TypedDict, total=False):
    info: Required[str]

    schema_type: Literal["STRING"]


class PartialTestCaseVersionRequestTestCaseDataSchemaGenerationBase(TypedDict, total=False):
    input: Required[str]

    expected_extra_info: PartialTestCaseVersionRequestTestCaseDataSchemaGenerationBaseExpectedExtraInfo

    expected_output: str


class PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember2(
    TypedDict, total=False
):
    text: Required[str]

    metadata: Dict[str, object]


class PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3UserMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["user"]]


class PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3AssistantMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["assistant"]]


class PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3SystemMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["system"]]


PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3: TypeAlias = Union[
    PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3UserMessage,
    PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3AssistantMessage,
    PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3SystemMessage,
]


class PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedExtraInfo(TypedDict, total=False):
    info: Required[str]

    schema_type: Literal["STRING"]


class PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember2(
    TypedDict, total=False
):
    text: Required[str]

    metadata: Dict[str, object]


class PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3UserMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["user"]]


class PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3AssistantMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["assistant"]]


class PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3SystemMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["system"]]


PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3: TypeAlias = Union[
    PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3UserMessage,
    PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3AssistantMessage,
    PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3SystemMessage,
]


class PartialTestCaseVersionRequestTestCaseDataSchemaFlexible(TypedDict, total=False):
    input: Required[
        Union[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    Iterable[
                        PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember2
                    ],
                    Iterable[
                        PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3
                    ],
                ],
            ],
        ]
    ]

    expected_extra_info: PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedExtraInfo

    expected_output: Union[
        str,
        Dict[
            str,
            Union[
                str,
                float,
                Iterable[
                    PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember2
                ],
                Iterable[
                    PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1PartialTestCaseVersionRequestTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3
                ],
            ],
        ],
    ]


PartialTestCaseVersionRequestTestCaseData: TypeAlias = Union[
    PartialTestCaseVersionRequestTestCaseDataArtifactSchemaGeneration,
    PartialTestCaseVersionRequestTestCaseDataSchemaGenerationBase,
    PartialTestCaseVersionRequestTestCaseDataSchemaFlexible,
]


class RestoreRequest(TypedDict, total=False):
    restore: Required[Literal[True]]
    """Set to true to restore the entity from the database."""

    evaluation_dataset_id: str


TestCaseUpdateParams: TypeAlias = Union[PartialTestCaseVersionRequest, RestoreRequest]
