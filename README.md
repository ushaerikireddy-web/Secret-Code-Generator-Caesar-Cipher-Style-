# Secret Code Generator (Python)

## 📄 Description
A command-line based Secret Code Generator built using Python.
It allows users to encode and decode messages using a Caesar cipher technique.
The program handles both uppercase and lowercase letters and skips non-alphabet characters.
 
## ⚙️ Features
- Encode messages by shifting letters forward
- Decode messages by shifting letters backward
- Handles both uppercase and lowercase letters
- Skips spaces, punctuation, and symbols
- Menu-driven interface with input validation
- Uses modular functions for encoding and decoding

## 📁 File
- secret_code_generator.py → Main Python program
- Output screenshots included

## 🖥️ Output :

### total cases = 4
1.	Encode → num == 1
2.	Decode → num == 2
3.	Exit → num == 3
4.	Invalid input → else (when the entered number is not 1, 2, or 3)
#### If we choose :  1
<img width="635" height="223" alt="image" src="https://github.com/user-attachments/assets/624dcacc-e2d7-429a-8772-dd66e78e1595" />


•	The program displays a menu with three options: Encode, Decode, and Exit.
•	When the user selects 1 (Encode), the program asks for a text input (Usha) and a shift value (2).
•	Each alphabet character is shifted forward by the given number using ASCII values while keeping the same case (uppercase/lowercase).
•	For the input Usha and shift 2, the letters change as: U→W, s→u, h→j, a→c.
•	The encoded result Wujc is displayed on the screen.
•	Non-alphabet characters (spaces, symbols) are not changed during encoding.
✅ This output confirms the program works as a Caesar Cipher encoding.

#### If we choose :  2
<img width="578" height="196" alt="image" src="https://github.com/user-attachments/assets/f956d90d-f2b3-4465-bb42-da2211a77d69" />

•	The program asks the user to choose an option: 1.Encode, 2.decode, or 3.Exit. Here, the user chose 2 (decode).
•	The user inputs the encoded message: Usha the "Coder"...!
•	The program asks for the shift value, which is 2 in this case. This is the number of positions each letter was shifted in the Caesar cipher.
•	The decode function shifts each alphabetic character backward by 2 positions in the alphabet.
•	Non-alphabetic characters (like spaces, quotes, dots, exclamation) remain unchanged.
•	The program prints the decoded message: Sqfy rfc "Ambcp"...! which is the original message before encoding.

#### If we choose :  3
<img width="508" height="200" alt="image" src="https://github.com/user-attachments/assets/fbafdb0a-57b2-4647-8598-6d508a0b56da" />

•	The user chose option 3 (Exit) from the menu, which tells the program to terminate.
•	The program responds with “Existing...” (likely a typo for “Exiting...”) and stops running.


#### If we choose :  4
<img width="482" height="177" alt="image" src="https://github.com/user-attachments/assets/ac91f157-d574-48e7-bfbd-237c77cb1ebb" />

•	The user entered 10, which is not a valid option in the menu (only 1, 2, or 3 are valid).
•	The program responds with “Invalid...”, indicating the input is not recognized.
