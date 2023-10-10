import scipy.integrate as spi
from math import cos
import warnings

class AvalancheSumHash20:
    def __init__(self, output_length, iterations, modulo_value):
        self.output_length = output_length
        self.iterations = iterations
        self.modulo_value = modulo_value

    def convert_text_to_positional_decimal(self, text):
        decimal_values = [ord(char) * (len(text) - i) ** 2 for i, char in enumerate(text)]
        return sum(decimal_values)

    def avalanche_sum_hash(self, x, input_text):
        result = x

        for _ in range(self.iterations):
            result = (result ^ x) + (result & x) | (result ^ x)
            result ^= ord(input_text[0])

            for bit in bin(x)[2:]:
                result = (result << 1) | int(bit)

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                result = int(spi.quad(cos, 0, result)[0])

            result = result % self.modulo_value
            x = (x + 1) % self.modulo_value

        return result

    def shift_digits(self, value):
        shifted_value = ""
        for digit in str(value)[::-1]:
            shifted_digit = (int(digit) + 7) % 10
            shifted_value += str(shifted_digit)
        return int(shifted_value)

    def concatenate_in_pattern(self, value, num_parts):
        value_str = str(value)
        length = len(value_str)

        part_size = length // num_parts
        parts = []

        for i in range(num_parts):
            start = i * part_size
            end = (i + 1) * part_size
            parts.append(value_str[start:end])

        concatenated_value = "".join(parts[num_parts // 2:] + parts[:num_parts // 2])
        return int(concatenated_value) % self.modulo_value  # Hier wird die Modulo-Operation hinzugefügt

    def encrypt(self, input_text):
        text_decimal_value = self.convert_text_to_positional_decimal(input_text)
        combined_value = text_decimal_value * self.output_length
        encrypted_value = self.avalanche_sum_hash(combined_value, input_text)
        shifted_encrypted_value = self.shift_digits(encrypted_value)
        concatenated_value = self.concatenate_in_pattern(shifted_encrypted_value, 5)

        # Modulo-Operation mit ausreichend großer Zahl
        concatenated_value %= 10**20

        return concatenated_value

if __name__ == "__main__":
    output_length = 79357612835769157957719395357591595
    iterations = 420
    modulo_value = 93537791153957593571955971579179595

    ash20 = AvalancheSumHash20(output_length, iterations, modulo_value)

    input_text = input("Text: ")
    encrypted_value = ash20.encrypt(input_text)

    print("Eingabe-Text:", input_text)
    print("Verschlüsselter Wert:", encrypted_value)
