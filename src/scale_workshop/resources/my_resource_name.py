# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import my_resource_name_my_method_params
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
from ..types.my_resource_name_my_method_response import MyResourceNameMyMethodResponse

__all__ = ["MyResourceNameResource", "AsyncMyResourceNameResource"]


class MyResourceNameResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MyResourceNameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stl-workshop-scale-20241031-python#accessing-raw-response-data-eg-headers
        """
        return MyResourceNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MyResourceNameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stl-workshop-scale-20241031-python#with_streaming_response
        """
        return MyResourceNameResourceWithStreamingResponse(self)

    def my_method(
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
    ) -> MyResourceNameMyMethodResponse:
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
        return self._get(
            "/v4/evaluation-datasets",
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
                    my_resource_name_my_method_params.MyResourceNameMyMethodParams,
                ),
            ),
            cast_to=MyResourceNameMyMethodResponse,
        )


class AsyncMyResourceNameResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMyResourceNameResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stl-workshop-scale-20241031-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMyResourceNameResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMyResourceNameResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stl-workshop-scale-20241031-python#with_streaming_response
        """
        return AsyncMyResourceNameResourceWithStreamingResponse(self)

    async def my_method(
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
    ) -> MyResourceNameMyMethodResponse:
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
        return await self._get(
            "/v4/evaluation-datasets",
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
                    my_resource_name_my_method_params.MyResourceNameMyMethodParams,
                ),
            ),
            cast_to=MyResourceNameMyMethodResponse,
        )


class MyResourceNameResourceWithRawResponse:
    def __init__(self, my_resource_name: MyResourceNameResource) -> None:
        self._my_resource_name = my_resource_name

        self.my_method = to_raw_response_wrapper(
            my_resource_name.my_method,
        )


class AsyncMyResourceNameResourceWithRawResponse:
    def __init__(self, my_resource_name: AsyncMyResourceNameResource) -> None:
        self._my_resource_name = my_resource_name

        self.my_method = async_to_raw_response_wrapper(
            my_resource_name.my_method,
        )


class MyResourceNameResourceWithStreamingResponse:
    def __init__(self, my_resource_name: MyResourceNameResource) -> None:
        self._my_resource_name = my_resource_name

        self.my_method = to_streamed_response_wrapper(
            my_resource_name.my_method,
        )


class AsyncMyResourceNameResourceWithStreamingResponse:
    def __init__(self, my_resource_name: AsyncMyResourceNameResource) -> None:
        self._my_resource_name = my_resource_name

        self.my_method = async_to_streamed_response_wrapper(
            my_resource_name.my_method,
        )
