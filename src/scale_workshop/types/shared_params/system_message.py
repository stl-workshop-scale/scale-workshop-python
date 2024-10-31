# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SystemMessage"]


class SystemMessage(TypedDict, total=False):
    content: Required[List[str]]

    role: Required[Literal["system"]]
