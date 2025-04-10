import random

def return_alphabet():
    return list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def generate_cipher_alphabet(key):
    alphabet = return_alphabet()
    scrambled_alphabet = alphabet.copy()
    random.seed(key)  # Seed the random number generator with the key
    random.shuffle(scrambled_alphabet)  # Shuffle the alphabet based on the key
    return dict(zip(alphabet, scrambled_alphabet))

def encrypt(plaintext, key):
    cipher_map = generate_cipher_alphabet(key)
    ciphertext = ""

    for char in plaintext.upper():
        if char.isalpha():
            ciphertext += cipher_map[char]
        else:
            ciphertext += char
        
    return ciphertext

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

# ==== Main Function ====
plaintext = "Austin Sternberg"

secret_key = random.randint(1, 100)  # Generate a random key for encryption
ciphertext = encrypt(plaintext, secret_key)
print(f"Ciphertext: {ciphertext}")

print("\nTry to guess the key!")
guess = ""

# ask if the user wants to be in easy or hard mode
mode = input("Choose difficulty level (easy/hard): ").strip().lower()
if mode == "easy":
    print("You will be given a higher/lower hint after each guess.")
else:
    print("You will not receive any hints.")

while guess != secret_key:
    guess = input("\nEnter your guess for the key (1-100): ")
    if not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue

    guess = int(guess)

    # easy mode will give hints
    if mode == "easy":
        if guess < secret_key:
            print("Higher!")
        elif guess > secret_key:
            print("Lower!")

    #hard mode will not give hints
    else:
        print("No hints provided., keep guessing!")

    if guess == secret_key:
        print("Correct!")
        break


# Decrypt the ciphertext using the guessed key
plaintext = decrypt(ciphertext, guess)
print(f"Decrypted plaintext: {plaintext}")

# display the encryption information
print("\nEncryption Information:")
print(f"Ciphertext:                  {ciphertext}")
# confirm the key used for encryption works for decryption
plaintext_check = decrypt(ciphertext, secret_key)
print(f"Decrypted with original key: {plaintext_check}")
print(f"Key used for encryption: {secret_key}")
print(f"Original Alphabet: {''.join(return_alphabet())}")
print(f"Alphabet mapping:  {''.join(generate_cipher_alphabet(secret_key).values())}")
# === End of Main Function ====
# Note: The random key generation and shuffling of the alphabet means that the same plaintext will produce different ciphertexts each time.