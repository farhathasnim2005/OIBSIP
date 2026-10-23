# OASIS INFOBYTE – Python Programming Internship

## Task 3: Random Password Generator

### Project Description
The Random Password Generator is a Python application that generates random passwords based on the user's selected preferences. Users can choose the password length and include uppercase letters, lowercase letters, numbers, and special symbols.

### Features
- Generates random passwords.
- Allows password lengths from 4 to 128 characters.
- Supports uppercase and lowercase letters.
- Supports numbers and special symbols.
- Allows users to customize password composition.
- Handles invalid input.
- Uses Python's `secrets` module for secure random generation.

### Technologies Used
- Python 3
- `secrets` module
- `string` module

### Installation
No external libraries are required. Install Python 3 and run the program.

### How to Run
1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

```bash
python main.py
```

4. Enter the desired password length.
5. Select the character types using `y` or `n`.
6. The generated password will be displayed.

### Example
```text
Password length (4-128): 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated password: [randomly generated password]
Password length: 12
```

*Note: The generated password will vary each time the program runs.*

### Project Structure

```text
Python-Task3-PasswordGenerator/
├── main.py
└── README.md
```

### Conclusion
This project demonstrates Python functions, conditional statements, user input handling, and secure random password generation.

### Internship Details
- Organization: OASIS INFOBYTE
- Track: Python Programming
- Task: Task 3 – Random Password Generator
