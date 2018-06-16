import json

with open('books.json') as json_file:  
    books = json.load(json_file)
    for book in books:
        print('Author: ' + book['author'])
        print('Title: ' + book['title'])
        print('Year: ' + str(book['year']))
        print('----------------------------------') 
