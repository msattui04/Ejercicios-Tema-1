def genereador_adn(longitud):
    import random

    bases = ['A', 'T', 'C', 'G']
    adn = ""
    for i in range(longitud):
        adn += random.choice(bases)
    return adn

print(genereador_adn(10))