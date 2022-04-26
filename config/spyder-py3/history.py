# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Sat Aug  7 13:41:28 2021)---
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Sat Aug  7 13:57:15 2021)---
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')
with open('/home/ranchhor/Desktop/ML/NLP/01 - The Fellowship Of The Ring.txt',\
          encoding="ISO-8859-1") as f:
    sentences = f.readlines()
    
print(sentences)
tokenizer = Tokenizer(oov_token = "<OOV>")
tokenizer.fit_on_texts(sentences)
text_sequences = tokenizer.texts_to_sequences(sentences)
word_index = tokenizer.word_index
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Sat Aug  7 14:04:53 2021)---
!wget --no-check-certificate \
    https://storage.googleapis.com/laurencemoroney-blog.appspot.com/sarcasm.json \
    -O /home/ranchhor/Desktop/ML/NLP/sarcasm.json
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')
print(df)
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')
print(df["headline"])
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Sat Aug  7 14:35:44 2021)---
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Sat Aug  7 20:51:59 2021)---
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Thu Jan 20 21:55:32 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
physical_devices = tf.config.expermental.list_physical_devices('GPU')
print("Number of Gpu: ", len(physical_devices))
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Thu Jan 20 22:19:59 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Fri Jan 21 22:36:21 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/MInOR.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Sat Jan 22 13:05:56 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    print(score)

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    print(max(score))

prediction("the food is not bad")



def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    print(le.inverse_transform(max(score)))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    print(labelencoder.inverse_transform(max(score)))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    
    print(labelencoder.inverse_transform(score))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    index = list(index(max(score)))
    print(labelencoder.inverse_transform(index))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = list(score.index(max(score)))
    print(labelencoder.inverse_transform(ind))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = list(np.argmax(score, axis=1))
    print(labelencoder.inverse_transform(max(ind)))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = list(np.argmax(score, axis=0))
    print(labelencoder.inverse_transform(max(ind)))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=1))
    print(labelencoder.inverse_transform(ind))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(labelencoder.inverse_transform(ind))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = list(np.argmax(score, axis=0))
    print(labelencoder.inverse_transform(ind))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(labelencoder.inverse_transform(ind))

prediction("the food is not bad")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(ind)

prediction("the food is not bad")
print(labelencoder.inverse_transform(12))
print(labelencoder.inverse_transform([12]))
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=1))
    print(labelencoder.inverse_transform([ind]))


prediction("i am happy")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am happy")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i will kill you")
prediction("i want to die")
prediction("i love her")
prediction("i am sick of her")
print(model.wv.most_similar('love'))
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
prediction("i hate her")
prediction("i am not happy")
prediction("i am  happy")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  happy")
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmin(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  happy")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmean(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  happy")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = (np.mean(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  happy")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = floor(np.mean(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  happy")
import math
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = math.floor(np.mean(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  happy")
import math
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = math.floor(np.mean(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  sad")
import math
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    print(score)
    ind = math.floor(np.mean(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  sad")
print(labelencoder.inverse_transform([13]))
print(labelencoder.inverse_transform([12]))
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = floor(np.mean(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  happy")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = list(np.array(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  happy")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = list(np.array(score))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  happy")
def prediction(review):
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = list(np.array(score))
    print(labelencoder.inverse_transform(ind))


prediction("i am  happy")
def prediction(review):
    
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = list(np.array(score))
    print(labelencoder.inverse_transform(ind))


prediction("i am  happy")
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
def prediction(review):
    review = clean_text(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)
    score=model.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction("i am  happy")
prediction("the food was bitter")
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Sat Jan 22 18:16:45 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
prediction("I am not sure")
prediction("This is fun")
prediction("i am lonely")

## ---(Sun Jan 23 00:56:20 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
import joblib
joblib.dump(model_history, 'minorlstm.pkl')
joblib.dump(labelencoder, 'lblencoder.pkl')
prediction("i will kill you")
prediction("i love her")
prediction("i kill him")
prediction(" him")
prediction("such a lonely day and it's mine")
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
from keras.models import load_model
model_history.save('minorlst.h5')
prediction("i am very sad")
prediction("i am very empty")
prediction("i am lonely")
prediction("i am not happy")
prediction("wow this is amazing")
prediction("bakemono")
prediction("gouri is a angry boy")
prediction("i will cut you into pieces")
prediction("i will cut you into pieces i am angry")
prediction("i will cut you into pieces i am angry so fucking angry")
prediction("so fucking angry")
prediction("i hateful sad")
prediction("i hateful")
prediction("i hate you")
from keras.models import load_model
model_history.save('minorlst.h5')
from keras.models import load_model
model.save('minorlst.h5')
pmodel = keras.models.load_model("minorlst.h5")
def prediction(review, pmodel):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)


    score=pmodel.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction(("i am very sad"),pmodel)
joblib.dump(labelencoder, 'lblencod.pkl')
pmodel = keras.models.load_model("minorlst.h5")
labelencoder = joblib.load('lblencod.pkl')

def prediction(review, pmodel, labelencoder):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
    print(review)


    score=pmodel.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(labelencoder.inverse_transform([ind]))


prediction(("i am very sad"),pmodel,labelencoder)
runfile('/home/ranchhor/Desktop/ML/NLP/MInOR.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/MInOR.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/MInOR.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Sun Jan 23 13:38:44 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/MInOR.py', wdir='/home/ranchhor/Desktop/ML/NLP')
pmodel = keras.models.load_model("minorlst1.h5")
labelencoder = joblib.load('lblencod1.pkl')

def prediction(review, pmodel, labelencoder):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)
    print(review)


    score=pmodel.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction(("i am  sad"),pmodel,labelencoder)
prediction(("sweet dreams are made of this"),pmodel,labelencoder)
def prediction(review):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)
    print(review)


    score=modellstm.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction("i am  sad")
def prediction(review):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)
    print(review)


    score=modelstm.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction("i am  sad")
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
prediction("i am  sad")
prediction("i am   not sad")
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
def prediction(review):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)
    print(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)
    print(review)


    score=modelstm.predict(review)
    score=score[0]
    ind = (np.argmax(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction("i am  sad")
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
prediction("i am   not sad")
prediction("i am  happy")
def prediction(review):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)
    print(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)
    print(review)


    score=modelstm.predict(review)
    score=score[0]
    ind = (np.mean(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction("i am   not sad")
def prediction(review):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)
    print(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)
    print(review)


    score=modelstm.predict(review)
    score=score[0]
    ind = math.ceil(np.mean(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction("i am   not sad")
prediction("i am happy")
prediction("i am crazy")
def prediction(review):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)

    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)



    score=modelstm.predict(review)
    score=score[0]
    print(score)
    ind = math.ceil(np.mean(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction("i am   not sad")
def prediction(review):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)

    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)



    score=modelstm.predict(review)
    score=score[0]
    print(score)
    ind = math.ceil(np.mean(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction("i am    sad")
def prediction(review):
    review = clean_text(review)
    tokenizer.fit_on_texts(review)

    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)



    score=modelstm.predict(review)
    score=score[0]
    print(score)
    ind = math.ceil(np.mean(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction("cracy but that's how it goes   sad")
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
prediction("i am  happy")

## ---(Sun Jan 23 16:05:35 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/MInOR.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
def prediction(review):

    tokenizer.fit_on_texts(review)
    print(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)



    score=modelstm.predict(review)
    score=score[0]
    print(score)
    ind = (np.argmax(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction("i am   not sad")
def prediction(review):

    tokenizer.fit_on_texts(review)
    print(review)
    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)
    print(review)


    score=modelstm.predict(review)
    score=score[0]
    print(score)
    ind = (np.argmax(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction("i am   not sad")
print(X_test[0])
train_df['text'].head()
rediction(['i','am','not','sad'])
prediction(['i','am','not','sad'])
prediction(['i','am','sad'])
prediction(['i','am','happy'])
def prediction(review):


    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)
    print(review)


    score=modelstm.predict(review)
    score=score[0]
    print(score)
    ind = (np.argmax(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction(['i','am','happy'])
def prediction(review):


    review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=30)
    print(review)


    score=modelstm.predict(review)
    score=score[0]
    print(score)
    ind = (np.argmax(score, axis=0))
    print(ind)
    print(labelencoder.inverse_transform([ind]))

prediction(['i','am','anger'])
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
prediction(['i','am','crazy'])
prediction(['you are crazy'])
prediction('you are crazy')
prediction('you are stupid')
prediction('he is stupid')

## ---(Thu Jan 27 10:48:48 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/MInOR.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Sun Mar  6 16:22:15 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')

## ---(Thu Mar 10 21:37:26 2022)---
runfile('/home/ranchhor/Desktop/ML/NLP/MInOR.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/word2vec.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/MInOR.py', wdir='/home/ranchhor/Desktop/ML/NLP')
runfile('/home/ranchhor/Desktop/ML/NLP/minorproj.py', wdir='/home/ranchhor/Desktop/ML/NLP')