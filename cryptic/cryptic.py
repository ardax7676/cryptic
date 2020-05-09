import requests
from bs4 import BeautifulSoup
import sys

class Cryptic:
    def __init__(self):
        self.r = requests.get("https://altin.in/fiyat/bitcoin")
        self.soup = BeautifulSoup(self.r.content, "html.parser")
        self.ltc_info = self.soup.find("li", {"title": "LTC:USD Satış"})
        self.btc_info = self.soup.find("li", {"title": "BTC:USD Satış"})
        self.eth_info = self.soup.find("li", {"title": "ETH:USD Satış"})

    def price(self,output = "str"):
        if output == "str":
            return self._price
        elif output == "int":
            return self.__Int()
        elif output == "float":
            return self.__Float()
        else:
            print("Error")
            sys.exit(1)

    def __Int(self):
        return int(float(self._price))

    def __Float(self):
        return float(self._price)

class Btc(Cryptic):
    def __init__(self):
        super().__init__()
        self._price = self.btc_info.text
class Eth(Cryptic):
    def __init__(self):
        super().__init__()
        self._price = self.eth_info.text
class Ltc(Cryptic):
    def __init__(self):
        super().__init__()
        self._price = self.ltc_info.text

if __name__ != "__main__":
    btc = Btc()
    eth = Eth()
    ltc = Ltc()
else:
    sys.exit()


