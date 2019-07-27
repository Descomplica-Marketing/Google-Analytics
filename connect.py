# import libraries
import httplib2
from googleapiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow, GoogleCredentials

from credentials import client_id, client_secret, redirect_uri, access_code, access_token, refresh_token

# create connection based on project credentials
flow = OAuth2WebServerFlow(client_id=client_id,
                           client_secret=client_secret,
                           scope='https://www.googleapis.com/auth/analytics',
                           redirect_uri=redirect_uri)

# capture different states of connection
if access_code == '':
    # first run prints oauth URL
    auth_uri = flow.step1_get_authorize_url()
    print(auth_uri)
elif access_token == '' and refresh_token == '':
    # second run returns access and refresh token
    credentials = flow.step2_exchange(access_code)
    print(credentials.access_token)
    print(credentials.refresh_token)
else:
    # third and future run connect through access token an refresh token
    credentials = GoogleCredentials(access_token, client_id, client_secret, refresh_token, 3920,
                                    'https://accounts.google.com/o/oauth2/token', 'test')
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = build('analyticsreporting', 'v4', http=http)
