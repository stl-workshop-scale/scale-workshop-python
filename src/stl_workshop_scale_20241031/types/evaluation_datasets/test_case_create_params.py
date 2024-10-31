# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TestCaseCreateParams",
    "TestCaseData",
    "TestCaseDataArtifactSchemaGeneration",
    "TestCaseDataArtifactSchemaGenerationExpectedExtraInfo",
    "TestCaseDataSchemaGenerationBase",
    "TestCaseDataSchemaGenerationBaseExpectedExtraInfo",
    "TestCaseDataSchemaFlexible",
    "TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember2",
    "TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3",
    "TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3UserMessage",
    "TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3AssistantMessage",
    "TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3SystemMessage",
    "TestCaseDataSchemaFlexibleExpectedExtraInfo",
    "TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember2",
    "TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3",
    "TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3UserMessage",
    "TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3AssistantMessage",
    "TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3SystemMessage",
]


class TestCaseCreateParams(TypedDict, total=False):
    test_case_data: Required[TestCaseData]

    account_id: str


class TestCaseDataArtifactSchemaGenerationExpectedExtraInfo(TypedDict, total=False):
    info: Required[str]

    schema_type: Literal["STRING"]


class TestCaseDataArtifactSchemaGeneration(TypedDict, total=False):
    artifact_ids_filter: Required[List[str]]

    input: Required[str]

    expected_extra_info: TestCaseDataArtifactSchemaGenerationExpectedExtraInfo

    expected_output: str


class TestCaseDataSchemaGenerationBaseExpectedExtraInfo(TypedDict, total=False):
    info: Required[str]

    schema_type: Literal["STRING"]


class TestCaseDataSchemaGenerationBase(TypedDict, total=False):
    input: Required[str]

    expected_extra_info: TestCaseDataSchemaGenerationBaseExpectedExtraInfo

    expected_output: str


class TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember2(
    TypedDict, total=False
):
    text: Required[str]

    metadata: Dict[str, object]


class TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3UserMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["user"]]


class TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3AssistantMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["assistant"]]


class TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3SystemMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["system"]]


TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3: TypeAlias = Union[
    TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3UserMessage,
    TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3AssistantMessage,
    TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3SystemMessage,
]


class TestCaseDataSchemaFlexibleExpectedExtraInfo(TypedDict, total=False):
    info: Required[str]

    schema_type: Literal["STRING"]


class TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember2(
    TypedDict, total=False
):
    text: Required[str]

    metadata: Dict[str, object]


class TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3UserMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["user"]]


class TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3AssistantMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["assistant"]]


class TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3SystemMessage(
    TypedDict, total=False
):
    content: Required[List[str]]

    role: Required[Literal["system"]]


TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3: TypeAlias = Union[
    TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3UserMessage,
    TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3AssistantMessage,
    TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3SystemMessage,
]


class TestCaseDataSchemaFlexible(TypedDict, total=False):
    input: Required[
        Union[
            str,
            Dict[
                str,
                Union[
                    str,
                    float,
                    Iterable[
                        TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember2
                    ],
                    Iterable[
                        TestCaseDataSchemaFlexibleInputUnionMember1TestCaseDataSchemaFlexibleInputUnionMember1ItemUnionMember3
                    ],
                ],
            ],
        ]
    ]

    expected_extra_info: TestCaseDataSchemaFlexibleExpectedExtraInfo

    expected_output: Union[
        str,
        Dict[
            str,
            Union[
                str,
                float,
                Iterable[
                    TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember2
                ],
                Iterable[
                    TestCaseDataSchemaFlexibleExpectedOutputUnionMember1TestCaseDataSchemaFlexibleExpectedOutputUnionMember1ItemUnionMember3
                ],
            ],
        ],
    ]


TestCaseData: TypeAlias = Union[
    TestCaseDataArtifactSchemaGeneration, TestCaseDataSchemaGenerationBase, TestCaseDataSchemaFlexible
]
