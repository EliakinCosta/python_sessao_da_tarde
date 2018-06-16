import csv

with open('people.csv') as people_file:
    people_reader = csv.reader(people_file, delimiter="|")    
    for person in people_reader:
        print(person)
