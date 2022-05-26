# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as file:
        txt = file.read()
    return txt

def count_words():
    txt = read_file_content("./story.txt")
    words = txt.split()
    word_count = {}
    for word in words:
        word_count[word] = words.count(word)
    print(word_count)
    return word_count

read_file_content("./story.txt")
count_words()
    