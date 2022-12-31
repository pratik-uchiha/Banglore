from flask import Flask, render_template, request, jsonify
from utils import HousePricePrediction

hpp = HousePricePrediction()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')



@app.route('/get_location_names')
def get_location_names():
    locations = hpp.get_location_names()
    return jsonify({'locations':locations})


@app.route('/predict_home_price', methods = ['POST','GET'])
def predict_home_price():
    if request.method == 'POST':
        user_data = request.form
        total_sqrt = eval(user_data['sqft'])
        bhk = eval(user_data['bhk'])
        bath = eval(user_data['bath'])
        location = user_data['loc']
        
        price = hpp.get_house_price(location,total_sqrt,bath,bhk)
        # return jsonify({'Predicted House Price':price})
        if price > 99:
            price_new = round((price/100),2)
            price_new = str(price_new)+'Cr'
            return render_template('home.html', prediction_text = price_new)
        
        else:   
            price_new = str(price) + ' Lakhs'
            return render_template('home.html', prediction_text = price_new)
        # return render_template('home.html', prediction_text = price)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)