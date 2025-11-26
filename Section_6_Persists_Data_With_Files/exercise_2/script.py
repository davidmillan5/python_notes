countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for country in countries:
    file = f"{country}.txt"
    filename = open(file, 'w')
    filename.write(country)
    filename.close()