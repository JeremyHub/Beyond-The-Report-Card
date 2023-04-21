#%%
import pandas as pd
import numpy as np

# %%
county_gcs_data = pd.read_csv("../AllDatasets/seda_county_long_gcs_4.1.csv")

# %%
ca_county_gcs = county_gcs_data.loc[county_gcs_data['stateabb'] == 'CA' , :].reset_index()
# %%
ca_county_gcs

# %%
gcs_mean_list = []
for col_name in ca_county_gcs.columns:
    if 'gcs_mn_' in col_name:
        gcs_mean_list.append(col_name)
# %%
gcs_mean_list
# %%
id_vars = ['fips', 'stateabb', 'sedacountyname', 'subject', 'grade', 'year']
col_list = id_vars + gcs_mean_list
# %%
col_list
# %%
col_tuple = tuple(i for i in col_list)
# %%
col_tuple
# %%
clean_ca_county_gcs = ca_county_gcs.loc[:, col_tuple]
# %%
clean_ca_county_gcs
# %%
long_clean_ca_county_gcs = pd.melt(clean_ca_county_gcs, id_vars=id_vars, value_vars=gcs_mean_list,value_name='gcs_value', ignore_index=False)
long_clean_ca_county_gcs['student_category'] = long_clean_ca_county_gcs['variable'].str[-3:]
long_clean_ca_county_gcs['clean_student_category'] = long_clean_ca_county_gcs['student_category'].apply(lambda x: \
                                                    'All' if x == 'all' \
                                                    else 'Asian' if x == 'asn' \
                                                    else 'Black' if x == 'blk' \
                                                    else 'Economically Disadvantaged (ECD)' if x == 'ecd' \
                                                    else 'Female' if x == 'fem' \
                                                    else 'Hispanic' if x == 'hsp' \
                                                    else 'Male' if x == 'mal' \
                                                    else 'Male-Female Gap' if x == 'mfg' \
                                                    else 'Multiracial' if x == 'mtr' \
                                                    else 'Native American' if x == 'nam' \
                                                    else 'Non-Economically Disadvantaged (Non-ECD)' if x == 'nec' \
                                                    else 'Non-ECD-ECD Gap' if x == 'neg' \
                                                    else 'White-Asian Gap' if x == 'wag' \
                                                    else 'White-Black Gap' if x == 'wbg' \
                                                    else 'White-Hispanic Gap' if x == 'whg' \
                                                    else 'White' if x == 'wht' \
                                                    else 'White-Multiracial Gap' if x == 'wmg' \
                                                    else 'White-Native American Gap' if x == 'wng' \
                                                    else np.nan)
#%%
long_clean_ca_county_gcs[['student_category', 'clean_student_category']].drop_duplicates()

# %%
math_ca_gcs = long_clean_ca_county_gcs.loc[long_clean_ca_county_gcs['subject'] == 'mth', :]
math_ca_gcs
# %%
rla_ca_gcs = long_clean_ca_county_gcs.loc[long_clean_ca_county_gcs['subject'] == 'rla', :]
rla_ca_gcs
# %%
math_ca_gcs['year'].unique()
# %%
rla_ca_gcs['year'].unique()
# %%
math_ca_gcs.to_csv('math_ca_gcs_df.csv')
rla_ca_gcs.to_csv('rla_ca_gcs_df.csv')
# %%
