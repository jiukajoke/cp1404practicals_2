def extract_name(email):
    # Split the email by "@" to get the name part
    name = email.split("@")[0]
    # Capitalize the first letter of each word in the name
    return " ".join([part.capitalize() for part in name.split(".")])

def main():
    email_dict = {}
    while True:
        email = input("Email: ")
        if not email:
            break  # Exit loop if the user enters a blank email
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm in ('', 'y'):
            # Use the extracted name
            email_dict[email] = name
        else:
            # Ask the user for the correct name
            correct_name = input("Name: ")
            email_dict[email] = correct_name

    # Print the stored emails and names
    for email, name in email_dict.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
