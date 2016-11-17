#!/usr/bin/ env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

lista = []
imagens = []

url = "http://www.sinonimos.com.br/manifestacao/"


def pesquisa(url):
    global lista
    global imagens
    html = urlopen(url)
    site = BeautifulSoup(html, "lxml")

    for link in site.findAll("a"):
        if 'href' in link.attrs:
            if "/" in link.attrs['href'][0]:
                if not link.attrs['href'] in lista:
                    lista += [link.attrs['href']]
                    print (link.attrs['href'])
    for link in site.findAll("img"):
        if 'src' in link.attrs:
            if not link.attrs['src'] in imagens:
                imagens += [link.attrs['src']]


pesquisa(url)
for i in lista:
    pesquisa(url + i)

for i in lista:
    print(i)
print(len(lista))

for i in imagens:
    print(i)

