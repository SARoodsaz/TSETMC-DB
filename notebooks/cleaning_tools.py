''' cleaning_tools '''

# Python program to create a module

import pandas as pd
import numpy as np
import regex as re
import persiantools as ps
import datetime as dte
import networkx as nx
import streamlit as lt
import jdatetime as jdt
from datetime import time
import statsmodels as stat
import os
import glob
from glob import glob
from operator import itemgetter
from persiantools import characters
from persiantools.jdatetime import JalaliDate
import persiantools
import re
from re import search
import itertools
from statistics import mode
import random
import matplotlib.pyplot as plt
from datetime import datetime as dat
from numpy import random as nprnd
from pyvis.network import Network
from networkx import NetworkXError
from networkx import bipartite
import networkx.algorithms.connectivity as nxcon
from networkx.algorithms import approximation as nxp
import networkx.algorithms.community as nxcom
import math
import time
from difflib import SequenceMatcher
import html
import random
from faker import Faker

m_list = 'list of functions is [excel_to_csv, csv_to_xlsx, P_E, words_clean, remove_extra_space, remove_space, date_timestamp, date_corrector, finding_value_str,finding_value_str,checking_words,checking_company_person,insert_code,df_sorting,remove_dup,find_null,df_null_value,finding_diffrences,reading_file,cleanning_dataframe,group_by_sum,treshold_and_select,stats_simple_clustering]'
definition = 'this madule contain cleaning tools for cleansing data it can cleaning string,price,numbers as codes, date,time and etc'

def excel_to_csv(path,dirr):
    extention='xlsx'
    os.chdir(path)
    for file in os.listdir(path):
        file_xlsx= pd.read_ecxel(file)
        file_xlsx.to_csv(dirr+"\\"+file.split('.')[0]+".csv",index=False, encoding='utf-8-sig')
excel_to_csv_dif= 'this function is for changing type of dataframe file from excel to csv'

def csv_to_xlsx(path,dirr):
    extention='csv'
    os.chdir(path)
    for file in os.listdir(path):
        file_xlsx= pd.read_csv(file)
        file_xlsx.to_excel(dirr+"\\"+file.split('.')[0]+".xlsx",index=False)
csv_to_xlsx_def = 'this function is for vhanging dataframe file from csv to excell format'

def P_E (df):
    def unique_value(df,column):
        x= df[column].drop_duplicates()
        return x
    columns= df.columns.tolist()
    print(f'list of columns: {columns}')
    columns_list=[]
    input_1=None
    while input_1 != 'finish':
        input_1= input('select column: ')
        columns_list.append(input_1)
    if 'finish' in columns_list:
        columns_list.remove('finish')
    for j in columns_list:
        u = unique_value(df,[j])
        input_2= input(f'{j} in your dataframe has {len(u)} unique value; do you want to replace: (N/Y)')
        if input_2=='n':
            continue
        else:
            dict_replace={}
            c=1
            for i in u.iloc[:,0]:
                input_3= input(f'{c} what is replace of {i}')
                dict_replace[i]= input_3
                if input_3 =='break':
                    break
                else:
                    c+=1
        input_4= input('do you want creat new column?')
        if input_4 == 'break':
            break
        else:
            if input_4=='y':
                name=''
                input_5= input('name of new column: ')
                df[f'{input_5}']= df[j].replace(dict_replace)
            else:
                df[j]= df[j].replace(dict_replace)
P_E_def = 'this function is for manual translating persian values to english'

def words_clean(df,columns_list:list):
    for j in columns_list:
        v= df[j].value_counts()
        input_1= input(f'{j} has: {v}/n do wou want to clean: (n/y)')
        if input_1=='n':
            continue
        else:
            list_replace=[]
            input_2=None
            while input_2 != 'finish':
                input_2= input ('what is the words to remove: ')
                list_replace.append(input_2)
            if 'finish' in list_replace:
                list_replace.remove('finish')
            input_3= input('do you want to creat new column: ')
            if input_3 =='break':
                break
            else:
                if input_3=='y':
                    name=''
                    input_4= input('new column name: ')
                    df[f'{input_4}']= df[j].replace(regex=list_replace,value='')
                else:
                    df[j]= df[j].replace(regex=list_replace,value='')
words_clean_def = 'this function is for removing or cleaning specific word or character in dataframe'

def remove_extra_space (pd_series):
    pd_series=pd_series.astype(str)
    pd_series=pd_series.str.strip(' ')
    return pd_series
remove_extra_space_def = 'this function is for removing extra espace in string or other data in specific dataframe series'

def remove_space(pd_series):
    pd_series= pd_series.astype(str)
    pd_series.replace(r' ','',regex=True)
    return pd_series
remove_space_def= 'this function removes all spaces in string or other values in specific datafarme series'

def date_timestamp(pd_series):
    pd_series=pd_series.astype(str)
    date = pd_series.apply (lambda x: str(x).split(' ')[0])
    return date
date_timestamp_def = 'this function is for correcting date with timestamp with removing timestamp'

def finding_value_str(df):
    y = df.columns.tolist()
    print('Note: it takes case sensitive values.')
    keyword= input('keyword for search')
    dict_name={}
    for k in y:
        try:
            l= df[df[k].str.contains(keyword)]
            dict_name[k]= l.index.tolist()
        except:
            continue
    print(dict_name)
finding_value_str_def = 'this function is for finding str value in datafame'

def checking_words(df):
    '''this function find differences in dictation or code of person name with natioanl code'''
    def check(df):
        national_id_list= list(dict.fromkeys(df['person_national_code']))
        if 'nan' in national_id_list:
            national_id_list.remove('nan')
        list_for_check=[]
        person_with_nan= []
        for i in national_id_list:
            list_index= df.loc[df['person_national_code']==i].index.tolist()
            sub_df= df.loc[list_index]
            list_person_name= list(dict.fromkeys(sub_df['person_name']))
            if 'nan' in list_person_name:
                print(f'there is nan in {i} person name')
                person_with_nan.append(i)
            if len(list_person_name)>1:
                list_for_check.append({i : list_person_name})
        return list_for_check
    list_for_check=['0']
    c=1
    while len(list_for_check)!=0:
        start_time= dte.datetime.now()
        print('------------------------------------------------------------------------')
        print(f'step_{str(c)}')
        list_for_check= check(df)
        if len(list_for_check) > 0 :
            print('there is problem in word dictation or code')
            print(list_for_check)
            for i in list_for_check:
                for key,value in i.items():
                    list_index_1= df.loc[df['person_national_code']==key].index.tolist()
                    sub_df_1= df.loc[list_index_1]
                    list_person_1= list(dict.fromkeys(sub_df_1['person_name']))
                    for j in list_person_1:
                        input_3= input(f'for {j} : dictation or code or nothing: ')
                        if input_3== 'dict' or input_3=='یهزف':
                            input_4= input(f'enter new dictation for {i} :')
                            df['person_name'] = df['person_name'].replace([j], input_4)
                        if input_3=='code' or input_3=='زخیث':
                            input_4= input(f'enter new code for {j} :')
                            df['person_national_code']= df['person_national_code'].mask(df['person_name']==j, input_4)
                        if input_3=='nothing' or input_3=='دخفاهدل':
                            continue
            c= c+1
        end_time= dte.datetime.now()
        print('Duration: {}'.format(end_time - start_time))
    print('there is no problem in word dictation or code')
    return df
checking_words_def= 'this function find differences in dictation or code of person name with natioanl code'

def checking_company_person(df, national_company_series,national_person_series,company_name_series,person_name_series):
    """ checking dictation and code of company name and person name"""
    def ckeck(df, national_company_series,national_person_series,company_name_series,person_name_series):
        national_id_list= list(dict.fromkeys(df[national_company_series]))
        if 'nan' in national_id_list:
            national_id_list.remove('nan')
        list_for_check=[]
        person_with_nan=[]
        company_with_nan=[]
        for i in national_id_list:
            list_index_company= df.loc[df[national_company_series]==i].index.tolist()
            list_index_person= df.loc[df[national_person_series]==i].index.tolist()
            sub_df_person= df.loc[list_index_person]
            sub_df_company= df.loc[list_index_company]
            list_person_name= list(dict.fromkeys(sub_df_person[person_name_series]))
            list_company_name= list(dict.fromkeys(sub_df_company[company_name_series]))
            if 'nan' in list_person_name:
                print(f'there is nan in {i} {person_name_series}')
                list_person_name.remove('nan')
                person_with_nan.append(i)
            if 'nan' in list_company_name:
                print(f'there is nan in {i} {company_name_series}')
                list_company_name.remove('nan')
                company_with_nan.append(i)
            if len(list_person_name)>1 or len (list_company_name)>1:
                for j in list_company_name:
                    list_person_name.append(j)
                list_person_name= list(dict.fromkeys(list_person_name))
                list_for_check.append({i : list_person_name})
        return list_for_check
    list_for_check=['0']
    c = 1
    while len(list_for_check)!= 0:
        start_time= dte.datetime.now()
        print('----------------------------------------------------------------------------')
        print(f'step_{str(c)}')
        list_for_check= ckeck(df, national_company_series,national_person_series,company_name_series,person_name_series)
        if len(list_for_check)>0:
            print('there is problem in word dictation or code')
            print(list_for_check)
            for i in list_for_check:
                for key,value in i.items():
                    list_index_company= df.loc[df[national_company_series]==key].index.tolist()
                    list_index_person= df.loc[df[national_person_series]== key].index.tolist()
                    sub_df_company= df.loc[list_index_company]
                    suc_df_person= df.loc[list_index_person]
                    list_person_name= list(dict.fromkeys(suc_df_person[person_name_series]))
                    list_company_name= list(dict.fromkeys(sub_df_company[company_name_series]))
                    for x in list_company_name:
                        list_person_name.append(x)
                    list_person_name= list(dict.fromkeys(list_person_name))
                    for j in list_person_name:
                        input_3= input(f'for {j} : dictation or code or nathing: ')
                        if input_3== 'dict' or input_3== 'یهزف':
                            input_4= input(f'enter new dictation for {j}')
                            df[company_name_series] = df[company_name_series].replace([j], input_4)
                            df[person_name_series] = df[person_name_series].replace([j], input_4)
                        if input_3== 'code' or input_3== 'زخیث':
                            input_4 = input(f'enter new code for {j}')
                            df[national_company_series] = df[national_company_series].mask(df[company_name_series]==j, input_4)
                            df[national_person_series] = df[national_person_series].mask(df[person_name_series]==j, input_4)
                        if input_3== 'nothing' or 'دخفاهدل':
                            continue
            c= c+1
        end_time= dte.datetime.now()
        print('Duration: {}'.format(end_time - start_time))
    print('there is no problem in word dictation or code')
    return df
checking_company_person_def = 'this function is for checking dictation and code of company name and person name'

def insert_code(df, code_column_name, name_column_name):
    def checking_dictation(df, person_name):
        input_1 = input(f'insert new dictation for {person_name}: ')
        list_index_name= df.loc[df['person_name']== person_name].index_tolist()
        df.loc[list_index_name , ['person_name']] == [input_1]
    nan_person_national_code= df.loc[df[code_column_name]=='nan']
    nan_person_name= list(nan_person_national_code[name_column_name])
    nan_person_name_drop_duplicate= list(dict.fromkeys(nan_person_name))
    nan_person_name_drop_duplicate.sort(reversed=True)
    print('len nan_person_name ', len(nan_person_name))
    print('len nan_person_name_drop_duplicate ', len(nan_person_name_drop_duplicate))
    for i in nan_person_name_drop_duplicate:
        list_index= df.loc[df[name_column_name]==i].index.tolist()
        input_1= input(f'for {i} : (code/dict/next/done)')
        if input_1=='code'or input_1=='زخیث':
            input_3= input(f'insert code for {i} :')
            df.loc[list_index, [code_column_name]]=[input_3]
            input_2= input('Running checking dictation (n/y)')
            if input_2=='y' or input_2=='غ':
                checking_dictation(df, person_name=i)
            if input_2=='n' or input_2=='د':
                continue
        if input_1=='dict' or 'یهزف':
            input_3 = input(f'new dict for {i} :')
            df.loc[list_index, [name_column_name]]=[input_3]
        if input_1== 'next' or 'دثطف':
            continue
        if input_1== 'done' or input_1 =='یخدث':
            break
    return df
insert_code_def = 'this function is for inserting value for missing one for each record'

def df_sorting(df,distination_path=None):
    input_1= input('choose  number of columns for sorting')
    int_input_1=int(input_1)
    c=0
    sort_by=[]
    while c != int_input_1:
        input_4= input('choose columns for sorting: ')
        sort_by.append(input_4)
        c+=1
    input_2= input('do you want to nan value being at first: (Y/N)')
    if input_2 =='y':
        na_method='First'
    if input_2 =='n':
        na_method='Last'
    input_3= input('do you want to sort from smalest to largest (y/n)')
    if input_2 =='y':
        acending_method= False
    if input_3 == 'n':
        acending_method=True
    df_sorted= df.sort_values(by=sort_by,ascending=acending_method,na_position=na_method,ignore_index=True)
    if distination_path==None:
        file_name= input('choose name for sorted file')
        df_sorted.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
    if distination_path==None:
        pass
    return df_sorted
df_sorting_def= 'this function is for sorting values based on sepecific columns'

def remove_dup(df,distination_path=None):
    print(f'length of dataframe is {len(df)}')
    input_1 = int(input('number of columns for checking duplicates: '))
    c=0
    subset_list=[]
    while c != input_1:
        input_2= input('choose columns for checking duplicates:')
        subset_list.append(input_2)
        c+=1
    input_3= input('choose method of drop duplicate (last/first)') #it means that in first method keep first one and drop the others an in the last method keep last one and drop the others
    df_drop_dup=df.drop_duplicates(subset=subset_list,keep=input_3,ignore_index=True)
    if distination_path==None:
        pass
    if distination_path!=None:
        file_name= input('choose name for removed duplicate file file')
        df_drop_dup.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
    return df_drop_dup
remove_dup_def = 'this function is for removing duplicate values in dataframe'

def find_null (df):
    print(f'main dataframe length is {len(df)}')
    print('----------------------------------------------------')
    df_columns= df.columns.tolist()
    print(df_columns)
    print('----------------------------------------------------')
    null_list=[]
    for i in df_columns:
        df_null_bool= pd.isnull(df[i])
        df_null= df[df_null_bool]
        num_null= len(df_null)
        null_tuple= (i,num_null)
        null_list.append(null_tuple)
    print('rusult of serching for null values in dataframe is: ')
    print(null_list)
    return null_list
find_null_def = 'this function is for finding null values in entier dataframe'

def df_null_value(df,distination_path):
    input_1 = input('choose a column for finding null values: ')
    df_null = df[df[f'{input_1}'].isnull()]
    input_2 = input('choose name for null dataframe')
    df_null.to_csv(distination_path+'//'+input_2+'.csv',index=False,encoding='utf-8-sig')
    return df_null
df_null_value_def='this function for export a dataframe that contain null values from main dataframe'

def finding_diffrences(df1,df2,distination_path=None):
    column_list_f= df1.columns.tolist()
    column_list_s= df2.columns.tolist()
    if column_list_f==column_list_s:
        if df1.equals(df2)==True:
            print('given dataframes are the same')
        else:
            print('given dataframes have some diffrences')
            print(column_list_f)
            input_1= input('choose a columns for finding diffrences')
            df_dif= df1[~(df1[f'{input_1}'].isin(df2[f'{input_1}']))].reset_index(drop=True)
            if distination_path==None:
                pass
            if distination_path!=None:
                file_name= input('choose name for difference file file')
                df_dif.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
            return df_dif
    else:
        print('thay dont have same columns')
finding_diffrences_def = 'this function is for finding diffrences between two dataframes'

def reading_file(df=None,read_path=None,distination_path=None):
    if read_path != None:
        all_df=[]
        for file in os.listdir(read_path):
            name, extension = os.path.splitext(read_path+'\\'+file)
            file_extention= extension
            if file_extention == '.xlsx' or file_extention=='.xls':
                df= pd.read_excel(read_path+'\\'+file)
                all_df.append(df)
                print(f'{file.split(".")[0]}, {len(df)}, columns number is {len(df.columns)}')
            if file_extention == '.csv':
                df = pd.read_csv(read_path+'\\'+file)
                all_df.append(df)
                print(f'{file.split(".")[0]}, {len(df)}, columns number is {len(df.columns)}')
        df_raw= pd.concat(all_df, ignore_index=True).reset_index(drop=True)
    elif df != None:
        df_raw=df
    elif df != None and read_path != None:
        print('KeyErrore: shouldd given one of the read_path or df')
    if distination_path!=None:
        df.to_csv(distination_path+'//'+'df_raw.csv',index=False,encoding='utf-8-sig')
    if distination_path==None:
        pass
    return df_raw
reading_file_def = 'this function is for reading and merging files'

def cleanning_dataframe(df,distination_path=None):
    def column_clustering(df):
        columns= df.columns.tolist()
        print(f'columns name are: {columns}')
        string_columns=[]
        code_columns=[]
        price_columns=[]
        input_1=None
        while input_1!='finish':
            input_1= input('choose type of clusters: (string\price\code) ')
            if input_1=='string':
                input_2=None
                while input_2!='finish':
                    input_2=input('choose string column')
                    string_columns.append(input_2)
                if 'finish' in string_columns:
                    string_columns.remove('finish')
            if input_1=='code':
                input_2=None
                while input_2!='finish':
                    input_2=input('choose code column')
                    code_columns.append(input_2)
                if 'finish' in code_columns:
                    code_columns.remove('finish')
            if input_1=='price':
                input_2=None
                while input_2!='finish':
                    input_2=input('choose price column')
                    price_columns.append(input_2)
                if 'finish' in price_columns:
                    price_columns.remove('finish')
        return string_columns,code_columns,price_columns
    def code_clean(df, code_columns):
        for i in code_columns:
            try:
                df[i]= df[i].replace(['nan',np.nan,'NaN'],1000000000001234)
                df[i]=df[i].replace(r'-','',regex=True)
                df[i]=df[i].apply(np.int64)
                df[i]= df[i].astype(str)
                df[i]= df[i].replace(r'1000000000001234',np.nan, regex=True)
            except:
                print(f'error is in {i}')
        return df
    def price_clean (df, price_columns):
        input_1= input('type of price: (float/int)')
        if input_1=='int':
            for i in price_columns:
                try:
                    df[i]= df[i].apply(lambda x: x.astype(str))
                    df[i]=df[i].apply(lambda x: x(np.int64))
                except:
                    print(f'error is in {i}')
        if input_1=='float':
            for i in price_columns:
                try:
                    df[i]= df[i].apply(lambda x: x.astype(float))
                except:
                    print(f'error is in {i}')
        return df
    def string_clean(df,string_columns):
        for i in string_columns:
            try:
                df[i]= df[i].apply(lambda x: str(x))
                df[i]=df[i].str.lower()
                df[i]= df[i].apply(lambda x: re.sub(' +',' ',x))
                df[i]=df[i].str.strip()
                df[i]=df[i].replace('  ',' ')
                df[i]=df[i].replace('(','-')
                df[i]=df[i].replace(')','')
                df[i]=df[i].replace('_',' ')
                df[i]=df[i].apply(lambda x: characters.ar_to_fa(x))
                df[i]=df[i].replace(regex=r'\u200c',value=' ')
                df[i]=df[i].replace(regex=r'\u200e',value=' ')
                df[i]=df[i].str.strip(' ')
                df[i]=df[i].replace(regex=['مجتمع','سهامی خاص','شرکت','سهامی عام','مسئولیت محدود','گروه','مادرتخصصی','هلدینگ','مجتمع','طرف','مادر تخصصی','مسولیت محدود','()'],value='')
                df[i]=df[i].str.strip()
                df[i]=df[i].replace('_',' ')
                df[i]=df[i].replace('-',' ')
            except:
                print(f'error is in {i}')
        return df
    def change_column_name(df):
        print(f'main column names are: {df.columns.tolist()}')
        columns=df.columns.tolist()
        def changing_name(df,columns):
            for i in columns:
                new_name= input(f'Insert new name for {i}: ')
                df.rename(columns={i:new_name},inplace=True)
            print('------------------------------------------------------')
        changing_name(df, columns)
        print(f'new columns name is: {df.columns.tolist()}')
        input_1= None
        while input_1 != 'y':
            input_1= input('the result is correct: (y/n)')
            print(input_1)
            columns=[]
            input_2= None
            while input_2 != 'finish':
                input_2 = input('select columns to correct: ')
                columns.append(input_2)
            if 'finish' in columns:
                columns.remove('finish')
            print(f'list of columns for correction: {columns}')
            changing_name(df,columns)
            print(f'new columns name is: {df.columns.tolist()}')
    input_2= input('Do you want change the headers')
    if input_2 == 'y':
        change_column_name(df)
    if input_2=='n':
        pass
    input_1= input('Do you want string cleanning: (y/n)')
    input_3 = input('Do you want code cleanning: (y/n)')
    input_4 = input('Do you want price cleanning: (y/n)')
    if input_1 == 'y':
        print('String cleanning prosses in running')
        string_columns= column_clustering(df)[0]
        df= string_clean(df=df, string_columns=string_columns)
    if input_1 == 'n':
        pass
    if input_3 == 'y':
        print('Code cleanning prosses in running')
        code_columns= column_clustering(df)[1]
        df= code_clean(df=df, code_columns=code_columns)
    if input_3 == 'n':
        pass
    if input_4 == 'y':
        print('Price cleanning prosses in running')
        Price_columns= column_clustering(df)[2]
        df= price_clean(df=df, price_columns=Price_columns)
    if input_4 == 'n':
        pass
    if distination_path == None:
        pass
    if distination_path != None:
        file_name= input('choose name for cleaned file')
        df.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
    return df
cleanning_dataframe_def = 'this function is for claening dataframe with some prossessor like string,price,codes and columns headers'

def group_by_sum(df,distination_path=None):
    print(f'length of df is {len(df)}')
    print(f'the columns of df is {df.columns.tolist()}')
    number_of_group_by=int(input('number of columns to group by: '))
    c=0
    group_by_column=[]
    while c != number_of_group_by:
        group_by= input('select a column to group by: ')
        group_by_column.append(group_by)
        c+=1
    sum_column= input('select a column to sumation: ')
    df_grup_sum= df.groupby(by=group_by_column)[sum_column].sum().to_frame(name=sum_column).reset_index()
    print(df_grup_sum.columns.tolist())
    if distination_path==None:
        pass
    if distination_path!=None:
        file_name= input('choose a name for group by file')
        df_grup_sum.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
    print(df.columns.tolist())
    select_value= input('choose a column in main dataframe for selcting items:')
    df_select_list= df[select_value].tolist()
    df_selected_by_group_by= df[df[select_value].isin(df_select_list)]
    number_of_drop_columns=int(input('number of columns to drop for merging files: '))
    c=0
    drop_column=[]
    while c != number_of_drop_columns:
        drop_c= input('select a column to drop: ')
        drop_column.append(drop_c)
        c+=1
    df_selected_by_group_by.drop(columns=drop_column,inplace=True)
    if distination_path==None:
        pass
    if distination_path!=None:
        file_name= input('choose a name for df selected by groupby file')
        df_selected_by_group_by.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
    df_merged= df_selected_by_group_by.merge(df_grup_sum)
    if distination_path==None:
        pass
    if distination_path!=None:
        file_name= input('choose a name for df merged by groupby file')
        df_merged.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
    return df_grup_sum, df_selected_by_group_by, df_merged
group_by_sum_def = 'this function is for groupby and calculate sumation in dataframe'

def treshold_and_select (df,distination_path=None):
    #------------------------------------------------------------------------------------------------------
    #sorting
    print(f'columns of dataframe is {df.columns.tolist()}')
    sort_value= input('choose a column for sorting: ')
    df_sorted= df.sort_values(sort_value,acsending=False).reset_index()
    #-----------------------------------------------------------------------------------------------------
    #cumulative frequency
    cumulative_column= input('which column do you want to calculate cumulative frequency from: ')
    df_sorted['cumulative_frequency']= df_sorted[cumulative_column].cumsum()
    sum_col= df_sorted[cumulative_column].sum()
    relative_list=[]
    for i in df_sorted['cumulative_frequency']:
        cal_num= (i/sum_col)*100
        relative_list.append(cal_num)
    df_sorted['relative_cumulative_frequency']= relative_list
    df_sorted.drop(columns='index', inplace=True)
    if distination_path==None:
        pass
    if distination_path!=None:
        saving_option=input('Do you want to save: (y/n)')
        if saving_option == 'y':
            file_name= input('choose a name for df selected by groupby file')
            df_sorted.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
        if saving_option == 'n':
            pass
    #-----------------------------------------------------------------------------------------------------
    #select top one
    selecting_option= input('do you want to select data (y/n)')
    if selecting_option == 'y':
        number_of_select= int(input('how many times do you want to select?'))
        c=0
        while c != number_of_select:
            select_int= int(input('make a top part to select'))
            df_selected= df_sorted[:select_int]
            sum_value= input('which column do you want to sum')
            print(f'the sumation of {sum_value} in all selected dataframe is{df_selected[sum_value].sum}')
            if distination_path==None:
                pass
            if distination_path!=None:
                saving_option=input('Do you want to save: (y/n)')
                if saving_option == 'y':
                    file_name= input('choose a name for df selected by groupby file')
                    df_selected.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
                if saving_option == 'n':
                    pass
    if selecting_option=='n':
        pass
    #--------------------------------------------------------------------------------------------------------
    #treshold
    treshold_option= input('do you want to set treshold for data (y/n)')
    if treshold_option == 'y':
        number_of_treshold= int(input('how many times do you want to put tresholds?'))
        c=0
        while c != number_of_treshold:
            treshold_column= input('which column to put treshold on: ')
            treshold_number= int(input('set tereshold'))
            df_treshold= df_sorted.loc[df_sorted[treshold_column]<=treshold_number]
            sum_value= input('which column do you want to sum')
            print(f'the sumation of {sum_value} in all selected dataframe is{df_treshold[sum_value].sum}')
            if distination_path==None:
                pass
            if distination_path!=None:
                saving_option=input('Do you want to save: (y/n)')
                if saving_option == 'y':
                    file_name= input('choose a name for df selected by groupby file')
                    df_selected.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
                if saving_option == 'n':
                    pass
    if treshold_option =='n':
        pass
    return df_sorted
treshold_and_select_def = 'this function is for mange a treshold for specific data for selecting data'

def stats_simple_clustering (df=None,read_path=None,distination_path=None):
    def reading_file(df=None,read_path=None,distination_path=None):
        if read_path != None:
            all_df=[]
            for file in os.listdir(read_path):
                name, extension = os.path.splitext(read_path+'\\'+file)
                file_extention= extension
                if file_extention == '.xlsx' or file_extention=='.xls':
                    df= pd.read_excel(read_path+'\\'+file)
                    all_df.append(df)
                    print(f'{file.split(".")[0]}, {len(df)}, columns number is {len(df.columns)}')
                if file_extention == '.csv':
                    df = pd.read_csv(read_path+'\\'+file)
                    all_df.append(df)
                    print(f'{file.split(".")[0]}, {len(df)}, columns number is {len(df.columns)}')
            df_raw= pd.concat(all_df, ignore_index=True).reset_index(drop=True)
        elif df != None:
            df_raw=df
        elif df != None and read_path != None:
            print('KeyErrore: shouldd given one of the read_path or df')
        if distination_path!=None:
            df.to_csv(distination_path+'//'+'df_raw.csv',index=False,encoding='utf-8-sig')
        if distination_path==None:
            pass
        return df_raw
    def cleanning_dataframe(df,distination_path=None):
        def column_clustering(df):
            columns= df.columns.tolist()
            print(f'columns name are: {columns}')
            string_columns=[]
            code_columns=[]
            price_columns=[]
            input_1=None
            while input_1!='finish':
                input_1= input('choose type of clusters: (string\price\code) ')
                if input_1=='string':
                    input_2=None
                    while input_2!='finish':
                        input_2=input('choose string column')
                        string_columns.append(input_2)
                    if 'finish' in string_columns:
                        string_columns.remove('finish')
                if input_1=='code':
                    input_2=None
                    while input_2!='finish':
                        input_2=input('choose code column')
                        code_columns.append(input_2)
                    if 'finish' in code_columns:
                        code_columns.remove('finish')
                if input_1=='price':
                    input_2=None
                    while input_2!='finish':
                        input_2=input('choose price column')
                        price_columns.append(input_2)
                    if 'finish' in price_columns:
                        price_columns.remove('finish')
            return string_columns,code_columns,price_columns
        def code_clean(df, code_columns):
            for i in code_columns:
                try:
                    df[i]= df[i].replace(['nan',np.nan,'NaN'],1000000000001234)
                    df[i]=df[i].replace(r'-','',regex=True)
                    df[i]=df[i].apply(np.int64)
                    df[i]= df[i].astype(str)
                    df[i]= df[i].replace(r'1000000000001234',np.nan, regex=True)
                except:
                    print(f'error is in {i}')
            return df
        def price_clean (df, price_columns):
            input_1= input('type of price: (float/int)')
            if input_1=='int':
                for i in price_columns:
                    try:
                        df[i]= df[i].apply(lambda x: x.astype(str))
                        df[i]=df[i].apply(lambda x: x(np.int64))
                    except:
                        print(f'error is in {i}')
            if input_1=='float':
                for i in price_columns:
                    try:
                        df[i]= df[i].apply(lambda x: x.astype(float))
                    except:
                        print(f'error is in {i}')
            return df
        def string_clean(df,string_columns):
            for i in string_columns:
                try:
                    df[i]= df[i].apply(lambda x: str(x))
                    df[i]=df[i].str.lower()
                    df[i]= df[i].apply(lambda x: re.sub(' +',' ',x))
                    df[i]=df[i].str.strip()
                    df[i]=df[i].replace('  ',' ')
                    df[i]=df[i].replace('(','-')
                    df[i]=df[i].replace(')','')
                    df[i]=df[i].replace('_',' ')
                    df[i]=df[i].apply(lambda x: characters.ar_to_fa(x))
                    df[i]=df[i].replace(regex=r'\u200c',value=' ')
                    df[i]=df[i].replace(regex=r'\u200e',value=' ')
                    df[i]=df[i].str.strip(' ')
                    df[i]=df[i].replace(regex=['مجتمع','سهامی خاص','شرکت','سهامی عام','مسئولیت محدود','گروه','مادرتخصصی','هلدینگ','مجتمع','طرف','مادر تخصصی','مسولیت محدود','()'],value='')
                    df[i]=df[i].str.strip()
                    df[i]=df[i].replace('_',' ')
                    df[i]=df[i].replace('-',' ')
                except:
                    print(f'error is in {i}')
            return df
        def change_column_name(df):
            print(f'main column names are: {df.columns.tolist()}')
            columns=df.columns.tolist()
            def changing_name(df,columns):
                for i in columns:
                    new_name= input(f'Insert new name for {i}: ')
                    df.rename(columns={i:new_name},inplace=True)
                print('------------------------------------------------------')
            changing_name(df, columns)
            print(f'new columns name is: {df.columns.tolist()}')
            input_1= None
            while input_1 != 'y':
                input_1= input('the result is correct: (y/n)')
                print(input_1)
                columns=[]
                input_2= None
                while input_2 != 'finish':
                    input_2 = input('select columns to correct: ')
                    columns.append(input_2)
                if 'finish' in columns:
                    columns.remove('finish')
                print(f'list of columns for correction: {columns}')
                changing_name(df,columns)
                print(f'new columns name is: {df.columns.tolist()}')
        input_2= input('Do you want change the headers')
        if input_2 == 'y':
            change_column_name(df)
        if input_2=='n':
            pass
        input_1= input('Do you want string cleanning: (y/n)')
        input_3 = input('Do you want code cleanning: (y/n)')
        input_4 = input('Do you want price cleanning: (y/n)')
        if input_1 == 'y':
            print('String cleanning prosses in running')
            string_columns= column_clustering(df)[0]
            df= string_clean(df=df, string_columns=string_columns)
        if input_1 == 'n':
            pass
        if input_3 == 'y':
            print('Code cleanning prosses in running')
            code_columns= column_clustering(df)[1]
            df= code_clean(df=df, code_columns=code_columns)
        if input_3 == 'n':
            pass
        if input_4 == 'y':
            print('Price cleanning prosses in running')
            Price_columns= column_clustering(df)[2]
            df= price_clean(df=df, price_columns=Price_columns)
        if input_4 == 'n':
            pass
        if distination_path == None:
            pass
        if distination_path != None:
            file_name= input('choose name for cleaned file')
            df.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
        return df
    def group_by_sum(df,distination_path=None):
        print(f'length of df is {len(df)}')
        print(f'the columns of df is {df.columns.tolist()}')
        number_of_group_by=int(input('number of columns to group by: '))
        c=0
        group_by_column=[]
        while c != number_of_group_by:
            group_by= input('select a column to group by: ')
            group_by_column.append(group_by)
            c+=1
        sum_column= input('select a column to sumation: ')
        df_grup_sum= df.groupby(by=group_by_column)[sum_column].sum().to_frame(name=sum_column).reset_index()
        print(df_grup_sum.columns.tolist())
        if distination_path==None:
            pass
        if distination_path!=None:
            file_name= input('choose a name for group by file')
            df_grup_sum.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
        print(df.columns.tolist())
        select_value= input('choose a column in main dataframe for selcting items:')
        df_select_list= df[select_value].tolist()
        df_selected_by_group_by= df[df[select_value].isin(df_select_list)]
        number_of_drop_columns=int(input('number of columns to drop for merging files: '))
        c=0
        drop_column=[]
        while c != number_of_drop_columns:
            drop_c= input('select a column to drop: ')
            drop_column.append(drop_c)
            c+=1
        df_selected_by_group_by.drop(columns=drop_column,inplace=True)
        if distination_path==None:
            pass
        if distination_path!=None:
            file_name= input('choose a name for df selected by groupby file')
            df_selected_by_group_by.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
        df_merged= df_selected_by_group_by.merge(df_grup_sum)
        if distination_path==None:
            pass
        if distination_path!=None:
            file_name= input('choose a name for df merged by groupby file')
            df_merged.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
        return df_grup_sum, df_selected_by_group_by, df_merged
    def treshold_and_select (df,distination_path=None):
        #------------------------------------------------------------------------------------------------------
        #sorting
        print(f'columns of dataframe is {df.columns.tolist()}')
        sort_value= input('choose a column for sorting: ')
        df_sorted= df.sort_values(sort_value,acsending=False).reset_index()
        #-----------------------------------------------------------------------------------------------------
        #cumulative frequency
        cumulative_column= input('which column do you want to calculate cumulative frequency from: ')
        df_sorted['cumulative_frequency']= df_sorted[cumulative_column].cumsum()
        sum_col= df_sorted[cumulative_column].sum()
        relative_list=[]
        for i in df_sorted['cumulative_frequency']:
            cal_num= (i/sum_col)*100
            relative_list.append(cal_num)
        df_sorted['relative_cumulative_frequency']= relative_list
        df_sorted.drop(columns='index', inplace=True)
        if distination_path==None:
            pass
        if distination_path!=None:
            saving_option=input('Do you want to save: (y/n)')
            if saving_option == 'y':
                file_name= input('choose a name for df selected by groupby file')
                df_sorted.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
            if saving_option == 'n':
                pass
        #-----------------------------------------------------------------------------------------------------
        #select top one
        selecting_option= input('do you want to select data (y/n)')
        if selecting_option == 'y':
            number_of_select= int(input('how many times do you want to select?'))
            c=0
            while c != number_of_select:
                select_int= int(input('make a top part to select'))
                df_selected= df_sorted[:select_int]
                sum_value= input('which column do you want to sum')
                print(f'the sumation of {sum_value} in all selected dataframe is{df_selected[sum_value].sum}')
                if distination_path==None:
                    pass
                if distination_path!=None:
                    saving_option=input('Do you want to save: (y/n)')
                    if saving_option == 'y':
                        file_name= input('choose a name for df selected by groupby file')
                        df_selected.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
                    if saving_option == 'n':
                        pass
        if selecting_option=='n':
            pass
        #--------------------------------------------------------------------------------------------------------
        #treshold
        treshold_option= input('do you want to set treshold for data (y/n)')
        if treshold_option == 'y':
            number_of_treshold= int(input('how many times do you want to put tresholds?'))
            c=0
            while c != number_of_treshold:
                treshold_column= input('which column to put treshold on: ')
                treshold_number= int(input('set tereshold'))
                df_treshold= df_sorted.loc[df_sorted[treshold_column]<=treshold_number]
                sum_value= input('which column do you want to sum')
                print(f'the sumation of {sum_value} in all selected dataframe is{df_treshold[sum_value].sum}')
                if distination_path==None:
                    pass
                if distination_path!=None:
                    saving_option=input('Do you want to save: (y/n)')
                    if saving_option == 'y':
                        file_name= input('choose a name for df selected by groupby file')
                        df_selected.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
                    if saving_option == 'n':
                        pass
        if treshold_option =='n':
            pass
        return df_sorted
    #------------------------------------------------------------------------
    #Reading
    if df != None:
        if distination_path != None:
            df_raw= reading_file(df=df,distination_path=distination_path)
        if distination_path == None:
            df_raw = reading_file (df=df,distination_path=None)
    if df == None:
        if distination_path != None:
            df_raw= reading_file(read_path=None,distination_path=distination_path)
        if distination_path == None:
            df_raw = reading_file (read_path=None,distination_path=None)
    #---------------------------------------------------------------------------
    #Cleaning
    df_cleaned= cleanning_dataframe(df=df_raw, distination_path=distination_path)
    #---------------------------------------------------------------------------
    #GroupBy
    df_groupby= group_by_sum(df=df_cleaned,distination_path=distination_path)[2]
    #---------------------------------------------------------------------------
    # Treshold_simple
    df_final = treshold_and_select(df=df_groupby,distination_path=distination_path)
    return df_final
stats_simple_clustering_def = 'this function is for simple statistical clustering and selcting data by tereshold'

def column_clustering(df):
    columns= df.columns.tolist()
    print(f'columns name are: {columns}')
    string_columns=[]
    code_columns=[]
    price_columns=[]
    input_1=None
    while input_1!='finish':
        input_1= input('choose type of clusters: (string\price\code) ')
        if input_1=='string':
            input_2=None
            while input_2!='finish':
                input_2=input('choose string column')
                string_columns.append(input_2)
            if 'finish' in string_columns:
                string_columns.remove('finish')
        if input_1=='code':
            input_2=None
            while input_2!='finish':
                input_2=input('choose code column')
                code_columns.append(input_2)
            if 'finish' in code_columns:
                code_columns.remove('finish')
        if input_1=='price':
            input_2=None
            while input_2!='finish':
                input_2=input('choose price column')
                price_columns.append(input_2)
            if 'finish' in price_columns:
                price_columns.remove('finish')
    return string_columns,code_columns,price_columns
column_clustering_def = 'this function is for clustering columns of dataframe into tree parts'

def code_clean(df, code_columns):
    for i in code_columns:
        try:
            df[i]= df[i].replace(['nan',np.nan,'NaN'],1000000000001234)
            df[i]=df[i].replace(r'-','',regex=True)
            df[i]=df[i].apply(np.int64)
            df[i]= df[i].astype(str)
            df[i]= df[i].replace(r'1000000000001234',np.nan, regex=True)
        except:
            print(f'error is in {i}')
    return df
code_clean_def = 'this function is for cleaning code context'

def price_clean (df, price_columns):
    input_1= input('type of price: (float/int)')
    if input_1=='int':
        for i in price_columns:
            try:
                df[i]= df[i].apply(lambda x: x.astype(str))
                df[i]=df[i].apply(lambda x: x(np.int64))
            except:
                print(f'error is in {i}')
    if input_1=='float':
        for i in price_columns:
            try:
                df[i]= df[i].apply(lambda x: x.astype(float))
            except:
                print(f'error is in {i}')
    return df
price_clean_def = 'this function is for cleaning price context'

def string_clean(df,string_columns):
    for i in string_columns:
        try:
            df[i]= df[i].apply(lambda x: str(x))
            df[i]=df[i].str.lower()
            df[i]= df[i].apply(lambda x: re.sub(' +',' ',x))
            df[i]=df[i].str.strip()
            df[i]=df[i].replace('  ',' ')
            df[i]=df[i].replace('(','-')
            df[i]=df[i].replace(')','')
            df[i]=df[i].replace('_',' ')
            df[i]=df[i].apply(lambda x: characters.ar_to_fa(x))
            df[i]=df[i].replace(regex=r'\u200c',value=' ')
            df[i]=df[i].replace(regex=r'\u200e',value=' ')
            df[i]=df[i].str.strip(' ')
            df[i]=df[i].replace(regex=['مجتمع','سهامی خاص','شرکت','سهامی عام','مسئولیت محدود','گروه','مادرتخصصی','هلدینگ','مجتمع','طرف','مادر تخصصی','مسولیت محدود','()'],value='')
            df[i]=df[i].str.strip()
            df[i]=df[i].replace('_',' ')
            df[i]=df[i].replace('-',' ')
        except:
            print(f'error is in {i}')
    return df
string_clean_def = 'this function is for cleaning string context'

def change_column_name(df):
    print(f'main column names are: {df.columns.tolist()}')
    columns=df.columns.tolist()
    def changing_name(df,columns):
        for i in columns:
            new_name= input(f'Insert new name for {i}: ')
            df.rename(columns={i:new_name},inplace=True)
        print('------------------------------------------------------')
    changing_name(df, columns)
    print(f'new columns name is: {df.columns.tolist()}')
    input_1= None
    while input_1 != 'y':
        input_1= input('the result is correct: (y/n)')
        print(input_1)
        columns=[]
        input_2= None
        while input_2 != 'finish':
            input_2 = input('select columns to correct: ')
            columns.append(input_2)
        if 'finish' in columns:
            columns.remove('finish')
        print(f'list of columns for correction: {columns}')
        changing_name(df,columns)
        print(f'new columns name is: {df.columns.tolist()}')
change_column_name_def = 'this function is for changing headers name in dataframe'

def generate_fake_deposit_data (num_sample):
    data = []
    for _ in range(num_sample):
        customer_name = Faker.name()
        account_number = Faker.uuid4()
        deposit_amount = round (random.uniform(1000, 100000), 2)
        transaction_date = Faker.date_between_dates(dte.date(2023, 1, 1), dte.date(2023, 12, 12))

        data.append({
            'CustomerName' : customer_name,
            'AccountNumber' : account_number,
            'DepositAmount' : deposit_amount,
            'TransactionDate' : transaction_date
        })
    return data
generate_fake_deposit_data_def = 'this function is for making fake dataset for deposit'

def generate_fake_transaction_data (num_customers, max_transaction_per_customers, inistial_balance):
    data = []
    for customer_id in range (1 , num_customers +1):
        balance = inistial_balance
        transaction_per_customers = random.randrange(1,max_transaction_per_customers)
        for _ in range(transaction_per_customers):
            transaction_date = Faker.date_between_dates(dte.date(2023, 1, 1), dte.date(2023, 12, 12))
            transaction_amount = round( random.uniform(-100000000,100000000),0)
            
            if (balance + transaction_amount)<0:
               transaction_amount = -balance
            
            balance += transaction_amount

            data.append({
                'CustomerId' : customer_id,
                'TransactionDate' : transaction_date,
                'TransactionAmount' : transaction_amount,
                'RemainingDeposit' : balance
            })

    return data
generate_fake_transaction_data_def = 'this function is for making fake dataset for transations'

def date_correction (df, date_seperator,date_column,date_type,out_date_type):
    date_corrected_list=[]
    year_list =[]
    month_list = []
    day_list=[]
    if date_type =='en':
        if out_date_type == 'fa':
            for i in df[date_column]:
                year = str(i).split(date_seperator)[0]
                year_list.append(year)
                month = str(i).split(date_seperator)[1]
                month_list.append(month)
                day = str(i).split(date_seperator)[2]
                day_list.append(day)
                date = JalaliDate(dte.date(year=int(year),month=int(month),day=int(day)))
                date_corrected_list.append(date)
        if out_date_type == 'en':
            for i in df[date_column]:
                year = str(i).split(date_seperator)[0]
                year_list.append(year)
                month = str(i).split(date_seperator)[1]
                month_list.append(month)
                day = str(i).split(date_seperator)[2]
                day_list.append(day)
                date = year + '-' + month + '-' + day
                date_corrected_list.append(date)
    if date_type == 'fa':
        if out_date_type == 'fa':
            for i in df[date_column]:
                year = str(i).split(date_seperator)[0]
                year_list.append(year)
                month = str(i).split(date_seperator)[1]
                month_list.append(month)
                day = str(i).split(date_seperator)[2]
                day_list.append(day)
                date = year + '-' + month + '-' + day
                date_corrected_list.append(date)
        if out_date_type == 'en':
            for i in df[date_column]:
                year = str(i).split(date_seperator)[0]
                year_list.append(year)
                month = str(i).split(date_seperator)[1]
                month_list.append(month)
                day = str(i).split(date_seperator)[2]
                day_list.append(day)
                date = year + '-' + month + '-' + day
                jalali_date = jdt.datetime.strptime(date, "%Y-%m-%d")
                gregorian_date = jalali_date.togregorian()
                date_corrected_list.append(gregorian_date)
    return year_list,month_list,day_list,date_corrected_list
date_correction = 'this function is for changing date type from gregorian to jalali or versa and split year,month and day of main date type'

def transaction_analysis (df,distination_path=None):
    def df_sorting(df,distination_path=None):
        input_1= input('choose  number of columns for sorting')
        int_input_1=int(input_1)
        c=0
        sort_by=[]
        while c != int_input_1:
            input_4= input('choose columns for sorting: ')
            sort_by.append(input_4)
            c+=1
        df_sorted= df.sort_values(by=sort_by,ascending=True,ignore_index=True)
        if distination_path!=None:
            file_name= input('choose name for sorted file')
            df_sorted.to_csv(distination_path+'//'+file_name+'.csv',index=False,encoding='utf-8-sig')
        if distination_path==None:
            pass
        return df_sorted
    def format_with_seperator (value):
        return '{:,.0f}'.format(value)
    df_main_columns = df.columns.tolist()
    print(df_main_columns)
    analysis_type = input('based on df main columns which method of analysis should be selected: (with_withdraw / normal)')
    if analysis_type == 'with_withdraw':
        print(f'length of df is {len(df)}')
        number_of_group_by=int(input('number of columns to group by: '))
        c=0
        group_by_column=[]
        while c != number_of_group_by:
            group_by= input('select a column to group by: ')
            group_by_column.append(group_by)
            c+=1
        # for deposit sumation
        operation_column_deposit= input('select a deposit column to sumation: ')
        condition = (df[operation_column_deposit]<0)
        if condition.any():
            print('there is at least one Negative value in deposit column')
            df[operation_column_deposit+'corrected'] = df[operation_column_deposit].abs()
            df_deposit_sum= df.groupby(by=group_by_column)[operation_column_deposit+'corrected'].sum().to_frame(name=operation_column_deposit+'sum').reset_index()
            df_deposit = df.loc[df[operation_column_deposit+'corrected']>0]
            df_deposit_count = df_deposit.groupby(by=group_by_column).size().reset_index(name=operation_column_deposit+'count')
            df_deposit_sum_count = df_deposit_sum.merge(df_deposit_count)
            print(f'diposit sumation dataframe columns is{df_deposit_sum.columns.tolist()}')
            print(f'diposit count dataframe columns is{df_deposit_count.columns.tolist()}')
            print(f'diposit count and sumation dataframe columns is{df_deposit_sum_count.columns.tolist()}')
            if distination_path==None:
                pass
            if distination_path!=None:
                df_deposit_sum.to_csv(distination_path+'//'+'df_deposit_sum'+'.csv',index=False,encoding='utf-8-sig')
                df_deposit_count.to_csv(distination_path+'//'+'df_deposit_count'+'.csv',index=False,encoding='utf-8-sig')
                df_deposit_sum_count.to_csv(distination_path+'//'+'df_deposit_sum_count'+'.csv',index=False,encoding='utf-8-sig')
        else:
            df_deposit_sum= df.groupby(by=group_by_column)[operation_column_deposit].sum().to_frame(name=operation_column_deposit+'sum').reset_index()
            df_deposit = df.loc[df[operation_column_deposit]>0]
            df_deposit_count = df_deposit.groupby(by=group_by_column).size().reset_index(name=operation_column_deposit+'count')
            df_deposit_sum_count = df_deposit_sum.merge(df_deposit_count)
            print(f'diposit sumation dataframe columns is{df_deposit_sum.columns.tolist()}')
            print(f'diposit count dataframe columns is{df_deposit_count.columns.tolist()}')
            print(f'diposit count and sumation dataframe columns is{df_deposit_sum_count.columns.tolist()}')
            if distination_path==None:
                pass
            if distination_path!=None:
                df_deposit_sum.to_csv(distination_path+'//'+'df_deposit_sum'+'.csv',index=False,encoding='utf-8-sig')
                df_deposit_count.to_csv(distination_path+'//'+'df_deposit_count'+'.csv',index=False,encoding='utf-8-sig')
                df_deposit_sum_count.to_csv(distination_path+'//'+'df_deposit_sum_count'+'.csv',index=False,encoding='utf-8-sig')
        # for withdrawls sumation
        operation_column_withdrawls= input('select a withdrawls column to sumation: ')
        condition_withdrawls = (df[operation_column_withdrawls]>0)
        if condition_withdrawls.any():
            print('there is at least one Positive value in deposit column')
            df[operation_column_withdrawls+'corrected'] = df[operation_column_withdrawls].apply(lambda x: -x if x>0 else x)
            df_withdrawl_sum= df.groupby(by=group_by_column)[operation_column_withdrawls+'corrected'].sum().to_frame(name=operation_column_withdrawls+'sum').reset_index()
            df_withdrawl = df.loc[df[operation_column_withdrawls+'corrected']<0]
            df_withdrawl_count = df_withdrawl.groupby(by=group_by_column).size().reset_index(name=operation_column_withdrawls+'count')
            df_withdrawl_sum_count = df_withdrawl_sum.merge(df_withdrawl_count)
            print(f'withdrawl sumation dataframe columns is{df_withdrawl_sum.columns.tolist()}')
            print(f'withdrawl count dataframe columns is{df_withdrawl_count.columns.tolist()}')
            print(f'withdrawl count and sumation dataframe columns is{df_withdrawl_sum_count.columns.tolist()}')
            if distination_path==None:
                pass
            if distination_path!=None:
                df_withdrawl.to_csv(distination_path+'//'+'df_withdrawl_sum'+'.csv',index=False,encoding='utf-8-sig')
                df_withdrawl_count.to_csv(distination_path+'//'+'df_withdrawl_count'+'.csv',index=False,encoding='utf-8-sig')
                df_withdrawl_sum_count.to_csv(distination_path+'//'+'df_withdrawl_sum_count'+'.csv',index=False,encoding='utf-8-sig')
        else:
            df_withdrawl_sum= df.groupby(by=group_by_column)[operation_column_withdrawls].sum().to_frame(name=operation_column_withdrawls+'sum').reset_index()
            df_withdrawl = df.loc[df[operation_column_withdrawls]<0]
            df_withdrawl_count = df_withdrawl.groupby(by=group_by_column).size().reset_index(name=operation_column_withdrawls+'count')
            df_withdrawl_sum_count = df_withdrawl_sum.merge(df_withdrawl_count)
            print(f'withdrawl sumation dataframe columns is{df_withdrawl_sum.columns.tolist()}')
            print(f'withdrawl count dataframe columns is{df_withdrawl_count.columns.tolist()}')
            print(f'withdrawl count and sumation dataframe columns is{df_withdrawl_sum_count.columns.tolist()}')
            if distination_path==None:
                pass
            if distination_path!=None:
                df_withdrawl.to_csv(distination_path+'//'+'df_withdrawl_sum'+'.csv',index=False,encoding='utf-8-sig')
                df_withdrawl_count.to_csv(distination_path+'//'+'df_withdrawl_count'+'.csv',index=False,encoding='utf-8-sig')
                df_withdrawl_sum_count.to_csv(distination_path+'//'+'df_withdrawl_sum_count'+'.csv',index=False,encoding='utf-8-sig')
    if analysis_type == 'normal':
        print(f'length of df is {len(df)}')
        number_of_group_by=int(input('number of columns to group by: '))
        c=0
        group_by_column=[]
        while c != number_of_group_by:
            group_by= input('select a column to group by: ')
            group_by_column.append(group_by)
            c+=1
        operation_column= input('select a column to sumation and count for deposit and withdrawls: ')
        # for deposit sumation
        df_deposit = df.loc[df[operation_column]>0]
        df_deposit_sum= df_deposit.groupby(by=group_by_column)[operation_column].sum().to_frame(name='deposit_sum').reset_index()
        df_deposit_count = df_deposit.groupby(by=group_by_column).size().reset_index(name='deposit_count')
        df_deposit_sum_count = df_deposit_sum.merge(df_deposit_count)
        print(f'diposit sumation dataframe columns is{df_deposit_sum.columns.tolist()}')
        print(f'diposit count dataframe columns is{df_deposit_count.columns.tolist()}')
        print(f'diposit count and sumation dataframe columns is{df_deposit_sum_count.columns.tolist()}')
        if distination_path==None:
            pass
        if distination_path!=None:
            df_deposit_sum.to_csv(distination_path+'//'+'df_deposit_sum'+'.csv',index=False,encoding='utf-8-sig')
            df_deposit_count.to_csv(distination_path+'//'+'df_deposit_count'+'.csv',index=False,encoding='utf-8-sig')
            df_deposit_sum_count.to_csv(distination_path+'//'+'df_deposit_sum_count'+'.csv',index=False,encoding='utf-8-sig')
        # for withdrawls sumation
        df_withdrawl = df.loc[df[operation_column]<0]
        df_withdrawl_sum= df_withdrawl.groupby(by=group_by_column)[operation_column].sum().to_frame(name='withdrawl_sum').reset_index()
        df_withdrawl_count = df_withdrawl.groupby(by=group_by_column).size().reset_index(name='withdrawl_count')
        df_withdrawl_sum_count = df_withdrawl_sum.merge(df_withdrawl_count)
        print(f'withdrawl sumation dataframe columns is{df_withdrawl_sum.columns.tolist()}')
        print(f'withdrawl count dataframe columns is{df_withdrawl_count.columns.tolist()}')
        print(f'withdrawl count and sumation dataframe columns is{df_withdrawl_sum_count.columns.tolist()}')
        if distination_path==None:
            pass
        if distination_path!=None:
            df_withdrawl.to_csv(distination_path+'//'+'df_withdrawl_sum'+'.csv',index=False,encoding='utf-8-sig')
            df_withdrawl_count.to_csv(distination_path+'//'+'df_withdrawl_count'+'.csv',index=False,encoding='utf-8-sig')
            df_withdrawl_sum_count.to_csv(distination_path+'//'+'df_withdrawl_sum_count'+'.csv',index=False,encoding='utf-8-sig')
    
    df_main_sorted = df_sorting(df,distination_path=distination_path)
    print(df_main_sorted.columns.tolist())
    number_of_group_by_last_remain=int(input('number of columns to group by for last remain deposit: '))
    c=0
    group_by_column_last_remain_deposit=[]
    while c != number_of_group_by_last_remain:
        group_by= input('select a column to group by: ')
        group_by_column_last_remain_deposit.append(group_by)
        c+=1
    remainig_deposit = input('select remaining deposit columns')
    last_remain_deposit = df_main_sorted.groupby(group_by_column_last_remain_deposit)[remainig_deposit].last().reset_index()
    df_transaction_sum_count = df_deposit_sum_count.merge(df_withdrawl_sum_count)
    df_final_transaction_analysis = df_transaction_sum_count.merge(last_remain_deposit)
    if distination_path==None:
        pass
    if distination_path!=None:
        df_transaction_sum_count.to_csv(distination_path+'//'+'df_transaction_sum_count'+'.csv',index=False,encoding='utf-8-sig')
        df_final_transaction_analysis.to_csv(distination_path+'//'+'df_final_transaction_analysis'+'.csv',index=False,encoding='utf-8-sig')
    
    # avrage
    print(df_final_transaction_analysis.columns.tolist())
    whant_avg = input('do want to calculate avrage')
    if whant_avg == 'y':
        num_avg = int(input('how many times do whant to calculate: '))
        c = 0
        while c != num_avg:
            main_value = input('select a main column for dividing')
            divided_value =  input('select a column for divided by: ')
            name_new_column = input('name of new avrage column')
            df_final_transaction_analysis[name_new_column] = df_final_transaction_analysis[main_value] / df_final_transaction_analysis[divided_value]
            c += 1
    else:
        pass
        
    # changig format
    print(df_final_transaction_analysis.columns.tolist())
    num_changing_format_column = int(input('number of type to changing format'))
    c = 0
    while c != num_changing_format_column:
        format_type = input('which type of format do you want (str/int)')
        if format_type == 'str':
            changing_format_list = []
            num_columns = int(input('number of columns for changing str format'))
            d = 0
            while d != num_columns:
                list_columns = input('columns for changing str format')
                changing_format_list.append(list_columns)
                d += 1
            for i in changing_format_list:
                try:
                    df_final_transaction_analysis[i] = df_final_transaction_analysis[i].apply(lambda x: str(x))
                except:
                    print(f'there is a problem in {i}')
            c += 1
        if format_type == 'int':
            changing_format_list = []
            num_columns = int(input('number of columns for changing int format'))
            d = 0
            while d != num_columns:
                list_columns = input('columns for changing int format')
                changing_format_list.append(list_columns)
                d += 1
            for i in changing_format_list:
                try:
                    df_final_transaction_analysis[i] = df_final_transaction_analysis[i].apply(lambda x: int(x))
                except:
                    print(f'there is a problem in {i}')
            c += 1
    chang_abs = input('do you want change negative value to positive: ')
    if chang_abs == 'y':
        number_abs_columns = int(input('how many columns do you want to change: '))
        k = 0
        columns_for_abs = []
        while k != number_abs_columns:
            abs_columns = input('columns for change: ')
            columns_for_abs.append(abs_columns)
            k += 1
        for i in columns_for_abs:
            df_final_transaction_analysis[i] = df_final_transaction_analysis[i].abs()
    else:
        pass
    # condition
    print(df_final_transaction_analysis.columns.tolist())
    whant_con = input('do want to put condition')
    if whant_con == 'y':
        num_con = int(input('how many times do whant to insert condition: '))
        c = 0
        while c != num_con:
            main_value = input('select a main column for put condition on')
            con_situation = input('condition is (=/</>)')
            if con_situation == '=':
                print('condition is about (=)')
                condition_value =  int(input('value for checking condition with '))
                name_new_column = input('name of new condition column')
                df_final_transaction_analysis[name_new_column]=np.where(df_final_transaction_analysis[main_value] == condition_value,'equal','not_equal')
                c += 1
            if con_situation == '>':
                print('condition is about (>)')
                condition_value =  int(input('value for checking condition with '))
                name_new_column = input('name of new condition column')
                df_final_transaction_analysis[name_new_column]=np.where(df_final_transaction_analysis[main_value] > condition_value,'High','Low')
                c += 1
            if con_situation == '<':
                print('condition is about (<)')
                condition_value =  int(input('value for checking condition with '))
                name_new_column = input('name of new condition column')
                df_final_transaction_analysis[name_new_column]=np.where(df_final_transaction_analysis[main_value] < condition_value,'Low','High')
                c += 1
    else:
        pass

    # df_final_transaction_analysis = df_final_transaction_analysis.applymap(lambda x: '{:,}'.format(x) if isinstance(x, (int,float)) else x)
    whant_format_sep = input('do you want thouand seperator: ')
    if whant_format_sep == 'y':
        number_sep_columns = int(input('how many columns do you want to insert thousand seperator: '))
        c = 0
        columns_for_sep = []
        while c != number_sep_columns:
            sep_columns = input('columns for change: ')
            columns_for_sep.append(sep_columns)
            c += 1
        for i in columns_for_sep:
            new_name = input('new name for sperated column')
            df_final_transaction_analysis[new_name] = df_final_transaction_analysis[i].apply(format_with_seperator)

    if distination_path==None:
        pass
    if distination_path!=None:
        df_final_transaction_analysis.to_csv(distination_path+'//'+'df_final_transaction_analysis'+'.csv',index=False,encoding='utf-8-sig')

    return df_final_transaction_analysis
transaction_analysis_def = 'this function is for analysis deposit and withdrawls in transaction dataframe with calculate avrage and reamaining amount of each costumer deposit'

