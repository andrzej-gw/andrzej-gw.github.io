import wikipediaapi
import requests
from bs4 import BeautifulSoup

def main():
    wikipedia_api = wikipediaapi.Wikipedia('Aplikacje_WWW (jedrekgwiazda@gmail.com)', 'en')

    wikipedia_odpowiedz = wikipedia_api.page("Chess opening")

    with open("index.md", "w") as index:
        index.write("# Chess openings\n\n")
        index.write(wikipedia_odpowiedz.summary+"\n\n")
        index.write("[Short list of some fancy openings](https://andrzej-gw.github.io/chess_openings)\n\n")

    request_otwarc = requests.get('https://www.thechesswebsite.com/chess-openings/')

    strona_z_otwarciami = request_otwarc.text

    soup = BeautifulSoup(strona_z_otwarciami, 'html.parser')

    lista_otwarc = []

    for otwarcie in soup.find_all("h5"):
        lista_otwarc.append(otwarcie.string)

    ile_otwarc = 0

    with open("chess_openings.md", "w") as plik_z_lista_otwarc:
        plik_z_lista_otwarc.write("# List of chess openings:\n\n")

        for otwarcie in lista_otwarc:

            wikipedia_odpowiedz = wikipedia_api.page(otwarcie)
            print("Czy sa dane o "+otwarcie, end="? : ")
            print(wikipedia_odpowiedz.exists())
            
            if wikipedia_odpowiedz.exists():
                ile_otwarc += 1
                nazwa = "".join(otwarcie.split())
                plik_z_lista_otwarc.write("["+otwarcie+"](https://andrzej-gw.github.io/"+nazwa+")\n\n")
                with open(nazwa+".md", "w") as plik_z_otwarciem:
                    plik_z_otwarciem.write("# "+otwarcie+"\n\n")
                    plik_z_otwarciem.write(wikipedia_odpowiedz.summary+"\n\n")
                if ile_otwarc == 50:
                    break

main()
