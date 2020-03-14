import os, shutil
import requests
import json

cont = 0;
caminhoPre = 'C:/Users/Digo/Documents/imgAPI/'
caminhoPos = 'C:/Users/Digo/Documents/imgAPI/envio/'

for x, y, arquivo in os.walk(caminhoPre):
    print(arquivo)
    break



for img in arquivo:
    os.replace(caminhoPre+img,caminhoPos+img)
    cont += 1
    
    
print(cont)