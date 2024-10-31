# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import evaluation_datasets_test_case_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.evaluation_datasets_test_case_list_response import EvaluationDatasetsTestCaseListResponse

__all__ = ["EvaluationDatasetsTestCasesResource", "AsyncEvaluationDatasetsTestCasesResource"]


class EvaluationDatasetsTestCasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationDatasetsTestCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stl-workshop-scale/scale-workshop-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationDatasetsTestCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationDatasetsTestCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stl-workshop-scale/scale-workshop-python#with_streaming_response
        """
        return EvaluationDatasetsTestCasesResourceWithStreamingResponse(self)

    def list(
        self,
        evaluation_dataset_id: str | NotGiven = NOT_GIVEN,
        *,
        account_id: Optional[str] | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetsTestCaseListResponse:
        """
        ### Description

        List all test cases for a selected dataset.

        Args:
          limit: Maximum number of artifacts to be returned by the given endpoint. Defaults to
              100 and cannot be greater than 10k.

          page: Page number for pagination to be returned by the given endpoint. Starts at page
              1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_dataset_id:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_dataset_id` but received {evaluation_dataset_id!r}"
            )
        return self._get(
            f"/v4/evaluation-datasets/{evaluation_dataset_id}/test-cases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "include_archived": include_archived,
                        "limit": limit,
                        "page": page,
                    },
                    evaluation_datasets_test_case_list_params.EvaluationDatasetsTestCaseListParams,
                ),
            ),
            cast_to=EvaluationDatasetsTestCaseListResponse,
        )


class AsyncEvaluationDatasetsTestCasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationDatasetsTestCasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stl-workshop-scale/scale-workshop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationDatasetsTestCasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationDatasetsTestCasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stl-workshop-scale/scale-workshop-python#with_streaming_response
        """
        return AsyncEvaluationDatasetsTestCasesResourceWithStreamingResponse(self)

    async def list(
        self,
        evaluation_dataset_id: str | NotGiven = NOT_GIVEN,
        *,
        account_id: Optional[str] | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetsTestCaseListResponse:
        """
        ### Description

        List all test cases for a selected dataset.

        Args:
          limit: Maximum number of artifacts to be returned by the given endpoint. Defaults to
              100 and cannot be greater than 10k.

          page: Page number for pagination to be returned by the given endpoint. Starts at page
              1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_dataset_id:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_dataset_id` but received {evaluation_dataset_id!r}"
            )
        return await self._get(
            f"/v4/evaluation-datasets/{evaluation_dataset_id}/test-cases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_id": account_id,
                        "include_archived": include_archived,
                        "limit": limit,
                        "page": page,
                    },
                    evaluation_datasets_test_case_list_params.EvaluationDatasetsTestCaseListParams,
                ),
            ),
            cast_to=EvaluationDatasetsTestCaseListResponse,
        )


class EvaluationDatasetsTestCasesResourceWithRawResponse:
    def __init__(self, evaluation_datasets_test_cases: EvaluationDatasetsTestCasesResource) -> None:
        self._evaluation_datasets_test_cases = evaluation_datasets_test_cases

        self.list = to_raw_response_wrapper(
            evaluation_datasets_test_cases.list,
        )


class AsyncEvaluationDatasetsTestCasesResourceWithRawResponse:
    def __init__(self, evaluation_datasets_test_cases: AsyncEvaluationDatasetsTestCasesResource) -> None:
        self._evaluation_datasets_test_cases = evaluation_datasets_test_cases

        self.list = async_to_raw_response_wrapper(
            evaluation_datasets_test_cases.list,
        )


class EvaluationDatasetsTestCasesResourceWithStreamingResponse:
    def __init__(self, evaluation_datasets_test_cases: EvaluationDatasetsTestCasesResource) -> None:
        self._evaluation_datasets_test_cases = evaluation_datasets_test_cases

        self.list = to_streamed_response_wrapper(
            evaluation_datasets_test_cases.list,
        )


class AsyncEvaluationDatasetsTestCasesResourceWithStreamingResponse:
    def __init__(self, evaluation_datasets_test_cases: AsyncEvaluationDatasetsTestCasesResource) -> None:
        self._evaluation_datasets_test_cases = evaluation_datasets_test_cases

        self.list = async_to_streamed_response_wrapper(
            evaluation_datasets_test_cases.list,
        )
