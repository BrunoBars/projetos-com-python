import requests
import pyttsx3
import msvcrt
from bs4 import BeautifulSoup
from tkinter import *

# Variável global para controlar se o código está sendo executado
is_running = False

def start_button_click():
    global is_running
    is_running = True
    
    url = "https://www.cnnbrasil.com.br/"

    headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    news = soup. find_all('a', class_='home__post')

    try:
        with open("resultado.txt", "r") as file:
            resultado = file.readlines()
            resultado = [x.strip() for x in resultado]
    except FileNotFoundError:
        resultado = []

    for new in news:
        titulo = new.find('span', class_="home__title__label").get_text().strip()
        conteudo = new.find('h3', class_='home__title').get_text().strip()
        noticia = titulo + '. ' + conteudo   

        if noticia not in resultado: 
                
                engine = pyttsx3.init()
                engine.setProperty('rate', 250)
                engine.say(noticia)
                engine.runAndWait()
                resultado.append(noticia)
                

                with open("resultado.txt", "w") as file:
                    file.writelines("%s\n" % item for item in resultado)

def stop_button_click():
    global is_running
    is_running = False
    
root = Tk()

# Cria o botão de início
start_button = Button(root, text="Iniciar", command=start_button_click)
start_button.pack()

# Cria o botão de parada
stop_button = Button(root, text="Parar", command=stop_button_click)
stop_button.pack()

root.mainloop()
