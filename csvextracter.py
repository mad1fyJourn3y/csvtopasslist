import csv

# Input and output file names
csv_file = 'chrome_passwords.csv'  # Change to your actual file name
output_file = 'unique_password_list.txt'

# Read CSV and extract unique passwords
unique_passwords = set()

try:
    with open(csv_file, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            password = row.get('password', '').strip()  # Get password and remove whitespace
            if password:
                unique_passwords.add(password)  # Add password to the set (duplicates removed)

    # Save unique passwords to output file
    with open(output_file, 'w') as outfile:
        for password in sorted(unique_passwords):  # Sort passwords alphabetically before saving
            outfile.write(password + '\n')

    print(f"Unique password list saved to {output_file}. Found {len(unique_passwords)} unique passwords.")

except FileNotFoundError:
    print(f"Error: The file '{csv_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
