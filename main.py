#!/venv/bin/python3
import os
from bs4 import BeautifulSoup
import requests
import smtplib


class ShulzHopperRequester:
    def __init__(self):
        self.url = 'https://shulz.ru/catalog/?c=1'
        self.button_locator = "//a[@id='buy_button_link']/text()"
        self.gmail_sender = ''
        self.gmail_password = ''
        self.send_to = ''
        self.subject = 'Изменения в наличии велосипедов'

    def run_parser(self):
        page = requests.get(self.url)
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text, 'lxml')
        text_on_page = (soup.find(id='status78')).text.strip()
        if text_on_page == "Ожидается":
            self.__mail_sender(text_on_page)
            os.system(f"./termux_notification.bash 'Велосипеда Shulz Hopper 3 нет в наличии'")
        else:
            os.system(f"./termux_notification.bash 'Статус изменился на:{text_on_page.capitalize()}'")
            self.__mail_sender(text_on_page)

    def __mail_sender(self, status):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.gmail_sender, self.gmail_password)
        server.sendmail(self.gmail_sender,
                        self.send_to,
                        f"Subject: {self.subject} \n\n "
                        f"Статус наличия велосипедов Shulz Hopper 3 изменен на: {status}".encode('utf-8'))


if __name__ == '__main__':
    notifayer = ShulzHopperRequester()
    notifayer.run_parser()
