from churn_model import config
from churn_model.processing.load_data import load_pipeline
from churn_model.processing.validation import validate_inputs
import typing as t
import logging
import pandas as pd

# import numpy as np

_logger = logging.getLogger(__file__)

pipeline = load_pipeline(filename=config.app_config.final_pipeline)


def make_prediction(*, input_data: t.Union[pd.DataFrame, dict]) -> dict:

    if type(input_data) != type(pd.DataFrame):

        try:
            input_data = pd.DataFrame(input_data)
        except:
            input_data = pd.DataFrame(input_data, index=[0])

    a, error = validate_inputs(input_data=input_data)

    results = dict(predictions=None, version="0.0.1", errors=error)

    if not error:
        prediction = pipeline.predict(input_data[config.model_config.features])

        _logger.info(
            f"Making predictions with model version: {'0.0.1'} "
            f"Predictions: {prediction}"
        )
        results["predictions"] = list(prediction)

    return results
