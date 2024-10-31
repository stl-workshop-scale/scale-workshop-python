# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MyResourceNameMyMethodResponse", "Item", "ItemEvaluationDatasetVersion"]


class ItemEvaluationDatasetVersion(BaseModel):
    id: str
    """The unique identifier of the entity."""

    account_id: str
    """The ID of the account that owns the given entity."""

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    created_by_user_id: str
    """The user who originally created the entity."""

    draft: bool
    """Boolean to check whether or not the evaluation dataset is in draft mode"""

    evaluation_dataset_id: str
    """The ID of the associated evaluation dataset."""

    num: int
    """The version number, automatically incremented on creation"""

    archived_at: Optional[datetime] = None
    """The date and time when the entity was archived in ISO format."""

    published_at: Optional[datetime] = None
    """
    The date and time that all test case results for the evaluation were completed
    for the evaluation in ISO format.
    """


class Item(BaseModel):
    id: str
    """The unique identifier of the entity."""

    account_id: str
    """The ID of the account that owns the given entity."""

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    created_by_user_id: str
    """The user who originally created the entity."""

    name: str
    """The name of the dataset"""

    schema_type: Literal["GENERATION", "FLEXIBLE"]
    """The schema type of the dataset."""

    updated_at: datetime
    """The date and time when the entity was last updated in ISO format."""

    archived_at: Optional[datetime] = None
    """The date and time when the entity was archived in ISO format."""

    evaluation_dataset_versions: Optional[List[ItemEvaluationDatasetVersion]] = None

    knowledge_base_id: Optional[str] = None
    """ID of the knowledge base that the evaluation dataset is associated with."""

    out_of_date: Optional[bool] = None
    """
    Boolean to check whether or not the knowledge base has been uploaded to since
    publication of the dataset.
    """

    schema_sub_type: Optional[Literal["summarization", "translation"]] = None

    vendor: Optional[Literal["scale"]] = None
    """The vendor of the evaluation dataset (e.g.

    'Scale' for Scale off-the-shelf datasets). Null if the evaluation dataset is not
    from a vendor (e.g., is created by the customer).
    """


class MyResourceNameMyMethodResponse(BaseModel):
    current_page: int
    """The current page number."""

    items: List[Item]
    """The data returned for the current page."""

    items_per_page: int
    """The number of items per page."""

    total_item_count: int
    """The total number of items of the query"""