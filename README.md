# b3ticker
Web Scraping tickers in B3 - Brasil Bolsa Balcão S.A., formerly BM&amp;FBOVESPA, is a stock exchange located in São Paulo, Brazil

## Features
Crawling CVM codes and B3 tickers from B3 url.

## Requirements
* BeautifulSoup - http://www.crummy.com/software/BeautifulSoup/

## Cloning and Install
```
git clone https://github.com/allan-oliveira/B3Ticker
cd B3Ticker
sudo python setup.py install
```

## Usage
```
from b3ticker import B3Ticker
import string

def export_data(lpath, lst):
    with open(lpath, 'w') as f:
        for item in lst:
            f.write("%s\n" % item)

def main():
    test_set = set(string.ascii_uppercase).union(set(string.digits))
    b3ticker = B3Ticker()
    cvm_codes = b3ticker.get_cvm_codes(test_set)
    export_data('cvm_codes.txt', cvm_codes)

    b3_tickers = b3ticker.get_b3_tickers(cvm_codes)
    export_data('b3_tickers.txt', b3_tickers)

if __name__ == '__main__':
    main()
```