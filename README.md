# Password Strength Analyzer



## Project Overview



The **Password Strength Analyzer** is a simple Python application that evaluates the strength of a user-entered password. It checks whether the password meets common security requirements such as minimum length, uppercase and lowercase letters, numbers, and special characters. The application also identifies commonly used weak passwords and suggests ways to create stronger passwords.



This project helps users understand the importance of creating secure passwords and introduces basic cybersecurity concepts.



---



## Features



* Checks password length (minimum 8 characters)

* Verifies the presence of:



  * Uppercase letters

  * Lowercase letters

  * Numbers

  * Special characters

* Detects common weak passwords

* Rates password strength as:



  * Weak

  * Medium

  * Strong

* Suggests improvements for weak passwords

* **Optional:** Stores hashed passwords to prevent password reuse



---



## Technologies Used



* Python 3

* `re` (Regular Expressions)

* `hashlib` (SHA-256 Hashing)

* File Handling (Optional)



---



## Project Structure



```

Password-Strength-Analyzer/

│── Password-Strength.py 



└── README.md

```



---



## How It Works



1. The user enters a password.

2. The program checks:



   * Password length

   * Uppercase letters

   * Lowercase letters

   * Numbers

   * Special characters

3. It compares the password with a list of common weak passwords.

4. A strength score is calculated.

5. The program displays whether the password is **Weak**, **Medium**, or **Strong**.

6. If the password is weak, suggestions are provided to improve it.

7. (Optional) The password is hashed using SHA-256 and compared with previously stored hashes to prevent reuse.



---



## Installation



1. Clone the repository:



```bash

git clone https://github.com/your-username/password-strength-analyzer.git

```



2. Navigate to the project folder:



```bash

cd password-strength-analyzer

```



3. Run the program:



```bash

python password_strength.py

```



---



## Example



### Input



```

Enter your password: hello123

```



### Output



```

Add at least one uppercase letter.

Add at least one special character.



Password Strength: Medium



Suggested Strong Password:

Example@123

```



---



## Learning Outcomes



By completing this project, you will learn:



* Password security principles

* Regular expressions in Python

* Conditional statements

* File handling

* Basic cryptography using SHA-256 hashing

* Writing secure password validation logic



---



## Future Improvements



* Graphical User Interface (GUI)

* Password generator

* Entropy-based strength calculation

* Password breach detection using public APIs

* Database integration for password history

* Real-time password strength meter



---



## Author



**Joshua S**



Cybersecurity Mini Project
