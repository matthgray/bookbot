def count_words(text):
    """Return the number of words in the given text string."""
    words = text.split()  # Split the text into words based on whitespace
    return len(words)  
def read_and_count_words_from_book():
    # Open the file located in the "books" folder and read its contents
    with open('books/frankenstein.txt', 'r') as file:
        contents = file.read()
        # Print the contents to the console (optional, can be commented out)
        # print(contents)

        # Count the words in the book and print the count
        word_count = count_words(contents)
        print(f"The book contains {word_count} words.")

# Run the function to read the book and count its words
read_and_count_words_from_book()