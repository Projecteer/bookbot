import sys
from stats import wordCount, charCount, sortDict
#print("greetings boots")
#def wordCount(text):
#    totalWords = len(text.split())
#    print(f"Found {totalWords} total words")

def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    #entireText = get_book_text("books/frankenstein.txt")
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    entireText = get_book_text(sys.argv[1])
    #print(entireText)
    #print(sys.argv)
    wordCount(entireText)
    #wordCount(sys.argv)
    charDict = charCount(entireText)
    sortDict(charDict)

main()