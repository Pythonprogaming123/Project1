import sqlite3

# connect to the database or create a new one if it doesn't exist
conn = sqlite3.connect('project.db')
#conn.execute("Drop table books");

"""
# create a table to hold information about books
conn.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    review TEXT
                )''')

# add some sample data
conn.execute("INSERT INTO books (id,title, author, review) VALUES (1,'The Great Gatsby', 'F. Scott Fitzgerald', 'A classic tale of love and loss')")
conn.execute("INSERT INTO books (id,title, author, review) VALUES (2,'To Kill a Mockingbird', 'Harper Lee', 'A powerful examination of racial injustice in the South')")
conn.execute("INSERT INTO books (id,title, author, review) VALUES (3,'1984', 'George Orwell', 'A cautionary tale of a totalitarian society')")
conn.execute("INSERT INTO books (id,title, author, review) VALUES (4,'A Passage to India', 'E.m. Forster', 'Set against the backdrop of the British Raj and the Indian independence movement in the 1920s')")
conn.execute("INSERT INTO books (id,title, author, review) VALUES (5,'Anna Karenina', 'Leo Tolstoy', 'A doomed love affair between the sensuous and rebellious Anna and dashing officer, Count Vronsky')")
conn.execute("INSERT INTO books (id,title, author, review) VALUES (6,'Pride and Prejudice', 'Jane Austen', 'Shows the importance of environment and upbringing in developing the character and morality of young people')")
conn.execute("INSERT INTO books (id,title, author, review) VALUES (7,'War and Peace', 'Leo Tolstoy', 'Invasion of Napolean in Russia in 1812')")
conn.execute("INSERT INTO books (id,title, author, review) VALUES (8,'The Odyssey', 'Homer', ' Involves the irresistible plot line of a worthy hero trying desperately to get back to his city, his family, and his throne')")
conn.execute("INSERT INTO books (id,title, author, review) VALUES (9,'The White Tiger', 'Aravind Adiga', 'A darkly humorous perspective of Indian struggle in class system in a globalized world as told through a retrospective narration from Balram Halwai, a village boy.')")
conn.execute("INSERT INTO books (id,title, author, review) VALUES (10,'The Good Soldier', 'Ford Madox Ford', 'A searing study of moral dissolution behind the facade of an English gentleman')")

# commit the changes to the database
conn.commit()
"""
# function to print the review of a book
def print_review(id):
    # query the database for the review of the specified book
    cur = conn.cursor()
    cur.execute("SELECT title,review FROM books WHERE id=?", (id,))
    review = cur.fetchone()
    if review:
        print(f"Review of ",review[0],":\n" ,review[1])
    else:
        print(f"Enter the right index.")

# menu 
print("1.The Great Gatsby\n2.To Kill a Mockingbird\n3.George Orwell\n4.A Passage to India\n5.Anna Karenina\n6.Pride and Prejudice\n7.War and Peace\n8.The Odyssey\n9.The White Tiger\n10.The Good Soldier")
n=int(input(print(f"\nEnter the number corresponding to book to get the details:")))
print_review(n)

# close the database connection
conn.close()
