import os
import json
import time




# ======================================================================================================================
# Fonctions utiles
# ======================================================================================================================






# Check if a file is too old
def check_data_file(filename, duration_in_seconds):
    try:
        # Vérifier si le fichier existe
        if not os.path.isfile(filename):
            return False

        # Obtenir le temps de création du fichier
        creation_date = os.path.getctime(filename)

        # Calculer l'âge du fichier en secondes
        file_age = time.time() - creation_date

        # Vérifier si le fichier est trop ancien
        if file_age > duration_in_seconds:
            print("========================================")
            print(f"💀💀 -- {filename} is outdated -- 💀💀")
            return False

        return True

    except Exception as e:
        # Gérer les exceptions et erreurs
        print(f"Une erreur s'est produite : {e}")
        return False


# Store data in a file
def store_scraped_data(filename, content):
    try:
        # Check if the file exists
        if os.path.isfile(filename):
            # Delete the file
            os.remove(filename)

    except Exception as e:
        # Handle any exceptions that may occur
        print(f"An error occurred: {e}")

    # Write in file
    print(f"📌📌 -- Write in file {filename} -- 📌📌")
    with open(filename, 'w') as file:
        json.dump(content, file)
