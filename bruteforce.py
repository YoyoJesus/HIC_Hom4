import random

# Returns standard alphabet
def return_alphabet():
    return list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Re-generates cipher alphabet based on a key
def generate_cipher_alphabet(key):
    alphabet = return_alphabet()
    scrambled_alphabet = alphabet.copy()
    random.seed(key)
    random.shuffle(scrambled_alphabet)
    return dict(zip(alphabet, scrambled_alphabet))

# Decrypts ciphertext using guessed key
def decrypt(ciphertext, key):
    cipher_map = generate_cipher_alphabet(key)
    reverse_map = {v: k for k, v in cipher_map.items()}
    plaintext = ""
    for char in ciphertext.upper():
        if char.isalpha():
            plaintext += reverse_map[char]
        else:
            plaintext += char
    return plaintext

# === Brute Force Function ===
def brute_force_cipher(ciphertext, known_word=None, key_range=100):
    print("Attempting brute-force attack...\n")
    successful_guesses = []

    for key in range(1, key_range + 1):
        decrypted = decrypt(ciphertext, key)
        if known_word:
            if known_word.upper() in decrypted:
                print(f"[MATCH] Key: {key} -> {decrypted}")
                successful_guesses.append((key, decrypted))
        else:
            print(f"Key {key}: {decrypted}")

    if not successful_guesses and known_word:
        print("\nNo matches found with the known word.")
    return successful_guesses

# === Example Usage ===
ciphertext = input("Paste the ciphertext to brute-force: ").strip()
known_word = input("Enter a known word or phrase from the original plaintext (leave empty to show all): ").strip() or None

brute_force_cipher(ciphertext, known_word=known_word)
