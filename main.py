

def get_book_text(book_path):
    with open(book_path) as file:
        
        return file.read()


def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    print(text)
    
    
main()