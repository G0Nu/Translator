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
string = "Hello how are you?, I'm fine thank and you?. I'm very glad you are here. Because? you are a nice person. Yahoo"
def Cleaning(x):#creating a function
    '''How does the function works? Basically I clean the data, I needed to lowercase, then splited by dots so it can separate sentences, this is important for the context.
    Then I send it to another list in the loop (the loop reads each item of the list instead of the whole list) Z = 0 so it can start at the begining of the list and each time the loop ends it plus 1
    so it goes to the next item on the list until the list its over, then I saved each word separately to the new list and that new list appended to the actual data set called all_Words.
    '''
    x = x.lower()#lowe case
    #newstring = x.split(".")#removing punctuation
    # x = ''.join(newstring)
    #x = x.split(".")
    #x = ''.join(letter for letter in x) 
    #rint(x)
    x = x.replace("?",".")
    x = x.replace("!",".")
    x = x.split(".")
    print(x,"\n\n\n\n")
    z = 0
    new_list = []
    for e in x:
        e = x[z]
        e = e.split(".")
        new_list.append(e)
        z = z+1
    print(new_list)
    z=0
    for i in new_list:
        i = x[z]
        sent_list = []
        res = ''.join(letter for letter in i if letter.isalnum() or letter.isspace())#removing special characters using isalnum() and exceptuating spaces
        words = res.split()
        sent_list.extend(words)
        all_words.append(sent_list)
        z = z+1
    print(all_words)
    #x = ''.join(letter for letter in x)
    newstring = ''.join(letter for letter in x if letter.isalnum() or letter.isspace())#removing special characters using isalnum() and exceptuating spaces
    #print(newstring)
    
#print(string,"\n")

Cleaning(string)
sent = ["Hello how are you?! I am trying to tell. you, you are beautifull!"]

'''
With NLTK
'''
'''
def clean_text(text):

    text = text.lower() #lowercase
    text = text.translate(str.maketrans('','',string.punctuation.replace(' ', '')))#remove punctuation without spaces

#removing punctuation
    #text = text.split(".")
    words = nltk.word_tokenize(text)#tokenizing or spliting the words

    #Lemmatize or stemming 
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    print(words)
    return ''.join(words)
'''
    

def remove_numbers(text):
    string_list = [''.join([char for char in string if not char.isdigit()]) for string in content] #to remove numbers from a string list
    text = ''.join(string_list)
    return text
    
# newcontent = clean_text(content)
# print(newcontent)
# no_numbers = remove_numbers(content)
# print(no_numbers)
#data = clean_text(content)
# print(data)