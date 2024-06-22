library = {}

def add_book():#要家書的邏輯程式
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """
    
    book_info = input("Enter the book title, genre, and price (separated by '|'): ")
   
    title, genre, price = book_info.split("|")#先變成列表
    if title in library:
        print(f"{title} not found in the library.")
        print()
    else:
        library[title] = {"genre": genre, "price": price+".00"}
        print("Added",f"{title} to the library.")
      
        
  
    if len(library) == 0:
        print("No books in the library.")
    else:
    	print()
    	for title in sorted(library.keys()):#把key提出來
            print(f"{title} ({library[title]['genre']}, ${library[title]['price']})")

def remove_book():#移除書要用的邏輯程式
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    
    title = input("Enter the title of the book you want to remove: ")
    print()
    if title in library:#條件判斷
        del library[title]
        print("Removed"f"{title} from the library.")
    else:
        print(f"Error: {title} not found in the library.")
    print()

def get_book_info():#取的資訊要用的邏輯程式
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    title = input("Enter the title of the book: ")
    print()
    if title in library:
        print(f"Title: {title}\nGenre: {library[title]['genre']}\nPrice: {library[title]['price']}")
    else:
        print(f"Error: {title} not found  in the library.")


def list_books():#列出所有書本要用的邏輯程式
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
    	print()
    	print("\nThe library is empty.\n")
    	return False
    print()
    for title, book_info in sorted(library.items()):
        genre, price = book_info["genre"], book_info["price"]
        print(f"{title} ({genre}, ${price}.)")
    print()
    return True

def list_books_by_genre():#依類別印出的邏輯程式
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    
    genre = input("Enter the genre to search for: ")
    print()
    books_found = False
    for title, book_info in sorted(library.items()):
        if book_info["genre"] == genre:
            if not books_found:
                print(f"All books in the {genre} genre:")
                books_found = True
            print(f"{title} ({book_info['genre']}, ${book_info['price']})")
    if not books_found:
        print(f"No books found in the {genre} genre.")

while True:#print出menu
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")