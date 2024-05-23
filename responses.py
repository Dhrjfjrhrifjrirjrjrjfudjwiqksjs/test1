
import requests
import asyncio 
import random 
liste = ("https://m.media-amazon.com/images/M/MV5BNjMxMDJkNGQtMDkwMy00ZmQyLThjNWQtODYyODU2MmYwYTA1XkEyXkFqcGdeQXVyMTQ3MjMyMTYz._V1_FMjpg_UX1000_.jpg","https://m.media-amazon.com/images/I/51K4w8DY5cL._AC_UF894,1000_QL80_DpWeblab_.jpg","https://i0.wp.com/www.nerdsandbeyond.com/wp-content/uploads/2024/03/01e8f2831c6071036502e1816d2cd14acde06934bc579ad00d9f92188f3ec7e8.jpg?fit=800%2C450&ssl=1", "https://demonslayer-hinokami.sega.com/img/purchase/digital-deluxe.jpg")
def get_response(message: str) -> str:
    p_message = message.lower()
    if p_message == "moin moin":
        return "Whats up?"
    elif p_message.__contains__("mudda"):
        return "jo deine mudda!"
    elif p_message == "was ist der beste manga?":
        return "https://imgsrv.crunchyroll.com/cdn-cgi/image/format=auto,fit=contain,width=1200,height=675,quality=85/catalog/crunchyroll/4305090653ee4239dd0d797f1a4a6bdf.jpe"
    elif p_message == "was ist deine anime empfehlung?":
        anzahl_bilder_der_liste = len (liste)
        random_zahl = random.randint(0,anzahl_bilder_der_liste -1) 
        return liste[random_zahl]
    elif p_message == "random bilder":
        verschiedene_zahlen = random.randint(1,250) 
        url = "https://rickandmortyapi.com/api/character/"
        neue_url = url+ str(verschiedene_zahlen)
        r = requests.get(neue_url) 
        return (r.json()["image"])
    elif p_message == "Teewasser":
        return "Wie lange soll der Timer dauern"
    else:
        return "jo"



async def set_timer(dauer: int, thema: str): 
        await asyncio.sleep(dauer)
        return f'Der Timer für{thema}ist abgelaufen!'