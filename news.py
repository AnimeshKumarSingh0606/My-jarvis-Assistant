import requests
import plyer
import time

try:
    url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=2606a35885384640a5d2592e449ad907')

    response = requests.get(url)

    data = response.json()

    def notifyMe(title, message):

        plyer.notification.notify(
            title=title,
            message=message,
            timeout=15
        )

    articles=data["articles"]

    for i in articles[:5]:
        title=i["title"]
        content=i["content"]
        notifyMe(title[:64], content)
        time.sleep(5)

        
except Exception as e:
    print(e)