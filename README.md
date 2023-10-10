# ash-20 hash function
The ASH-20 hash function is a cryptographic safe hash function developed by Joshua Dean Pond in 2023.
## about the ash-20 hash function
The ASH-20 hash function uses complex mathematical operators to create a safe and non-traceable hash function. This makes it suitable for cryptographic applications where the integrity of data must be ensured.
## installation
bash: pip install avalanchesumhash20
## documentation
A detailed documentation of the ASH-20 hash function is included in the script. You can find them and more details in the [Script-Dokumentation](avalanchesumhash20/docs/script_documentation.pdf).
## example script
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

## example output
    C:\Users\Joshua\OneDrive\Desktop>ASH-20
    Text: Hello World
    Eingabe-Text: Hello World
    Verschlüsselter Wert: 72730973721879097623944926376665313
    
    C:\Users\Joshua\OneDrive\Desktop>

This is an example of how you can encrypt a text
## Mathematical Operators
The ASH-20 hash function uses complex mathematical operators to create a safe and non-traceable hash function. This makes it suitable for cryptographic applications where the integrity of data must be ensured. All mathematical aspects are explained here: [mathematical aspects](avalanchesumhash20/docs/Mathematische_Aspekte.pdf).

The ASH-20 hash function uses various mathematical operators to ensure safety and Einweg-Natur hash function:
### Avalanche (cos function):
Using the derivative function cos creates a Avalanche-Effekt in which small changes in the input text lead to drastically different hash values. The function: [f(H) = aH² + bH + c](avalanchesumhash20/docs/Einwegfunktion.pdf).
The "H" in the function represents the hash.

### XOR Operation (⊕):
The XOR operation is used to combine bits in the hash value and ensure that small changes in the input text lead to unpredictable changes in the hash. See [XOR combination](avalanchesumhash20/docs/xor.pdf)
### OR (|):
The OR operation is used to set certain bits in the hash value to increase complexity and security.
### AND (&):
The AND operation is used to delete certain bits in the hash value and to influence the distribution of bits.
### functions of higher grades and square functions:
In addition to the basic operations, functions of higher degrees and square functions are also used to make the hash a one-way hash. This increases the complexity and makes it difficult to trace the hash value. See examples: [Math. Operators (unit function)](avalanchesumhash20/docs/Einwegfunktion.pdf)
### bit shift (shift) to 7:
By shifting the bits in the hash value by 7 positions, the distribution of bits is further changed and the safety is increased.
### modulo with outputlength:
The application of the Modulo-Operators with the Output-Length ensures that the hash value remains within the desired length.
### fragmentation and chaining of the hashes:
The hash value is divided and repositioned to increase the Einweg-Natur of the hash function.
## license
This project is licensed under the MIT license - see the [LICENSE](LICENSE)-Datei for details.
## contact
Joshua Dean Pond Email: [joshua.pond11@gmail.com](mailto:joshua.pond11@gmail.com)
