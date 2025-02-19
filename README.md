# Middleware

On réalise ici un **middleware** pour aller consommer les APIs OpenData fournies par les villes ou structures.

L'objectif est de ne pas avoir à réécrire les clients à chaque modification des APIs utilisées.
De plus, les clés API ne sont pas exposées dans le code source.

# Dépendances

pip install -r requirements.txt --break-system-packages

# Lancement

python middleware.py

# Postman Collection

Pour tester les routes, le dossier **PostmanCollection** contient une collection de requêtes Postman.

# Déploiement

Le déploiement se fait sur Vercel.
https://dev.to/andrewbaisden/how-to-deploy-a-python-flask-app-to-vercel-2o5k

# TODO

- Documentation Swagger
- A la réception d'une requête, vérifier si le fichier existe déjà et s'il n'est pas trop ancien
- Si le fichier est trop ancien, le supprimer et en créer un nouveau à partir d'une requête
- Si le fichier est à jour, le renvoyer directement
- Trop ancien: 1 minute

- Gestion du http_status_code 429
    Rate limit exceeded ! You reach the limit of 1 requests per 1 seconds