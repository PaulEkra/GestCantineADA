# Gestion Cantine ADA

Projet pour une cantine, permettant d'effectuer un CRUD le menu et les plats et des recherches en fonction du nom des plats

## Les étapes d'installation de l'application :
- Ouvrer un terminal puis cloner le lien github de l'application : git clone https://github.com/PaulEkra/GestCantineADA.git
- Créer un environnement virtuel dans le repertoire ( python ou python3 pour Unix/MacOs -m venv nom_environnement de prefence venv ou env)
- Naviguer vers le fichier activate.bat soit dans scripts ou bin, puis activer l'environnement (source activate pour Unix/MacoS ou activate pour windows)
- Revener au dossier de base de votre projet puis installer les dépendances de l'application à partir du fichier requirements.txt (pip(Windows) ou pip3(Unix/Mac) install -r requirements.txt)
- Créer une base de données MySQL nommée 'cantine_db' et et configuer les paramètres dans le fichier settings.py du dossier GestCantineADA  
- Naviguez vers le repertoire source (src) puis créer et appliquer les migrations : python manage.py makemigrations ensuite python manage.py migrate
  
## Les instructions de démarrage :
- Naviguez vers le repertoire source (src) puis lancer le server : python manage.py runserver, vous pouvez preciser le port python manage.py runserver numeros_port ( exple : python manage.py runserver 8888)
  
## description des fonctionnalités principales de l'application :
- CRUD des menus
- CRUD des plats
- Possibilité de faire des recherches en fonction du nom d'un plat dans la liste des plats ou des menus
