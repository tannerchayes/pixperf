

import csv

if __name__ == '__main__':
    print("hello")

    with open('csv_stuff', 'r') as csv_ness:
        new_ness = csv.DictReader(csv_ness)
        for row in new_ness:
            print(row['title'], row['content'], row['date'])

