import pytest
from churn_model import config
from churn_model.processing.load_data import load_dataset
import pandas as pd
import numpy as np



dic = [{'mobile_number': 7000543722,
  'circle_id': 109,
  'loc_og_t2o_mou': 0.0,
  'std_og_t2o_mou': 0.0,
  'loc_ic_t2o_mou': 0.0,
  'last_date_of_month_6': '6/30/2014',
  'last_date_of_month_7': '7/31/2014',
  'last_date_of_month_8': '8/31/2014',
  'arpu_6': 580.954,
  'arpu_7': 641.811,
  'arpu_8': 551.188,
  'onnet_mou_6': 997.86,
  'onnet_mou_7': 918.31,
  'onnet_mou_8': 971.68,
  'offnet_mou_6': 373.89,
  'offnet_mou_7': 465.78,
  'offnet_mou_8': 423.04,
  'roam_ic_mou_6': 0.0,
  'roam_ic_mou_7': 0.0,
  'roam_ic_mou_8': 0.0,
  'roam_og_mou_6': 0.0,
  'roam_og_mou_7': 0.0,
  'roam_og_mou_8': 0.0,
  'loc_og_t2t_mou_6': 60.03,
  'loc_og_t2t_mou_7': 111.23,
  'loc_og_t2t_mou_8': 40.06,
  'loc_og_t2m_mou_6': 56.89,
  'loc_og_t2m_mou_7': 177.73,
  'loc_og_t2m_mou_8': 118.41,
  'loc_og_t2f_mou_6': 1.71,
  'loc_og_t2f_mou_7': 2.51,
  'loc_og_t2f_mou_8': 1.26,
  'loc_og_t2c_mou_6': 0.88,
  'loc_og_t2c_mou_7': 3.31,
  'loc_og_t2c_mou_8': 0.0,
  'loc_og_mou_6': 118.64,
  'loc_og_mou_7': 291.48,
  'loc_og_mou_8': 159.74,
  'std_og_t2t_mou_6': 937.83,
  'std_og_t2t_mou_7': 807.08,
  'std_og_t2t_mou_8': 931.61,
  'std_og_t2m_mou_6': 314.39,
  'std_og_t2m_mou_7': 283.34,
  'std_og_t2m_mou_8': 303.36,
  'std_og_t2f_mou_6': 0.0,
  'std_og_t2f_mou_7': 0.0,
  'std_og_t2f_mou_8': 0.0,
  'std_og_t2c_mou_6': 0.0,
  'std_og_t2c_mou_7': 0.0,
  'std_og_t2c_mou_8': 0.0,
  'std_og_mou_6': 1252.23,
  'std_og_mou_7': 1090.43,
  'std_og_mou_8': 1234.98,
  'isd_og_mou_6': 0.0,
  'isd_og_mou_7': 0.0,
  'isd_og_mou_8': 0.0,
  'spl_og_mou_6': 2.13,
  'spl_og_mou_7': 8.23,
  'spl_og_mou_8': 1.76,
  'og_others_6': 0.99,
  'og_others_7': 0.0,
  'og_others_8': 0.0,
  'total_og_mou_6': 1374.01,
  'total_og_mou_7': 1390.14,
  'total_og_mou_8': 1396.49,
  'loc_ic_t2t_mou_6': 47.34,
  'loc_ic_t2t_mou_7': 31.24,
  'loc_ic_t2t_mou_8': 27.58,
  'loc_ic_t2m_mou_6': 98.99,
  'loc_ic_t2m_mou_7': 228.44,
  'loc_ic_t2m_mou_8': 134.73,
  'loc_ic_t2f_mou_6': 10.14,
  'loc_ic_t2f_mou_7': 17.06,
  'loc_ic_t2f_mou_8': 8.88,
  'loc_ic_mou_6': 156.49,
  'loc_ic_mou_7': 276.76,
  'loc_ic_mou_8': 171.19,
  'std_ic_t2t_mou_6': 12.03,
  'std_ic_t2t_mou_7': 8.91,
  'std_ic_t2t_mou_8': 16.13,
  'std_ic_t2m_mou_6': 16.34,
  'std_ic_t2m_mou_7': 31.86,
  'std_ic_t2m_mou_8': 15.74,
  'std_ic_t2f_mou_6': 0.0,
  'std_ic_t2f_mou_7': 0.0,
  'std_ic_t2f_mou_8': 0.0,
  'std_ic_t2o_mou_6': 0.0,
  'std_ic_t2o_mou_7': 0.0,
  'std_ic_t2o_mou_8': 0.0,
  'std_ic_mou_6': 28.38,
  'std_ic_mou_7': 40.78,
  'std_ic_mou_8': 31.88,
  'total_ic_mou_6': 184.88,
  'total_ic_mou_7': 317.54,
  'total_ic_mou_8': 203.08,
  'spl_ic_mou_6': 0.0,
  'spl_ic_mou_7': 0.0,
  'spl_ic_mou_8': 0.0,
  'isd_ic_mou_6': 0.0,
  'isd_ic_mou_7': 0.0,
  'isd_ic_mou_8': 0.0,
  'ic_others_6': 0.0,
  'ic_others_7': 0.0,
  'ic_others_8': 0.0,
  'total_rech_num_6': 10,
  'total_rech_num_7': 10,
  'total_rech_num_8': 8,
  'total_rech_amt_6': 655,
  'total_rech_amt_7': 707,
  'total_rech_amt_8': 763,
  'max_rech_amt_6': 110,
  'max_rech_amt_7': 128,
  'max_rech_amt_8': 150,
  'date_of_last_rech_6': '6/28/2014',
  'date_of_last_rech_7': '7/29/2014',
  'date_of_last_rech_8': '8/31/2014',
  'last_day_rch_amt_6': 110,
  'last_day_rch_amt_7': 128,
  'last_day_rch_amt_8': 130,
  'date_of_last_rech_data_6': None,
  'date_of_last_rech_data_7': '7/11/2014',
  'date_of_last_rech_data_8': None,
  'max_rech_data_6': None,
  'max_rech_data_7': 8.0,
  'max_rech_data_8': None,
  'count_rech_2g_6': None,
  'count_rech_2g_7': 1.0,
  'count_rech_2g_8': None,
  'count_rech_3g_6': None,
  'count_rech_3g_7': 0.0,
  'count_rech_3g_8': None,
  'vol_2g_mb_6': 0.0,
  'vol_2g_mb_7': 0.0,
  'vol_2g_mb_8': 0.0,
  'vol_3g_mb_6': 0.0,
  'vol_3g_mb_7': 0.0,
  'vol_3g_mb_8': 0.0,
  'arpu_3g_6': None,
  'arpu_3g_7': 0.0,
  'arpu_3g_8': None,
  'arpu_2g_6': None,
  'arpu_2g_7': 0.0,
  'arpu_2g_8': None,
  'night_pck_user_6': None,
  'night_pck_user_7': 1.0,
  'night_pck_user_8': None,
  'monthly_2g_6': 0,
  'monthly_2g_7': 0,
  'monthly_2g_8': 0,
  'sachet_2g_6': 0,
  'sachet_2g_7': 1,
  'sachet_2g_8': 0,
  'monthly_3g_6': 0,
  'monthly_3g_7': 0,
  'monthly_3g_8': 0,
  'sachet_3g_6': 0,
  'sachet_3g_7': 0,
  'sachet_3g_8': 0,
  'fb_user_6': None,
  'fb_user_7': 0.0,
  'fb_user_8': None,
  'aon': 415,
  'aug_vbc_3g': 0.0,
  'jul_vbc_3g': 0.0,
  'jun_vbc_3g': 0.0,
  'total_rech_data_amt_6': None,
  'total_rech_data_amt_7': 8.0,
  'total_rech_data_amt_8': None},
 {'mobile_number': 7000726888,
  'circle_id': 109,
  'loc_og_t2o_mou': 0.0,
  'std_og_t2o_mou': 0.0,
  'loc_ic_t2o_mou': 0.0,
  'last_date_of_month_6': '6/30/2014',
  'last_date_of_month_7': '7/31/2014',
  'last_date_of_month_8': '8/31/2014',
  'arpu_6': 215.06,
  'arpu_7': 1148.263,
  'arpu_8': 102.3,
  'onnet_mou_6': 13.33,
  'onnet_mou_7': 60.29,
  'onnet_mou_8': 3.71,
  'offnet_mou_6': 307.58,
  'offnet_mou_7': 3202.44,
  'offnet_mou_8': 209.84,
  'roam_ic_mou_6': 20.23,
  'roam_ic_mou_7': 0.0,
  'roam_ic_mou_8': 0.0,
  'roam_og_mou_6': 56.71,
  'roam_og_mou_7': 0.0,
  'roam_og_mou_8': 0.0,
  'loc_og_t2t_mou_6': 0.0,
  'loc_og_t2t_mou_7': 32.43,
  'loc_og_t2t_mou_8': 0.65,
  'loc_og_t2m_mou_6': 8.78,
  'loc_og_t2m_mou_7': 100.99,
  'loc_og_t2m_mou_8': 11.31,
  'loc_og_t2f_mou_6': 0.0,
  'loc_og_t2f_mou_7': 4.69,
  'loc_og_t2f_mou_8': 1.88,
  'loc_og_t2c_mou_6': 0.0,
  'loc_og_t2c_mou_7': 9.53,
  'loc_og_t2c_mou_8': 3.78,
  'loc_og_mou_6': 8.78,
  'loc_og_mou_7': 138.13,
  'loc_og_mou_8': 13.84,
  'std_og_t2t_mou_6': 0.0,
  'std_og_t2t_mou_7': 27.86,
  'std_og_t2t_mou_8': 3.06,
  'std_og_t2m_mou_6': 255.83,
  'std_og_t2m_mou_7': 3076.39,
  'std_og_t2m_mou_8': 185.48,
  'std_og_t2f_mou_6': 0.0,
  'std_og_t2f_mou_7': 11.33,
  'std_og_t2f_mou_8': 7.38,
  'std_og_t2c_mou_6': 0.0,
  'std_og_t2c_mou_7': 0.0,
  'std_og_t2c_mou_8': 0.0,
  'std_og_mou_6': 255.83,
  'std_og_mou_7': 3115.59,
  'std_og_mou_8': 195.93,
  'isd_og_mou_6': 0.0,
  'isd_og_mou_7': 0.0,
  'isd_og_mou_8': 0.0,
  'spl_og_mou_6': 0.0,
  'spl_og_mou_7': 12.51,
  'spl_og_mou_8': 4.25,
  'og_others_6': 0.0,
  'og_others_7': 0.0,
  'og_others_8': 0.0,
  'total_og_mou_6': 264.61,
  'total_og_mou_7': 3266.24,
  'total_og_mou_8': 214.03,
  'loc_ic_t2t_mou_6': 2.01,
  'loc_ic_t2t_mou_7': 16.89,
  'loc_ic_t2t_mou_8': 1.94,
  'loc_ic_t2m_mou_6': 0.6,
  'loc_ic_t2m_mou_7': 75.88,
  'loc_ic_t2m_mou_8': 39.91,
  'loc_ic_t2f_mou_6': 0.0,
  'loc_ic_t2f_mou_7': 7.99,
  'loc_ic_t2f_mou_8': 9.18,
  'loc_ic_mou_6': 2.61,
  'loc_ic_mou_7': 100.78,
  'loc_ic_mou_8': 51.04,
  'std_ic_t2t_mou_6': 0.0,
  'std_ic_t2t_mou_7': 0.0,
  'std_ic_t2t_mou_8': 10.43,
  'std_ic_t2m_mou_6': 13.09,
  'std_ic_t2m_mou_7': 58.76,
  'std_ic_t2m_mou_8': 55.29,
  'std_ic_t2f_mou_6': 0.0,
  'std_ic_t2f_mou_7': 0.0,
  'std_ic_t2f_mou_8': 0.0,
  'std_ic_t2o_mou_6': 0.0,
  'std_ic_t2o_mou_7': 0.0,
  'std_ic_t2o_mou_8': 0.0,
  'std_ic_mou_6': 13.09,
  'std_ic_mou_7': 58.76,
  'std_ic_mou_8': 65.73,
  'total_ic_mou_6': 15.71,
  'total_ic_mou_7': 159.54,
  'total_ic_mou_8': 116.78,
  'spl_ic_mou_6': 0.0,
  'spl_ic_mou_7': 0.0,
  'spl_ic_mou_8': 0.0,
  'isd_ic_mou_6': 0.0,
  'isd_ic_mou_7': 0.0,
  'isd_ic_mou_8': 0.0,
  'ic_others_6': 0.0,
  'ic_others_7': 0.0,
  'ic_others_8': 0.0,
  'total_rech_num_6': 4,
  'total_rech_num_7': 13,
  'total_rech_num_8': 0,
  'total_rech_amt_6': 256,
  'total_rech_amt_7': 1352,
  'total_rech_amt_8': 0,
  'max_rech_amt_6': 110,
  'max_rech_amt_7': 130,
  'max_rech_amt_8': 0,
  'date_of_last_rech_6': '6/30/2014',
  'date_of_last_rech_7': '7/30/2014',
  'date_of_last_rech_8': None,
  'last_day_rch_amt_6': 110,
  'last_day_rch_amt_7': 130,
  'last_day_rch_amt_8': 0,
  'date_of_last_rech_data_6': None,
  'date_of_last_rech_data_7': None,
  'date_of_last_rech_data_8': None,
  'max_rech_data_6': None,
  'max_rech_data_7': None,
  'max_rech_data_8': None,
  'count_rech_2g_6': None,
  'count_rech_2g_7': None,
  'count_rech_2g_8': None,
  'count_rech_3g_6': None,
  'count_rech_3g_7': None,
  'count_rech_3g_8': None,
  'vol_2g_mb_6': 0.0,
  'vol_2g_mb_7': 0.0,
  'vol_2g_mb_8': 0.0,
  'vol_3g_mb_6': 0.0,
  'vol_3g_mb_7': 0.0,
  'vol_3g_mb_8': 0.0,
  'arpu_3g_6': None,
  'arpu_3g_7': None,
  'arpu_3g_8': None,
  'arpu_2g_6': None,
  'arpu_2g_7': None,
  'arpu_2g_8': None,
  'night_pck_user_6': None,
  'night_pck_user_7': None,
  'night_pck_user_8': None,
  'monthly_2g_6': 0,
  'monthly_2g_7': 0,
  'monthly_2g_8': 0,
  'sachet_2g_6': 0,
  'sachet_2g_7': 0,
  'sachet_2g_8': 0,
  'monthly_3g_6': 0,
  'monthly_3g_7': 0,
  'monthly_3g_8': 0,
  'sachet_3g_6': 0,
  'sachet_3g_7': 0,
  'sachet_3g_8': 0,
  'fb_user_6': None,
  'fb_user_7': None,
  'fb_user_8': None,
  'aon': 695,
  'aug_vbc_3g': 0.0,
  'jul_vbc_3g': 0.0,
  'jun_vbc_3g': 0.0,
  'total_rech_data_amt_6': None,
  'total_rech_data_amt_7': None,
  'total_rech_data_amt_8': None},
 {'mobile_number': 7000188324,
  'circle_id': 109,
  'loc_og_t2o_mou': 0.0,
  'std_og_t2o_mou': 0.0,
  'loc_ic_t2o_mou': 0.0,
  'last_date_of_month_6': '6/30/2014',
  'last_date_of_month_7': '7/31/2014',
  'last_date_of_month_8': '8/31/2014',
  'arpu_6': 610.774,
  'arpu_7': 637.067,
  'arpu_8': 0.0,
  'onnet_mou_6': 993.18,
  'onnet_mou_7': 702.88,
  'onnet_mou_8': None,
  'offnet_mou_6': 340.88,
  'offnet_mou_7': 437.41,
  'offnet_mou_8': None,
  'roam_ic_mou_6': 0.0,
  'roam_ic_mou_7': 1.65,
  'roam_ic_mou_8': None,
  'roam_og_mou_6': 0.0,
  'roam_og_mou_7': 92.14,
  'roam_og_mou_8': None,
  'loc_og_t2t_mou_6': 6.86,
  'loc_og_t2t_mou_7': 4.94,
  'loc_og_t2t_mou_8': None,
  'loc_og_t2m_mou_6': 55.16,
  'loc_og_t2m_mou_7': 91.58,
  'loc_og_t2m_mou_8': None,
  'loc_og_t2f_mou_6': 0.0,
  'loc_og_t2f_mou_7': 0.0,
  'loc_og_t2f_mou_8': None,
  'loc_og_t2c_mou_6': 0.0,
  'loc_og_t2c_mou_7': 0.0,
  'loc_og_t2c_mou_8': None,
  'loc_og_mou_6': 62.03,
  'loc_og_mou_7': 96.53,
  'loc_og_mou_8': None,
  'std_og_t2t_mou_6': 986.31,
  'std_og_t2t_mou_7': 660.49,
  'std_og_t2t_mou_8': None,
  'std_og_t2m_mou_6': 276.11,
  'std_og_t2m_mou_7': 287.99,
  'std_og_t2m_mou_8': None,
  'std_og_t2f_mou_6': 0.0,
  'std_og_t2f_mou_7': 1.78,
  'std_og_t2f_mou_8': None,
  'std_og_t2c_mou_6': 0.0,
  'std_og_t2c_mou_7': 0.0,
  'std_og_t2c_mou_8': None,
  'std_og_mou_6': 1262.43,
  'std_og_mou_7': 950.28,
  'std_og_mou_8': None,
  'isd_og_mou_6': 7.14,
  'isd_og_mou_7': 1.83,
  'isd_og_mou_8': None,
  'spl_og_mou_6': 2.45,
  'spl_og_mou_7': 0.0,
  'spl_og_mou_8': None,
  'og_others_6': 0.0,
  'og_others_7': 0.0,
  'og_others_8': None,
  'total_og_mou_6': 1334.06,
  'total_og_mou_7': 1048.64,
  'total_og_mou_8': 0.0,
  'loc_ic_t2t_mou_6': 7.46,
  'loc_ic_t2t_mou_7': 8.73,
  'loc_ic_t2t_mou_8': None,
  'loc_ic_t2m_mou_6': 105.69,
  'loc_ic_t2m_mou_7': 88.21,
  'loc_ic_t2m_mou_8': None,
  'loc_ic_t2f_mou_6': 0.0,
  'loc_ic_t2f_mou_7': 0.0,
  'loc_ic_t2f_mou_8': None,
  'loc_ic_mou_6': 113.16,
  'loc_ic_mou_7': 96.94,
  'loc_ic_mou_8': None,
  'std_ic_t2t_mou_6': 42.83,
  'std_ic_t2t_mou_7': 3.86,
  'std_ic_t2t_mou_8': None,
  'std_ic_t2m_mou_6': 12.24,
  'std_ic_t2m_mou_7': 17.68,
  'std_ic_t2m_mou_8': None,
  'std_ic_t2f_mou_6': 0.0,
  'std_ic_t2f_mou_7': 0.0,
  'std_ic_t2f_mou_8': None,
  'std_ic_t2o_mou_6': 0.0,
  'std_ic_t2o_mou_7': 0.0,
  'std_ic_t2o_mou_8': None,
  'std_ic_mou_6': 55.08,
  'std_ic_mou_7': 21.54,
  'std_ic_mou_8': None,
  'total_ic_mou_6': 191.18,
  'total_ic_mou_7': 142.21,
  'total_ic_mou_8': 0.0,
  'spl_ic_mou_6': 0.0,
  'spl_ic_mou_7': 0.0,
  'spl_ic_mou_8': None,
  'isd_ic_mou_6': 21.71,
  'isd_ic_mou_7': 5.46,
  'isd_ic_mou_8': None,
  'ic_others_6': 1.21,
  'ic_others_7': 18.25,
  'ic_others_8': None,
  'total_rech_num_6': 9,
  'total_rech_num_7': 8,
  'total_rech_num_8': 3,
  'total_rech_amt_6': 726,
  'total_rech_amt_7': 740,
  'total_rech_amt_8': 0,
  'max_rech_amt_6': 110,
  'max_rech_amt_7': 128,
  'max_rech_amt_8': 0,
  'date_of_last_rech_6': '6/25/2014',
  'date_of_last_rech_7': '7/24/2014',
  'date_of_last_rech_8': '8/19/2014',
  'last_day_rch_amt_6': 110,
  'last_day_rch_amt_7': 110,
  'last_day_rch_amt_8': 0,
  'date_of_last_rech_data_6': None,
  'date_of_last_rech_data_7': None,
  'date_of_last_rech_data_8': None,
  'max_rech_data_6': None,
  'max_rech_data_7': None,
  'max_rech_data_8': None,
  'count_rech_2g_6': None,
  'count_rech_2g_7': None,
  'count_rech_2g_8': None,
  'count_rech_3g_6': None,
  'count_rech_3g_7': None,
  'count_rech_3g_8': None,
  'vol_2g_mb_6': 0.0,
  'vol_2g_mb_7': 0.0,
  'vol_2g_mb_8': 0.0,
  'vol_3g_mb_6': 0.0,
  'vol_3g_mb_7': 0.0,
  'vol_3g_mb_8': 0.0,
  'arpu_3g_6': None,
  'arpu_3g_7': None,
  'arpu_3g_8': None,
  'arpu_2g_6': None,
  'arpu_2g_7': None,
  'arpu_2g_8': None,
  'night_pck_user_6': None,
  'night_pck_user_7': None,
  'night_pck_user_8': None,
  'monthly_2g_6': 0,
  'monthly_2g_7': 0,
  'monthly_2g_8': 0,
  'sachet_2g_6': 0,
  'sachet_2g_7': 0,
  'sachet_2g_8': 0,
  'monthly_3g_6': 0,
  'monthly_3g_7': 0,
  'monthly_3g_8': 0,
  'sachet_3g_6': 0,
  'sachet_3g_7': 0,
  'sachet_3g_8': 0,
  'fb_user_6': None,
  'fb_user_7': None,
  'fb_user_8': None,
  'aon': 597,
  'aug_vbc_3g': 0.0,
  'jul_vbc_3g': 0.0,
  'jun_vbc_3g': 0.0,
  'total_rech_data_amt_6': None,
  'total_rech_data_amt_7': None,
  'total_rech_data_amt_8': None},
 {'mobile_number': 7001728632,
  'circle_id': 109,
  'loc_og_t2o_mou': 0.0,
  'std_og_t2o_mou': 0.0,
  'loc_ic_t2o_mou': 0.0,
  'last_date_of_month_6': '6/30/2014',
  'last_date_of_month_7': '7/31/2014',
  'last_date_of_month_8': '8/31/2014',
  'arpu_6': 1091.43,
  'arpu_7': 1752.845,
  'arpu_8': 840.061,
  'onnet_mou_6': 208.64,
  'onnet_mou_7': 289.34,
  'onnet_mou_8': 226.64,
  'offnet_mou_6': 462.53,
  'offnet_mou_7': 759.63,
  'offnet_mou_8': 650.71,
  'roam_ic_mou_6': 0.0,
  'roam_ic_mou_7': 0.0,
  'roam_ic_mou_8': 0.0,
  'roam_og_mou_6': 0.0,
  'roam_og_mou_7': 0.0,
  'roam_og_mou_8': 0.0,
  'loc_og_t2t_mou_6': 175.76,
  'loc_og_t2t_mou_7': 289.34,
  'loc_og_t2t_mou_8': 218.19,
  'loc_og_t2m_mou_6': 334.48,
  'loc_og_t2m_mou_7': 539.09,
  'loc_og_t2m_mou_8': 633.36,
  'loc_og_t2f_mou_6': 0.0,
  'loc_og_t2f_mou_7': 0.96,
  'loc_og_t2f_mou_8': 1.23,
  'loc_og_t2c_mou_6': 0.0,
  'loc_og_t2c_mou_7': 0.61,
  'loc_og_t2c_mou_8': 0.0,
  'loc_og_mou_6': 510.24,
  'loc_og_mou_7': 829.41,
  'loc_og_mou_8': 852.79,
  'std_og_t2t_mou_6': 32.88,
  'std_og_t2t_mou_7': 0.0,
  'std_og_t2t_mou_8': 8.45,
  'std_og_t2m_mou_6': 7.43,
  'std_og_t2m_mou_7': 29.14,
  'std_og_t2m_mou_8': 11.94,
  'std_og_t2f_mou_6': 0.0,
  'std_og_t2f_mou_7': 0.0,
  'std_og_t2f_mou_8': 0.0,
  'std_og_t2c_mou_6': 0.0,
  'std_og_t2c_mou_7': 0.0,
  'std_og_t2c_mou_8': 0.0,
  'std_og_mou_6': 40.31,
  'std_og_mou_7': 29.14,
  'std_og_mou_8': 20.39,
  'isd_og_mou_6': 76.96,
  'isd_og_mou_7': 175.36,
  'isd_og_mou_8': 0.0,
  'spl_og_mou_6': 43.65,
  'spl_og_mou_7': 19.36,
  'spl_og_mou_8': 6.83,
  'og_others_6': 0.21,
  'og_others_7': 0.0,
  'og_others_8': 0.0,
  'total_og_mou_6': 671.39,
  'total_og_mou_7': 1053.29,
  'total_og_mou_8': 880.03,
  'loc_ic_t2t_mou_6': 32.04,
  'loc_ic_t2t_mou_7': 54.33,
  'loc_ic_t2t_mou_8': 33.23,
  'loc_ic_t2m_mou_6': 143.11,
  'loc_ic_t2m_mou_7': 320.48,
  'loc_ic_t2m_mou_8': 214.44,
  'loc_ic_t2f_mou_6': 0.0,
  'loc_ic_t2f_mou_7': 0.0,
  'loc_ic_t2f_mou_8': 0.31,
  'loc_ic_mou_6': 175.16,
  'loc_ic_mou_7': 374.81,
  'loc_ic_mou_8': 247.99,
  'std_ic_t2t_mou_6': 6.23,
  'std_ic_t2t_mou_7': 1.64,
  'std_ic_t2t_mou_8': 0.0,
  'std_ic_t2m_mou_6': 23.04,
  'std_ic_t2m_mou_7': 31.06,
  'std_ic_t2m_mou_8': 25.93,
  'std_ic_t2f_mou_6': 0.0,
  'std_ic_t2f_mou_7': 0.0,
  'std_ic_t2f_mou_8': 0.0,
  'std_ic_t2o_mou_6': 0.0,
  'std_ic_t2o_mou_7': 0.0,
  'std_ic_t2o_mou_8': 0.0,
  'std_ic_mou_6': 29.28,
  'std_ic_mou_7': 32.71,
  'std_ic_mou_8': 25.93,
  'total_ic_mou_6': 243.16,
  'total_ic_mou_7': 469.28,
  'total_ic_mou_8': 273.93,
  'spl_ic_mou_6': 0.0,
  'spl_ic_mou_7': 0.0,
  'spl_ic_mou_8': 0.0,
  'isd_ic_mou_6': 38.71,
  'isd_ic_mou_7': 61.74,
  'isd_ic_mou_8': 0.0,
  'ic_others_6': 0.0,
  'ic_others_7': 0.0,
  'ic_others_8': 0.0,
  'total_rech_num_6': 13,
  'total_rech_num_7': 15,
  'total_rech_num_8': 7,
  'total_rech_amt_6': 1420,
  'total_rech_amt_7': 1988,
  'total_rech_amt_8': 1048,
  'max_rech_amt_6': 128,
  'max_rech_amt_7': 200,
  'max_rech_amt_8': 200,
  'date_of_last_rech_6': '6/28/2014',
  'date_of_last_rech_7': '7/26/2014',
  'date_of_last_rech_8': '8/28/2014',
  'last_day_rch_amt_6': 128,
  'last_day_rch_amt_7': 150,
  'last_day_rch_amt_8': 130,
  'date_of_last_rech_data_6': None,
  'date_of_last_rech_data_7': None,
  'date_of_last_rech_data_8': None,
  'max_rech_data_6': None,
  'max_rech_data_7': None,
  'max_rech_data_8': None,
  'count_rech_2g_6': None,
  'count_rech_2g_7': None,
  'count_rech_2g_8': None,
  'count_rech_3g_6': None,
  'count_rech_3g_7': None,
  'count_rech_3g_8': None,
  'vol_2g_mb_6': 0.0,
  'vol_2g_mb_7': 0.0,
  'vol_2g_mb_8': 0.0,
  'vol_3g_mb_6': 0.0,
  'vol_3g_mb_7': 0.0,
  'vol_3g_mb_8': 0.0,
  'arpu_3g_6': None,
  'arpu_3g_7': None,
  'arpu_3g_8': None,
  'arpu_2g_6': None,
  'arpu_2g_7': None,
  'arpu_2g_8': None,
  'night_pck_user_6': None,
  'night_pck_user_7': None,
  'night_pck_user_8': None,
  'monthly_2g_6': 0,
  'monthly_2g_7': 0,
  'monthly_2g_8': 0,
  'sachet_2g_6': 0,
  'sachet_2g_7': 0,
  'sachet_2g_8': 0,
  'monthly_3g_6': 0,
  'monthly_3g_7': 0,
  'monthly_3g_8': 0,
  'sachet_3g_6': 0,
  'sachet_3g_7': 0,
  'sachet_3g_8': 0,
  'fb_user_6': None,
  'fb_user_7': None,
  'fb_user_8': None,
  'aon': 3557,
  'aug_vbc_3g': 0.0,
  'jul_vbc_3g': 0.0,
  'jun_vbc_3g': 0.0,
  'total_rech_data_amt_6': None,
  'total_rech_data_amt_7': None,
  'total_rech_data_amt_8': None},
 {'mobile_number': 7000874406,
  'circle_id': 109,
  'loc_og_t2o_mou': 0.0,
  'std_og_t2o_mou': 0.0,
  'loc_ic_t2o_mou': 0.0,
  'last_date_of_month_6': '6/30/2014',
  'last_date_of_month_7': '7/31/2014',
  'last_date_of_month_8': '8/31/2014',
  'arpu_6': 557.676,
  'arpu_7': 391.77,
  'arpu_8': 324.604,
  'onnet_mou_6': 104.34,
  'onnet_mou_7': 196.93,
  'onnet_mou_8': 362.78,
  'offnet_mou_6': 881.56,
  'offnet_mou_7': 471.66,
  'offnet_mou_8': 186.66,
  'roam_ic_mou_6': 0.0,
  'roam_ic_mou_7': 0.0,
  'roam_ic_mou_8': 0.0,
  'roam_og_mou_6': 0.0,
  'roam_og_mou_7': 0.0,
  'roam_og_mou_8': 0.0,
  'loc_og_t2t_mou_6': 37.64,
  'loc_og_t2t_mou_7': 18.46,
  'loc_og_t2t_mou_8': 46.78,
  'loc_og_t2m_mou_6': 293.26,
  'loc_og_t2m_mou_7': 193.09,
  'loc_og_t2m_mou_8': 112.59,
  'loc_og_t2f_mou_6': 44.51,
  'loc_og_t2f_mou_7': 25.16,
  'loc_og_t2f_mou_8': 22.33,
  'loc_og_t2c_mou_6': 0.0,
  'loc_og_t2c_mou_7': 0.0,
  'loc_og_t2c_mou_8': 0.0,
  'loc_og_mou_6': 375.43,
  'loc_og_mou_7': 236.73,
  'loc_og_mou_8': 181.71,
  'std_og_t2t_mou_6': 66.69,
  'std_og_t2t_mou_7': 178.46,
  'std_og_t2t_mou_8': 315.99,
  'std_og_t2m_mou_6': 543.78,
  'std_og_t2m_mou_7': 253.39,
  'std_og_t2m_mou_8': 51.73,
  'std_og_t2f_mou_6': 0.0,
  'std_og_t2f_mou_7': 0.0,
  'std_og_t2f_mou_8': 0.0,
  'std_og_t2c_mou_6': 0.0,
  'std_og_t2c_mou_7': 0.0,
  'std_og_t2c_mou_8': 0.0,
  'std_og_mou_6': 610.48,
  'std_og_mou_7': 431.86,
  'std_og_mou_8': 367.73,
  'isd_og_mou_6': 0.0,
  'isd_og_mou_7': 0.0,
  'isd_og_mou_8': 0.0,
  'spl_og_mou_6': 0.0,
  'spl_og_mou_7': 0.0,
  'spl_og_mou_8': 0.0,
  'og_others_6': 0.0,
  'og_others_7': 0.0,
  'og_others_8': 0.0,
  'total_og_mou_6': 985.91,
  'total_og_mou_7': 668.59,
  'total_og_mou_8': 549.44,
  'loc_ic_t2t_mou_6': 16.74,
  'loc_ic_t2t_mou_7': 9.69,
  'loc_ic_t2t_mou_8': 15.13,
  'loc_ic_t2m_mou_6': 272.26,
  'loc_ic_t2m_mou_7': 147.56,
  'loc_ic_t2m_mou_8': 103.28,
  'loc_ic_t2f_mou_6': 200.19,
  'loc_ic_t2f_mou_7': 80.26,
  'loc_ic_t2f_mou_8': 27.79,
  'loc_ic_mou_6': 489.21,
  'loc_ic_mou_7': 237.53,
  'loc_ic_mou_8': 146.21,
  'std_ic_t2t_mou_6': 0.7,
  'std_ic_t2t_mou_7': 3.18,
  'std_ic_t2t_mou_8': 1.83,
  'std_ic_t2m_mou_6': 0.7,
  'std_ic_t2m_mou_7': 5.71,
  'std_ic_t2m_mou_8': 12.49,
  'std_ic_t2f_mou_6': 0.0,
  'std_ic_t2f_mou_7': 0.0,
  'std_ic_t2f_mou_8': 0.0,
  'std_ic_t2o_mou_6': 0.0,
  'std_ic_t2o_mou_7': 0.0,
  'std_ic_t2o_mou_8': 0.0,
  'std_ic_mou_6': 1.4,
  'std_ic_mou_7': 8.89,
  'std_ic_mou_8': 14.33,
  'total_ic_mou_6': 490.61,
  'total_ic_mou_7': 250.33,
  'total_ic_mou_8': 160.86,
  'spl_ic_mou_6': 0.0,
  'spl_ic_mou_7': 0.0,
  'spl_ic_mou_8': 0.0,
  'isd_ic_mou_6': 0.0,
  'isd_ic_mou_7': 0.0,
  'isd_ic_mou_8': 0.0,
  'ic_others_6': 0.0,
  'ic_others_7': 3.9,
  'ic_others_8': 0.31,
  'total_rech_num_6': 7,
  'total_rech_num_7': 5,
  'total_rech_num_8': 7,
  'total_rech_amt_6': 687,
  'total_rech_amt_7': 427,
  'total_rech_amt_8': 457,
  'max_rech_amt_6': 110,
  'max_rech_amt_7': 110,
  'max_rech_amt_8': 130,
  'date_of_last_rech_6': '6/26/2014',
  'date_of_last_rech_7': '7/20/2014',
  'date_of_last_rech_8': '8/31/2014',
  'last_day_rch_amt_6': 110,
  'last_day_rch_amt_7': 110,
  'last_day_rch_amt_8': 0,
  'date_of_last_rech_data_6': None,
  'date_of_last_rech_data_7': None,
  'date_of_last_rech_data_8': '8/31/2014',
  'max_rech_data_6': None,
  'max_rech_data_7': None,
  'max_rech_data_8': 23.0,
  'count_rech_2g_6': None,
  'count_rech_2g_7': None,
  'count_rech_2g_8': 3.0,
  'count_rech_3g_6': None,
  'count_rech_3g_7': None,
  'count_rech_3g_8': 0.0,
  'vol_2g_mb_6': 0.0,
  'vol_2g_mb_7': 0.0,
  'vol_2g_mb_8': 0.22,
  'vol_3g_mb_6': 0.0,
  'vol_3g_mb_7': 0.0,
  'vol_3g_mb_8': 0.0,
  'arpu_3g_6': None,
  'arpu_3g_7': None,
  'arpu_3g_8': 0.0,
  'arpu_2g_6': None,
  'arpu_2g_7': None,
  'arpu_2g_8': 2.4,
  'night_pck_user_6': None,
  'night_pck_user_7': None,
  'night_pck_user_8': 0.0,
  'monthly_2g_6': 0,
  'monthly_2g_7': 0,
  'monthly_2g_8': 0,
  'sachet_2g_6': 0,
  'sachet_2g_7': 0,
  'sachet_2g_8': 3,
  'monthly_3g_6': 0,
  'monthly_3g_7': 0,
  'monthly_3g_8': 0,
  'sachet_3g_6': 0,
  'sachet_3g_7': 0,
  'sachet_3g_8': 0,
  'fb_user_6': None,
  'fb_user_7': None,
  'fb_user_8': 0.0,
  'aon': 461,
  'aug_vbc_3g': 0.0,
  'jul_vbc_3g': 0.0,
  'jun_vbc_3g': 0.0,
  'total_rech_data_amt_6': None,
  'total_rech_data_amt_7': None,
  'total_rech_data_amt_8': 207.0}]

y = [{'Churn': 1}, {'Churn': 0}, {'Churn': 0}, {'Churn': 0}, {'Churn': 0}]

@pytest.fixture(scope='session')
def input_data():

#     x_train = load_dataset(filename=config.app_config.x_train)
#     y_train = load_dataset(filename=config.app_config.y_train)
    x_train = pd.DataFrame(dic)
    #x_train = x_train.replace({None:np.nan})
    y_train = pd.DataFrame(y)

    return x_train, y_train
