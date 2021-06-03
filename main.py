import requests
from bs4 import BeautifulSoup

def printRequest(r, method, url_solicitada, form=None):
    print('\nURL Solicitada da requisicao: '.ljust(28, ' ') + url_solicitada)
    print('URL Efetiva da requisicao: '.ljust(30, ' ') + r.url)
    print('History redirect: '.ljust(30, ' ') + str(r.history))
    print('Status code: '.ljust(30, ' ') +
          str(r.status_code) + '\tReason: ' + str(r.reason))
    print('Elapsed: '.ljust(30, ' ') + str(r.elapsed) +
          '\tEnconding: ' + str(r.encoding))
    if form != None:
        printForm(form)
    print('\nOs headers da requisicao do ' + method + ' sao: ' + '\n')
    print("\n".join("{} {}".format(k.ljust(28, ' '), v.ljust(30, ' '))
                    for k, v in r.request.headers.items()))
    print('\nOs headers da resposta do ' + method + ' sao: ' + '\n')
    print("\n".join("{} {}".format(k.ljust(28, ' '), v.ljust(30, ' '))
                    for k, v in r.headers.items()))
    print('\n' + ''.ljust(158, '='))


def printForm(form):
    print('\nForm da requisicao:')
    print("\n".join("{} ".format(k) for k in form.items()))

with requests.Session() as session:

    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'})

    url_custom = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm'
    ar = 'BJ230414885BR'
    # ar = 'BK285863866BR'

    form = {'acao': 'track',
            'objetos': ar,
            'btnPesq': 'Buscar',
            }

    r = session.post(url_custom, data=form, allow_redirects=True)
    soup = BeautifulSoup(r.content, "html.parser")

    status = "Não entregue"
    tags = soup.find_all('strong')    
    for tag in tags:
        if tag.text == 'Objeto entregue ao destinatário':
            status = "Entregue"


    print(status)
    # print(soup.encode("utf-8"))