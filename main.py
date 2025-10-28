import sys
from stats import get_book_word_cnt, get_char_occur_cnt, get_sorted_dict

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_book_word_cnt(text)
    char_occur = get_char_occur_cnt(text)
    sorted_char_occur = get_sorted_dict(char_occur)
    
    print_report(path, word_count, sorted_char_occur)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(path, num_words, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for chars in sorted:
        print(f"{chars["char"]}: {chars["num"]}")
    print("============= END ===============")
main()