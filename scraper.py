import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/dp/B01HBF5WBI/ref=pantry_car_hybr_de'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[1:])

    if(converted_price < 18.0):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 18.0):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('lenovo3s540@gmail.com', '25december1999')

    subject = 'Price fell down!'
    body = 'check the amazon link https://www.amazon.in/dp/B01HBF5WBI/ref=pantry_car_hybr_de'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'lenovo3s540@gmail.com',
        'sainihimanshu.1999@gmail.com',
        msg
    )

    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(3600)
