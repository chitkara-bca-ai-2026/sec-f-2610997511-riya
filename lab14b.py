#Week 7 - Library Book Collection (14b.py)

# 1. Setup Initial Data
books = [
    ("Python Basics", "John Doe", "2019", "Programming"),
    ("AI Fundamentals", "Jane Smith", "2021", "AI"),
    ("Data Analysis", "Alice Brown", "2020", "Data Science"),
    ("Software Engineering Principles", "Bob White", "2018", "Software Engineering")
]
Library_categories = set()
for book in books:
    Library_categories.add(book[3])

student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

while True:
    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ").strip()
    
    if choice == "1":
        print("\n--- Cataloged Books ---")
        for book in books:
            title, author, year, category = book
            print(f"Title: {title}, Author: {author}, Year: {year}, Category: {category}")
        print(f"Total Books: {len(books)}")
    elif choice == "2":
        print("\n--- Add New Book Record ---")
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        year = input("Enter year: ").strip()
        category = input("Enter category: ").strip()
        if title and author and year and category:
            new_book = (title, author, year, category)
            books.append(new_book)
            Library_categories.add(category)
            print(f'[SUCCESS] "{title}" added to library catalog.')
        else:
            print("Error: All fields are required to add a book.")
    elif choice == "3":
        print("--- Unique Categories Available in Library (Set) ---")
        sorted_categories = sorted(Library_categories)
        for cat in sorted_categories:
            print(f"- {cat}")
        print(f"Total Unique Genres: {len(sorted_categories)}")
    elif choice == "4":
        print("--- Add to Student Wishlist ---")
        req_category = input("Enter requested category: ").strip()
        if req_category:
            student_wishlist.add(req_category)
            print(f'[SUCCESS] "{req_category}" added to student wishlist.')
        else:
            print("Error: Category name cannot be empty.")
    elif choice == "5":
        print("=========== CATEGORY GAP ANALYSIS ===========")
        print(f"Library Holdings (Set): {sorted(list(Library_categories))}")
        print(f"Student Wishlist (Set): {sorted(list(student_wishlist))}")
        print("-" * 55)        
        already_in_stock = sorted(list(student_wishlist & Library_categories))
        print(f"1. Already in Stock (Intersection &):\n   {already_in_stock}")
        purchase_order = sorted(list(student_wishlist - Library_categories))
        print(f"2. Purchase Order Needed (Difference -):\n   {purchase_order}")
        combined_coverage = sorted(list(student_wishlist | Library_categories))
        print(f"3. Full Combined Genre Coverage (Union |):\n   {combined_coverage}")
        print("=" * 55)
    elif choice == "6":
        print("Thank you for using the Library Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")