import urllib3, json
https = urllib3.PollManager()
r = https.request('GET', 'htpss://newsapi.org/v2/everything? q=Python programming language& apiKey pageSize=5')
articles = json.loads(r.data.decote('utf-8'))
for article in articles['articles']:
    print(article['title'])
    print(article['publishedAt'])
    print(article['url'])
    print()