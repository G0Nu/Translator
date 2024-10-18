from cgitb import text
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

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
    text = text.translate(str.maketrans('','',string.punctuation))#removing punctuation
    words = nltk.word_tokenize(text)#tokenizing or spliting the words

    #Lemmatize or stemming 
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ''.join(words)
    
text = "This is a sample sentence, showing off the stop words filtration."
print(text,"\n\n")
newtext = clean_text(text)
print(newtext)
