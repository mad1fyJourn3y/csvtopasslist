# Unique Password List Generator

This Python script extracts unique passwords from a CSV file containing passwords and generates a list of unique passwords. The output is saved in a sorted text file.

## Features
- Extracts passwords from a CSV file.
- Removes duplicate passwords automatically using a set.
- Saves unique passwords to a sorted text file.
- Handles errors like missing files or incorrect data formats.

## Requirements
- Python 3.x

### Required Python Libraries:
- `csv` (standard library, no installation needed)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/unique-password-list-generator.git
   cd unique-password-list-generator
   ```
2. Install dependencies (if any):
  ```bash
   pip install -r requirements.txt
   ```
#Usage
Place your CSV file (e.g., chrome_passwords.csv) in the project directory. The CSV file should have a column labeled password containing the passwords.

Run the script:

```bash
python generate_unique_password_list.py
```
The script will generate a file named unique_password_list.txt containing the unique passwords sorted alphabetically.

#Example CSV Input
Your CSV file should look like this (with a column password):
```csv
username,password
user1	123456
user2	mysecretpassword
user3	123456
user4	qwerty
```
#Example Output
After running the script, the generated unique_password_list.txt will contain:
```csv
Copy
Edit
123456
mysecretpassword
qwerty
```
#Error Handling
FileNotFoundError: If the input file is not found, an error message will be displayed.
General Exceptions: Other issues with the script (e.g., incorrect CSV format) will trigger an error with a relevant message.
#License
This project is licensed under the MIT License - see the LICENSE file for details.

#Contact
For questions or contributions, feel free to contact me via GitHub or email.
