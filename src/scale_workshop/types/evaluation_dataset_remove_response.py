# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["EvaluationDatasetRemoveResponse"]


class EvaluationDatasetRemoveResponse(BaseModel):
    count: int

    success: bool
