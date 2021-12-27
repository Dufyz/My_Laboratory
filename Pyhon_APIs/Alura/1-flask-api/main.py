import pickle
import os 

from typing import Text
from flask_basicauth import BasicAuth
from flask import Flask, request, jsonify
from textblob import TextBlob

cols = ['tamanho', 'ano', 'garagem']
model = pickle.load(open('models/model.sav', 'rb'))

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'root'
app.config['BASIC_AUTH_PASSWORD'] = 'root'
auth = BasicAuth(app)

@app.route('/')
def home():
    return 'App 1'

@app.route('/polarity/<sentence>')
@auth.required
def polarity(sentence):
    sentence = TextBlob(sentence)
    sentence = sentence.translate(to = 'en')
    polarity = sentence.sentiment.polarity
    return f'A polaridade encontrada foi de: {polarity}'

@app.route('/houses/', methods=['POST'])
@auth.required
def houses_prices():
    data = request.get_json()
    data = [data[col] for col in cols]
    predict = model.predict([data])
    return jsonify(preco = predict[0])

app.run(debug = True, host = '0.0.0.0')