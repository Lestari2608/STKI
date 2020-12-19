import re  # impor modul regular expression
import string
import nltk
# impor word_tokenize dari modul nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory 
import xml.etree.ElementTree as ET

tree = ET.parse('items.xml')
root = tree.getroot()

factory = StemmerFactory()
stemmer = factory.create_stemmer()

for elem in root:
    for subelem in elem:
        print(subelem.text)
		
print("1.Tahap lowercase")
lowerCase = subelem.text.lower()
print(lowerCase)

# Menghapus angka
print("menghapus angka")
hapusAngka = re.sub(r"\d+", "", lowerCase)
print(hapusAngka)

# Menghapus tanda baca
print("menghapus tanda baca")
tandaBaca = hapusAngka.translate(str.maketrans("", "", string.punctuation))
print(tandaBaca)

# Menghapus whitepace (karakter kosong)
print("whitspace")
karakterKosong = tandaBaca.strip()
print(karakterKosong)

# 2. Tokenizin
print("2.Tahap Tokenisasi")
# tokenizing kata
print("tokenisasi kata")
tokens = nltk.tokenize.word_tokenize(karakterKosong)
print(tokens)

# Frequensi
print("frekuensi")
kemunculan = nltk.FreqDist(tokens)
print(kemunculan.most_common())

# 3. Filtering (Stopword Removal)
print("3.Tahap stopword")
# Filtering
filter = word_tokenize(karakterKosong)
listStopword = set(stopwords.words('indonesian'))

removed = []
for t in filter:
    if t not in listStopword:
        removed.append(t)
print(removed)

# Stemming bahasa indonesia menggunakan Python Sastrawi
print("4.Tahap stemming")
for y in removed:
    print(y, " : ", stemmer.stem(y))
    # k = stemmer.stem(y)
#     kemunculan = nltk.FreqDist(stemmer.stem(y))
# print(kemunculan.most_common())