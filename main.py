def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    words_count = count_words(text)
    # print(words_count)
    letter_counts = count_letter(text)
    # print(letter_counts)
    print_repport(words_count,letter_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letter(text):
    text = text.lower()
    letter_counts = {}
    for letter in text:
        if letter.isalpha():
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts

def print_repport(words_count,letter_counts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    # letter_counts = letter_counts.items()
    result = list()
    for letter,count in list(letter_counts.items()):
        result.append((letter,count))
    # print(result)
    sorted_result = sorted(result, key=lambda x: x[1],reverse=True)
    for item in sorted_result:
        print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End report ---")
main()
