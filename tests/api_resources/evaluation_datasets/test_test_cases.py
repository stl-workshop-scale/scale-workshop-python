# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scale_workshop import ScaleWorkshop, AsyncScaleWorkshop
from scale_workshop.pagination import SyncPageNumberPage, AsyncPageNumberPage
from scale_workshop.types.evaluation_datasets import (
    TestCase,
    TestCaseBatchResponse,
    TestCaseDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestCases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.create(
            evaluation_dataset_id="evaluation_dataset_id",
            test_case_data={
                "artifact_ids_filter": ["string", "string", "string"],
                "input": "input",
            },
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.create(
            evaluation_dataset_id="evaluation_dataset_id",
            test_case_data={
                "artifact_ids_filter": ["string", "string", "string"],
                "input": "input",
                "expected_extra_info": {
                    "info": "info",
                    "schema_type": "STRING",
                },
                "expected_output": "expected_output",
            },
            account_id="account_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.test_cases.with_raw_response.create(
            evaluation_dataset_id="evaluation_dataset_id",
            test_case_data={
                "artifact_ids_filter": ["string", "string", "string"],
                "input": "input",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.test_cases.with_streaming_response.create(
            evaluation_dataset_id="evaluation_dataset_id",
            test_case_data={
                "artifact_ids_filter": ["string", "string", "string"],
                "input": "input",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.create(
                evaluation_dataset_id="",
                test_case_data={
                    "artifact_ids_filter": ["string", "string", "string"],
                    "input": "input",
                },
            )

    @parametrize
    def test_method_retrieve(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.retrieve(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.retrieve(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.test_cases.with_raw_response.retrieve(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.test_cases.with_streaming_response.retrieve(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.retrieve(
                test_case_id="",
                evaluation_dataset_id="evaluation_dataset_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.retrieve(
                test_case_id="test_case_id",
                evaluation_dataset_id="",
            )

    @parametrize
    def test_method_update_overload_1(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.update(
            test_case_id="test_case_id",
            restore=False,
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.update(
            test_case_id="test_case_id",
            restore=False,
            evaluation_dataset_id="evaluation_dataset_id",
            account_id="account_id",
            test_case_data={
                "artifact_ids_filter": ["string", "string", "string"],
                "input": "input",
                "expected_extra_info": {
                    "info": "info",
                    "schema_type": "STRING",
                },
                "expected_output": "expected_output",
            },
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.test_cases.with_raw_response.update(
            test_case_id="test_case_id",
            restore=False,
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.test_cases.with_streaming_response.update(
            test_case_id="test_case_id",
            restore=False,
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.update(
                test_case_id="",
                restore=False,
                evaluation_dataset_id="evaluation_dataset_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.update(
                test_case_id="test_case_id",
                restore=False,
                evaluation_dataset_id="",
            )

    @parametrize
    def test_method_update_overload_2(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.update(
            test_case_id="test_case_id",
            restore=True,
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.update(
            test_case_id="test_case_id",
            restore=True,
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.test_cases.with_raw_response.update(
            test_case_id="test_case_id",
            restore=True,
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.test_cases.with_streaming_response.update(
            test_case_id="test_case_id",
            restore=True,
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.update(
                test_case_id="",
                restore=True,
                evaluation_dataset_id="evaluation_dataset_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.update(
                test_case_id="test_case_id",
                restore=True,
                evaluation_dataset_id="",
            )

    @parametrize
    def test_method_list(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.list(
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(SyncPageNumberPage[TestCase], test_case, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.list(
            evaluation_dataset_id="evaluation_dataset_id",
            account_id="account_id",
            include_archived=True,
            limit=1,
            page=1,
        )
        assert_matches_type(SyncPageNumberPage[TestCase], test_case, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.test_cases.with_raw_response.list(
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(SyncPageNumberPage[TestCase], test_case, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.test_cases.with_streaming_response.list(
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(SyncPageNumberPage[TestCase], test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.list(
                evaluation_dataset_id="",
            )

    @parametrize
    def test_method_delete(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.delete(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCaseDeleteResponse, test_case, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.delete(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCaseDeleteResponse, test_case, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.test_cases.with_raw_response.delete(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCaseDeleteResponse, test_case, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.test_cases.with_streaming_response.delete(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCaseDeleteResponse, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.delete(
                test_case_id="",
                evaluation_dataset_id="evaluation_dataset_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.delete(
                test_case_id="test_case_id",
                evaluation_dataset_id="",
            )

    @parametrize
    def test_method_batch(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.batch(
            evaluation_dataset_id="evaluation_dataset_id",
            items=[
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
            ],
        )
        assert_matches_type(TestCaseBatchResponse, test_case, path=["response"])

    @parametrize
    def test_method_batch_with_all_params(self, client: ScaleWorkshop) -> None:
        test_case = client.evaluation_datasets.test_cases.batch(
            evaluation_dataset_id="evaluation_dataset_id",
            items=[
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                        "expected_extra_info": {
                            "info": "info",
                            "schema_type": "STRING",
                        },
                        "expected_output": "expected_output",
                    },
                    "account_id": "account_id",
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                        "expected_extra_info": {
                            "info": "info",
                            "schema_type": "STRING",
                        },
                        "expected_output": "expected_output",
                    },
                    "account_id": "account_id",
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                        "expected_extra_info": {
                            "info": "info",
                            "schema_type": "STRING",
                        },
                        "expected_output": "expected_output",
                    },
                    "account_id": "account_id",
                },
            ],
        )
        assert_matches_type(TestCaseBatchResponse, test_case, path=["response"])

    @parametrize
    def test_raw_response_batch(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.test_cases.with_raw_response.batch(
            evaluation_dataset_id="evaluation_dataset_id",
            items=[
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCaseBatchResponse, test_case, path=["response"])

    @parametrize
    def test_streaming_response_batch(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.test_cases.with_streaming_response.batch(
            evaluation_dataset_id="evaluation_dataset_id",
            items=[
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCaseBatchResponse, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_batch(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.test_cases.with_raw_response.batch(
                evaluation_dataset_id="",
                items=[
                    {
                        "test_case_data": {
                            "artifact_ids_filter": ["string", "string", "string"],
                            "input": "input",
                        }
                    },
                    {
                        "test_case_data": {
                            "artifact_ids_filter": ["string", "string", "string"],
                            "input": "input",
                        }
                    },
                    {
                        "test_case_data": {
                            "artifact_ids_filter": ["string", "string", "string"],
                            "input": "input",
                        }
                    },
                ],
            )


class TestAsyncTestCases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.create(
            evaluation_dataset_id="evaluation_dataset_id",
            test_case_data={
                "artifact_ids_filter": ["string", "string", "string"],
                "input": "input",
            },
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.create(
            evaluation_dataset_id="evaluation_dataset_id",
            test_case_data={
                "artifact_ids_filter": ["string", "string", "string"],
                "input": "input",
                "expected_extra_info": {
                    "info": "info",
                    "schema_type": "STRING",
                },
                "expected_output": "expected_output",
            },
            account_id="account_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.test_cases.with_raw_response.create(
            evaluation_dataset_id="evaluation_dataset_id",
            test_case_data={
                "artifact_ids_filter": ["string", "string", "string"],
                "input": "input",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.test_cases.with_streaming_response.create(
            evaluation_dataset_id="evaluation_dataset_id",
            test_case_data={
                "artifact_ids_filter": ["string", "string", "string"],
                "input": "input",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.create(
                evaluation_dataset_id="",
                test_case_data={
                    "artifact_ids_filter": ["string", "string", "string"],
                    "input": "input",
                },
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.retrieve(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.retrieve(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.test_cases.with_raw_response.retrieve(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.test_cases.with_streaming_response.retrieve(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.retrieve(
                test_case_id="",
                evaluation_dataset_id="evaluation_dataset_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.retrieve(
                test_case_id="test_case_id",
                evaluation_dataset_id="",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.update(
            test_case_id="test_case_id",
            restore=False,
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.update(
            test_case_id="test_case_id",
            restore=False,
            evaluation_dataset_id="evaluation_dataset_id",
            account_id="account_id",
            test_case_data={
                "artifact_ids_filter": ["string", "string", "string"],
                "input": "input",
                "expected_extra_info": {
                    "info": "info",
                    "schema_type": "STRING",
                },
                "expected_output": "expected_output",
            },
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.test_cases.with_raw_response.update(
            test_case_id="test_case_id",
            restore=False,
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.test_cases.with_streaming_response.update(
            test_case_id="test_case_id",
            restore=False,
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.update(
                test_case_id="",
                restore=False,
                evaluation_dataset_id="evaluation_dataset_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.update(
                test_case_id="test_case_id",
                restore=False,
                evaluation_dataset_id="",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.update(
            test_case_id="test_case_id",
            restore=True,
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.update(
            test_case_id="test_case_id",
            restore=True,
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.test_cases.with_raw_response.update(
            test_case_id="test_case_id",
            restore=True,
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.test_cases.with_streaming_response.update(
            test_case_id="test_case_id",
            restore=True,
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.update(
                test_case_id="",
                restore=True,
                evaluation_dataset_id="evaluation_dataset_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.update(
                test_case_id="test_case_id",
                restore=True,
                evaluation_dataset_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.list(
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(AsyncPageNumberPage[TestCase], test_case, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.list(
            evaluation_dataset_id="evaluation_dataset_id",
            account_id="account_id",
            include_archived=True,
            limit=1,
            page=1,
        )
        assert_matches_type(AsyncPageNumberPage[TestCase], test_case, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.test_cases.with_raw_response.list(
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(AsyncPageNumberPage[TestCase], test_case, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.test_cases.with_streaming_response.list(
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(AsyncPageNumberPage[TestCase], test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.list(
                evaluation_dataset_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.delete(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCaseDeleteResponse, test_case, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.delete(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(TestCaseDeleteResponse, test_case, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.test_cases.with_raw_response.delete(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCaseDeleteResponse, test_case, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.test_cases.with_streaming_response.delete(
            test_case_id="test_case_id",
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCaseDeleteResponse, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.delete(
                test_case_id="",
                evaluation_dataset_id="evaluation_dataset_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.delete(
                test_case_id="test_case_id",
                evaluation_dataset_id="",
            )

    @parametrize
    async def test_method_batch(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.batch(
            evaluation_dataset_id="evaluation_dataset_id",
            items=[
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
            ],
        )
        assert_matches_type(TestCaseBatchResponse, test_case, path=["response"])

    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncScaleWorkshop) -> None:
        test_case = await async_client.evaluation_datasets.test_cases.batch(
            evaluation_dataset_id="evaluation_dataset_id",
            items=[
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                        "expected_extra_info": {
                            "info": "info",
                            "schema_type": "STRING",
                        },
                        "expected_output": "expected_output",
                    },
                    "account_id": "account_id",
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                        "expected_extra_info": {
                            "info": "info",
                            "schema_type": "STRING",
                        },
                        "expected_output": "expected_output",
                    },
                    "account_id": "account_id",
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                        "expected_extra_info": {
                            "info": "info",
                            "schema_type": "STRING",
                        },
                        "expected_output": "expected_output",
                    },
                    "account_id": "account_id",
                },
            ],
        )
        assert_matches_type(TestCaseBatchResponse, test_case, path=["response"])

    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.test_cases.with_raw_response.batch(
            evaluation_dataset_id="evaluation_dataset_id",
            items=[
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCaseBatchResponse, test_case, path=["response"])

    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.test_cases.with_streaming_response.batch(
            evaluation_dataset_id="evaluation_dataset_id",
            items=[
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
                {
                    "test_case_data": {
                        "artifact_ids_filter": ["string", "string", "string"],
                        "input": "input",
                    }
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCaseBatchResponse, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_batch(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.test_cases.with_raw_response.batch(
                evaluation_dataset_id="",
                items=[
                    {
                        "test_case_data": {
                            "artifact_ids_filter": ["string", "string", "string"],
                            "input": "input",
                        }
                    },
                    {
                        "test_case_data": {
                            "artifact_ids_filter": ["string", "string", "string"],
                            "input": "input",
                        }
                    },
                    {
                        "test_case_data": {
                            "artifact_ids_filter": ["string", "string", "string"],
                            "input": "input",
                        }
                    },
                ],
            )
