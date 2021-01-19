import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/anilkumarpanda/python-training-2021/main/data/UCI_Credit_Card.csv')

#https://stackoverflow.com/a/48869651

def bill_manipulation(row):
    """
    Add doc strings.
    """
    if row['MARRIAGE'] == 1:
        return row['BILL_AMT1'] * row['BILL_AMT1']
    else:
        return row['BILL_AMT1']         

def bill_reduction(row):
  """
  Add doc strings.
  """
  row['BILL_MANIPULATION']=row['BILL_MANIPULATION']/row['LIMIT_BAL']
  
  if row['BILL_MANIPULATION'] >=500:
    return row['BILL_AMT2']*0
  else:
    return row['BILL_AMT2']
    

df['BILL_MANIPULATION'] = df.apply(bill_manipulation, axis=1)
df['BILL_AMT2'] = df.apply(bill_reduction,axis=1)