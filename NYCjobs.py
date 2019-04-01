import pandas as pd
import os

pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 27)

#IMPORTING DATA/ONLY NEED TO RUN ONCE
#import requests
#response = requests.get("https://data.cityofnewyork.us/resource/kpav-sd4t.json").json()
#for data in response:
#    print(data)
#data = pd.DataFrame(response)
#data.to_csv('nycjobs_feb_data.csv', index=False)

#CONSTANTS
#base = '/Users/alexandrubordei/PycharmProjects/NYCJobs/venv/data nyc jobs/Jobs CSV Files'
#suffix = 0

#WHICH FILE NAME TO PICK
#Template_Name = "NYC_Jobs_"

#for fname in os.listdir(base):
    #[NYC_JOBS_123, "CSV"] LOOP AND BREAK FILE EXTENSION
#    file_list = fname.split('.')

    #NYC_JOBS_123 GET FIRST ITEM(NYC_JOBS_123) AND STORE INTO VARIABLE
#    base_fname = file_list[0]

    #["NYC", "JOBS", "123"] BREAK NYC_JOBS_123 BY "_"
#    base_fname_list = base_fname.split('_')


    #"123" TAKE LAST ITEM "123"
#    fname_num = base_fname_list[-1]

    #TURN LAST ITEM INTO INT, CALL INT NUM
#    num = int(fname_num)

    #IF
#    if suffix < num:
#        suffix = num

#new_name = template_name + str(suffix + 1)+'.csv'

#FILE NAME PATH

base = '/Users/alexandrubordei/PycharmProjects/NYCJobs/venv/data nyc jobs/Jobs CSV Files'
fname = 'nycjobs_feb_data.csv'
data = pd.read_csv(os.path.join(base, fname))

#KEEP CERTAIN COLUMNS
keep_cols = data.columns[:29,]

#REMOVE UNUSED COLUMNS TO CONDENSE DATA SET
data = data.drop(['title_code_no', 'post_until', 'posting_date', 'posting_updated', 'process_date'], axis=1)


#REMOVE ANY JOB LEVELS THAT AREN'T 0
data = data.loc[data['level'] == '0']


#REMOVE ANY JOB TYPES THAT ARE NOT EXTERNAL APPLICATIONS ONLY
data = data.loc[data['posting_type'] == 'External']


#data to be printed
dat = data.loc[:, keep_cols]


#PRINT DATAFRAME AND PRINT HEADERS FOR DATAFRAME

print(data)
