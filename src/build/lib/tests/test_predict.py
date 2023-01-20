from churn_model.predict import make_prediction
from churn_model import config
from churn_model.processing.load_data import load_dataset
import pytest

x = load_dataset(filename=config.app_config.x_train).head(5)

input1 = x.copy()
input2 = x.to_dict(orient='records')
input3 = x.head(1).to_dict(orient='records')

t = (input1, input2, input3)


@pytest.mark.parametrize('inputv', t)
def test_prediction_when_dataframe(inputv):

    results = make_prediction(input_data=inputv)

    assert results is not None
    assert isinstance(results['predictions'], list) == True
