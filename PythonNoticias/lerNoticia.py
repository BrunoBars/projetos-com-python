import requests
import pyttsx3
import msvcrt
from bs4 import BeautifulSoup

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
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b' ':    # this will check if space key is pressed
                    engine.setProperty('volume', 0)
                    print("Paused, Press Space to Resume")
                    while True:
                        if msvcrt.kbhit():
                            key = msvcrt.getch()
                            if key == b' ':
                                engine.setProperty('volume', 1)
                                print("Resumed")
                                break
                            elif key == b'\x1b': # aqui vai verificar de a tecla esc foi precionado
                                engine.stop()
                                break
                else:
                    engine.stop()
                    break

            
                   
            
            engine.runAndWait()
            resultado.append(noticia)
            

            with open("resultado.txt", "w") as file:
                file.writelines("%s\n" % item for item in resultado)


            


                    





