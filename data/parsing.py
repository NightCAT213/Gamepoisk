from bs4 import BeautifulSoup
import requests


def pars(link):
    res = requests.get('https://www.babybus.com/global/ru/index')