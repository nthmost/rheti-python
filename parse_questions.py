from csv import DictReader
dr = DictReader(open('questions.csv'))

for item in dr:
    print(item)


