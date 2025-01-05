import requests
from bs4 import BeautifulSoup
#designando a pagina
pagina=requests.get('https://myanimelist.net/topanime.php')
dados_pagina=BeautifulSoup(pagina.text, 'html.parser')

# Encontrar todos os elementos h3 com a classe anime_ranking_h3
dados_ranking=dados_pagina.find_all('h3', class_='anime_ranking_h3')

# Abrir o arquivo uma vez antes do loop
with open('C:/Users/Luiz/OneDrive/Documentos/Projetos/Automação de Tarefas no SQL SERVER com Python/nome-animes.txt', 'a') as arquivo:
   for h3 in dados_ranking:
     nome_anime=h3.find('a').text
     arquivo.write('\n{}'.format(nome_anime))





