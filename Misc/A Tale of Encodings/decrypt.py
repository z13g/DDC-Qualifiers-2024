def bin_to_ascii(bin_str):
    """Konverterer en binær streng til dens ASCII-repræsentation, ignorerer ikke-binære tegn."""
    # Fjern alle ikke-binære tegn fra strengen
    cleaned_bin_str = ''.join(filter(lambda x: x in '01', bin_str))
    
    # Konverter den rensede binære streng til ASCII
    ascii_text = ''.join([chr(int(cleaned_bin_str[i:i+8], 2)) for i in range(0, len(cleaned_bin_str), 8)])
    return ascii_text


def caesar_cipher(text, shifts):
    """Anvender Caesar-cipher dekodning på en tekst med specifikke skift og undtagelser."""
    decoded_text = ''
    shift_index = 0  # Reset for hver karakter
    for char in text:
        # Tjek om karakteren er en af de specificerede undtagelser
        if char in ['d', 'c', '_', '{', '}']:
            decoded_text += char
            continue  # Fortsæt til næste karakter uden at ændre shift_index
        
        shift = shifts[shift_index % len(shifts)]
        shift_index += 1  # Opdater shift_index for hver karakter der ikke er en undtagelse

        # Håndter dekodning for alfabetske tegn under hensyntagen til casing
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decoded_char = chr((ord(char) - start + shift) % 26 + start)
            decoded_text += decoded_char
        else:
            # Tilføj ikke-alfabetske tegn direkte til det dekodede tekst
            decoded_text += char

    return decoded_text

# Binær streng eksempel (placer din binære streng her)
bin_str = "010001004401101111440110111043011001017B010111114E010110016F0110010174011101005F01111101"

# Specifikke skift for Caesar-cipher dekodningen
shifts = [-3, -6, -4, 0, -10, 8, -12, 9, 11, 5]

# Konverter binær streng til ASCII
# Konverter binær streng til ASCII og anvend Caesar-cipher dekodning
ascii_text = bin_to_ascii(bin_str)  # Antager at denne funktion er defineret som før
decoded_text = caesar_cipher(ascii_text, shifts)

print("Dekodet tekst:", decoded_text)
