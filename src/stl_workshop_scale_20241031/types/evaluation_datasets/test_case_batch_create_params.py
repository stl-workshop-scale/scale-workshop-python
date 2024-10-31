# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TestCaseBatchCreateParams",
    "Body",
    "BodyTestCaseData",
    "BodyTestCaseDataArtifactSchemaGeneration",
    "BodyTestCaseDataArtifactSchemaGenerationExpectedExtraInfo",
    "BodyTestCaseDataSchemaGenerationBase",
    "BodyTestCaseDataSchemaGenerationBaseExpectedExtraInfo",
    "BodyTestCaseDataSchemaFlexible",
    "BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember2",
    "BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3",
    "BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3UserMessage",
    "BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3AssistantMessage",
    "BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3SystemMessage",
    "BodyTestCaseDataSchemaFlexibleExpectedExtraInfo",
    "BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember2",
    "BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3",
    "BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3UserMessage",
    "BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3AssistantMessage",
    "BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3SystemMessage",
]


class TestCaseBatchCreateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyTestCaseDataArtifactSchemaGenerationExpectedExtraInfo(TypedDict, total=False):
    info: Required[str]

    schema_type: Literal["STRING"]


class BodyTestCaseDataArtifactSchemaGeneration(TypedDict, total=False):
    artifact_ids_filter: Required[List[str]]

    input: Required[str]

    expected_extra_info: BodyTestCaseDataArtifactSchemaGenerationExpectedExtraInfo

    expected_output: str


class BodyTestCaseDataSchemaGenerationBaseExpectedExtraInfo(TypedDict, total=False):
    info: Required[str]

    schema_type: Literal["STRING"]


class BodyTestCaseDataSchemaGenerationBase(TypedDict, total=False):
    input: Required[str]

    expected_extra_info: BodyTestCaseDataSchemaGenerationBaseExpectedExtraInfo

    expected_output: str


class BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember2(
    TypedDict, total=False
):
    text: Required[str]

    metadata: Dict[str, object]


class BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3UserMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["user"]]


class BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3AssistantMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["assistant"]]


class BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3SystemMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["system"]]


BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3: TypeAlias = Union[
    BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3UserMessage,
    BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3AssistantMessage,
    BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3SystemMessage,
]


class BodyTestCaseDataSchemaFlexibleExpectedExtraInfo(TypedDict, total=False):
    info: Required[str]

    schema_type: Literal["STRING"]


class BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember2(
    TypedDict, total=False
):
    text: Required[str]

    metadata: Dict[str, object]


class BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3UserMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["user"]]


class BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3AssistantMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["assistant"]]


class BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3SystemMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["system"]]


BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3: TypeAlias = Union[
    BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3UserMessage,
    BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3AssistantMessage,
    BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3SystemMessage,
]


class BodyTestCaseDataSchemaFlexible(TypedDict, total=False):
    input: Required[
        Union[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    Iterable[
                        BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember2
                    ],
                    Iterable[
                        BodyTestCaseDataSchemaFlexibleInputUnionMember1BodyTestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3
                    ],
                ],
            ],
        ]
    ]

    expected_extra_info: BodyTestCaseDataSchemaFlexibleExpectedExtraInfo

    expected_output: Union[
        str,
        Dict[
            str,
            Union[
                str,
                float,
                Iterable[
                    BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember2
                ],
                Iterable[
                    BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1BodyTestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3
                ],
            ],
        ],
    ]


BodyTestCaseData: TypeAlias = Union[
    BodyTestCaseDataArtifactSchemaGeneration, BodyTestCaseDataSchemaGenerationBase, BodyTestCaseDataSchemaFlexible
]


class Body(TypedDict, total=False):
    test_case_data: Required[BodyTestCaseData]

    account_id: str
