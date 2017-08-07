import csv
'''
PART 1:
Read in drinks.csv
Store the header in a list called 'header'
Store the data in a list of lists called 'data'
Hint: you've already seen this code!
'''
header  = []
data = []
i = 0

with open('drinks.csv', newline="") as f:
    readin = csv.reader(f, delimiter=',', quotechar='|')
    for row in readin:
        if 'aso' in row[0]:
            print(header)
            print(row)
        if i == 0:
            header.append(row)
        else:
            data.append(row)
        i += 1
print(header)
print(i)
print(len(data))
'''
PART 2:
Isolate the beer_servings column in a list of integers called 'beers'
Hint: you can use a list comprehension to do this in one line
Expected output:
    beers == [0, 89, ..., 32, 64]
    len(beers) == 193
'''
# get beer pos
beer_mark = 0
for detail in header[0]:
    if 'eer' in detail:
        beer_mark = beer_mark
        break
    else:
        beer_mark += 1
# print(beer_mark) =>1

beers = []
for row in data:
    beers.append(row[beer_mark])


'''
PART 3:
Create separate lists of NA and EU beer servings: 'NA_beers', 'EU_beers'
Hint: you can use a list comprehension with a condition
Expected output:
    NA_beers == [102, 122, ..., 197, 249]
    len(NA_beers) == 23
    EU_beers == [89, 245, ..., 206, 219]
    len(EU_beers) == 45
'''
NA_beers = []
EU_beers = []
for row in data:
    if 'NA' in row[5]:
        NA_beers.append(row[1])

for row in data:
    if 'EU' in row[5]:
        EU_beers.append(row[1])

print(len(NA_beers))
print(len(EU_beers))

'''
PART 4:
Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
Hint: don't forget about data types!
Expected output:
    NA_avg == 145.43
    EU_avg == 193.78
'''

NA_beers = (sum(int(a) for a in NA_beers))/ len(NA_beers)
print("{:.2f}".format(NA_beers))
EU_beers = (sum(int(a) for a in EU_beers))/ len(EU_beers)
print("{:.2f}".format(EU_beers))

'''
PART 5:
Write a CSV file called 'avg_beer.csv' with two columns and three rows.
The first row is the column headers: 'continent', 'avg_beer'
The second and third rows contain the NA and EU values.
Hint: think about what data structure will make this easy
Expected output (in the actual file):
    continent,avg_beer
    NA,145.43
    EU,193.78
'''


with open('booz_avg.csv', 'w', newline="") as writing:
    boozwriter = csv.writer(writing,  delimiter=" ", quotechar="|",
        quoting=csv.QUOTE_MINIMAL)
    boozwriter.writerow(['continent'] + ['avg_beer'])
    boozwriter.writerow(['NA'] + ["{:.2f}".format(NA_beers)])
    boozwriter.writerow(['EU'] + ["{:.2f}".format(EU_beers)])






