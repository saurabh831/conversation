from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
import nltk
from main import prediction_, get_resp

stopwords = set(stopwords.words('german'))
stopwords.add("?")
stemmer = LancasterStemmer()

def remove_(msg):
    result = [i for i in msg if not i in stopwords]
    return result

s = ""
a = "ist ein kleineres Unternehmen sicherer gegen Hackerangriffe?"
wrd = stemmer.stem(a.lower())
wo = nltk.word_tokenize(wrd)
print(wo)
b = remove_(wo)
print(b)
for i in b:
    s = s + i + " "
print(s)
d = ["3"]
c = prediction_(s, d)
e =  get_resp(s, d)
print(c)
print(e)