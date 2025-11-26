countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

counter = 0

for filename in filenames:
    file = open(filename, 'w')
    #for country in countries:
    file.write(countries[counter])
    file.close()
    counter +=1