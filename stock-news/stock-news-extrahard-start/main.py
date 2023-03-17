import requests
import smtplib


STOCK = 'MCD'
COMPANY_NAME = "McDonald's Corporation"
STOCK_API_KEY = 'GQFFX1DNJY4GI58D'
STOCK_URL = 'https://www.alphavantage.co/query'

NEWS_API = '6866c7ba6498429ea786c7123c375776'
NEWS_URL = 'https://newsapi.org/v2/everything?'

MY_EMAIL = 'day32.0001@gmail.com'
MY_PASSWORD = 'wgnavynehmlbghzu'
TO_EMAIL = 'muhammad.mamleev1998@gmail.com'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}
response = requests.get(STOCK_URL, params=parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
data_list = [value for (day, value) in data.items()]
yesterday_close = data_list[0]['4. close']
d_before_yesterday_close = data_list[1]['4. close']
# print(d_before_yesterday_close)
# print(data_list[1])

diff = round(float(yesterday_close) / float(d_before_yesterday_close) * 100 - 100, 1)
emoji = None
if float(yesterday_close) - float(d_before_yesterday_close) > 0:
    emoji = '$$$'
else:
    emoji = '^^^'
# print(diff)
if diff > 5:
    # print('Get News')

    parameters_news = {
        'q': COMPANY_NAME,
        'sortBy': 'popularity',
        'apikey': NEWS_API,
    }

    response_news = requests.get(NEWS_URL, params=parameters_news)
    data_news = response_news.json()
    articles = data_news['articles'][:3]
    # print(articles)
    messages = []
    for article in articles:
        news_title = article['title'].encode('utf-8')
        news_description = article['description'].encode('utf-8')
        messages.append(f'{STOCK}: {emoji} {diff}%\nHeadline: {news_title}.\nBrief: {news_description}.')
        # print(f'{STOCK}: {indicator}{diff}%\nHeadline: {news_title}\nBrief: {news_description}')
    print(messages)

    for message in messages:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f'Subject:STOCK ALERT!\n\n{message}'
            )




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

