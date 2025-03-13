from stats import get_word_count

def get_book_text(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents


def main():
    test_var = "./books/frankenstein.txt"
    file_contents = get_book_text(test_var)
    num_words = get_word_count(file_contents)
    print(f"{num_words} words found in the document")

main()