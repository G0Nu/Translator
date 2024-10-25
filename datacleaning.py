from hmac import new
from re import X
from tkinter import Y
from isort import file
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


f = open('ch_books.text','r')
content = f.read()
f.close()
all_words = []


#WITHOUT NLTK:
def Cleaning(x):#creating a function
    '''How does the function works? Basically I clean the data, I needed to lowercase, then splited by dots so it can separate sentences, this is important for the context.
    Then I send it to another list in the loop (the loop reads each item of the list instead of the whole list) Z = 0 so it can start at the begining of the list and each time the loop ends it plus 1
    so it goes to the next item on the list until the list its over, then I saved each word separately to the new list and that new list appended to the actual data set called all_Words.
    '''
    x = x.lower()#lower case
    x = x.replace("?",".")
    x = x.replace("!",".")
    
    x = x.split(".")
    #print(x,"\n\n\n\n")
    z = 0
    new_list = []
    for e in x:
        e = x[z]
        e = e.split(".")
        new_list.append(e)
        z = z+1
    #print(new_list)
    z=0
    lemmatizer = WordNetLemmatizer()
    for i in new_list:
        i = x[z]
        sent_list = []
        res = ''.join(letter for letter in i if letter.isalnum() or letter.isspace())#removing special characters using isalnum() and exceptuating spaces
        words = res.split()
        sent_list.extend(words)
        sent_list = [lemmatizer.lemmatize(word) for word in sent_list]
        all_words.append(sent_list)
        
        z = z+1
    return all_words
data = Cleaning(content)
print(data)



