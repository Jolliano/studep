import numpy as np

from flask import Flask, request, render_template

import pickle

app = Flask(__name__, template_folder='templates')

loaded_model = pickle.load(open("model.pkl", "rb"))

#create our "home" route using the "index.html" page
@app.route('/')
def home():
    return render_template('index.html')


#Set a post method to yield predictions on page
@app.route('/', methods = ['POST'])
def predict():
	#obtain all form values and place them in an array, convert into integers
    features = [x for x in request.form.values()]
    #Combine them all into a final numpy array
    final_features = [np.array(features)]
    #predict the price given the values inputted by user
    prediction = loaded_model.predict(final_features)
    if int(prediction)== 0:
        return render_template('index.html', prediction_text = "You are not currently in danger of having Depression.")
    else:
        return render_template('index.html', prediction_text = "Omo, you are in danger of being depressed.")

#Run app
if __name__ == "__main__":
    app.run(debug=True)
