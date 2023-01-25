import pytz
import requests
from datetime import datetime

URL1 = 'https://d.flashscore.com/x/feed/fp_37_'
OFFSET = 0
URL2 = '_3_en_1'
TIMEZONE = 'Europe/Minsk'
CONTENT_LENGTH = 100
SPORT_KINDS = ['Super-G', 'Slalom', 'Giant Slalom', 'Downhill']


async def get_data(offset=0):
    current_url = URL1 + str(offset) + URL2
    headers = {"x-fsign": "SW9D1eZo"}
    r = requests.get(url=current_url, headers=headers)
    result = r.text
    pairs = []
    if len(r.content) < CONTENT_LENGTH:
        return pairs
    is_available = False
    for line in SPORT_KINDS:
        if line.lower() in result.lower():
            is_available = True
    if not is_available:
        return pairs
    result = result[10:]
    list_values = result.split('¬~ZA÷')

    for item in list_values:
        tmp = item.split('¬ZN÷')
        event_title = tmp[0].split('¬ZEE÷')[0]
        event_date = datetime.fromtimestamp(int(tmp[1].split('|¬ZSS÷')[0]), pytz.timezone(TIMEZONE))
        pairs.append(event_date.strftime('%Y-%m-%d %H:%M') + " - " + event_title)
    return pairs
