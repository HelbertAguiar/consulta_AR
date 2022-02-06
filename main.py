import requests
from bs4 import BeautifulSoup

# TO:DO Implements an Solver Captcha 

class RequestApi():

    url_custom_api:str = 'https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm'

    def request(self, code_to_tracker):
        with requests.Session() as session:
            session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'})
            form = {'acao': 'track',
                    'objetos': code_to_tracker,
                    'btnPesq': 'Buscar',
                    }
            return session.post(self.url_custom_api, data=form, allow_redirects=True)
    
    # def printRequest(self, r, method, url_solicitada, form=None):
    #     print('\nURL Solicitada da requisicao: '.ljust(28, ' ') + url_solicitada)
    #     print('URL Efetiva da requisicao: '.ljust(30, ' ') + r.url)
    #     print('History redirect: '.ljust(30, ' ') + str(r.history))
    #     print('Status code: '.ljust(30, ' ') +
    #         str(r.status_code) + '\tReason: ' + str(r.reason))
    #     print('Elapsed: '.ljust(30, ' ') + str(r.elapsed) +
    #         '\tEnconding: ' + str(r.encoding))
    #     if form != None:
    #         printForm(form)
    #     print('\nOs headers da requisicao do ' + method + ' sao: ' + '\n')
    #     print("\n".join("{} {}".format(k.ljust(28, ' '), v.ljust(30, ' '))
    #                     for k, v in r.request.headers.items()))
    #     print('\nOs headers da resposta do ' + method + ' sao: ' + '\n')
    #     print("\n".join("{} {}".format(k.ljust(28, ' '), v.ljust(30, ' '))
    #                     for k, v in r.headers.items()))
    #     print('\n' + ''.ljust(158, '='))


    # def printForm(self, form):
    #     print('\nForm da requisicao:')
    #     print("\n".join("{} ".format(k) for k in form.items()))

class TrackerAR():

    def query(self, code_ar):
        req = RequestApi()
        response = req.request(code_ar)
        soup = BeautifulSoup(response.content, "html.parser")

        with open("log.html", "w") as f:
            f.write(response.text)

tracker = TrackerAR()
tracker.query("BK285877825BR")