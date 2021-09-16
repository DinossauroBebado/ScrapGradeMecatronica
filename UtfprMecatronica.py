from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import info

PATH = "C:\Program Files (x86)\chromedriver.exe"

usuario = info.usuario
senha = info.senha

site = "https://sistemas2.utfpr.edu.br/login?returnUrl=%2Fdpls%2Fsistema%2Faluno01%2Fmpmenu.inicio"


def login(usuario, senha):
    web.find_element_by_xpath(
        '/html/body/app-root/app-login/div/div/p-card/div/div/div/div/form/div[2]/div/input').send_keys(usuario)
    web.find_element_by_xpath(
        '/html/body/app-root/app-login/div/div/p-card/div/div/div/div/form/div[3]/div/input').send_keys(senha)
    web.find_element_by_xpath(
        '/html/body/app-root/app-login/div/div/p-card/div/div/div/div/form/div[4]/div/button/span[2]').click()
    print('Logado ')


def matrizesCuriculares():
    # Clica nas matrizes curriculares
    web.find_element_by_xpath(
        '/html/body/div[3]/div/center/table/tbody/tr/td[11]').click()
    iframe = web.find_element_by_xpath('/html/body/iframe')
    web.switch_to.frame(iframe)  # entra no iframe
    print("on Iframe")
    sleep(1)
    html_tabela = web.page_source  # pega o html da tabela
    web.switch_to.default_content()
    web.close()
    return html_tabela


def read_html():
    soup = BeautifulSoup(matrizesCuriculares(), 'html.parser')

    grade = soup.find(id="grade")

    tbodys = grade.find_all('tbody')

    tread = grade.find('thead')

    # adiciona o cabecalho --> esta repetido sei la pq

    matrix_curricular_mecatronica = '<table>' + str(tread) + '\n'

    # passa pelos tbodys juntando todos em um so

    for tbody in tbodys:
        matrix_curricular_mecatronica = matrix_curricular_mecatronica + \
            str(tbody)

    matrix_curricular_mecatronica = matrix_curricular_mecatronica + '</table'
    df = pd.read_html(matrix_curricular_mecatronica)

    print(df[0].iloc[50])


if __name__ == '__main__':

    web = webdriver.Chrome(PATH)
    web.get(site)
    login(usuario, senha)
    sleep(1)
    read_html()
