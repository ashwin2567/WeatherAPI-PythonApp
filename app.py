from flask import Flask, request
import requests
app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get('http://api.weatherapi.com/v1/current.json?key=c4b11476343946c2bb3145213231804&q=London&aqi=no')
    data = response.json()
    return data['location']['name'] + str(data['current']['temp_c'])

@app.route('/allow/<city_name>')
def ondemand(city_name):
    try:
        name = request.args.get('name')
        response = requests.get('http://api.weatherapi.com/v1/current.json?key=c4b11476343946c2bb3145213231804&q='+city_name+'&aqi=no');
        data = response.json()
        return data['location']['name'] + str(data['current']['temp_c'])
    except requests.exceptions as errh:
            print("temp")
            return "An Http Error occurred:"

@app.route('/city/<string:city_name>')
def func(city_name: str):
    print('Request for index page received')
    response = requests.get('http://api.weatherapi.com/v1/current.json?key=c4b11476343946c2bb3145213231804&q='+city_name+'&aqi=no');
    data = response.json()
    stre = 'Current  in %s is %d℃ but it feels like %d℃.' % (data['location']['name'], data['current']['temp_c'], data['current']['feelslike_c'])
    return  stre


if __name__ == "__main__":
    app.run(debug=True)