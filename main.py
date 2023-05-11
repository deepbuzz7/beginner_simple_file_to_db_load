import pandas
import psycopg2
from ddl import *

#reading the csv file using pandas
data=pandas.read_csv('goodreads_data.csv')

#connecting to postgres
#conn = psycopg2.connect(host="pgdb", database="best_books", user="root", password="root")
conn = psycopg2.connect(host="pgdb", database="postgres", user="root", password="root")
cur=conn.cursor()
conn.set_session(autocommit=True)
cur.execute(drop_database)
cur.execute(create_database)
cur.close()
conn.close()
conn = psycopg2.connect(host="pgdb", database="best_books", user="root", password="root")
cur=conn.cursor()
cur.execute(create_books_table)
cur.execute(create_authors_table)
cur.execute(create_genres_table)
cur.execute(create_book_author_table)
cur.execute(create_book_genre_table)

for index,row in data.iterrows():
    book_name=row['Book'].replace("'","\''").replace('"','').strip()
    author_name=row['Author'].replace("'","\''")
    book_description=str(row['Description'])[0:1000].replace("'","").replace('"','').strip()
    book_genres=row['Genres']
    avg_rating=row['Avg_Rating']
    num_ratings=int(row['Num_Ratings'].replace(",",""))
    url=row['URL'].strip()

    #insert in book table
    book_table_insert_query=f"INSERT INTO BOOKS(BOOK_NAME,BOOK_DESCRIPTION,AVG_RATING,NUMBER_OF_RATINGS,URL) VALUES('{book_name}','{book_description}',{avg_rating},{num_ratings},'{url}')"
    cur.execute(book_table_insert_query)

    #insert into authors table
    authors=author_name.split(",")
    for a in authors:
        #search if author is already there
        cur.execute(f"select * from AUTHORS WHERE AUTHOR_NAME='{a.strip()}'")
        if len(cur.fetchall())==0:
            #its not there
            author_insert_query=f"INSERT INTO AUTHORS(AUTHOR_NAME) VALUES('{a.strip()}')"
            cur.execute(author_insert_query)
        else:
            pass
    
    #insert into genres table
    # clean the data
    genres=book_genres.replace("[","").replace("]","").replace("'","").split(",")
    for g in genres:
        #search if genre is already there
        cur.execute(f"select * from genres where genre='{g.strip()}'")
        if len(cur.fetchall())==0:
            #not there
            genre_insert_query=f"INSERT INTO GENRES(GENRE) VALUES('{g.strip()}')"
            cur.execute(genre_insert_query)
        else:
            pass
    
    #inserting into map book author
    cur.execute(f"select book_id from books where book_name='{book_name}'")
    book_id=cur.fetchall()[0][0]
    for a in authors:
        cur.execute(f"select author_id from authors where author_name='{a.strip()}'")
        author_id=cur.fetchall()[0][0]
        map_book_author_insert_query=f"INSERT INTO MAP_BOOK_AUTHOR(BOOK_ID,AUTHOR_ID)VALUES({book_id},{author_id})"
        cur.execute(map_book_author_insert_query)
    
    #inserting into map book genre
    for g in genres:
        cur.execute(f"select genre_id from genres where genre='{g.strip()}'")
        genre_id=cur.fetchall()[0][0]
        map_book_genre_insert_query=f"INSERT INTO MAP_BOOK_GENRE(BOOK_ID,GENRE_ID) VALUES({book_id},{genre_id})"
        cur.execute(map_book_genre_insert_query)

conn.commit()
cur.close()
conn.close()
print("completed inserting the data")






