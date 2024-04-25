def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count_dict = get_num_characters(text)
    char_count_list = get_sorted_list(char_count_dict)
    report(book_path, num_words, char_count_list)


def report(book_path, num_words, char_count_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("Character Counts:")
    for char, count in char_count_list:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    char_count_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            char_count_dict[char] = char_count_dict.get(char, 0) + 1
    return char_count_dict


def get_count(key):
    return key[1]


def get_sorted_list(char_count_dict):
    char_count_list = [(char, count) for char, count in char_count_dict.items()]
    char_count_list.sort(key=get_count, reverse=True)
    return char_count_list

main()