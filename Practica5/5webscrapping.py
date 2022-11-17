import requests
from bs4 import BeautifulSoup
import re
from datetime import date
from io import open


def personal_info(url):
    webpage_response = requests.get(url)

    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    today = date.today()

    infobox = soup.find(class_="infobox")
    infobox = str(infobox)
    infobox = infobox.split("<tr>")[4:]

    for element in infobox:
        matchName = re.findall(">Nombre<", element)
        if matchName:
            name = element.split("\n")[1].split("<")[0]

        matchBorn = re.findall(">Nacimiento<", element)
        if matchBorn:
            bornPlace = element.split("\n")[1].split("<")[2]
            bornPlace = re.findall('title="(\w+)', bornPlace)[0]
            bornDate = element.split("\n")[1].split("<")[0]

        matchActive = re.findall(">Años<", element)
        if matchActive:
            active = element.split(">")
            for x in active:
                match = re.findall("(\d{4})", x)
                if match:
                    active = int(match[0])
                    years = (today.year - active)+1
                    years = str(years)
                    
        matchPodiums = re.findall(">Podios<", element)
        if matchPodiums:
            podiums = element.split("\n")[1].split("<")[0]

        matchWins = re.findall(">Victorias<", element)
        if matchWins:
            victorias = element.split("\n")[1].split("<")[0]            

    return name, bornDate, bornPlace, podiums, victorias, years


name, age, bornPlace, podiums, victories, years = personal_info("https://es.wikipedia.org/wiki/Sergio_P%C3%A9rez")


salida = open("salida.txt", "a")
salida.write(" Nombre: " + name)
salida.write("\n\n Edad: " + age)
salida.write("\n\n Ciudad: " + bornPlace)
salida.write("\n\n Podios: "+podiums)
salida.write("\n\n Victorias: "+victories)
salida.write("\n\n Años activo: "+years)

salida.close()

