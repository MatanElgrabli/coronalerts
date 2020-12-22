import pandas as pd
from . import models


def save_lab_tests_dataframe():
    import os
    from scipy.signal import savgol_filter

    base_dir = os.path.dirname(os.path.realpath(__file__))

    lab_tests_df = pd.read_csv(os.path.join(base_dir, 'corona_lab_tests.csv'))[
        ['test_date', 'corona_result']]
    lab_tests_positive_df = lab_tests_df.loc[lab_tests_df['corona_result'] == 'חיובי']
    lab_tests_positive_cum_df = lab_tests_positive_df.groupby('test_date').count()

    result_df = pd.DataFrame(index=lab_tests_positive_cum_df.index)

    result_df['data'] = lab_tests_positive_cum_df['corona_result']
    result_df['savgol_smoothed_data'] = \
        savgol_filter(lab_tests_positive_cum_df['corona_result'], 51, 3).astype('int32').clip(0)

    result_df.to_csv(os.path.join(base_dir, 'corona_lab_tests_result.csv'))


def request_table(resource_id='9eedd26c-019b-433a-b28b-efcc98de378d', limit=100):
    url = f"https://data.gov.il/api/3/action/datastore_search?resource_id={resource_id}" \
          f"&include_total={True}&limit={limit}"
    import requests
    response = requests.get(url)
    response_json = response.json()
    records = response_json['result']['records']
    records_df = pd.DataFrame(records)
    return records_df.set_index('_id')


def sample_lab_tests_data(data):
    data = data.replace({'NULL': None})
    data = data.replace({'שלילי': False, 'חיובי': True})
    data = data.replace({'No': False, 'Yes': True})
    data['test_for_corona_diagnosis'] = data['test_for_corona_diagnosis'].replace(
        {'0': False, '1': True})
    return data

#
# lab_tests_gov_database_id = 'dcf999c1-d394-4b57-a5e0-9d014a62e046'
# df = request_table(lab_tests_gov_database_id, limit=10 ** 5)
# df = sample_lab_tests_data(df)
# save_LabTest_table(df)
#
# print(df)
# print('============= DONE =============')
