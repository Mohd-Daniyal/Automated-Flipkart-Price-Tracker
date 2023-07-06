import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/realme-11-pro-5g-sunrise-beige-128-gb/p/itm3f783627a36ec?pid=MOBGPUNGXUZQKTTB&param=32323&otracker=clp_bannerads_1_19.bannerAdCard.BANNERADS_xz_mobile-phones-store_YOPBIW4FYATR"
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(name="div", class_="_30jeq3 _16Jk6d").text
price_without_currency = price.split("₹")
price_float = float(price_without_currency[1].replace(",",""))
title = soup.find(name="span", class_="B_NuCI").text
buy_price = 30000.0

if price_float < buy_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587 ) as connection:
        connection.starttls()
        result=connection.login("mohddaniyal.hasan2022@vitstudent.ac.in", "lxgvpnttzbmgjsis")
        connection.sendmail(
            from_addr = "mohddaniyal.hasan2022@vitstudent.ac.in",
            to_addrs = "hassansahaab88@gmail.com",
            msg=f"Subject:Flipkart Price Alert\n\n{message}\n{url}".encode("utf-8")
        )