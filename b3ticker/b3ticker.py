
from requests import get
from bs4 import BeautifulSoup
from collections import OrderedDict

class B3Ticker:
    def __init__(self):
        self._headers = OrderedDict() 
        self._headers["Host"] = "bvmf.bmfbovespa.com.br"
        self._headers["Connection"] = "keep-alive"
        self._headers["Upgrade-Insecure-Requests"] = "1"
        self._headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
        self._headers["Accept"] = "*/*"
        self._headers["Accept-Encoding"] = "gzip, deflate"
        self._headers["Accept-Language"] = "en-US,en;q=0.9"
    
    def _get_soup(self, url):
        response = get(url, headers=self._headers)
        return BeautifulSoup(response.text, 'html.parser')

    def get_cvm_codes(self, expression_list):
        links = []
        for target_list in expression_list:
            url = f'http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx?Letra={target_list}'
            soup = self._get_soup(url)
            links += soup.select('#ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_grdEmpresa_ctl01 > tbody > tr > td:nth-of-type(1) > a')
        return list(map(lambda x : x.get('href', None).replace('ResumoEmpresaPrincipal.aspx?codigoCvm=',''), links))
    
    def get_b3_tickers(self, expression_list):
        links = []
        for target_list in expression_list:
            url = f'http://bvmf.bmfbovespa.com.br/pt-br/mercados/acoes/empresas/ExecutaAcaoConsultaInfoEmp.asp?CodCVM={target_list}'
            soup = self._get_soup(url)
            links += soup.select('.LinkCodNeg')
        return set(list(map(lambda x : x.getText(), links)))        
