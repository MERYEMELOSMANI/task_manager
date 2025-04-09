# storage.py - Module pour gérer la persistance des données
# Sauvegarde et charge les tâches depuis un fichier JSON

import json
import os

# Chemin du fichier de sauvegarde
# Je le mets dans le même dossier que le script pour simplifier
TASKS_FILE = "tasks.json"

def load_tasks():
    """
    Charge les tâches depuis le fichier JSON
    
    Returns:
        Liste des tâches chargées ou liste vide si le fichier n'existe pas
    """
    try:
        # Vérifie si le fichier existe
        if not os.path.exists(TASKS_FILE):
            print(f"Aucun fichier de tâches trouvé. Création d'une nouvelle liste...")
            return []
        
        # Ouvre et charge le fichier JSON
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
            
            # Petit message de debug que j'ai laissé pour moi
            print(f"Chargement de {len(tasks)} tâches depuis {TASKS_FILE}")
            return tasks
            
    except json.JSONDecodeError:
        # Gère le cas où le fichier existe mais n'est pas un JSON valide
        print(f"Erreur: Le fichier {TASKS_FILE} est corrompu. Création d'une nouvelle liste...")
        return []
    except Exception as e:
        # Gère les autres erreurs possibles
        print(f"Erreur lors du chargement des tâches: {str(e)}")
        return []

def save_tasks(tasks):
    """
    Sauvegarde les tâches dans le fichier JSON
    
    Args:
        tasks: Liste des tâches à sauvegarder
    """
    try:
        # Ouvre le fichier en mode écriture et sauvegarde les tâches
        with open(TASKS_FILE, 'w') as file:
            # J'utilise indent=2 pour que le fichier soit plus lisible
            # si je veux l'éditer manuellement
            json.dump(tasks, file, indent=2)
            
            # Petit message de debug que j'ai laissé pour moi
            print(f"Sauvegarde de {len(tasks)} tâches dans {TASKS_FILE}")
            
    except Exception as e:
        # Gère les erreurs possibles
        print(f"Erreur lors de la sauvegarde des tâches: {str(e)}")
