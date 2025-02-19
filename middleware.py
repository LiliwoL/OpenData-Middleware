# ======================================================================================================================
# Middleware qui fournira aux pages l'accès aux données
# ======================================================================================================================


# ======================================================================================================================
# Import the necessary modules
# ======================================================================================================================
import dotenv
import requests
import json
from json import JSONDecodeError
import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import datetime
import platform
import time

# Import the console module from the inc package
from inc import console
from inc import file
# ======================================================================================================================



# ======================================================================================================================
# Création de l'application
# ======================================================================================================================
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
# ======================================================================================================================



# ======================================================================================================================
# Définition des headers utilisés dans toutes les requêtes
# ======================================================================================================================
env = dotenv.dotenv_values('.env')

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',

    'X-Cda-Lr-Api-Key': env['API_KEY'],
}
# ======================================================================================================================


# ======================================================================================================================
# Route pour récupérer les prochains bus
# ======================================================================================================================
@app.route('/api/v1/nextbus/<busStopNumber>/<numberBus>')
def nextBus(busStopNumber, numberBus):

    # Test la présence du fichier

    # Sinon, fait une requête
    
    # Construction de l'url
    global resp_dict
    url = 'https://api.agglo-larochelle.fr/production/yelo-api/next-bus-siri/%s/%s.json' % (busStopNumber, numberBus)

    result = requests.get(url, headers=headers)
    try:
        resp_dict = result.json()
    except JSONDecodeError:
        print('Response could not be serialized')

    print(result)
    return resp_dict


# ======================================================================================================================
# Route pour récupérer l'état des stations vélos
# ======================================================================================================================
@app.route('/api/v1/yelo/bikes-real-time')
def bikesrealtime():

    # Filename
    filename = 'DATA/' + 'siri-yelo-velos.json'

    # Test la présence du fichier
    if file.check_data_file(filename, 60):
        # Data file is ok, let's use it
        try:
            resp_dict = json.load(filename)
        except JSONDecodeError:
            print('Response could not be serialized')


    else:
        # Data file is too old !

        # Construction de l'url
        url = 'https://api.agglo-larochelle.fr/production/yelo-api/bikes-real-time.json'

        # Récupération des données
        result = requests.get(url, headers=headers)

        try:
            resp_dict = result.json()

            # Stockage dans un fichier
            file.store_scraped_data(filename, resp_dict)


        except JSONDecodeError:
            print('Response could not be serialized')

    return resp_dict


@app.route("/")
def home():
    return "Flask Vercel Example - Hello World", 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404
# ======================================================================================================================

# Lancement de l'app
console.clear_console()
print( console.generate_figlet_text("Hope And Data - La Rochelle"))

if __name__ == '__main__':
    app.run(debug=True)