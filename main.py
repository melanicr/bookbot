from stats import num_words, counting, sorting
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents




def main():
    path = sys.argv[1]
    content = get_book_text(path)
    
    
    num = num_words(content)
    letters = counting(content)
    the_list = sorting(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for item in the_list:
        print(f"{item["word"]}: {item["count"]}")
    print("============= END ===============")



main()
