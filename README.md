# ASH-20 Hashfunktion

Die ASH-20 Hashfunktion ist eine kryptografisch sichere Hashfunktion, entwickelt von Joshua Dean Pond im Jahr 2023. 

## Über die ASH-20 Hashfunktion

Die ASH-20 Hashfunktion verwendet komplexe mathematische Operatoren, um eine sichere und nicht rückkehrbare Hashfunktion zu erstellen. Dies macht sie geeignet für kryptografische Anwendungen, bei denen die Integrität von Daten gewährleistet sein muss.

## Installation

bash: pip install avalanchesumhash20

## Dokumentation

Eine ausführliche Dokumentation der ASH-20 Hashfunktion ist im Skript enthalten. Sie können sie finden und weitere Details in der [Script-Dokumentation](
avalanchesumhash20/docs/script_documentation.pdf).


## Beispiel script
```
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
```
## Beispiel Output
```
C:\Users\Joshua\OneDrive\Desktop>ASH-20
Text: Hello World
Eingabe-Text: Hello World
Verschlüsselter Wert: 72730973721879097623944926376665313

C:\Users\Joshua\OneDrive\Desktop>
```
Das ist ein beispiel wie sie einen Text verschlüsseln können


## Mathematische Operatoren
Die ASH-20 Hashfunktion verwendet komplexe mathematische Operatoren, um eine sichere und nicht rückkehrbare Hashfunktion zu erstellen. Dies macht sie geeignet für kryptografische Anwendungen, bei denen die Integrität von Daten gewährleistet sein muss.

Die ASH-20 Hashfunktion nutzt verschiedene mathematische Operatoren, um die Sicherheit und Einweg-Natur der Hashfunktion zu gewährleisten:

### Avalanche: 
Durch die Verwendung der Ableitungsfunktion cos wird ein Avalanche-Effekt erzeugt, bei dem kleine Änderungen im Eingabetext zu drastisch unterschiedlichen Hashwerten führen.

### XOR (Exklusives Oder): 
Die XOR-Operation wird verwendet, um Bits im Hashwert zu kombinieren und dabei sicherzustellen, dass kleine Änderungen im Eingabetext zu unvorhersehbaren Änderungen im Hash führen. Siehe [XOR-Verknüpfung](avalanchesumhash20/docs/xor_verknüpfung.pdf)

### OR (Oder):
Die OR-Operation wird verwendet, um bestimmte Bits im Hashwert zu setzen, um die Komplexität und Sicherheit zu erhöhen.

### AND (Und):
Die AND-Operation wird verwendet, um bestimmte Bits im Hashwert zu löschen und die Verteilung der Bits zu beeinflussen.

### Funktionen höheren Grades und quadratische Funktionen:
Neben den grundlegenden Operationen werden auch Funktionen höheren Grades sowie quadratische Funktionen eingesetzt, um den Hash zu einem einweg Hash zu machen. Dies erhöht die Komplexität und erschwert das Zurückverfolgen des Hashwertes. Genaue beispiele siehe: [Math. Operatoren (Einwegfunktion)](avalanchesumhash20/docs/Einwegfunktion.pdf)

### Bitverschiebung (Shift) um 7:
Durch die Verschiebung der Bits im Hashwert um 7 Positionen wird die Verteilung der Bits weiter verändert und die Sicherheit erhöht.

### Modulo mit Outputlength:
Die Anwendung des Modulo-Operators mit der Output-Length stellt sicher, dass der Hashwert innerhalb der gewünschten Länge bleibt.

### Zerstückung und Verkettung des Hashes:
Der Hashwert wird zerstückelt und neu angeordnet, um die Einweg-Natur der Hashfunktion zu verstärken.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE)-Datei für Details.

## Kontakt

Joshua Dean Pond  
Email: joshua.pond11@gmail.com
