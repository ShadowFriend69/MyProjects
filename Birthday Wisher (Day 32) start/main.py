# import smtplib
#
# my_email = 'mukhammad.mamleev@mail.ru'
# my_password = 'rn5JHnEwmEQhCFTPi6F2'
#
# with smtplib.SMTP('smtp.mail.ru') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs='mamleevaaisha228@gmail.com',
#         msg='Subject:Test\n\nThis is the body of my email'
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# year = now.year
# print(year)
# month = now.month
# print(month)
# day_af_week = now.weekday()
#
# print(day_af_week)
#
#
# date_of_birth = dt.datetime(year=1998, month=1, day=2, hour=6)
# print(date_of_birth)


import smtplib
import datetime as dt
from random import choice

MY_EMAIL = 'mukhammad.mamleev@mail.ru'
MY_PASSWORD = 'rn5JHnEwmEQhCFTPi6F2'


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open('quotes.txt') as data_file:
        data = data_file.readlines()
        quote = choice(data)

    with smtplib.SMTP('smtp.mail.ru') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f'Subject:Monday Quote!\n\n{quote}'
        )







