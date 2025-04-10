# How to run my Encryption Code

Run the code with the following (from the root folder the code is in):
```
python .\encryption.py

```

From here you will be shown the cipher text and will be prompted to choose either 'easy' or 'hard' mode.

Selecting easy mode will give you hints about how far off your key guess is - hard mode will not give these

You will then be prompted to enter an integer from 1-100 until you guess the cipher key correctly, at which point it will print out the cipher text, and information about the encryption process:

```
Enter your guess for the key (1-100): 51
Correct!
Decrypted plaintext: AUSTIN STERNBERG

Encryption Information:
Ciphertext:          TVIXAP IXCMPDCMS
Decrypted plaintext: AUSTIN STERNBERG
Key used for encryption: 51
Original Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet mapping:  TDUYCNSBALEGWPJKOMIXVZFRQH
```

**Please Note:** The alphabet mappings will be different each time, so the above will not necessarily work


# How to run the Bruteforce script

This serves as an example of how a brute force attack could be done on the encryption code.

To run:
```
python bruteforce.py
```

It will prompt for the cipher text of the encryption program - copy and paste the given ciphertext there

It will then prompt for known plaintext words - give one if you have one

It will then spit out either all of the possible key decryptions or the correct key (if you gave partial plaintext)

```
Key 49: KLQJMH QJZDHWZDR
Key 50: QPYDEZ YDSJZCSJL
Key 51: AUSTIN STERNBERG
Key 52: POZXJV ZXNDVGNDE
Key 53: ZOCSRV CSMJVFMJH
Key 54: PUIOKV IODTVNDTJ
```