import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

url = "Your Wishlisted Product URL"
header = {
    "User-Agent" : "Your data",
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
        result=connection.login("sender email", "app password")
        connection.sendmail(
            from_addr = "Sender email address",
            to_addrs = "Receiver email address",
            msg=f"Subject:Flipkart Price Alert\n\n{message}\n{url}".encode("utf-8")
        )
