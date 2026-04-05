from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("Houseprice.html")

@app.route("/predict", methods=["POST"])
def predict():
    area = int(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    location = request.form["location"]


    loc_suburban = 0
    loc_rural = 0

    if location == "Suburban":
        loc_suburban = 1
    elif location == "Rural":
        loc_rural = 1
   

   
    input_data = pd.DataFrame({
        "Area": [area],
        "Bedrooms": [bedrooms],
        "Location_Rural": [loc_rural],
        "Location_Suburban": [loc_suburban]
    })
    input_data=input_data[model.feature_names_in_]

    prediction = model.predict(input_data)[0]

    return render_template("Houseprice.html",prediction=int(prediction))



if __name__ == "__main__":
    app.run(debug=True)
