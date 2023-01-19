import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.ensemble import StackingClassifier
from churn_model.config.core import config, DATA_DIR, BEST_MODEL_DIR
import typing as t
import logging
import joblib

_logger = logging.getLogger(__name__)
_version = '0.0.1'


def load_dataset(*, filename: str) -> pd.DataFrame:

    df = pd.read_csv(f'{DATA_DIR}/{filename}')
    return df


def load_pipeline(*, filename: str) -> Pipeline:

    path = f'{BEST_MODEL_DIR}/{filename}'

    pipeline = joblib.load(path)
    return pipeline


def load_model(*, filename: str) -> StackingClassifier:

    path = f'{BEST_MODEL_DIR}/{filename}'

    model = joblib.load(path)
    return model


def save_pipeline(*, pipeline_to_save: Pipeline) -> None:

    save_pipeline_name = f"{config.app_config.saved_pipeline_name}{_version}.pkl"
    save_path = BEST_MODEL_DIR / save_pipeline_name

    joblib.dump(pipeline_to_save, save_path)
    _logger.info(f'pipeline saved at {save_pipeline_name}')


def save_model(*, model_to_save: StackingClassifier) -> None:

    save_model_name = f"{config.app_config.saved_model_name}{_version}.pkl"
    save_path = BEST_MODEL_DIR / save_model_name

    joblib.dump(model_to_save, save_path)
    _logger.info(f'pipeline saved at {save_model_name}')


def remove_old_pipelines(*, files_to_keep: t.List[str]) -> None:
    """
    Remove old model pipelines.

    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    """
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in BEST_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()
