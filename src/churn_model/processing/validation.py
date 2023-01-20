import pandas as pd
import numpy as np
import typing as t
from churn_model import config
from marshmallow import Schema, fields, ValidationError


class InputSchema(Schema):

    onnet_mou_6 = fields.Float(allow_nan=False)
    onnet_mou_7 = fields.Float(allow_nan=False)
    onnet_mou_8 = fields.Float(allow_nan=False)
    offnet_mou_6 = fields.Float(allow_nan=False)
    offnet_mou_7 = fields.Float(allow_nan=False)
    offnet_mou_8 = fields.Float(allow_nan=False)
    roam_ic_mou_6 = fields.Float(allow_nan=False)
    roam_ic_mou_7 = fields.Float(allow_nan=False)
    roam_ic_mou_8 = fields.Float(allow_nan=False)
    roam_og_mou_6 = fields.Float(allow_nan=False)
    roam_og_mou_7 = fields.Float(allow_nan=False)
    roam_og_mou_8 = fields.Float(allow_nan=False)
    loc_og_t2t_mou_6 = fields.Float(allow_nan=False)
    loc_og_t2t_mou_7 = fields.Float(allow_nan=False)
    loc_og_t2t_mou_8 = fields.Float(allow_nan=False)
    loc_og_t2m_mou_6 = fields.Float(allow_nan=False)
    loc_og_t2m_mou_7 = fields.Float(allow_nan=False)
    loc_og_t2m_mou_8 = fields.Float(allow_nan=False)
    loc_og_t2f_mou_6 = fields.Float(allow_nan=False)
    loc_og_t2f_mou_7 = fields.Float(allow_nan=False)
    loc_og_t2f_mou_8 = fields.Float(allow_nan=False)
    loc_og_t2c_mou_6 = fields.Float(allow_nan=False)
    loc_og_t2c_mou_7 = fields.Float(allow_nan=False)
    loc_og_t2c_mou_8 = fields.Float(allow_nan=False)
    loc_og_mou_6 = fields.Float(allow_nan=False)
    loc_og_mou_7 = fields.Float(allow_nan=False)
    loc_og_mou_8 = fields.Float(allow_nan=False)
    std_og_t2t_mou_6 = fields.Float(allow_nan=False)
    std_og_t2t_mou_7 = fields.Float(allow_nan=False)
    std_og_t2t_mou_8 = fields.Float(allow_nan=False)
    std_og_t2m_mou_6 = fields.Float(allow_nan=False)
    std_og_t2m_mou_7 = fields.Float(allow_nan=False)
    std_og_t2m_mou_8 = fields.Float(allow_nan=False)
    std_og_t2f_mou_6 = fields.Float(allow_nan=False)
    std_og_t2f_mou_7 = fields.Float(allow_nan=False)
    std_og_t2f_mou_8 = fields.Float(allow_nan=False)
    std_og_mou_6 = fields.Float(allow_nan=False)
    std_og_mou_7 = fields.Float(allow_nan=False)
    std_og_mou_8 = fields.Float(allow_nan=False)
    isd_og_mou_6 = fields.Float(allow_nan=False)
    isd_og_mou_7 = fields.Float(allow_nan=False)
    isd_og_mou_8 = fields.Float(allow_nan=False)
    spl_og_mou_6 = fields.Float(allow_nan=False)
    spl_og_mou_7 = fields.Float(allow_nan=False)
    spl_og_mou_8 = fields.Float(allow_nan=False)
    og_others_6 = fields.Float(allow_nan=False)
    og_others_7 = fields.Float(allow_nan=False)
    og_others_8 = fields.Float(allow_nan=False)
    loc_ic_t2t_mou_6 = fields.Float(allow_nan=False)
    loc_ic_t2t_mou_7 = fields.Float(allow_nan=False)
    loc_ic_t2t_mou_8 = fields.Float(allow_nan=False)
    loc_ic_t2m_mou_6 = fields.Float(allow_nan=False)
    loc_ic_t2m_mou_7 = fields.Float(allow_nan=False)
    loc_ic_t2m_mou_8 = fields.Float(allow_nan=False)
    loc_ic_t2f_mou_6 = fields.Float(allow_nan=False)
    loc_ic_t2f_mou_7 = fields.Float(allow_nan=False)
    loc_ic_t2f_mou_8 = fields.Float(allow_nan=False)
    loc_ic_mou_6 = fields.Float(allow_nan=False)
    loc_ic_mou_7 = fields.Float(allow_nan=False)
    loc_ic_mou_8 = fields.Float(allow_nan=False)
    std_ic_t2t_mou_6 = fields.Float(allow_nan=False)
    std_ic_t2t_mou_7 = fields.Float(allow_nan=False)
    std_ic_t2t_mou_8 = fields.Float(allow_nan=False)
    std_ic_t2m_mou_6 = fields.Float(allow_nan=False)
    std_ic_t2m_mou_7 = fields.Float(allow_nan=False)
    std_ic_t2m_mou_8 = fields.Float(allow_nan=False)
    std_ic_t2f_mou_6 = fields.Float(allow_nan=False)
    std_ic_t2f_mou_7 = fields.Float(allow_nan=False)
    std_ic_t2f_mou_8 = fields.Float(allow_nan=False)
    std_ic_mou_6 = fields.Float(allow_nan=False)
    std_ic_mou_7 = fields.Float(allow_nan=False)
    std_ic_mou_8 = fields.Float(allow_nan=False)
    spl_ic_mou_6 = fields.Float(allow_nan=False)
    spl_ic_mou_7 = fields.Float(allow_nan=False)
    spl_ic_mou_8 = fields.Float(allow_nan=False)
    isd_ic_mou_6 = fields.Float(allow_nan=False)
    isd_ic_mou_7 = fields.Float(allow_nan=False)
    isd_ic_mou_8 = fields.Float(allow_nan=False)
    ic_others_6 = fields.Float(allow_nan=False)
    ic_others_7 = fields.Float(allow_nan=False)
    ic_others_8 = fields.Float(allow_nan=False)
    total_rech_num_6 = fields.Float(allow_nan=False)
    total_rech_num_7 = fields.Float(allow_nan=False)
    total_rech_num_8 = fields.Float(allow_nan=False)
    max_rech_amt_6 = fields.Float(allow_nan=False)
    max_rech_amt_7 = fields.Float(allow_nan=False)
    max_rech_amt_8 = fields.Float(allow_nan=False)
    last_day_rch_amt_6 = fields.Float(allow_nan=False)
    last_day_rch_amt_7 = fields.Float(allow_nan=False)
    last_day_rch_amt_8 = fields.Float(allow_nan=False)
    sachet_2g_7 = fields.Float(allow_nan=False)
    sachet_2g_8 = fields.Float(allow_nan=False)
    aon = fields.Float(allow_nan=False)

    monthly_3g_6 = fields.Integer()
    monthly_2g_7 = fields.Integer()
    monthly_2g_8 = fields.Integer()
    sachet_2g_6 = fields.Integer()
    sachet_3g_7 = fields.Integer()
    monthly_3g_8 = fields.Integer()
    monthly_2g_6 = fields.Integer()
    sachet_3g_8 = fields.Integer()
    sachet_3g_6 = fields.Integer()
    monthly_3g_7 = fields.Integer()
    date_of_last_rech_6 = fields.Str()
    date_of_last_rech_7 = fields.Str()
    date_of_last_rech_8 = fields.Str()


def validate_inputs(
    *, input_data: pd.DataFrame
) -> t.Tuple[pd.DataFrame, t.Optional[dict]]:

    col = list(
        set(config.model_config.categorical + config.model_config.numerical)
        - set(
            [
                "delta_vol_3g",
                "delta_total_og_mou",
                "delta_total_ic_mou",
                "delta_vbc_3g",
                "delta_arpu",
                "delta_total_rech_amt",
            ]
        )
    )
    input_data1 = input_data[col]
    input_data1 = input_data1.replace({np.nan: None}).to_dict(orient="records")

    schema = InputSchema(many=True)
    error = None

    try:
        schema.load(input_data1)
    except ValidationError as exc:
        error = exc.messages

    return input_data, error
