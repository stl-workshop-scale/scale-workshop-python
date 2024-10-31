# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from scale_workshop import ScaleWorkshop, AsyncScaleWorkshop
from scale_workshop.types import (
    EvaluationDatasetListResponse,
    EvaluationDatasetResponseSchema,
    EvaluationDatasetPublishResponse,
    EvaluationDatasetRetrieveResponse,
    AutoGeneratedDraftTestCaseApproveBatch,
    DeleteResponseEvaluationDatasetsSchemaObject,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.create(
            account_id="account_id",
            name="name",
            schema_type="GENERATION",
            type="manual",
        )
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.with_raw_response.create(
            account_id="account_id",
            name="name",
            schema_type="GENERATION",
            type="manual",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.with_streaming_response.create(
            account_id="account_id",
            name="name",
            schema_type="GENERATION",
            type="manual",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.create(
            account_id="account_id",
            knowledge_base_id="knowledge_base_id",
            name="name",
            schema_type="GENERATION",
            type="autogenerated",
        )
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.with_raw_response.create(
            account_id="account_id",
            knowledge_base_id="knowledge_base_id",
            name="name",
            schema_type="GENERATION",
            type="autogenerated",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.with_streaming_response.create(
            account_id="account_id",
            knowledge_base_id="knowledge_base_id",
            name="name",
            schema_type="GENERATION",
            type="autogenerated",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.create(
            account_id="account_id",
            advanced_config={"foo": ["string", "string", "string"]},
            harms_list=["string", "string", "string"],
            name="name",
            schema_type="GENERATION",
            type="safety",
        )
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.with_raw_response.create(
            account_id="account_id",
            advanced_config={"foo": ["string", "string", "string"]},
            harms_list=["string", "string", "string"],
            name="name",
            schema_type="GENERATION",
            type="safety",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.with_streaming_response.create(
            account_id="account_id",
            advanced_config={"foo": ["string", "string", "string"]},
            harms_list=["string", "string", "string"],
            name="name",
            schema_type="GENERATION",
            type="safety",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.retrieve(
            "evaluation_dataset_id",
        )
        assert_matches_type(EvaluationDatasetRetrieveResponse, evaluation_dataset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.with_raw_response.retrieve(
            "evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(EvaluationDatasetRetrieveResponse, evaluation_dataset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.with_streaming_response.retrieve(
            "evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(EvaluationDatasetRetrieveResponse, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update_overload_1(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.update(
            evaluation_dataset_id="evaluation_dataset_id",
            name="name",
            restore=False,
        )
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.with_raw_response.update(
            evaluation_dataset_id="evaluation_dataset_id",
            name="name",
            restore=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.with_streaming_response.update(
            evaluation_dataset_id="evaluation_dataset_id",
            name="name",
            restore=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.with_raw_response.update(
                evaluation_dataset_id="",
                name="name",
                restore=False,
            )

    @parametrize
    def test_method_update_overload_2(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.update(
            evaluation_dataset_id="evaluation_dataset_id",
            restore=True,
        )
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.with_raw_response.update(
            evaluation_dataset_id="evaluation_dataset_id",
            restore=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.with_streaming_response.update(
            evaluation_dataset_id="evaluation_dataset_id",
            restore=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.with_raw_response.update(
                evaluation_dataset_id="",
                restore=True,
            )

    @parametrize
    def test_method_list(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.list()
        assert_matches_type(EvaluationDatasetListResponse, evaluation_dataset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.list(
            account_id="account_id",
            include_archived=True,
            limit=1,
            page=1,
        )
        assert_matches_type(EvaluationDatasetListResponse, evaluation_dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(EvaluationDatasetListResponse, evaluation_dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(EvaluationDatasetListResponse, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.delete(
            "evaluation_dataset_id",
        )
        assert_matches_type(DeleteResponseEvaluationDatasetsSchemaObject, evaluation_dataset, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.with_raw_response.delete(
            "evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(DeleteResponseEvaluationDatasetsSchemaObject, evaluation_dataset, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.with_streaming_response.delete(
            "evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(DeleteResponseEvaluationDatasetsSchemaObject, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_approve_batch(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.approve_batch(
            evaluation_dataset_id="evaluation_dataset_id",
            autogenerated_draft_test_cases=["string", "string", "string"],
        )
        assert_matches_type(AutoGeneratedDraftTestCaseApproveBatch, evaluation_dataset, path=["response"])

    @parametrize
    def test_method_approve_batch_with_all_params(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.approve_batch(
            evaluation_dataset_id="evaluation_dataset_id",
            autogenerated_draft_test_cases=["string", "string", "string"],
            force=True,
        )
        assert_matches_type(AutoGeneratedDraftTestCaseApproveBatch, evaluation_dataset, path=["response"])

    @parametrize
    def test_raw_response_approve_batch(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.with_raw_response.approve_batch(
            evaluation_dataset_id="evaluation_dataset_id",
            autogenerated_draft_test_cases=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(AutoGeneratedDraftTestCaseApproveBatch, evaluation_dataset, path=["response"])

    @parametrize
    def test_streaming_response_approve_batch(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.with_streaming_response.approve_batch(
            evaluation_dataset_id="evaluation_dataset_id",
            autogenerated_draft_test_cases=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(AutoGeneratedDraftTestCaseApproveBatch, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_approve_batch(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.with_raw_response.approve_batch(
                evaluation_dataset_id="",
                autogenerated_draft_test_cases=["string", "string", "string"],
            )

    @parametrize
    def test_method_publish(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.publish(
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(EvaluationDatasetPublishResponse, evaluation_dataset, path=["response"])

    @parametrize
    def test_method_publish_with_all_params(self, client: ScaleWorkshop) -> None:
        evaluation_dataset = client.evaluation_datasets.publish(
            evaluation_dataset_id="evaluation_dataset_id",
            force=True,
        )
        assert_matches_type(EvaluationDatasetPublishResponse, evaluation_dataset, path=["response"])

    @parametrize
    def test_raw_response_publish(self, client: ScaleWorkshop) -> None:
        response = client.evaluation_datasets.with_raw_response.publish(
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = response.parse()
        assert_matches_type(EvaluationDatasetPublishResponse, evaluation_dataset, path=["response"])

    @parametrize
    def test_streaming_response_publish(self, client: ScaleWorkshop) -> None:
        with client.evaluation_datasets.with_streaming_response.publish(
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = response.parse()
            assert_matches_type(EvaluationDatasetPublishResponse, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_publish(self, client: ScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            client.evaluation_datasets.with_raw_response.publish(
                evaluation_dataset_id="",
            )


class TestAsyncEvaluationDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.create(
            account_id="account_id",
            name="name",
            schema_type="GENERATION",
            type="manual",
        )
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.with_raw_response.create(
            account_id="account_id",
            name="name",
            schema_type="GENERATION",
            type="manual",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.with_streaming_response.create(
            account_id="account_id",
            name="name",
            schema_type="GENERATION",
            type="manual",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.create(
            account_id="account_id",
            knowledge_base_id="knowledge_base_id",
            name="name",
            schema_type="GENERATION",
            type="autogenerated",
        )
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.with_raw_response.create(
            account_id="account_id",
            knowledge_base_id="knowledge_base_id",
            name="name",
            schema_type="GENERATION",
            type="autogenerated",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.with_streaming_response.create(
            account_id="account_id",
            knowledge_base_id="knowledge_base_id",
            name="name",
            schema_type="GENERATION",
            type="autogenerated",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.create(
            account_id="account_id",
            advanced_config={"foo": ["string", "string", "string"]},
            harms_list=["string", "string", "string"],
            name="name",
            schema_type="GENERATION",
            type="safety",
        )
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.with_raw_response.create(
            account_id="account_id",
            advanced_config={"foo": ["string", "string", "string"]},
            harms_list=["string", "string", "string"],
            name="name",
            schema_type="GENERATION",
            type="safety",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.with_streaming_response.create(
            account_id="account_id",
            advanced_config={"foo": ["string", "string", "string"]},
            harms_list=["string", "string", "string"],
            name="name",
            schema_type="GENERATION",
            type="safety",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.retrieve(
            "evaluation_dataset_id",
        )
        assert_matches_type(EvaluationDatasetRetrieveResponse, evaluation_dataset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.with_raw_response.retrieve(
            "evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(EvaluationDatasetRetrieveResponse, evaluation_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.with_streaming_response.retrieve(
            "evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(EvaluationDatasetRetrieveResponse, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.update(
            evaluation_dataset_id="evaluation_dataset_id",
            name="name",
            restore=False,
        )
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.with_raw_response.update(
            evaluation_dataset_id="evaluation_dataset_id",
            name="name",
            restore=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.with_streaming_response.update(
            evaluation_dataset_id="evaluation_dataset_id",
            name="name",
            restore=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.with_raw_response.update(
                evaluation_dataset_id="",
                name="name",
                restore=False,
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.update(
            evaluation_dataset_id="evaluation_dataset_id",
            restore=True,
        )
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.with_raw_response.update(
            evaluation_dataset_id="evaluation_dataset_id",
            restore=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.with_streaming_response.update(
            evaluation_dataset_id="evaluation_dataset_id",
            restore=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(EvaluationDatasetResponseSchema, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.with_raw_response.update(
                evaluation_dataset_id="",
                restore=True,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.list()
        assert_matches_type(EvaluationDatasetListResponse, evaluation_dataset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.list(
            account_id="account_id",
            include_archived=True,
            limit=1,
            page=1,
        )
        assert_matches_type(EvaluationDatasetListResponse, evaluation_dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(EvaluationDatasetListResponse, evaluation_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(EvaluationDatasetListResponse, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.delete(
            "evaluation_dataset_id",
        )
        assert_matches_type(DeleteResponseEvaluationDatasetsSchemaObject, evaluation_dataset, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.with_raw_response.delete(
            "evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(DeleteResponseEvaluationDatasetsSchemaObject, evaluation_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.with_streaming_response.delete(
            "evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(DeleteResponseEvaluationDatasetsSchemaObject, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_approve_batch(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.approve_batch(
            evaluation_dataset_id="evaluation_dataset_id",
            autogenerated_draft_test_cases=["string", "string", "string"],
        )
        assert_matches_type(AutoGeneratedDraftTestCaseApproveBatch, evaluation_dataset, path=["response"])

    @parametrize
    async def test_method_approve_batch_with_all_params(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.approve_batch(
            evaluation_dataset_id="evaluation_dataset_id",
            autogenerated_draft_test_cases=["string", "string", "string"],
            force=True,
        )
        assert_matches_type(AutoGeneratedDraftTestCaseApproveBatch, evaluation_dataset, path=["response"])

    @parametrize
    async def test_raw_response_approve_batch(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.with_raw_response.approve_batch(
            evaluation_dataset_id="evaluation_dataset_id",
            autogenerated_draft_test_cases=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(AutoGeneratedDraftTestCaseApproveBatch, evaluation_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_approve_batch(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.with_streaming_response.approve_batch(
            evaluation_dataset_id="evaluation_dataset_id",
            autogenerated_draft_test_cases=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(AutoGeneratedDraftTestCaseApproveBatch, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_approve_batch(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.with_raw_response.approve_batch(
                evaluation_dataset_id="",
                autogenerated_draft_test_cases=["string", "string", "string"],
            )

    @parametrize
    async def test_method_publish(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.publish(
            evaluation_dataset_id="evaluation_dataset_id",
        )
        assert_matches_type(EvaluationDatasetPublishResponse, evaluation_dataset, path=["response"])

    @parametrize
    async def test_method_publish_with_all_params(self, async_client: AsyncScaleWorkshop) -> None:
        evaluation_dataset = await async_client.evaluation_datasets.publish(
            evaluation_dataset_id="evaluation_dataset_id",
            force=True,
        )
        assert_matches_type(EvaluationDatasetPublishResponse, evaluation_dataset, path=["response"])

    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncScaleWorkshop) -> None:
        response = await async_client.evaluation_datasets.with_raw_response.publish(
            evaluation_dataset_id="evaluation_dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_dataset = await response.parse()
        assert_matches_type(EvaluationDatasetPublishResponse, evaluation_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncScaleWorkshop) -> None:
        async with async_client.evaluation_datasets.with_streaming_response.publish(
            evaluation_dataset_id="evaluation_dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_dataset = await response.parse()
            assert_matches_type(EvaluationDatasetPublishResponse, evaluation_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_publish(self, async_client: AsyncScaleWorkshop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_dataset_id` but received ''"):
            await async_client.evaluation_datasets.with_raw_response.publish(
                evaluation_dataset_id="",
            )
