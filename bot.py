from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome('../drivers/chromedriver')
login = ''
senha = ''
linkSorteio = 'https://www.instagram.com/p/CYmAbLqrTm_/'
comentarios = ['Eu quero', 'Eu querooo', 'Já ganhei', 'É meeeu', 'Já agradeço por ter ganhado kk', 'É meu', 'Só vem!', 'Vou ganhar']

driver.get('https://www.instagram.com/accounts/login/')

time.sleep(2) # Espera 2seg para então inserir usuário e senha

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(login)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)

time.sleep(3)

driver.get(linkSorteio)

time.sleep(3)

def sorteio():
    comentario = random.randint(0, 7)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').click()
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').send_keys(comentarios[comentario])
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').send_keys(Keys.ENTER)

i = 0

while (i<6):
    j = 0
    while (j<10):
        sorteio()
        i += 1
        time.sleep(45)
    time.sleep(600)