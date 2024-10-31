# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StringExtraInfoSchema"]


class StringExtraInfoSchema(BaseModel):
    info: str

    kind_schema: Optional[Literal["STRING"]] = None
