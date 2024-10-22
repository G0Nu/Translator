
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


'''
WITHOUT NLTK:
string = "Hello how are you?, I'm fine thank you. I'm very glad you are here. Because you are a nice person. Yahoo"
def Cleaning(x):#creating a function
    x.lower()#lowe case
    #newstring = x.split(".")#removing punctuation
    # x = ''.join(newstring)

    newstring = ''.join(letter for letter in x if letter.isalnum() or letter.isspace())#removing special characters using isalnum() and exceptuating spaces
    print(newstring)
print(string,"\n")

Cleaning(string)
'''

'''
With NLTK
'''
def clean_text(text):

    text = text.lower() #lowercase
    text = text.translate(str.maketrans('','',string.punctuation.replace(' ', '')))#remove punctuation without spaces

#removing punctuation
    words = nltk.word_tokenize(text)#tokenizing or spliting the words

    #Lemmatize or stemming 
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    print(words)
    return ''.join(words)
    

def remove_numbers(text):
    string_list = [''.join([char for char in string if not char.isdigit()]) for string in content] #to remove numbers from a string list
    text = ''.join(string_list)
    return text
    
# newcontent = clean_text(content)
# print(newcontent)
# no_numbers = remove_numbers(content)
# print(no_numbers)
data = clean_text(content)
# print(data)