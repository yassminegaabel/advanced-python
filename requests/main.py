import requests

# GET
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)
print(response.json())

# GET liste
users = requests.get("https://jsonplaceholder.typicode.com/users")
for user in users.json():
    print(user['name'])

# POST
new_post = {"title": "Mon titre", "body": "Mon contenu", "userId": 1}
r = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print(r.status_code, r.json())

# Gestion erreurs
try:
    r = requests.get("https://jsonplaceholder.typicode.com/users/9999")
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"Erreur HTTP : {e}")