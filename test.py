from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
import nltk
from main import prediction_, get_resp
from data import delete__

stopwords = set(stopwords.words('german'))
stopwords.add("?")
stemmer = LancasterStemmer()

def remove_inp(msg):
    s = ""
    wrd = stemmer.stem(msg.lower())
    wo = nltk.word_tokenize(wrd)
    result = [i for i in wo if not i in stopwords]
    for i in result:
        s = s + i + " "
    return s

a = "kleineres unternehmen sicherer hackerangriffe"
b = remove_inp(a)
#print(b)

d = ["3"]
#c = prediction_(b, d)
#e = get_resp(b, d)
delete__(b)
print(c)
#print(e)