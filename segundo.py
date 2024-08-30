texto = input(print("Digite um texto:"))
letra = "a"

contagem = texto.lower().count(letra)

if letra in texto:
    print("A letra 'A' está presente ",contagem," vezez no texto.")
else:
    print("A letra 'A' não está presente no texto")