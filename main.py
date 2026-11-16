from books import books
from functions import display_books,borrow_book,return_book

# //added to test to test it 

while True:
    display_books()
    prompt = input("Press:     \n b  to borrow a book \n r  to return a book \n q to quit the program")
    if prompt.lower() == 'b':
        user_input = int(input('Enter the id of the book you want to borrow:  '))
        borrow_book(user_input)
        pass
    elif prompt.lower() == 'r':
        user_input = int(input('Enter the id of the book you want to return:  '))
        return_book(user_input)
        pass
    elif prompt.lower() == 'q':
        break
    else:
        print (f'This is not a correct input try again later \n\n')









