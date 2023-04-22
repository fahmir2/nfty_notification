import requests

url = 'https://ntfy.sh/hobs'
message = 'Sale pete morocha?'.encode(encoding='utf-8')
title = 'sapeeeeee'
priority = 'Urgent'
tags = 'eggplant'

response = requests.post(url,
                         data=message,
                         headers={
                            'Title': title,
                            'Priority': priority,
                            'Tags': tags,
                         })

if response.status_code == 200:
    print('Notificacion exitosa')
else:
    print('Algo salio mal')