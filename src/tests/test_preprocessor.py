import pytest
from churn_model.processing.preprocessor import dropAndRenameColumns, createFeatures
from churn_model import config


def test_dropAndRenameColumns(input_data):

    x_train, y_train = input_data
    l = list(x_train.columns)
    for i in config.model_config.drop:
        assert i in l

    for i in config.model_config.rename.keys():
        assert i in l
    tt = dropAndRenameColumns(features=config.model_config.drop,
                              features_rename=config.model_config.rename,
                              categorical=config.model_config.categorical)
    x = tt.fit_transform(x_train)

    for i in config.model_config.drop:
        assert i not in list(x.columns)

    for i in config.model_config.rename.keys():
        assert i not in list(x.columns)


def test_createFeature(input_data):
    x_train, y_trian = input_data

    l = [
        'vol_2g_mb_8', 'vol_2g_mb_6', 'vol_2g_mb_7', 'vol_3g_mb_8',
        'vol_3g_mb_6', 'vol_3g_mb_7',
        'total_og_mou_8', 'total_og_mou_6', 'total_og_mou_7',
        'total_ic_mou_8', 'total_ic_mou_6', 'total_ic_mou_7',
        'vbc_3g_8', 'vbc_3g_6', 'vbc_3g_7', 'arpu_8', 'arpu_6', 'arpu_7',
        'total_rech_amt_8', 'total_rech_amt_6', 'total_rech_amt_7'

    ]

    tt = createFeatures()
    tt2 = dropAndRenameColumns(features=config.model_config.drop,
                               features_rename=config.model_config.rename,
                               categorical=config.model_config.categorical)
    x = tt2.fit_transform(x_train)
    for i in l:
        assert i in list(x.columns)

    x = tt.fit_transform(x)

    for i in l:
        assert i not in list(x.columns)
