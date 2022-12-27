import nltk
import pandas as pd
import re
import random

nltk.download('gutenberg')
print(nltk.corpus.gutenberg.fileids())

a = nltk.corpus.gutenberg.words('austen-emma.txt')
b = nltk.corpus.gutenberg.words('austen-persuasion.txt')
c = nltk.corpus.gutenberg.words('austen-sense.txt')
d = nltk.corpus.gutenberg.words('whitman-leaves.txt')

text_content_a = ''

for i in a:
    if len(re.findall('[a-zA-Z0-9]',i))>0:
        text_content_a = text_content_a + ' ' + i

split_content_a = []
n=100
for i in range(0, len(text_content_a), n):
   split_content_a.append(text_content_a[i : i + n])

book_a = ''
for i in range(200):
    random_content = random.choice(split_content_a)
    book_a = book_a + random_content

print(len(text_content_a))
print(len(book_a))
print(book_a)

text_content_b = ''
for i in b:
    if len(re.findall('[a-zA-Z0-9]',i))>0:
        text_content_b = text_content_b + ' ' + i

split_content_b = []
n=100
for i in range(0, len(text_content_b), n):
   split_content_b.append(text_content_b[i : i + n])

book_b = ''
import random
for i in range(200):
    random_content = random.choice(split_content_b)
    book_b = book_b + random_content

print(len(text_content_b))
print(len(book_b))
print(book_b)

text_content_c = ''
for i in c:
    if len(re.findall('[a-zA-Z0-9]',i))>0:
        text_content_c = text_content_c + ' ' + i


split_content_c = []
n=100
for i in range(0, len(text_content_c), n):
   split_content_c.append(text_content_c[i : i + n])

book_c = ''
import random
for i in range(200):
    random_content = random.choice(split_content_c)
    book_c = book_c + random_content

print(len(text_content_c))
print(len(book_c))
print(book_c)

text_content_d = ''
for i in d:
    if len(re.findall('[a-zA-Z0-9]',i))>0:
        text_content_d = text_content_d + ' ' + i

split_content_d = []
n=100
for i in range(0, len(text_content_d), n):
   split_content_d.append(text_content_d[i : i + n])

book_d = ''
import random
for i in range(200):
    random_content = random.choice(split_content_d)
    book_d = book_d + random_content

print(len(text_content_d))
print(len(book_d))
print(book_d)

Book1 = pd.Series([book_a])
Book2 = pd.Series([book_b])
Book3 = pd.Series([book_c])
Book4 = pd.Series([book_d])

print(pd.DataFrame({ 'Book1': Book1, 'Book2': Book2, 'Book3': Book3,'Book4': Book4}))



