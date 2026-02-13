# GUI_biblio

## Description

This repository contains the GUI for a library tracking and database management. It can be used to load a database (db) file, read it, and modify it. For now, the GUI is only able to load a database, following this format :

```sql
CREATE TABLE Books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    isbn TEXT UNIQUE,
    category_id INTEGER,
    available_copies INTEGER DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    birth_year INTEGER
);

CREATE TABLE Members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    adhesion BOOL,
    phone TEXT,
    membership_date TEXT DEFAULT (DATE('now')),  -- Stores date as YYYY-MM-DD
    first_inscription_year DATE
);

CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    member_id INTEGER,
    borrow_date TEXT DEFAULT (DATE('now')),
    return_date TEXT,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);
```
The goal of this project is to transform the way a library is working, from keeping tracks of the loans of books, memberships, etc in an excel file, to a more convenient version using a GUI and loading all the information in a database file.


The GUI was created using the Qt User Interface Compiler.

## Next steps

The next steps here are to implement the writing into the database from the GUI, and also the availability of a true database. 
