from functions import get_report_df

# Insert an array of your view ids in this format: [(view_id_1, view_id_1_name), (view_id_2, view_id_2_name)]

view_ids = []

df = get_report_df(view_ids=view_ids, metrics=[{'expression': 'ga:sessions'}, ],
                   dimensions=[{'name': 'ga:date'}, {'name': 'ga:source'},
                               {'name': 'ga:medium'},
                               {'name': 'ga:campaign'},
                               {'name': 'ga:adContent'},
                               {'name': 'ga:socialNetwork'},
                               {'name': 'ga:deviceCategory'}, ], filter='', )

print(df)