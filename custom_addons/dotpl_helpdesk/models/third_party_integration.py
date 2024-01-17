from odoo import api, fields, models
import requests


class ThirdPartyintegration(models.TransientModel):
    _name = "fetch_third_party_data"
    _description = "third party data"


    def _fetch_third_party_data(self):
        api_key = '2427d882c4751eb72924daa99782b905'  # Replace with your OpenWeatherMap API key
        city = 'London'
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric',  # You can change this to 'imperial' for Fahrenheit
        }
        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                # return data
                print(data)
            else:
                # return {'error': data['message']}
                print({'error': data['message']})
        except Exception as e:
            # return {'error': str(e)}
            print({'error': str(e)})

    def execute_third_party_data_fetch(self):
        # Call the _fetch_third_party_data method
        self._fetch_third_party_data()
