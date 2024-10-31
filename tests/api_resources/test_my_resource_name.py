# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scale_workshop import ScaleWorkshop, AsyncScaleWorkshop
from scale_workshop.types import MyResourceNameMyMethodResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMyResourceName:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_my_method(self, client: ScaleWorkshop) -> None:
        my_resource_name = client.my_resource_name.my_method()
        assert_matches_type(MyResourceNameMyMethodResponse, my_resource_name, path=["response"])

    @parametrize
    def test_method_my_method_with_all_params(self, client: ScaleWorkshop) -> None:
        my_resource_name = client.my_resource_name.my_method(
            account_id="account_id",
            include_archived=True,
            limit=1,
            page=1,
        )
        assert_matches_type(MyResourceNameMyMethodResponse, my_resource_name, path=["response"])

    @parametrize
    def test_raw_response_my_method(self, client: ScaleWorkshop) -> None:
        response = client.my_resource_name.with_raw_response.my_method()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        my_resource_name = response.parse()
        assert_matches_type(MyResourceNameMyMethodResponse, my_resource_name, path=["response"])

    @parametrize
    def test_streaming_response_my_method(self, client: ScaleWorkshop) -> None:
        with client.my_resource_name.with_streaming_response.my_method() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            my_resource_name = response.parse()
            assert_matches_type(MyResourceNameMyMethodResponse, my_resource_name, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMyResourceName:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_my_method(self, async_client: AsyncScaleWorkshop) -> None:
        my_resource_name = await async_client.my_resource_name.my_method()
        assert_matches_type(MyResourceNameMyMethodResponse, my_resource_name, path=["response"])

    @parametrize
    async def test_method_my_method_with_all_params(self, async_client: AsyncScaleWorkshop) -> None:
        my_resource_name = await async_client.my_resource_name.my_method(
            account_id="account_id",
            include_archived=True,
            limit=1,
            page=1,
        )
        assert_matches_type(MyResourceNameMyMethodResponse, my_resource_name, path=["response"])

    @parametrize
    async def test_raw_response_my_method(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.my_resource_name.with_raw_response.my_method()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        my_resource_name = await response.parse()
        assert_matches_type(MyResourceNameMyMethodResponse, my_resource_name, path=["response"])

    @parametrize
    async def test_streaming_response_my_method(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.my_resource_name.with_streaming_response.my_method() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            my_resource_name = await response.parse()
            assert_matches_type(MyResourceNameMyMethodResponse, my_resource_name, path=["response"])

        assert cast(Any, response.is_closed) is True
