#!/venv/bin/python3
import os
from bs4 import BeautifulSoup
import requests
"""
Инициализация начальных данных, юрл, локаторы,
"""

class ShulzHopperRequester:
    def __init__(self):
        self.url = 'https://shulz.ru/catalog/?id=78'
        self.button_locator = "//a[@id='buy_button_link']/text()"

    def run_parser(self):
        page = requests.get(self.url)
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text, 'lxml')
        ls = (soup.find(id='buy_button_link')).text
        os.system(f"./termux_notification.bash '{ls}'")

if __name__ == '__main__':
    notifayer = ShulzHopperRequester()
    notifayer.run_parser()

