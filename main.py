def count_words(text):
    """Count the number of words in the given text."""
    words = text.split()
    return len(words)

def count_character_frequencies(text):
    """Count the frequency of each character in the given text, converting to lowercase."""
    text = text.lower()  # Normalize text to lowercase
    character_counts = {}
    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def generate_report():
    # Read the text file
    with open('books/frankenstein.txt', 'r', encoding='utf-8') as file:
        contents = file.read()

    # Count the words in the book
    total_words = count_words(contents)
    print(f"The book contains {total_words} words.")

    # Count character frequencies in the book
    character_counts = count_character_frequencies(contents)

    # Print the character frequencies in a readable format
    for char, count in sorted(character_counts.items()):
        if char.isalpha():  # Optional: Filter to display only alphabetic characters
            print(f"The '{char}' character was found {count} times")

# Execute the report generation
generate_report()
