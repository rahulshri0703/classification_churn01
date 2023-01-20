from churn_model import pipeline
from churn_model import config
from churn_model.processing.validation import validate_inputs
from churn_model.processing.load_data import load_pipeline


def test_pipeline_dropRename(input_data):

    x_train, y_train = input_data
    pipeline = load_pipeline(filename=config.app_config.final_pipeline)

    for i in config.model_config.drop:
        assert i in list(x_train.columns)

    for i in config.model_config.rename.keys():
        assert i in list(x_train.columns)

    x = pipeline[:-1].transform(x_train)

    for i in config.model_config.drop:
        assert i not in list(x.columns)

    for i in config.model_config.rename.keys():
        assert i not in list(x.columns)


def test_predict_valid_input(input_data):

    x_train, y_train = input_data
    x_train = x_train.head(5)

    v, error = validate_inputs(input_data=x_train)
    x_train = x_train[config.model_config.features]

    pipeline = load_pipeline(filename=config.app_config.final_pipeline)
    yhat = pipeline.predict(x_train)

    assert yhat is not None
    assert error is None
