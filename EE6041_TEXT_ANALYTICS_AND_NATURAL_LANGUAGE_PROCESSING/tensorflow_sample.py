import tensorflow as tf
from tensorflow import  keras
from keras.preprocessing.text import Tokenizer

sentences=[
    'I love my dog',
    'I love my cat',
    'You love my dog!'

]
tokenizer=Tokenizer(num_words=100)
tokenizer.fit_on_texts(sentences)
word_index=tokenizer.word_index
print(word_index)