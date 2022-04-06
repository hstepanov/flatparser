#!/usr/bin/env python3
import os
import requests
from datetime import datetime
from datetime import date
from datetime import timedelta

user_id = os.getenv('MY_TG_USER_ID')
tg_token = os.getenv('TELEGRAM_BOT_TOKEN')
apikey = os.getenv('DOMRIA_APIKEY')
url_search = 'https://developers.ria.com/dom/search'
url_info = 'https://developers.ria.com/dom/info/'
url_post = 'https://api.telegram.org/bot'+tg_token+'/sendMessage'
yesterday_date = date.today() - timedelta(days=1)

# <-- lets find some proposal IDs --> #
get_payload = {"category": 1, "realty_type": 2, "operation_type": 3,
           "state_id": 5, "city_id": 5, "with_newbuilds": 0,
           "price_cur": 1, "wo_dupl": 1, "inspected": 0,
           "sort": "created_at", "period": 0, "api_key": apikey}
response = requests.get(
    url_search, headers={'Accept': 'application/json'}, params=get_payload)
founded_ids = response.json()

# <-- get URL for all founded proposals --> #
for item_id in founded_ids['items']:
    url = url_info+str(item_id)
    payload = {"api_key": apikey}
    response = requests.get(
        url, headers={'Accept': 'application/json'}, params=payload)
    result_link = response.json()

# <-- check if proposal new or not... --> #
for item_id in founded_ids['items']:
    url = url_info+str(item_id)
    payload = {"api_key": apikey}
    response = requests.get(
        url, headers={'Accept': 'application/json'}, params=payload)
    result_link = response.json()
    proposal_creation_date = datetime.strptime(result_link['created_at'][0:10], '%Y-%m-%d').date()
# <-- ...and send it to our bot --> #
    if proposal_creation_date > yesterday_date:
        message = str('https://dom.ria.com/uk/'+result_link['beautiful_url'])
        post_payload = {"chat_id": user_id, "text": message}
        requests.post(url_post, data=post_payload)
