import churn_model.processing.preprocessor as pp
from sklearn.impute import SimpleImputer
from feature_engine.encoding import RareLabelEncoder
from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import StandardScaler
from feature_engine.encoding import OneHotEncoder
from sklearn.pipeline import Pipeline
from churn_model import config

# import yaml

pipeline = Pipeline(
    [
        (
            "dropAndRename",
            pp.dropAndRenameColumns(
                features=config.model_config.drop,
                features_rename=config.model_config.rename,
                categorical=config.model_config.categorical,
            ),
        ),
        ("createFeature", pp.createFeatures()),
        (
            "nullZero",
            pp.sklearnWrapper(
                features=config.model_config.nullFillZero,
                transformer=SimpleImputer(strategy="constant", fill_value=0),
            ),
        ),
        (
            "nullMode",
            pp.sklearnWrapper(
                features=config.model_config.nullFillMode,
                transformer=SimpleImputer(strategy="most_frequent"),
            ),
        ),
        (
            "rare",
            RareLabelEncoder(
                tol=0.01, n_categories=3, variables=config.model_config.categorical
            ),
        ),
        (
            "one",
            OneHotEncoder(drop_last=True, variables=config.model_config.categorical),
        ),
        (
            "outlier",
            Winsorizer(
                capping_method="gaussian",
                tail="both",
                fold=3,
                variables=config.model_config.numerical,
            ),
        ),
        (
            "scale",
            pp.sklearnWrapper(
                features=config.model_config.numerical, transformer=StandardScaler()
            ),
        ),
    ]
)
