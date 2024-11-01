# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, overload

import httpx

from ...types import (
    evaluation_dataset_list_params,
    evaluation_dataset_update_params,
    evaluation_dataset_publish_params,
    evaluation_dataset_approve_batch_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .test_cases import (
    TestCasesResource,
    AsyncTestCasesResource,
    TestCasesResourceWithRawResponse,
    AsyncTestCasesResourceWithRawResponse,
    TestCasesResourceWithStreamingResponse,
    AsyncTestCasesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPageNumberPage, AsyncPageNumberPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.evaluation_dataset_list_response import EvaluationDatasetListResponse
from ...types.evaluation_dataset_remove_response import EvaluationDatasetRemoveResponse
from ...types.evaluation_dataset_update_response import EvaluationDatasetUpdateResponse
from ...types.evaluation_dataset_publish_response import EvaluationDatasetPublishResponse
from ...types.evaluation_dataset_retrieve_response import EvaluationDatasetRetrieveResponse
from ...types.evaluation_dataset_approve_batch_response import EvaluationDatasetApproveBatchResponse

__all__ = ["EvaluationDatasetsResource", "AsyncEvaluationDatasetsResource"]


class EvaluationDatasetsResource(SyncAPIResource):
    @cached_property
    def test_cases(self) -> TestCasesResource:
        return TestCasesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvaluationDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stl-workshop-scale/scale-workshop-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stl-workshop-scale/scale-workshop-python#with_streaming_response
        """
        return EvaluationDatasetsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        evaluation_dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetRetrieveResponse:
        """
        ### Description

        Gets the details of a dataset.

        Args:
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
            f"/v4/evaluation-datasets/{evaluation_dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationDatasetRetrieveResponse,
        )

    @overload
    def update(
        self,
        evaluation_dataset_id: str,
        *,
        name: str,
        restore: Literal[False],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetUpdateResponse:
        """
        ### Description

        Updates a evaluation dataset

        ### Details

        This API can be used to update the evaluation dataset that matches the ID that
        was passed in as a path parameter. To use this API, pass in the `id` that was
        returned from your Create Evaluation Dataset API call as a path parameter.

        Review the request schema to see the fields that can be updated.

        Args:
          name: The name of the dataset

          restore: Set to true to restore the entity from the database.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        evaluation_dataset_id: str,
        *,
        restore: Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetUpdateResponse:
        """
        ### Description

        Updates a evaluation dataset

        ### Details

        This API can be used to update the evaluation dataset that matches the ID that
        was passed in as a path parameter. To use this API, pass in the `id` that was
        returned from your Create Evaluation Dataset API call as a path parameter.

        Review the request schema to see the fields that can be updated.

        Args:
          restore: Set to true to restore the entity from the database.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "restore"], ["restore"])
    def update(
        self,
        evaluation_dataset_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        restore: Literal[False] | Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetUpdateResponse:
        if not evaluation_dataset_id:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_dataset_id` but received {evaluation_dataset_id!r}"
            )
        return self._patch(
            f"/v4/evaluation-datasets/{evaluation_dataset_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "restore": restore,
                },
                evaluation_dataset_update_params.EvaluationDatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationDatasetUpdateResponse,
        )

    def list(
        self,
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
    ) -> SyncPageNumberPage[EvaluationDatasetListResponse]:
        """
        ### Description

        Lists all evaluation datasets accessible to the user.

        ### Details

        This API can be used to list evaluation datasets. If a user has access to
        multiple accounts, all evaluation datasets from all accounts the user is
        associated with will be returned.

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
        return self._get_api_list(
            "/v4/evaluation-datasets",
            page=SyncPageNumberPage[EvaluationDatasetListResponse],
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
                    evaluation_dataset_list_params.EvaluationDatasetListParams,
                ),
            ),
            model=EvaluationDatasetListResponse,
        )

    def approve_batch(
        self,
        evaluation_dataset_id: str,
        *,
        autogenerated_draft_test_cases: List[str],
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetApproveBatchResponse:
        """
        Approve Auto Generated Test Cases Batch

        Args:
          autogenerated_draft_test_cases: Ids of auto generated draft test cases to be approved.

          force: Force approve a batch of autogenerated test case IDs for the evaluation dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_dataset_id:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_dataset_id` but received {evaluation_dataset_id!r}"
            )
        return self._post(
            f"/v4/evaluation-datasets/{evaluation_dataset_id}/approve-batch",
            body=maybe_transform(
                {"autogenerated_draft_test_cases": autogenerated_draft_test_cases},
                evaluation_dataset_approve_batch_params.EvaluationDatasetApproveBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force": force}, evaluation_dataset_approve_batch_params.EvaluationDatasetApproveBatchParams
                ),
            ),
            cast_to=EvaluationDatasetApproveBatchResponse,
        )

    def publish(
        self,
        evaluation_dataset_id: str,
        *,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetPublishResponse:
        """
        Publish Latest Evaluation Dataset Version

        Args:
          force: Force approve an evaluation dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_dataset_id:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_dataset_id` but received {evaluation_dataset_id!r}"
            )
        return self._post(
            f"/v4/evaluation-datasets/{evaluation_dataset_id}/publish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force": force}, evaluation_dataset_publish_params.EvaluationDatasetPublishParams
                ),
            ),
            cast_to=EvaluationDatasetPublishResponse,
        )

    def remove(
        self,
        evaluation_dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetRemoveResponse:
        """
        ### Description

        Deletes the dataset, and all other entities associated with the dataset, such as
        test cases, evaluations and results.

        ### Details

        **This is a permanent and destructive action that cannot be undone.**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_dataset_id:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_dataset_id` but received {evaluation_dataset_id!r}"
            )
        return self._delete(
            f"/v4/evaluation-datasets/{evaluation_dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationDatasetRemoveResponse,
        )


class AsyncEvaluationDatasetsResource(AsyncAPIResource):
    @cached_property
    def test_cases(self) -> AsyncTestCasesResource:
        return AsyncTestCasesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvaluationDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stl-workshop-scale/scale-workshop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stl-workshop-scale/scale-workshop-python#with_streaming_response
        """
        return AsyncEvaluationDatasetsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        evaluation_dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetRetrieveResponse:
        """
        ### Description

        Gets the details of a dataset.

        Args:
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
            f"/v4/evaluation-datasets/{evaluation_dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationDatasetRetrieveResponse,
        )

    @overload
    async def update(
        self,
        evaluation_dataset_id: str,
        *,
        name: str,
        restore: Literal[False],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetUpdateResponse:
        """
        ### Description

        Updates a evaluation dataset

        ### Details

        This API can be used to update the evaluation dataset that matches the ID that
        was passed in as a path parameter. To use this API, pass in the `id` that was
        returned from your Create Evaluation Dataset API call as a path parameter.

        Review the request schema to see the fields that can be updated.

        Args:
          name: The name of the dataset

          restore: Set to true to restore the entity from the database.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        evaluation_dataset_id: str,
        *,
        restore: Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetUpdateResponse:
        """
        ### Description

        Updates a evaluation dataset

        ### Details

        This API can be used to update the evaluation dataset that matches the ID that
        was passed in as a path parameter. To use this API, pass in the `id` that was
        returned from your Create Evaluation Dataset API call as a path parameter.

        Review the request schema to see the fields that can be updated.

        Args:
          restore: Set to true to restore the entity from the database.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "restore"], ["restore"])
    async def update(
        self,
        evaluation_dataset_id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        restore: Literal[False] | Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetUpdateResponse:
        if not evaluation_dataset_id:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_dataset_id` but received {evaluation_dataset_id!r}"
            )
        return await self._patch(
            f"/v4/evaluation-datasets/{evaluation_dataset_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "restore": restore,
                },
                evaluation_dataset_update_params.EvaluationDatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationDatasetUpdateResponse,
        )

    def list(
        self,
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
    ) -> AsyncPaginator[EvaluationDatasetListResponse, AsyncPageNumberPage[EvaluationDatasetListResponse]]:
        """
        ### Description

        Lists all evaluation datasets accessible to the user.

        ### Details

        This API can be used to list evaluation datasets. If a user has access to
        multiple accounts, all evaluation datasets from all accounts the user is
        associated with will be returned.

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
        return self._get_api_list(
            "/v4/evaluation-datasets",
            page=AsyncPageNumberPage[EvaluationDatasetListResponse],
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
                    evaluation_dataset_list_params.EvaluationDatasetListParams,
                ),
            ),
            model=EvaluationDatasetListResponse,
        )

    async def approve_batch(
        self,
        evaluation_dataset_id: str,
        *,
        autogenerated_draft_test_cases: List[str],
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetApproveBatchResponse:
        """
        Approve Auto Generated Test Cases Batch

        Args:
          autogenerated_draft_test_cases: Ids of auto generated draft test cases to be approved.

          force: Force approve a batch of autogenerated test case IDs for the evaluation dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_dataset_id:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_dataset_id` but received {evaluation_dataset_id!r}"
            )
        return await self._post(
            f"/v4/evaluation-datasets/{evaluation_dataset_id}/approve-batch",
            body=await async_maybe_transform(
                {"autogenerated_draft_test_cases": autogenerated_draft_test_cases},
                evaluation_dataset_approve_batch_params.EvaluationDatasetApproveBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force": force}, evaluation_dataset_approve_batch_params.EvaluationDatasetApproveBatchParams
                ),
            ),
            cast_to=EvaluationDatasetApproveBatchResponse,
        )

    async def publish(
        self,
        evaluation_dataset_id: str,
        *,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetPublishResponse:
        """
        Publish Latest Evaluation Dataset Version

        Args:
          force: Force approve an evaluation dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_dataset_id:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_dataset_id` but received {evaluation_dataset_id!r}"
            )
        return await self._post(
            f"/v4/evaluation-datasets/{evaluation_dataset_id}/publish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force": force}, evaluation_dataset_publish_params.EvaluationDatasetPublishParams
                ),
            ),
            cast_to=EvaluationDatasetPublishResponse,
        )

    async def remove(
        self,
        evaluation_dataset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationDatasetRemoveResponse:
        """
        ### Description

        Deletes the dataset, and all other entities associated with the dataset, such as
        test cases, evaluations and results.

        ### Details

        **This is a permanent and destructive action that cannot be undone.**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_dataset_id:
            raise ValueError(
                f"Expected a non-empty value for `evaluation_dataset_id` but received {evaluation_dataset_id!r}"
            )
        return await self._delete(
            f"/v4/evaluation-datasets/{evaluation_dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationDatasetRemoveResponse,
        )


class EvaluationDatasetsResourceWithRawResponse:
    def __init__(self, evaluation_datasets: EvaluationDatasetsResource) -> None:
        self._evaluation_datasets = evaluation_datasets

        self.retrieve = to_raw_response_wrapper(
            evaluation_datasets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            evaluation_datasets.update,
        )
        self.list = to_raw_response_wrapper(
            evaluation_datasets.list,
        )
        self.approve_batch = to_raw_response_wrapper(
            evaluation_datasets.approve_batch,
        )
        self.publish = to_raw_response_wrapper(
            evaluation_datasets.publish,
        )
        self.remove = to_raw_response_wrapper(
            evaluation_datasets.remove,
        )

    @cached_property
    def test_cases(self) -> TestCasesResourceWithRawResponse:
        return TestCasesResourceWithRawResponse(self._evaluation_datasets.test_cases)


class AsyncEvaluationDatasetsResourceWithRawResponse:
    def __init__(self, evaluation_datasets: AsyncEvaluationDatasetsResource) -> None:
        self._evaluation_datasets = evaluation_datasets

        self.retrieve = async_to_raw_response_wrapper(
            evaluation_datasets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            evaluation_datasets.update,
        )
        self.list = async_to_raw_response_wrapper(
            evaluation_datasets.list,
        )
        self.approve_batch = async_to_raw_response_wrapper(
            evaluation_datasets.approve_batch,
        )
        self.publish = async_to_raw_response_wrapper(
            evaluation_datasets.publish,
        )
        self.remove = async_to_raw_response_wrapper(
            evaluation_datasets.remove,
        )

    @cached_property
    def test_cases(self) -> AsyncTestCasesResourceWithRawResponse:
        return AsyncTestCasesResourceWithRawResponse(self._evaluation_datasets.test_cases)


class EvaluationDatasetsResourceWithStreamingResponse:
    def __init__(self, evaluation_datasets: EvaluationDatasetsResource) -> None:
        self._evaluation_datasets = evaluation_datasets

        self.retrieve = to_streamed_response_wrapper(
            evaluation_datasets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            evaluation_datasets.update,
        )
        self.list = to_streamed_response_wrapper(
            evaluation_datasets.list,
        )
        self.approve_batch = to_streamed_response_wrapper(
            evaluation_datasets.approve_batch,
        )
        self.publish = to_streamed_response_wrapper(
            evaluation_datasets.publish,
        )
        self.remove = to_streamed_response_wrapper(
            evaluation_datasets.remove,
        )

    @cached_property
    def test_cases(self) -> TestCasesResourceWithStreamingResponse:
        return TestCasesResourceWithStreamingResponse(self._evaluation_datasets.test_cases)


class AsyncEvaluationDatasetsResourceWithStreamingResponse:
    def __init__(self, evaluation_datasets: AsyncEvaluationDatasetsResource) -> None:
        self._evaluation_datasets = evaluation_datasets

        self.retrieve = async_to_streamed_response_wrapper(
            evaluation_datasets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            evaluation_datasets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            evaluation_datasets.list,
        )
        self.approve_batch = async_to_streamed_response_wrapper(
            evaluation_datasets.approve_batch,
        )
        self.publish = async_to_streamed_response_wrapper(
            evaluation_datasets.publish,
        )
        self.remove = async_to_streamed_response_wrapper(
            evaluation_datasets.remove,
        )

    @cached_property
    def test_cases(self) -> AsyncTestCasesResourceWithStreamingResponse:
        return AsyncTestCasesResourceWithStreamingResponse(self._evaluation_datasets.test_cases)
