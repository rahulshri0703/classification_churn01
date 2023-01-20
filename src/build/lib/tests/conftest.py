import pytest
from churn_model import config
from churn_model.processing.load_data import load_dataset


@pytest.fixture(scope='session')
def input_data():

    x_train = load_dataset(filename=config.app_config.x_train)
    y_train = load_dataset(filename=config.app_config.y_train)

    return x_train, y_train
