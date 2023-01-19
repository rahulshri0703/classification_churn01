import preprocessor as pp
from sklearn.impute import SimpleImputer
from feature_engine.encoding import RareLabelEncoder
from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import StandardScaler
from feature_engine.encoding import OneHotEncoder
from sklearn.pipeline import Pipeline
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

pipeline = Pipeline(
    [
        (
            'dropAndRename',
            pp.dropAndRenameColumns(
                features=config['drop'],
                features_rename=config['rename'],
                categorical=config['categorical']
            )
        ),
        (
            'createFeature',
            pp.createFeatures()
        ),
        (
            'nullZero',
            pp.sklearnWrapper(features=config['nullFillZero'],
                              transformer=SimpleImputer(
                                  strategy='constant', fill_value=0)
                              )
        ),
        (
            'nullMode',
            pp.sklearnWrapper(features=config['nullFillMode'],
                              transformer=SimpleImputer(
                                  strategy='most_frequent')
                              )
        ),
        (
            'rare',
            RareLabelEncoder(tol=0.01, n_categories=3,
                             variables=config['categorical']
                             )
        ),
        (
            'one',
            OneHotEncoder(drop_last=True, variables=config['categorical']
                          )
        ),
        (
            'outlier',
            Winsorizer(capping_method='gaussian', tail='both',
                       fold=3, variables=config['numerical']
                       )
        ),
        (
            'scale',
            pp.sklearnWrapper(features=config['numerical'],
                              transformer=StandardScaler()
                              )
        )
    ]
)
