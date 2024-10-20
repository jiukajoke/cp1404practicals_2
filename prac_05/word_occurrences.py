def count_word_occurrences(input_str):
    # Split the input string into words
    words = input_str.split()

    # Initialize a dictionary to store word counts
    word_counts = {}

    # Count the occurrences of each word
    for word in words:
        # Remove any punctuation from the word (optional)
        word = word.strip('.,!?')

        # Convert the word to lowercase to ensure case-insensitive counting
        word = word.lower()

        # Update the word count in the dictionary
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Find the length of the longest word for formatting
    max_word_length = max(len(word) for word in word_counts)

    # Sort the word counts alphabetically
    sorted_word_counts = sorted(word_counts.items())

    # Print the word counts with aligned output
    for word, count in sorted_word_counts:
        print(f"{word:>{max_word_length}} : {count}")

# Ask the user for input
user_input = input("Enter a string: ")

# Call the function with the user's input
count_word_occurrences(user_input)
