# ASH-20 Hashfunktion

Die ASH-20 Hashfunktion ist eine kryptografisch sichere Hashfunktion, entwickelt von Joshua Dean Pond im Jahr 2023. 

## Über die ASH-20 Hashfunktion

Die ASH-20 Hashfunktion verwendet komplexe mathematische Operatoren, um eine sichere und nicht rückkehrbare Hashfunktion zu erstellen. Dies macht sie geeignet für kryptografische Anwendungen, bei denen die Integrität von Daten gewährleistet sein muss.

## Installation

bash: pip install avalanchesumhash20

## Dokumentation

Eine ausführliche Dokumentation der ASH-20 Hashfunktion ist im Skript enthalten. Sie können sie finden und weitere Details in der [Script-Dokumentation](docs/script_documentation.pdf).


## Beispiel script
from avalanchesumhash20 import AvalancheSumHash20

def main():
    input_text = input("Text: ")
    output_length = 79357612835769157957719395357591595
    iterations = 420
    modulo_value = 93537791153957593571955971579179595

    hash_generator = AvalancheSumHash20(input_text, output_length, iterations, modulo_value)
    result = hash_generator.main()

    print("Eingabe-Text:", input_text)
    print("Verschlüsselter Wert:", result)

if __name__ == "__main__":
    main()

## Beispiel Output
```
C:\Users\Joshua\OneDrive\Desktop>ASH-20
Text: Hello World
Eingabe-Text: Hello World
Verschlüsselter Wert: 72730973721879097623944926376665313

C:\Users\Joshua\OneDrive\Desktop>

Das ist ein beispiel wie sie einen Text verschlüsseln können
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE)-Datei für Details.

## Kontakt

Joshua Dean Pond  
Email: joshua.pond11@gmail.com
