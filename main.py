
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words

from stats import character_numbers
    
from stats import sort_dictionary




if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def main():
    path_to_file = sys.argv[1]

    word_count = count_words(get_book_text(path_to_file))
    
    character_count = character_numbers(get_book_text(path_to_file))
    print(f"{character_count}")

    sorted_dictionary = sort_dictionary(character_count)


    print(f"============ BOOKBOT =============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ---------")
    for i in sorted_dictionary:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


main()