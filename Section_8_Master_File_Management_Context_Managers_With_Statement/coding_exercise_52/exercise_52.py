with open('story.txt', 'r') as file:
    string_variable = file.readlines()

with open('story_copy.txt', 'w') as file:
    file.write(str(string_variable[0]))