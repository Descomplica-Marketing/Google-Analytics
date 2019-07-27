import pandas as pd

from connect import service


def print_response(response):
    list = []
    # get report data
    for report in response.get('reports', []):
        # set column headers
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
        rows = report.get('data', {}).get('rows', [])

        for row in rows:
            # create dict for each row
            dict = {}
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            # fill dict with dimension header (key) and dimension value (value)
            for header, dimension in zip(dimensionHeaders, dimensions):
                dict[header] = dimension

            # fill dict with metric header (key) and metric value (value)
            for i, values in enumerate(dateRangeValues):
                for metric, value in zip(metricHeaders, values.get('values')):
                    # set int as int, float a float
                    if '.' in value or '.' in value:
                        dict[metric.get('name')] = float(value)
                    else:
                        dict[metric.get('name')] = int(value)

            list.append(dict)

        df = pd.DataFrame(list)
        return df


def get_report(analytics, start_date, end_date, view_id, metrics, dimensions, filter):
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': view_id,
                    'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
                    'metrics': metrics,
                    'dimensions': dimensions,
                    'pageSize': 10000,
                    'filtersExpression': filter
                }]
        }
    ).execute()


def return_ga_data(start_date, end_date, view_id, metrics, dimensions, filter):
    return print_response(get_report(service, start_date, end_date, view_id, metrics, dimensions, filter))


def get_report_df(view_ids, metrics, dimensions, filter):
    df = []

    for account_id, account_name in view_ids:
        tmp_df = return_ga_data(
            start_date='yesterday',
            end_date='today',
            view_id=account_id,
            metrics=metrics,
            dimensions=dimensions,
            filter=filter
        )

        tmp_df['account'] = account_name
        df.append(tmp_df)

    report = pd.concat(df, ignore_index=True)
    report.columns = map(str.lower, list(report.columns.str.replace('ga:', '')))

    return report
