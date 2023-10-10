from avalanchesumhash20 import AvalancheSumHash20

if __name__ == "__main__":
    # Setze die Parameter entsprechend deiner Anforderungen
    output_length = 79357612835769157957719395357591595
    iterations = 420
    modulo_value = 93537791153957593571955971579179595

    # Erstelle eine Instanz des AvalancheSumHash20-Objekts
    ash20 = AvalancheSumHash20(output_length, iterations, modulo_value)

    # Benutzereingabe für den zu verschlüsselnden Text
    input_text = input("Text: ")

    # Verschlüssele den Text
    encrypted_value = ash20.encrypt(input_text)

    # Gib die Ergebnisse aus
    print("Eingabe-Text:", input_text)
    print("Verschlüsselter Wert:", encrypted_value)
