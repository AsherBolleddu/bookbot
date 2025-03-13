from stats import get_word_count, get_num_letter_count, sorted_num_letter_count
import sys 

def get_book_text(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents


def main():
    # test_var = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    file_contents = get_book_text(path_to_book)
    
    print("----------- Word Count ----------")
    num_words = get_word_count(file_contents)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    letter_count_list = sorted_num_letter_count(get_num_letter_count(file_contents))
    for item in letter_count_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

main()