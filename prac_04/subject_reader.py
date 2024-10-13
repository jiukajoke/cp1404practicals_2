"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        subject_data.append(parts)  # Add the processed data to the list
    input_file.close()
    return subject_data


def display_subject_details(subject_data):
    """Display subject details in the desired format."""
    for subject_info in subject_data:
        subject = subject_info[0]
        lecturer = subject_info[1]
        num_students = subject_info[2]
        print(f"{subject} is taught by {lecturer} and has {num_students} students")


if __name__ == "__main__":
    main()
