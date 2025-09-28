def analizador_url(url):

    if "://" in url:
        partes = url.split("://")
        protocolo = partes[0]
        resto = partes[1]
    else:
        protocolo = "No encontrado"
        resto = url

    if "/" in resto:
        partes2 = resto.split("/", 1)
        dominio = partes2[0]
        recurso = partes2[1]
    else:
        dominio = resto
        recurso = "No hay recurso"

    return protocolo, dominio, recurso

url = "https://www.ejemplo.com/pagina1/recurso.html"

protocolo, dominio, recurso = analizador_url(url)

print("Protocolo:", protocolo)
print("Dominio:", dominio)
print("Recurso:", recurso)