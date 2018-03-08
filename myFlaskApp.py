from flask import Flask, render_template
from urllib.request import urlopen
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    #return 'Hello World!'
    return render_template("index.html")


@app.route('/weather', methods=['POST'])
def runweather():
    f = urlopen('http://api.wunderground.com/api/b27dbdfdaafdef52/geolookup/conditions/q/MN/Minneapolis.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    disp_location = parsed_json['current_observation']['display_location']['city']
    list_location = parsed_json['location']['nearby_weather_stations']['airport']['station'][0]['city']
    f.close()

    return render_template('weather.html',location=location,temp_f=temp_f,disp_location=disp_location,list_location=list_location)


@app.route('/radar', methods=['POST'])
def runradar():
    location = 'Minneapolis'
    return render_template('radar.html',location=location)


if __name__ == '__main__':
    app.run(debug=True)
