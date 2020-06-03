#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib
import libpysal
import segregation
from splot._viz_utils import shift_colormap
from segregation.local import MultiLocationQuotient, MultiLocalDiversity, MultiLocalEntropy, MultiLocalSimpsonInteraction, MultiLocalSimpsonConcentration, LocalRelativeCentralization

def prep_data(file):
    """Takes json as input. Reads, cleans, changes crs and sets index to make ready for visualization. Takes the file path as an argument(string).
    """
    df = gpd.read_file(file)
    #Let's rearrange the columns so that we can more easily create lists to calc LQs
    df = df[['labels', 'year', 'CFA01', 'CFA02', 'CFA03', 'CFA04', 'CFA05',
       'CFS01', 'CFS02', 'CFS03', 'CFS04', 'CFS05', 'create_date',
       'earnings_under_1250', 'earnings_1251_3333', 'earnings_over_3333',
       'education_lths','education_hs', 'education_some_college','education_bachelors', 
       'employees_under_30', 'employees_30_54', 'employees_55plus',
       'employees_asian', 'employees_black',
       'employees_hawaiian_pi', 'employees_hispanic',
       'employees_native_american', 'employees_not_hispanic',
       'employees_twoplus_races', 'employees_white', 'employees_male', 'employees_female',
       'housing_units', 'naics_11', 'naics_21', 'naics_22', 'naics_23',
       'naics_31_33', 'naics_42', 'naics_44_45', 'naics_48_89',
       'naics_51', 'naics_52', 'naics_53', 'naics_54', 'naics_55',
       'naics_56', 'naics_61', 'naics_62', 'naics_71', 'naics_72',
       'naics_81', 'naics_90', 'population', 'total_employees',
       'node_ids', 'emp', 'geometry']]
    #lets drop fields we dont care about
    df.drop(['create_date'], axis=1, inplace=True)
    #get ready for visualization
    df['label'] = df.index
    df = df.to_crs(epsg=3857)
    return df

def generate_lists(dataframe):
    df_columns = dataframe.columns.tolist()
    earnings_list = df_columns[12:15]
    edu_list= df_columns[15:19]
    workerage_list = df_columns[19:22]
    race_list = df_columns[22:30]
    sex_list = df_columns[30:32]
    jobs_list = df_columns[33:53]
    return(workerage_list,earnings_list,jobs_list,race_list,edu_list,sex_list)

def gen_workerage(dataframe):
    df_columns = dataframe.columns.tolist()
    workerage_list = df_columns[19:22]
    return(workerage_list)

def gen_earnings(dataframe):
    df_columns = dataframe.columns.tolist()
    earnings_list = df_columns[12:15]
    return(earnings_list)

def gen_jobs(dataframe):
    df_columns = dataframe.columns.tolist()
    jobs_list = df_columns[33:53]
    return(jobs_list)

def gen_race(dataframe):
    df_columns = dataframe.columns.tolist()
    race_list = df_columns[22:30]
    return(race_list)

def gen_edu(dataframe):
    df_columns = dataframe.columns.tolist()
    edu_list = df_columns[15:19]
    return(edu_list)

def gen_sex(dataframe):
    df_columns = dataframe.columns.tolist()
    sex_list = df_columns[30:32]
    return(sex_list)

def calc_lq(dataframe):
    """
    #nested list for LQ for loop
    lehd_lists = [workerage_list,workerwage_list,jobs_list,race_list,edu_list,sex_list,firmage_list,firmsize_list]
    index_list = WorkerAgeLQIndex, WorkerWageLQIndex, JobsLQIndex, RaceLQIndex, EduLQIndex, SexLQIndex, FirmAgeLQIndex,FirmSizeLQIndex
    for_list =  zip(lehd_lists,index_list)

    for lehd_lists,index_lists in for_list:
    for items in for_list:
        items = MultiLocationQuotient(SDlehd_blocks, lehd_lists[lehd_lists])
        SDlehd_blocks['LQ_' + lehd_list[lehd_lists]] = items.statistics[:,lehd_lists]
    """

    df_columns = dataframe.columns.tolist()
    earnings_list = df_columns[12:15]
    edu_list= df_columns[15:19]
    workerage_list = df_columns[19:22]
    race_list = df_columns[22:30]
    sex_list = df_columns[30:32]
    jobs_list = df_columns[33:53]

    WorkerAgeLQIndex = MultiLocationQuotient(dataframe, workerage_list)
    EarningsLQIndex = MultiLocationQuotient(dataframe, earnings_list)
    JobsLQIndex = MultiLocationQuotient(dataframe, jobs_list)
    RaceLQIndex = MultiLocationQuotient(dataframe, race_list)
    EduLQIndex = MultiLocationQuotient(dataframe, edu_list)
    SexLQIndex = MultiLocationQuotient(dataframe, sex_list)

    for items in range(len(workerage_list)):
        dataframe['LQ_' + workerage_list[items]] = WorkerAgeLQIndex.statistics[:,items]

    for items in range(len(earnings_list)):
        dataframe['LQ_' + earnings_list[items]] = EarningsLQIndex.statistics[:,items]

    for items in range(len(jobs_list)):
        dataframe['LQ_' + jobs_list[items]] = JobsLQIndex.statistics[:,items]

    for items in range(len(race_list)):
        dataframe['LQ_' + race_list[items]] = RaceLQIndex.statistics[:,items]
    
    for items in range(len(edu_list)):
        dataframe['LQ_' + edu_list[items]] = EduLQIndex.statistics[:,items]
    
    for items in range(len(sex_list)):
        dataframe['LQ_' + sex_list[items]] = SexLQIndex.statistics[:,items]

def graph_codes(dataframe,code):
    """A function that takes the dataframe, NAICS code(string). Graphs both the original
    and the LQ of the code using hvplot. Only necessary arguments are dataframe and code. """
    
    return dataframe.hvplot(c= code, tiles='OSM', title= code, alpha=0.6) + dataframe.hvplot(c= 'LQ_' + code, tiles='OSM', title= 'LQ_' + code, alpha=0.6)

# %%




