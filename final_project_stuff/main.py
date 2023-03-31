#%%
import pandas as pd
import numpy as np
import os

#%%
dir_list = os.listdir()
dir_list 

#%%
dir_list_path = []
for i in dir_list:
    if "csv" in i: 
        dir_list_path.append(i)

dir_list_path

#%%
ca_education = pd.read_csv(dir_list_path[0])
ca_education

#%%
seda_df = pd.read_csv(dir_list_path[1])
seda_df


#%%
ca_edu_metrics = pd.read_csv(dir_list_path[2])
ca_edu_metrics

#%%
merged_seda_school_df = pd.read_csv(dir_list_path[3])
merged_seda_school_df

#%%
science_ca_assesment = pd.read_csv(dir_list_path[4], sep="^")
science_ca_assesment


#%%
wiiiide_df = pd.read_csv(dir_list_path[5])
wiiiide_df

#%%
physical_fitness_df = pd.read_csv(dir_list_path[6])
physical_fitness_df


#%%
wiiiide_df.columns.values.tolist()

#%%
merged_seda_school_df.isna().sum()


#%%
# len('060162010232')
1.10017*(10^12)

# %%
len(clients[clients['ClientUno'].notna()])

# %%
questions.isna().sum()
# %%
len(questions)
# %%
# %%
subcategories['Subcategory']

#%%
questions = pd.read_csv(dir_list_path[5])
clean_questions = questions[questions['StateAbbr'] != 'ID']
clean_questions['Year'] = clean_questions['AskedOnUtc'].str[:4].astype(int)
clean_questions
# %%
question_answer_count = clean_questions.groupby('Category').count()[['QuestionUno', 'AskedByClientUno', 'TakenByAttorneyUno']]
for i in question_answer_count.columns:
    question_answer_count = question_answer_count.rename(columns={i: f"{i}Count"})
question_answer_count
#%%

question_answer_count['ResponseRate'] = question_answer_count['TakenByAttorneyUnoCount']/question_answer_count['QuestionUnoCount']
# %%
question_answer_count.sort_values(by = ['ResponseRate'], ascending=False)
## not all of the questions get answered
# %%
COLUMN = 'StateAbbr'
question_answer_count = clean_questions.groupby(COLUMN).count()[['QuestionUno', 'AskedByClientUno', 'TakenByAttorneyUno']]
for i in question_answer_count.columns:
    question_answer_count = question_answer_count.rename(columns={i: f"{i}Count"})
question_answer_count['ResponseRate'] = question_answer_count['TakenByAttorneyUnoCount']/question_answer_count['QuestionUnoCount']
#%%
question_answer_count.sort_values(by = ['ResponseRate'], ascending=False)

#%%
question_answer_count.sort_values(by = ['ResponseRate'], ascending=True)

# %%
COLUMN = ['StateAbbr', 'Category']
question_answer_count = clean_questions.groupby(COLUMN).count()[['QuestionUno', 'AskedByClientUno', 'TakenByAttorneyUno']]
for i in question_answer_count.columns:
    question_answer_count = question_answer_count.rename(columns={i: f"{i}Count"})
question_answer_count['ResponseRate'] = question_answer_count['TakenByAttorneyUnoCount']/question_answer_count['QuestionUnoCount']


#%%
COLUMN = ['Category', 'Subcategory']
question_answer_count = clean_questions.groupby(COLUMN).count()[['QuestionUno', 'AskedByClientUno', 'TakenByAttorneyUno']]
for i in question_answer_count.columns:
    question_answer_count = question_answer_count.rename(columns={i: f"{i}Count"})
question_answer_count['ResponseRate'] = question_answer_count['TakenByAttorneyUnoCount']/question_answer_count['QuestionUnoCount']
question_answer_count

# %%
question_answer_count.sort_values(by = ['ResponseRate'], ascending=False)

# %%
question_answer_count.sort_values(by = ['ResponseRate'], ascending=True)

# %%
question_answer_count.sort_values(by = ['QuestionUnoCount'], ascending=False)

# %%
# category_pct_count.sort_values(by=['pct'], ascending=False)
# %%
fam_children = clean_questions[clean_questions['Category'] == 'Family and Children']

#%%
len(fam_children['QuestionUno'].unique())

# %%
COLUMN = ['Category', 'Subcategory']
subcat_pct_count = fam_children.groupby(COLUMN).count()[['QuestionUno', 'TakenByAttorneyUno']]
for i in subcat_pct_count.columns:
    subcat_pct_count = subcat_pct_count.rename(columns={i: f"{i}Count"})
subcat_pct_count
#%%
subcat_pct_count['question_pct'] = subcat_pct_count['QuestionUnoCount']/len(fam_children['QuestionUno'].unique())
subcat_pct_count['response_rate'] = subcat_pct_count['TakenByAttorneyUnoCount']/subcat_pct_count['QuestionUnoCount']

# %%
subcat_pct_count.sort_values(by=['question_pct', 'response_rate'], ascending=False)

#%%
time_list = []
for i in clean_questions.columns: 
    if 'Utc' in i: 
        time_list.append(i)
time_list

# %%
questions = pd.read_csv(dir_list_path[5])
clean_questions = questions[questions['StateAbbr'] != 'ID']
clean_questions_with_date = clean_questions.copy()

#%%

### Add day of the week and month of Asked on timestamp
clean_questions_with_date['AskedOnDayOfTheWeek'] = pd.to_datetime(clean_questions_with_date['AskedOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.day_name()
clean_questions_with_date['AskedOnMonth'] = pd.to_datetime(clean_questions_with_date['AskedOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.month
clean_questions_with_date['AskedOnMonthName'] = pd.to_datetime(clean_questions_with_date['AskedOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.month_name()
clean_questions_with_date['AskedOnYear'] = pd.to_datetime(clean_questions_with_date['AskedOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.year


#%%
### Add day of the week and month of Asked on timestamp
clean_questions_with_date['TakenOnDayOfTheWeek'] = pd.to_datetime(clean_questions_with_date['TakenOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.day_name()
clean_questions_with_date['TakenOnMonth'] = pd.to_datetime(clean_questions_with_date['TakenOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.month
clean_questions_with_date['TakenOnMonthName'] = pd.to_datetime(clean_questions_with_date['TakenOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.month_name()
clean_questions_with_date['TakenOnYear'] = pd.to_datetime(clean_questions_with_date['TakenOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.year


### Add day of the week and month of Asked on timestamp
clean_questions_with_date['ClosedOnDayOfTheWeek'] = pd.to_datetime(clean_questions_with_date['ClosedOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.day_name()
clean_questions_with_date['ClosedOnMonth'] = pd.to_datetime(clean_questions_with_date['ClosedOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.month
clean_questions_with_date['ClosedOnMonthName'] = pd.to_datetime(clean_questions_with_date['ClosedOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.month_name()
clean_questions_with_date['ClosedOnYear'] = pd.to_datetime(clean_questions_with_date['ClosedOnUtc'], format='%Y-%m-%d %H:%M:%S').dt.year


# %%
clean_questions_with_date

# %%
clean_questions_with_date.to_csv('clean_questions_with_date.csv', index=False)

# %%
clean_questionposts = pd.read_csv('clean_questionposts.csv')
# %%
clean_questionposts
# %%
clean_questionposts['rn'] = clean_questionposts.sort_values(by=['id','QuestionUno', 'DateTime']).groupby("QuestionUno")["DateTime"].rank(method="first", ascending=True)

#%%
filtered_clean_questionposts = clean_questionposts[clean_questionposts['rn'] == 1.0].iloc[:,0:-1].reset_index(drop=True)

#%%
filtered_clean_questionposts

#%%
filtered_clean_questionposts.to_csv('filtered_clean_questionposts.csv', index=False)


#%%
clean_questionposts.sort_values(by=['DateTime'])


#%%
filtered_clean_questionposts = clean_questionposts[len(clean_questionposts['StateAbbr']) == 2]


#%%
filtered_clean_questionposts.sort_values(by=['Id'], ascending=False)

# %%
clean_questions

# %%
utc = []
for i in clean_questions_with_date.columns: 
    if "Utc" in i: 
        utc.append(i)
utc
# %%
pd.to_datetime(clean_questions_with_date['TakenOnUtc'], format='%Y-%m-%d %H:%M:%S')


# %%
survival_df = clean_questions_with_date[['Category','AskedOnUtc', 'TakenOnUtc', 'ClosedOnUtc']]
survival_df_v2 = survival_df.copy()
# %%
survival_df_v2['AskedOnUtc'] = pd.to_datetime(clean_questions_with_date['AskedOnUtc'], format='%Y-%m-%d %H:%M:%S')
survival_df_v2['TakenOnUtc'] = pd.to_datetime(clean_questions_with_date['TakenOnUtc'], format='%Y-%m-%d %H:%M:%S')
survival_df_v2['ClosedOnUtc'] = pd.to_datetime(clean_questions_with_date['ClosedOnUtc'], format='%Y-%m-%d %H:%M:%S')


# %%
survival_df_v2['AskedToTakenInHours'] = (survival_df_v2['TakenOnUtc'] - survival_df_v2['AskedOnUtc']).astype('timedelta64[h]')
survival_df_v2['AskedToTakenInDays'] = ((survival_df_v2['TakenOnUtc'] - survival_df_v2['AskedOnUtc']).astype('timedelta64[h]'))/24

survival_df_v2['TakenToClosedInHours'] = (survival_df_v2['ClosedOnUtc'] - survival_df_v2['TakenOnUtc']).astype('timedelta64[h]')
survival_df_v2['TakenToClosedInDays'] = ((survival_df_v2['ClosedOnUtc'] - survival_df_v2['TakenOnUtc']).astype('timedelta64[h]'))/24

# %%
survival_df_v2
# %%
survival_df_v2.to_csv('survival_df.csv')
# %%
len(questions['StateAbbr'].unique())
# %%
questions['StateAbbr'].unique()
# %%
## % of questions asked in each category
COLUMN = ['Category']
category_pct_count = clean_questions.groupby(COLUMN).count()[['QuestionUno']]
category_pct_count
#%%
for i in category_pct_count.columns:
    category_pct_count = category_pct_count.rename(columns={i: f"{i}Count"})
category_pct_count['pct'] = category_pct_count['QuestionUnoCount']/len(clean_questions['QuestionUno'].unique())
# %%
category_pct_count.sort_values(by=['pct'], ascending=False)

# %%
# lang_detect = pd.read_csv('lang_detect_output.csv')
# lang_detect

#%%
grammar = pd.read_csv('grammar_detect_output.csv')
grammar
# %%

# lang_cat['pct'] = lang_cat['QuestionUno']/len(lang_detect['QuestionUno'].unique())
# lang_cat.sort_values(by=['pct'], ascending=False)

# %%
# lang_detect[lang_detect['TopLang'] == 'hu']
# %%
questions = pd.read_csv(dir_list_path[5])
clean_questions = questions[questions['StateAbbr'] != 'ID']
question_answer = clean_questions[['QuestionUno', 'TakenByAttorneyUno', 'Category']]
question_answer_status = question_answer.copy()
# %%
question_answer_status['AnswerStatusTaken'] = np.where(question_answer_status['TakenByAttorneyUno'].isna(), 'No', 'Yes')

# %%
question_answer_status = question_answer_status[['QuestionUno', 'AnswerStatusTaken', 'Category']]
# %%
question_answer_status
# %%

#%%

# language_answer_count = merged_lang_answer_status.groupby(['TopLang', 'AnswerStatus']).count()[['QuestionUno']]
# language_answer_count = language_answer_count.reset_index()
# %%
# language_count = lang_detect.groupby(['TopLang']).count()[['QuestionUno']]
# language_count = language_count.reset_index()
# %%
# language_count
# %%
# top_lang_cat = language_answer_count.merge(language_count, on = 'TopLang', how='left')
# top_lang_cat['pct'] = top_lang_cat['QuestionUno_x']/top_lang_cat['QuestionUno_y']
# %%
# top_lang_cat
# %%
# clean_questions

# %%
attorney_count = attorneys[attorneys['StateAbbr'] != "ID"].groupby(['StateAbbr'])[['AttorneyUno']].count().reset_index()

# %%
question_count = clean_questions.groupby(['StateAbbr'])['QuestionUno'].count().reset_index()
# %%
merged_ds = attorney_count.merge(question_count, on='StateAbbr', how='left')
merged_ds['QuestionUno'] = np.where(merged_ds['QuestionUno'].isna(), 0, merged_ds['QuestionUno'])
merged_ds['QuestionAttorneyRatio'] = merged_ds['QuestionUno']/merged_ds['AttorneyUno']
# %%
merged_ds

#%%
merged_lang_answer_status = grammar.merge(question_answer_status, on='QuestionUno',  how='left')
merged_lang_answer_status['ProperEnglish'] = np.where(merged_lang_answer_status['TopLang'] == 'en', 'Yes', 'No')
merged_lang_answer_status
# %%
filtered_lang_answer = merged_lang_answer_status[['StateAbbr', 'QuestionUno', 'AnswerStatusTaken', 'ProperEnglish', 'NormMistakes', 'WordCount', 'Category']]
filtered_lang_answer

#%%
question_answer_ratio_df = filtered_lang_answer.merge(merged_ds[['StateAbbr', 'QuestionAttorneyRatio']], on='StateAbbr', how='left')
question_answer_ratio_df 

# %%
question_answer_ratio_df.to_csv('filtered_data_for_bivariate_exploration.csv')
# %%
clean_questions.isna().sum()

# %%
