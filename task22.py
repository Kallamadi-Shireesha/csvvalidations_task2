'''
import sys
import csv
from csvvalidator import *

field_names = (
               'col1',
               'col2',
               'col3'
               
               )

validator = CSVValidator(field_names)


# some simple value checks
validator.add_value_check('col1', str,
                          'EX3', 'study id must be an integer')
validator.add_value_check('col2', int,
                          'EX4', 'patient id must be an integer')

#validator.add_value_check('gender', enumeration('M', 'F'),  'EX5', 'invalid gender')
#validator.add_value_check('age_years', number_range_inclusive(0, 120, int),'EX6', 'invalid age in years')

validator.add_value_check('col3', datetime_string('%Y-%m-%d'),
                          'EX7', 'invalid date')

# a more complicated record check
def check_age_variables(r):
    age_years = int(r['age_years'])
    age_months = int(r['age_months'])
    valid = (age_months >= age_years * 12 and
             age_months % age_years < 12)
    if not valid:
        raise RecordError('EX8', 'invalid age variables')
validator.add_record_check(check_age_variables)

# validate the data and write problems to stdout
data = csv.reader('excel2.csv')
problems = validator.validate(data)
print(problems)
write_problems(problems, sys.stdout)
'''
import pandas as pd
import engarde.decorators as ed
from datetime import datetime
from cerberus import Validator
df = pd.read_csv('sample_sheet.csv')
#print(df.head)
#print(df.dtypes)
schema={'IMO' : {'type':'integer'},
            'SEQUENCE': {'type':'integer'},
            'EFFECTIVE_DATE' :  {'type':'integer'},
            'ORGANIZATION_NAME': {'type':'string'},
            'ORGANIZATION_CODE':{'type':'string'},
            'ORGANIZATION_STATUS': {'type':'float'},
            'VALID_FROM_DATETIME': {'type':'string'},
            'VALID_TO_DATETIME': {'type':'string'},
            'VALID_FROM_DATE': {'type':'string', 'regex': '0?[1-9]|[12][0-9]|3[01]- 0?[1-9]| 1[012]-\\d{4}'},
            'VALID_TO_DATE ':  {'type':'string', 'regex': '0?[1-9]|[12][0-9]|3[01]- 0?[1-9]| 1[012]-\\d{4}'},
            'DeathDate ': {'type':'string', 'regex': '0?[1-9]|[12][0-9]|3[01]- 0?[1-9]| 1[012]-\\d{4}' }}
#print(new_dtypes)
v=Validator(schema)
df_dict=df.to_dict(orient='records')
#print(df_dict)

#print records with invalid data type
for idx,record in enumerate(df_dict):
    if (v.validate(record) is True):
        continue
    else:
        print(f'Item{idx}:{v.errors}')
        
 
