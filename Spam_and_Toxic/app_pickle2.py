from flask import Flask,render_template,url_for,request
import pickle
import string
import pandas as pd


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    def remove_punc(txt):
        del_symbols = ['«', '»', '®', '´', '·','º', '½', '¾', '¿', '¡', '§', '£', '₤']
        plain_txt = (ch for ch in txt if(ch not in string.punctuation and ch not in string.digits and ch not in del_symbols))
        plain_txt = ''.join(plain_txt)
        return plain_txt
    
    vectorizer = pickle.load(open('vectorizer.pkl','rb'))
    classifier = pickle.load(open('one_vs_rest_classifier.pkl','rb'))
    if request.method == 'POST':
        user_input = request.form['comment']
        user_input = remove_punc(user_input)
        user_input = pd.Series(user_input)
        user_input = vectorizer.transform(user_input)
        output = classifier.predict(user_input)
        toxic = output[0][0]
        s_toxic = output[0][1]
        obscene = output[0][2]
        threat = output[0][3]
        insult = output[0][4]
        identity_hate = output[0][5]
        llis = [toxic, s_toxic, obscene, threat, insult, identity_hate]
        if 1 not in llis:
            fine = 1
            llis = [toxic, s_toxic, obscene, threat, insult, identity_hate, fine]
    return render_template('result2.html',lis = llis)



if __name__ == '__main__':
	app.run(debug=True)