# Shared Types

```python
from scale_workshop.types import (
    AssistantMessage,
    ChatMessage,
    FlexibleChunk,
    StringExtraInfoSchema,
    SystemMessage,
    UserMessage,
)
```

# EvaluationDatasets

Types:

```python
from scale_workshop.types import (
    EvaluationDatasetRetrieveResponse,
    EvaluationDatasetUpdateResponse,
    EvaluationDatasetListResponse,
    EvaluationDatasetApproveBatchResponse,
    EvaluationDatasetPublishResponse,
    EvaluationDatasetRemoveResponse,
)
```

Methods:

- <code title="get /v4/evaluation-datasets/{evaluation_dataset_id}">client.evaluation_datasets.<a href="./src/scale_workshop/resources/evaluation_datasets/evaluation_datasets.py">retrieve</a>(evaluation_dataset_id) -> <a href="./src/scale_workshop/types/evaluation_dataset_retrieve_response.py">EvaluationDatasetRetrieveResponse</a></code>
- <code title="patch /v4/evaluation-datasets/{evaluation_dataset_id}">client.evaluation_datasets.<a href="./src/scale_workshop/resources/evaluation_datasets/evaluation_datasets.py">update</a>(evaluation_dataset_id, \*\*<a href="src/scale_workshop/types/evaluation_dataset_update_params.py">params</a>) -> <a href="./src/scale_workshop/types/evaluation_dataset_update_response.py">EvaluationDatasetUpdateResponse</a></code>
- <code title="get /v4/evaluation-datasets">client.evaluation_datasets.<a href="./src/scale_workshop/resources/evaluation_datasets/evaluation_datasets.py">list</a>(\*\*<a href="src/scale_workshop/types/evaluation_dataset_list_params.py">params</a>) -> <a href="./src/scale_workshop/types/evaluation_dataset_list_response.py">SyncPageNumberPage[EvaluationDatasetListResponse]</a></code>
- <code title="post /v4/evaluation-datasets/{evaluation_dataset_id}/approve-batch">client.evaluation_datasets.<a href="./src/scale_workshop/resources/evaluation_datasets/evaluation_datasets.py">approve_batch</a>(evaluation_dataset_id, \*\*<a href="src/scale_workshop/types/evaluation_dataset_approve_batch_params.py">params</a>) -> <a href="./src/scale_workshop/types/evaluation_dataset_approve_batch_response.py">EvaluationDatasetApproveBatchResponse</a></code>
- <code title="post /v4/evaluation-datasets/{evaluation_dataset_id}/publish">client.evaluation_datasets.<a href="./src/scale_workshop/resources/evaluation_datasets/evaluation_datasets.py">publish</a>(evaluation_dataset_id, \*\*<a href="src/scale_workshop/types/evaluation_dataset_publish_params.py">params</a>) -> <a href="./src/scale_workshop/types/evaluation_dataset_publish_response.py">EvaluationDatasetPublishResponse</a></code>
- <code title="delete /v4/evaluation-datasets/{evaluation_dataset_id}">client.evaluation_datasets.<a href="./src/scale_workshop/resources/evaluation_datasets/evaluation_datasets.py">remove</a>(evaluation_dataset_id) -> <a href="./src/scale_workshop/types/evaluation_dataset_remove_response.py">EvaluationDatasetRemoveResponse</a></code>

## TestCases

Types:

```python
from scale_workshop.types.evaluation_datasets import (
    ArtifactSchemaGeneration,
    FlexibleTestCaseSchema,
    FlexibleTestCaseVersion,
    GenerationTestCaseSchema,
    GenerationTestCaseVersion,
    PaginatedTestCases,
    TestCase,
    TestCaseDeleteResponse,
    TestCaseBatchResponse,
)
```

Methods:

- <code title="post /v4/evaluation-datasets/{evaluation_dataset_id}/test-cases">client.evaluation_datasets.test_cases.<a href="./src/scale_workshop/resources/evaluation_datasets/test_cases.py">create</a>(evaluation_dataset_id, \*\*<a href="src/scale_workshop/types/evaluation_datasets/test_case_create_params.py">params</a>) -> <a href="./src/scale_workshop/types/evaluation_datasets/test_case.py">TestCase</a></code>
- <code title="get /v4/evaluation-datasets/{evaluation_dataset_id}/test-cases/{test_case_id}">client.evaluation_datasets.test_cases.<a href="./src/scale_workshop/resources/evaluation_datasets/test_cases.py">retrieve</a>(test_case_id, \*, evaluation_dataset_id) -> <a href="./src/scale_workshop/types/evaluation_datasets/test_case.py">TestCase</a></code>
- <code title="patch /v4/evaluation-datasets/{evaluation_dataset_id}/test-cases/{test_case_id}">client.evaluation_datasets.test_cases.<a href="./src/scale_workshop/resources/evaluation_datasets/test_cases.py">update</a>(test_case_id, \*, evaluation_dataset_id, \*\*<a href="src/scale_workshop/types/evaluation_datasets/test_case_update_params.py">params</a>) -> <a href="./src/scale_workshop/types/evaluation_datasets/test_case.py">TestCase</a></code>
- <code title="get /v4/evaluation-datasets/{evaluation_dataset_id}/test-cases">client.evaluation_datasets.test_cases.<a href="./src/scale_workshop/resources/evaluation_datasets/test_cases.py">list</a>(evaluation_dataset_id, \*\*<a href="src/scale_workshop/types/evaluation_datasets/test_case_list_params.py">params</a>) -> <a href="./src/scale_workshop/types/evaluation_datasets/test_case.py">SyncPageNumberPage[TestCase]</a></code>
- <code title="delete /v4/evaluation-datasets/{evaluation_dataset_id}/test-cases/{test_case_id}">client.evaluation_datasets.test_cases.<a href="./src/scale_workshop/resources/evaluation_datasets/test_cases.py">delete</a>(test_case_id, \*, evaluation_dataset_id) -> <a href="./src/scale_workshop/types/evaluation_datasets/test_case_delete_response.py">TestCaseDeleteResponse</a></code>
- <code title="post /v4/evaluation-datasets/{evaluation_dataset_id}/test-cases/batch">client.evaluation_datasets.test_cases.<a href="./src/scale_workshop/resources/evaluation_datasets/test_cases.py">batch</a>(evaluation_dataset_id, \*\*<a href="src/scale_workshop/types/evaluation_datasets/test_case_batch_params.py">params</a>) -> <a href="./src/scale_workshop/types/evaluation_datasets/test_case_batch_response.py">TestCaseBatchResponse</a></code>
