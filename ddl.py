drop_database='''DROP DATABASE IF EXISTS BEST_BOOKS'''
create_database='''CREATE DATABASE BEST_BOOKS'''
create_books_table='''CREATE TABLE BOOKS (
    BOOK_ID SERIAL PRIMARY KEY,
    BOOK_NAME VARCHAR(255) NOT NULL,
    BOOK_DESCRIPTION VARCHAR(1000) NOT NULL,
    AVG_RATING REAL,
    NUMBER_OF_RATINGS INTEGER,
    URL VARCHAR(1000)
)'''

create_authors_table='''CREATE TABLE AUTHORS(
    AUTHOR_ID SERIAL PRIMARY KEY,
    AUTHOR_NAME VARCHAR(255) NOT NULL
)'''

create_genres_table='''CREATE TABLE GENRES(
    GENRE_ID SERIAL PRIMARY KEY,
    GENRE VARCHAR(255)
)'''

create_book_author_table='''CREATE TABLE MAP_BOOK_AUTHOR(
    MAP_BOOK_AUTHOR_ID SERIAL PRIMARY KEY,
    BOOK_ID INTEGER NOT NULL,
    AUTHOR_ID INTEGER NOT NULL,
    CONSTRAINT fk_MAP_BOOK_AUTHOR_book_id FOREIGN KEY(BOOK_ID) REFERENCES BOOKS(BOOK_ID),
    CONSTRAINT fk_MAP_BOOK_AUTHOR_author_id FOREIGN KEY(AUTHOR_ID) REFERENCES AUTHORS(AUTHOR_ID)
)'''

create_book_genre_table='''CREATE TABLE MAP_BOOK_GENRE(
    MAP_BOOK_GENRE_ID SERIAL PRIMARY KEY,
    BOOK_ID INTEGER NOT NULL,
    GENRE_ID INTEGER NOT NULL,
    CONSTRAINT fk_MAP_BOOK_GENRE_book_id FOREIGN KEY(BOOK_ID) REFERENCES BOOKS(BOOK_ID),
    CONSTRAINT fk_MAP_BOOK_GENRE_genre_id FOREIGN KEY(GENRE_ID) REFERENCES GENRES(GENRE_ID)
)'''
