CREATE TABLE Inventory (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL,
    publication_date DATE,
    isbn TEXT UNIQUE NOT NULL
);
