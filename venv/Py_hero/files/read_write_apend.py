# read
# https://www.w3schools.com/python/python_file_handling.asp
# file = open('Notes_para.txt', 'r')
# write
file = open('para.txt', 'w')
# append
# file = open('Notes_para.txt', 'a')

# text = file.read()
# text = file.write()


var_para = """ paragraph is a series of related sentences developing a central idea, 
called the topic. Try to think about paragraphs in terms of thematic unity: 
a paragraph is a sentence or a group of sentences that supports one central,unified idea."""
text = file.write(var_para)
# print(text)
file = open('para.txt', 'r')
text = file.read()
print(text)
file.close()
print("file closed ")
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""