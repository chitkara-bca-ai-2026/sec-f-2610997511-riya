
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    (
        "Artificial Intelligence: A Modern Approach",
        "Stuart Russell",
        "2021",
        "AI",
    ),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering"),
]
library_categories = set()
for book in books:
    library_categories.add(book[3])
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

while True:
    print("==================================================")
    print("        LIBRARY BOOK & CATEGORY MANAGER")
    print("==================================================")
    print("Select an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
    choice = input("\nEnter your choice (1-6): ")
    if choice == "1":
        print("--- Current Library Catalog (Fixed Records) ---")
        index = 1
        for title, author, year, category in books:
            print(
                f'{index}. "{title}" by {author} ({year}) | Genre: {category}'
            )
            index += 1
        print(f"Total Books: {len(books)}")
    elif choice == "2":
        print("--- Add New Book Record ---")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")
        new_book = (title, author, year, category)
        books.append(new_book)
        library_categories.add(category)
        print(
            f'[SUCCESS] "{title}" added as an immutable catalog record.'
        )
        print(f'[INFO] Category set updated with: "{category}"')
    elif choice == "3":
        print("--- Unique Categories Available in Library (Set) ---")
        for cat in library_categories:
            print(f"- {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")
    elif choice == "4":
        print("--- Add Category to Student Wishlist ---")
        new_wishlist_cat = input("Enter genre to request: ")
        student_wishlist.add(new_wishlist_cat)
        print(
            f'[SUCCESS] "{new_wishlist_cat}" added to student wishlist.'
        )
    elif choice == "5":
        print("--- Category Gap Analysis ---")
        fulfilled_requests = student_wishlist.intersection(library_categories)
        missing_in_library = student_wishlist.difference(library_categories)
        all_unique_genres = student_wishlist.union(library_categories)
        print("1. Fulfilled Requests (In Library & Wishlist):")
        for cat in fulfilled_requests:
            print(f"   - {cat}")
        print("2. Missing Genres (Wishlisted but NOT in Library):")
        for cat in missing_in_library:
            print(f"   - {cat}")
        print("3. Combined Unique Catalog & Wishlist Genres:")
        for cat in all_unique_genres:
            print(f"   - {cat}")
    elif choice == "6":
        print("Exiting the Library Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
