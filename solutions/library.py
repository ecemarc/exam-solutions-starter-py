
books = [
    {"id": 1, "title": "Book A", "color": "green", "year": 1901},
    {"id": 2, "title": "Book B", "color": "red", "year": 1957},
    {"id": 3, "title": "Book C", "color": "green", "year": 1988},
    {"id": 4, "title": "Book D", "color": "blue", "year": 1923},
    {"id": 5, "title": "Book E", "color": "yellow", "year": 2017},
    {"id": 6, "title": "Book F", "color": "orange", "year": 2028}
]

if __name__ == "__main__":

    print("------------------")
    print("PROCESSING LIBRARY DATA...")
    print("------------------")
    # print(books)
    # breakpoint()

    #
    # QUESTION A
    #
    # Assuming the identifier, or "id" attribute, of each book is and will always be unique,
    # ... and assuming the order of books may vary,
    # ... "print" the title of the book whose identifier is equal to 4 (i.e. "Book D"):

print([p["title"] for p in books if p["id"] == 4][0])

#
# QUESTION B
#
# Assuming the "year" attribute represents the year a given book was published,
# ... "print" the number of books published before the year 1990 (i.e. 4):

old_books = []

for b in books:
    b_year = b["year"]
    if b_year < 1984:
        old_books.append(b)

print(len(old_books))
