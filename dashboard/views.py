from django.shortcuts import render
from django.views.generic.base import View


def index(request):
    import pandas as pd
    import os
    import requests
    from scipy.signal import savgol_filter

    resource_id = 'dcf999c1-d394-4b57-a5e0-9d014a62e046'
    limit = 10 ** 7
    filters = '{"corona_result": "חיובי"}'
    records_format = 'objects'
    fields = 'test_date'

    url = f"https://data.gov.il/api/3/action/datastore_search?" \
          f"resource_id={resource_id}&include_total={True}&limit={limit}" \
          f"&filters={filters}&records_format={records_format}&fields={fields}"

    response = requests.get(url)
    response_json = response.json()

    df = pd.DataFrame(response_json['result']['records'])
    df['count'] = 1

    df = df.groupby('test_date').count()
    df = df.drop(['NULL'])

    df['savgol_smoothed_data'] = savgol_filter(df['count'], 51, 3).astype('int32').clip(0)

    context = {
        'labels': df.index.tolist(),
        'data': df['count'].tolist(),
        'savgol_smoothed_data': df['savgol_smoothed_data'].tolist()
    }

    return render(request, 'dashboard/index.html', context)
