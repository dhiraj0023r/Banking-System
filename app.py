from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('bank_note_knn.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        
        variance = float(request.form['variance'])
        
        skewness = float(request.form['skewness'])
       
        curtosis = float(request.form['curtosis'])
       
        entropy = float(request.form['entropy'])

            
        prediction=model.predict([[variance, skewness, curtosis, entropy]])
        
        output = prediction

        if output == 0:
            return render_template('index.html',prediction_text="The note is legit", variance=variance, skewness=skewness, curtosis=curtosis, entropy=entropy)
        else:
            return render_template('index.html',prediction_text="The note is not legit", variance=variance, skewness=skewness, curtosis=curtosis, entropy=entropy)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
