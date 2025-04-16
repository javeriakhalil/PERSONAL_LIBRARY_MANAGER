import streamlit as st
 from collections import defaultdict
 
 # Initialize session state for library data
 if 'library' not in st.session_state:
     st.session_state.library = []
 
 # Function to add a book
 def add_book(title, author, genre):
     st.session_state.library.append({
         'title': title.title(),
         'author': author.title(),
         'genre': genre.title()
     })
     st.success(f"Book '{title}' added successfully!")
 
 # Function to remove a book by title
 def remove_book(title):
     title = title.title()
     for book in st.session_state.library:
         if book['title'] == title:
             st.session_state.library.remove(book)
             st.success(f"Book '{title}' removed successfully!")
             return
     st.warning("Book not found.")
 
 # Function to search books by title or author
 def search_books(query):
     query = query.lower()
     results = [
         book for book in st.session_state.library
         if query in book['title'].lower() or query in book['author'].lower()
     ]
     return results
 
 # Function to display all books
 def display_books():
     if st.session_state.library:
         st.write("### 📚 Library Books:")
         for book in st.session_state.library:
             st.write(f"- **{book['title']}** by *{book['author']}* [{book['genre']}]")
     else:
         st.info("No books in the library yet.")
 
 # Function to show statistics
 def show_statistics():
     if not st.session_state.library:
         st.info("No books to analyze.")
         return
 
     total_books = len(st.session_state.library)
     genre_count = defaultdict(int)
     author_count = defaultdict(int)
 
     for book in st.session_state.library:
         genre_count[book['genre']] += 1
         author_count[book['author']] += 1
 
     st.write(f"### 📊 Statistics:")
     st.write(f"- Total Books: **{total_books}**")
     st.write("- Books by Genre:")
     for genre, count in genre_count.items():
         st.write(f"  - {genre}: {count}")
     st.write("- Books by Author:")
     for author, count in author_count.items():
         st.write(f"  - {author}: {count}")
 
 # Streamlit UI
 st.set_page_config(page_title="📚 Personal Library Manager", page_icon="📖")
 st.title("📚 Personal Library Management System")
 
 menu = st.sidebar.selectbox("Choose an action", [
     "Add Book", "Remove Book", "Search Book", "Display Books", "Statistics", "Exit"
 ])
 
 if menu == "Add Book":
     st.subheader("➕ Add a New Book")
     title = st.text_input("Book Title")
     author = st.text_input("Author")
     genre = st.text_input("Genre")
     if st.button("Add Book"):
         if title and author and genre:
             add_book(title, author, genre)
         else:
             st.warning("Please fill in all fields.")
 
 elif menu == "Remove Book":
     st.subheader("➖ Remove a Book")
     title = st.text_input("Enter the title of the book to remove")
     if st.button("Remove Book"):
         if title:
             remove_book(title)
         else:
             st.warning("Please enter a book title.")
 
 elif menu == "Search Book":
     st.subheader("🔍 Search Books")
     query = st.text_input("Search by Title or Author")
     if query:
         results = search_books(query)
         if results:
             st.write("### Results:")
             for book in results:
                 st.write(f"- **{book['title']}** by *{book['author']}* [{book['genre']}]")
         else:
             st.warning("No books found.")
 
 elif menu == "Display Books":
     st.subheader("📚 All Books in Your Library")
     display_books()
 
 elif menu == "Statistics":
     st.subheader("📊 Library Statistics")
     show_statistics()
 
 elif menu == "Exit":
     st.subheader("👋 Thanks for using the Library Manager!")
     st.stop()