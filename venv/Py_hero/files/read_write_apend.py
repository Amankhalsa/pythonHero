# read
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