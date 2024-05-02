def get_response(message: str) -> str:
    p_message = message.lower()
    if p_message == "moin moin":
        return "Whats up?"
    elif p_message.__contains__("mudda"):
        return "jo deine mudda!"
    elif p_message == "was ist der beste manga?":
        return "https://imgsrv.crunchyroll.com/cdn-cgi/image/format=auto,fit=contain,width=1200,height=675,quality=85/catalog/crunchyroll/4305090653ee4239dd0d797f1a4a6bdf.jpe"
    else:
        return "jo"
    