from django.shortcuts import render


# Create your views here.
def index(request):
    import os

    import pandas as pd

    # todo: use api instead of predownloaded csv
    base_dir = os.path.dirname(os.path.realpath(__file__))

    corona_city_df = pd.read_csv(os.path.join(base_dir, 'corona_city_table.csv'))[
        ['City_Name', 'Date', 'Cumulative_verified_cases']]
    corona_city_df = corona_city_df[corona_city_df['Cumulative_verified_cases'] != '<15']

    last_date = corona_city_df['Date'].max()

    last_date_df = corona_city_df.loc[corona_city_df['Date'] == last_date]
    last_date_df['Cumulative_verified_cases'] = last_date_df['Cumulative_verified_cases'].astype(
        'int32').copy()
    last_date_df['Cumulative_verified_cases'] = pd.to_numeric(
        last_date_df['Cumulative_verified_cases'])
    df = last_date_df.sort_values(by='Cumulative_verified_cases')[-10:]
    data = df['Cumulative_verified_cases']
    labels = df['City_Name']

    context = {
        'labels': labels.tolist(),
        'data': data.tolist(),
    }

    return render(request, 'areas/index.html', context)
