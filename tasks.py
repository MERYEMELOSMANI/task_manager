# tasks.py - Module pour gérer les tâches dans mon gestionnaire
# Contient la logique pour ajouter, afficher, mettre à jour et supprimer des tâches

def add_task(tasks, description, priority):
    """
    Ajoute une nouvelle tâche à la liste
    
    Args:
        tasks: Liste des tâches existantes
        description: Description de la nouvelle tâche
        priority: Priorité de la tâche (Haute, Moyenne, Basse)
    
    Returns:
        Liste mise à jour avec la nouvelle tâche
    """
    # Génère un nouvel ID (le plus grand ID actuel + 1)
    new_id = 1
    if tasks:
        # J'utilise une liste en compréhension pour extraire tous les IDs
        # puis je trouve le max et j'ajoute 1
        new_id = max([task["id"] for task in tasks]) + 1
    
    # Crée la nouvelle tâche
    new_task = {
        "id": new_id,
        "description": description,
        "priority": priority
    }
    
    # Ajoute la tâche à la liste et retourne la liste mise à jour
    tasks.append(new_task)
    return tasks

def view_tasks(tasks):
    """
    Affiche toutes les tâches triées par priorité
    
    Args:
        tasks: Liste des tâches à afficher
    """
    # Définit l'ordre de priorité pour le tri
    priority_order = {"Haute": 1, "Moyenne": 2, "Basse": 3}
    
    # Trie les tâches par priorité
    # J'ai appris cette technique de tri avec une clé lambda sur un forum
    sorted_tasks = sorted(tasks, key=lambda x: priority_order[x["priority"]])
    
    # Affiche l'en-tête
    print(f"{'ID':<5} {'Priorité':<10} {'Description':<50}")
    print("-" * 65)
    
    # Affiche chaque tâche
    for task in sorted_tasks:
        # J'utilise le formatage de chaîne pour aligner les colonnes
        print(f"{task['id']:<5} {task['priority']:<10} {task['description']:<50}")

def update_task(tasks, task_id, new_description=None, new_priority=None):
    """
    Met à jour une tâche existante
    
    Args:
        tasks: Liste des tâches
        task_id: ID de la tâche à mettre à jour
        new_description: Nouvelle description (optionnel)
        new_priority: Nouvelle priorité (optionnel)
    
    Returns:
        Liste mise à jour des tâches
    """
    # Parcourt les tâches pour trouver celle avec l'ID correspondant
    for task in tasks:
        if task["id"] == task_id:
            # Met à jour la description si fournie
            if new_description is not None:
                task["description"] = new_description
            
            # Met à jour la priorité si fournie
            if new_priority is not None:
                task["priority"] = new_priority
            
            break
    
    return tasks

def delete_task(tasks, task_id):
    """
    Supprime une tâche de la liste
    
    Args:
        tasks: Liste des tâches
        task_id: ID de la tâche à supprimer
    
    Returns:
        Liste mise à jour des tâches (sans la tâche supprimée)
    """
    # Crée une nouvelle liste sans la tâche à supprimer
    # J'utilise une liste en compréhension pour filtrer
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    
    return updated_tasks
