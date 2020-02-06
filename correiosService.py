import requests
from bs4 import BeautifulSoup
import urllib
import datetime
from endereco import Endereco

if __name__ == "__main__":
    pass

session = requests.session()

def ConsultarCepPage(cep):
    filtro = {
    'relaxation':cep,
    'tipoCEP':'ALL',
    'semelhante': 'N'
    }

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7'}

    dados_retorno_get = session.get('http://www.buscacep.correios.com.br/sistemas/buscacep/', headers=head)

    dados_retorno_post = session.post('http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm', 
    data=filtro, headers=head, verify=False, allow_redirects=False)

    soup_dados_retorno = BeautifulSoup(dados_retorno_post.text, 'html.parser')
    linhas = soup_dados_retorno.find_all('tr')

    for p in linhas:
        p2 = p.find_all('td')
        if len(p2) == 4 and len(p2[3].getText()) == 9:
            endereco = Endereco(p2[0].getText(), p2[1].getText(), p2[2].getText(), p2[3].getText())

            return endereco

    raise ValueError(f'Cep não localizado!')