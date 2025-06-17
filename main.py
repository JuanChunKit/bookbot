from stats import count_words
from stats import count_characters
from stats import sort_on_num
from stats import sort_dic
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)


    char_count = count_characters(text)
#    for key in char_count:
#        print(f"'{key}': {char_count[key]}")

    sorted_list = sort_dic(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")
    # print(sorted_list)
    print("============= END ===============")
main()