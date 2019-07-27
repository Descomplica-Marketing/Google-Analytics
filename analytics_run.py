from functions import get_report_df

view_ids = [('196069492', 'Todos os dados')]

df = get_report_df(view_ids=view_ids, metrics=[{'expression': 'ga:sessions'}, ],
                   dimensions=[{'name': 'ga:date'}, {'name': 'ga:source'},
                               {'name': 'ga:medium'},
                               {'name': 'ga:campaign'},
                               {'name': 'ga:adContent'},
                               {'name': 'ga:socialNetwork'},
                               {'name': 'ga:deviceCategory'}, ], filter='', )

print(df)