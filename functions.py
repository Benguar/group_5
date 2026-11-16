from books import books

def borrow_book(book_id: str):
    for book in books:
        if book['book_id'] == book_id:
            if book.get('book_availability') == True:
                print(f"You can have book {book['book_name']} please keep it safe")
                book['book_availability'] = False

            else:
                print(f'{book["book_name"]} has been taken please select another book')
    print(f'No such book with id {book_id} select another book')

def display_books():
    for index,book in enumerate(books):
        if index == 0:
            print('No     book_name     book_availability \n\n')
        print(f'{index+1}     {book['book_name']}     {book["book_availability"]} \n')
    print("-------------------------------------------------")

def return_book(book_id: int):
    for book in books:
        if book["book_id"] == book_id:
            if book['book_availability'] == False:
                book['book_availability'] = True
                print(f'{book["book_name"]} has been returned successfully')
            else:
                print(f'{book["book_name"]} was never borrowed enter a valid book_id')
    