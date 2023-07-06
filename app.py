import requests
import re
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import MetaData, ImpressionMetrics, Base
from datetime import datetime

# Create an SQLite database file
engine = create_engine('sqlite:///my_database.db', echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)
# Create a session
session = Session()

# Check if the table already exists
inspector = inspect(engine)
print(inspector.get_table_names())
if 'MetaData' not in inspector.get_table_names():
    # Create the tables in the database
    Base.metadata.create_all(bind=engine)

print('Enter below mentioned pramaters to proceed: ')

DATE_START = input('Enter start date in YYYY-MM-DD format: ')
DATE_END = input('Enter end date in YYYY-MM-DD format: ')
DIMENSIONS= input('Enter dimension in "," comma seprated format with no space in between: ')
pattern = re.compile('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))')

#Validating DATE_START & END_DATE, Exception will be raised if date/date format is invalid
if re.match('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))', DATE_START) is None:
    raise Exception(f'Invalid date {DATE_START} Date format not supported, supported format is YYYY-MM-DD')
if re.match('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))', DATE_END) is None:
    raise Exception(f'Invalid date {DATE_END} Date format not supported, supported format is YYYY-MM-DD')

print('------------------------------------------------')
print('Date format validated successfully')
print('------------------------------------------------')
#Preparing Query parameters
params = {'allow_mock':'true',
          'period':'custom_date',
          'start_date':DATE_START,
          'end_date':DATE_END,
          'group_by':DIMENSIONS,
          'lock_on_collection':'false'}

print(f'Requesting data from server')

#making get request to server
response = requests.get(url = 'https://api.libring.com/v2/reporting/get',
                    params=params,
                    headers={'Authorization': 'Bearer DHDwhdFXfoGBYLPOZPvTTwJoS'},
                    verify=False)

#checking for the status code, status code 200 means success
if response.status_code == 200:
    print('------------------------------------------------')
    print('Data recieved from server')
    print('------------------------------------------------')
    count = 0
    try:
        data = response.json()
        data = data['connections']
        for row in data:
            d =  {
                "connection": row.get('connection',None),
                "country": row.get('country',None),
                "app": row.get('app',None),
                "platform": row.get('platform',None),
                "date": row.get('date',None),
                "ad_cpm": row.get('ad_cpm',None),
                "install_rate":row.get('install_rate',None),
                "iap_revenue": row.get('iap_revenue',None),
                "ad_revenue": row.get('ad_revenue',None),
                "spent": row.get('spent',None),
                "fill_rate": row.get('fill_rate',None),
                "ctr": row.get('ctr',None),
                "unfilled_impressions":row.get('unfilled_impressions',None),
                "downloads": row.get('downloads',None),
                "updates": row.get('updates',None),
                "returns": row.get('returns',None),
                "hits": row.get('hits',None),
                "user_sessions": row.get('user_sessions',None),
                "new_users": row.get('new_users',None),
                "dau": row.get('dau',None),
                "mau": row.get('mau',None),
                "requests": row.get('requests',None),
                "paying_users": row.get('paying_users',None),
                "acq_requests": row.get('acq_requests',None),
                "acq_impressions": row.get('acq_impressions',None),
                "acq_clicks": row.get('acq_clicks',None),
                "acq_completions": row.get('acq_completions',None),
                "acq_installs": row.get('acq_installs',None),
                "impressions": row.get('impressions',None),
                "clicks": row.get('clicks',None),
                "completions": row.get('completions',None),
                "conversions": row.get('conversions',None),
                "measurable_impressions": row.get('measurable_impressions',None),
                "viewable_impressions": row.get('viewable_impressions',None),
                "page_views": row.get('page_views',None),
                "iap_revenue_gross": row.get('iap_revenue_gross',None)
             }
            
            d['date'] = datetime.strptime(d['date'], "%Y-%m-%d").date()
            #print(type(d['date']))
            trow = MetaData(**d)
            session.add(trow)
            session.commit()
            metrixRow = ImpressionMetrics(connection = d['connection'],
                                        platform = d['platform'],
                                        country = d['country'],
                                        app = d['app'],
                                        date = d['date'],
                                        ad_revenue = d['ad_revenue'],
                                        impressions = d['impressions']
                                        )
            session.add(metrixRow)
            session.commit()
            count += 1
            #break
        print(f"{count} Rows inserted successfully.")

    except Exception as e:
        print(str(e))
    finally:
        # Close the session
        session.close()

#status code 401 means unathorised
elif response.status_code == 401:
    print('Unauthorised request')
else:
    print(f'Bad Request status code - {response.status_code}')
