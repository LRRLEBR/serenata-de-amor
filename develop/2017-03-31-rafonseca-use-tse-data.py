
# coding: utf-8

# ### TSE data example
# This is just a small example of how to use tse data. 
# In this script we filter the candidates in order to obtain a dataframe containing only politicians that were elected at least once.

# In[1]:

import pandas as pd
import numpy as np
import os


# In[2]:

DATASET_PATH= os.path.join(os.pardir,'data','2017-03-31-tse-candidates.xz')


# In[3]:

# Loading csv
cand_df=pd.read_csv(DATASET_PATH,encoding='utf-8',dtype=str)


# In[4]:

### Here, we quickly check the data using  value_counts() to get the frequency on each column
for name, col in cand_df.iteritems():
    print ('\t',name,'\n')
    print (col.value_counts())


# ### Only elected politicians
# Now, we process cancidacies data to obtain a list of elected politicians
# We use DESC_SIT_TOT_TURNO to figure out who has been elected. It is better to use the description column then the code column, since the codes dont seem to be consistent along the years.
# 

# In[5]:

ind_elected=cand_df.DESC_SIT_TOT_TURNO=='ELEITO'
ind_elected|=cand_df.DESC_SIT_TOT_TURNO=='ELEITO POR QP'
ind_elected|=cand_df.DESC_SIT_TOT_TURNO=='ELEITO POR MÉDIA'
ind_elected|=cand_df.DESC_SIT_TOT_TURNO=='MÉDIA'
# ind_elected|=cand_df.DESC_SIT_TOT_TURNO=='SUPLENTE'# should we consider it?


# In[6]:

politicians_df=cand_df.ix[ind_elected,['CPF_CANDIDATO','NOME_CANDIDATO','DESCRICAO_CARGO','DESCRICAO_UE','SIGLA_UF','ANO_ELEICAO']]


# In[7]:

politicians_df.sort_values('NOME_CANDIDATO')


# It is quite curious that alphabetically ordered in this way, the last politician is called...
