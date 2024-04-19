def count_character_frequencies(text):
    """Returns a dictionary with the count of each lowercase character in the text."""
    text = text.lower()  # Convert the text to lowercase to unify character cases
    character_counts = {}
    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def read_and_analyze_book():
    # Open the file located in the "books" folder and read its contents
    with open('books/frankenstein.txt', 'r', encoding='utf-8') as file:
        contents = file.read()

        # Count the characters in the book
        character_counts = count_character_frequencies(contents)

        # Print the character counts
        for character, count in sorted(character_counts.items()):
            print(f"'{character}': {count}")

# Call the function to perform the analysis
read_and_analyze_book()
