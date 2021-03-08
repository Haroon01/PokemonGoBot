import requests
from bs4 import BeautifulSoup
import lxml

class Scraper:

    def __init__(self):
        self.site = "https://thesilphroad.com/raid-bosses" # website where raid bosses are grabbed from

    def getRaidBoss(self):
        bosses = [] # where current bosses grabbed from website will be stored
        source = requests.get(self.site).text # get website source as text
        soup = BeautifulSoup(source, "lxml")
        pokemons = soup.findAll("div", attrs = {"class": "boss-name"}) # get div class text where raid bosses are displayed
        for pokemon in pokemons:
            bosses.append(pokemon) # add all raid bosses to a list
        return bosses

