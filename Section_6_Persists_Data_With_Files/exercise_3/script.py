filenames = ['doc.txt', 'report.txt', 'presentation.txt']
text = 'Hello'

for file in filenames:
    new_file = open(file,'w')
    new_file.write(text)
    new_file.close()