def main():
    path = "books/frankenstein.txt"
    book = get_book(path)
    # print(book)
    # print(word_count(book))
    # print(letter_count(book))
    book_report(path, book)

def get_book(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    words = book.split()
    return f"This book contains {len(words)} words"

def letter_count(text):
    letter_count = {}
    for letter in text.lower():
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    
    return letter_count

def book_report(title, book):
    print(f"--- Begin report of {title} ---")
    print(word_count(book))
    letters = letter_count(book)
    sorted = sorted_dict(letters)
    
    for key in sorted:
        if key.isalpha() == True:
            print(f"The '{key}' character was found {letters[key]} times.")
    
    print("--- End report ---")

def sorted_dict(unsorted_dict):
    sorted_letters = list(unsorted_dict.keys())
    sorted_letters.sort()
    sorted_dict = {i: unsorted_dict[i] for i in sorted_letters}
    return sorted_dict

main()
