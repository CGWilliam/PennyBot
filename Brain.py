

# RNN code is based on the tutorial by Dennybritz, and can be found here: https://github.com/dennybritz/rnn-tutorial-rnnlm & http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-2-implementing-a-language-model-rnn-with-python-numpy-and-theano/
# Code modified by C.G.William / Weeerdo5255

import os
import sys
from gru_theano import GRUTheano
import nltk
import pandas as pd

SENTENCE_START_TOKEN = "SENTENCE_START"
SENTENCE_END_TOKEN = "SENTENCE_END"
UNKNOWN_TOKEN = "UNKNOWN_TOKEN"

def generate_sentence(model, index_to_word, word_to_index, min_length=5):
    # We start the sentence with the start token
    new_sentence = [word_to_index[SENTENCE_START_TOKEN]]
    # Repeat until we get an end token
    while not new_sentence[-1] == word_to_index[SENTENCE_END_TOKEN]:
        next_word_probs = model.predict(new_sentence)[-1]
        samples = np.random.multinomial(1, next_word_probs)
        sampled_word = np.argmax(samples)
        new_sentence.append(sampled_word)
        # Seomtimes we get stuck if the sentence becomes too long, e.g. "........" :(
        # And: We don't want sentences with UNKNOWN_TOKEN's
        if len(new_sentence) > 100 or sampled_word == word_to_index[UNKNOWN_TOKEN]:
            return None
    if len(new_sentence) < min_length:
        return None
    return new_sentence

def print_sentence(s, index_to_word):
    sentence_str = [index_to_word[x] for x in s[1:-1]]
    singlestring = (" ".join(sentence_str))
    sys.stdout.flush()
    return singlestring

def generatesentences(model, n, index_to_word, word_to_index):
    for i in range(n):
        sent = None
        while not sent:
            sent = generate_sentence(model, index_to_word, word_to_index)
        stringout = print_sentence(sent, index_to_word)
        return stringout

def loadmodel(path, modelClass=GRUTheano):
    npzfile = np.load(path)
    E, U, W, V, b, c = npzfile["E"], npzfile["U"], npzfile["W"], npzfile["V"], npzfile["b"], npzfile["c"]
    hidden_dim, word_dim = E.shape[0], E.shape[1]
    print ("Building model model from %s with hidden_dim=%d word_dim=%d" % (path, hidden_dim, word_dim))
    sys.stdout.flush()
    model = modelClass(word_dim, hidden_dim=hidden_dim)
    model.E.set_value(E)
    model.U.set_value(U)
    model.W.set_value(W)
    model.V.set_value(V)
    model.b.set_value(b)
    model.c.set_value(c)
    return model

def load(filename):

    word_to_index = []
    index_to_word = []

    # Read the data and append SENTENCE_START and SENTENCE_END tokens
    print("Reading CSV file...")
    df = pd.read_csv(filename, dtype={'ID': object})
    saved_column = []

    for x in df.body:
        saved_column.append(str(x))

    sentences = []
    for x in saved_column:
        tokens = (nltk.sent_tokenize(x.lower()))
        #print(tokens)
        for i in tokens:
            sentences.append(i)

# Load AI CSV files
x_train, y_train, word_to_index, index_to_word = load("reddit-comments-2015.csv", 5000)

# Load AI model
files = os.listdir("./")
files = filter(lambda x: x.find("GRU") > -1, files)
name_n_timestamp = dict([(x, os.stat("./" +x).st_mtime) for x in files])
brain = max(name_n_timestamp, key=lambda k: name_n_timestamp.get(k))
model = loadmodel(brain)
x = 0
file = open("thoughts.txt", "w")
while x < 500:
    try:
        thoughtstring = (str(generatesentences(model, 3, index_to_word, word_to_index)) + "\n")
        file.write(thoughtstring)
    except:
        thoughtstring = ("Well, alright !")
    x += 1

file.close()

