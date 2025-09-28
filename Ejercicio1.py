import re

mensaje_encriptado = "i+t a^r&a|p o/t^e=r+c~e#s e)j=a?s!n+e*m n@u s$e e^t$sE"
mensaje_volteado = mensaje_encriptado[::-1]
solo_letras = ""

for caracter in mensaje_volteado:
    # Verificamos si el caracter es una letra o un espacio
    if caracter.isalpha() or caracter == " ":
        solo_letras += caracter

print(solo_letras)