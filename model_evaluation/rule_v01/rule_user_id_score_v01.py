# -*- coding: utf-8 -*-

# @Author: shu.wen
# @Date:   2016-05-30 15:31:15
# @Last Modified by:   shu.wen
# @Last Modified time: 2017-05-12 00:37:06
# 打分数据  /root/data/rule/RULE_USER_CATE_ACTION_SCORE_TBL.csv
__author__ = 'shu.wen'

import os
import sys
import csv
import time
import glob
import pandas
import math
import json
import numpy as np
# import pylab as pl
from sklearn import svm
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.externals import joblib
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.metrics import mean_squared_error
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_selection import f_regression
import re
import pandas
from sklearn import tree
from sklearn import ensemble
import random
from sklearn.externals.six import StringIO
# import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from collections import Counter
from sklearn.externals import joblib
from sklearn.tree import DecisionTreeClassifier
from math import isnan
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from  sklearn.ensemble import RandomForestClassifier
from  sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import KFold
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt
#import feature_trt_v5


if __name__ == '__main__':

    # step_01 读入数据集
    master_table_address = r'C:\shu.wen\opera\00_projects\99_competition\01_JData\data\rule\RULE_USER_CATE_ACTION_SCORE_TBL.csv'
    master_df = pandas.read_csv(master_table_address, sep='|', header=0)


    print 'row_cnt: %d'%(master_df.shape[0])
    print
    
    master_df_filter = master_df[
        ((master_df.USER_CATE_8_TYPE_2_CNT_06.isin([0,1,2,3,4]) & (master_df.USER_CATE_8_TYPE_5_CNT_06 == 2))
        | (master_df.USER_CATE_8_TYPE_2_CNT_06.isin([3,4,5]) & (master_df.USER_CATE_8_TYPE_6_CNT_06 > 15))
        | (master_df.USER_CATE_8_TYPE_5_CNT_05 > 1)
        | (master_df.USER_CATE_8_TYPE_2_CNT_05 > 1)
        #| (master_df.USER_CATE_8_TYPE_3_CNT_05 > 1)
        | (master_df.USER_REG_10_FLAG == 1)   
        )
        & (master_df.USER_SKU_DIS_CNT <= 3)
        & (master_df.USER_LV_CD.isin([3,4,5]))
    ]
    
    print 'row_cnt: %d'%(master_df_filter.shape[0])
    print
    
    user_id_candidate = set(master_df_filter.USER_ID)
    master_df['y_pre'] = master_df.USER_ID.apply(lambda x: 1 if x in user_id_candidate else 0)


    # step_01 读入数据集
    master_df[master_df['y_pre'] == 1][['USER_ID', 'USER_SKU_DIS_CNT']].to_csv(r'C:\shu.wen\opera\00_projects\99_competition\01_JData\data\rule\USER_ID_SCORE_CANDIDATE.csv', sep=',', index=False )
