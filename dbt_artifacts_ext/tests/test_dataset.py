from dbt_artifacts_ext.converter.matatika import MatatikaConverter


def test_convert_with_model_and_column_descriptions():
    converter = MatatikaConverter()
    converter.load_artifacts()

    contexts = converter.convert()
    context_with_descriptions = contexts[0]

    dataset_description: str = context_with_descriptions.data["description"]

    assert dataset_description.startswith('Test dbt model 1')
    assert '| Column |' in dataset_description
    assert '| Description |' in dataset_description
    assert '| --- |' in dataset_description
    assert '| model_column_1 |' in dataset_description
    assert '| model_column_2 |' in dataset_description
    assert '| model_column_3 |' in dataset_description

    assert 'This is my column_one description' in context_with_descriptions.metadata["columns"]["column_one"]["description"]


def test_convert_without_model_and_column_descriptions():
    converter = MatatikaConverter()
    converter.load_artifacts()

    contexts = converter.convert()
    context_without_description = contexts[1]

    dataset_description: str = context_without_description.data["description"]

    assert dataset_description.startswith('| Column |')
