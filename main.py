#!/usr/bin/env python3
# main.py - Point d'entrée pour mon gestionnaire de tâches en ligne de commande
# Créé pour mon usage personnel et pour ma candidature MLH

import os
import sys
from tasks import add_task, view_tasks, update_task, delete_task
from storage import load_tasks, save_tasks

def clear_screen():
    """Nettoie l'écran pour une meilleure lisibilité"""
    # J'ai trouvé cette astuce sur StackOverflow pour que ça marche sur Windows et Unix
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Affiche l'en-tête de mon application"""
    print("=" * 50)
    print("           MON GESTIONNAIRE DE TÂCHES")
    print("=" * 50)
    print("Développé par moi pour rester organisé(e) au quotidien")
    print("-" * 50)

def print_menu():
    """Affiche le menu principal avec les options disponibles"""
    print("\nQue voulez-vous faire?")
    print("1. Ajouter une tâche")
    print("2. Voir toutes les tâches")
    print("3. Mettre à jour une tâche")
    print("4. Supprimer une tâche")
    print("5. Quitter")
    return input("\nVotre choix (1-5): ")

def handle_add_task(tasks):
    """Gère l'ajout d'une nouvelle tâche"""
    clear_screen()
    print_header()
    print("\n--- AJOUTER UNE TÂCHE ---\n")
    
    # Demande la description
    description = input("Description de la tâche: ")
    if not description.strip():
        print("\nErreur: La description ne peut pas être vide!")
        input("\nAppuyez sur Entrée pour continuer...")
        return tasks
    
    # Demande la priorité
    print("\nPriorité:")
    print("1. Haute")
    print("2. Moyenne")
    print("3. Basse")
    priority_choice = input("\nChoisissez la priorité (1-3): ")
    
    # Conversion du choix en texte de priorité
    priority_map = {"1": "Haute", "2": "Moyenne", "3": "Basse"}
    if priority_choice not in priority_map:
        print("\nChoix invalide! La priorité sera définie comme 'Moyenne'.")
        priority = "Moyenne"
    else:
        priority = priority_map[priority_choice]
    
    # Ajoute la tâche et sauvegarde
    tasks = add_task(tasks, description, priority)
    save_tasks(tasks)
    
    print("\nTâche ajoutée avec succès!")
    input("\nAppuyez sur Entrée pour continuer...")
    return tasks

def handle_view_tasks(tasks):
    """Affiche toutes les tâches triées par priorité"""
    clear_screen()
    print_header()
    print("\n--- LISTE DES TÂCHES ---\n")
    
    if not tasks:
        print("Aucune tâche pour le moment. Ajoutez-en une!")
    else:
        view_tasks(tasks)
    
    input("\nAppuyez sur Entrée pour continuer...")
    return tasks

def handle_update_task(tasks):
    """Gère la mise à jour d'une tâche existante"""
    clear_screen()
    print_header()
    print("\n--- METTRE À JOUR UNE TÂCHE ---\n")
    
    if not tasks:
        print("Aucune tâche à mettre à jour!")
        input("\nAppuyez sur Entrée pour continuer...")
        return tasks
    
    # Affiche les tâches pour que l'utilisateur puisse choisir
    view_tasks(tasks)
    
    try:
        task_id = int(input("\nEntrez l'ID de la tâche à mettre à jour: "))
        
        # Vérifie si l'ID existe
        task_exists = False
        for task in tasks:
            if task["id"] == task_id:
                task_exists = True
                break
        
        if not task_exists:
            print(f"\nErreur: Aucune tâche avec l'ID {task_id}!")
            input("\nAppuyez sur Entrée pour continuer...")
            return tasks
        
        # Demande ce qu'il faut mettre à jour
        print("\nQue voulez-vous mettre à jour?")
        print("1. Description")
        print("2. Priorité")
        print("3. Les deux")
        update_choice = input("\nVotre choix (1-3): ")
        
        new_description = None
        new_priority = None
        
        # Mise à jour de la description
        if update_choice in ["1", "3"]:
            new_description = input("\nNouvelle description: ")
            if not new_description.strip():
                print("La description ne peut pas être vide! Mise à jour annulée.")
                input("\nAppuyez sur Entrée pour continuer...")
                return tasks
        
        # Mise à jour de la priorité
        if update_choice in ["2", "3"]:
            print("\nNouvelle priorité:")
            print("1. Haute")
            print("2. Moyenne")
            print("3. Basse")
            priority_choice = input("\nChoisissez la priorité (1-3): ")
            
            priority_map = {"1": "Haute", "2": "Moyenne", "3": "Basse"}
            if priority_choice not in priority_map:
                print("\nChoix invalide! La priorité ne sera pas modifiée.")
            else:
                new_priority = priority_map[priority_choice]
        
        # Mise à jour de la tâche et sauvegarde
        tasks = update_task(tasks, task_id, new_description, new_priority)
        save_tasks(tasks)
        
        print("\nTâche mise à jour avec succès!")
        
    except ValueError:
        print("\nErreur: Veuillez entrer un ID valide (nombre entier)!")
    
    input("\nAppuyez sur Entrée pour continuer...")
    return tasks

def handle_delete_task(tasks):
    """Gère la suppression d'une tâche"""
    clear_screen()
    print_header()
    print("\n--- SUPPRIMER UNE TÂCHE ---\n")
    
    if not tasks:
        print("Aucune tâche à supprimer!")
        input("\nAppuyez sur Entrée pour continuer...")
        return tasks
    
    # Affiche les tâches pour que l'utilisateur puisse choisir
    view_tasks(tasks)
    
    try:
        task_id = int(input("\nEntrez l'ID de la tâche à supprimer: "))
        
        # Vérifie si l'ID existe
        task_exists = False
        for task in tasks:
            if task["id"] == task_id:
                task_exists = True
                break
        
        if not task_exists:
            print(f"\nErreur: Aucune tâche avec l'ID {task_id}!")
            input("\nAppuyez sur Entrée pour continuer...")
            return tasks
        
        # Confirmation de suppression
        confirm = input(f"\nÊtes-vous sûr de vouloir supprimer la tâche {task_id}? (o/n): ")
        if confirm.lower() != 'o':
            print("\nSuppression annulée.")
            input("\nAppuyez sur Entrée pour continuer...")
            return tasks
        
        # Supprime la tâche et sauvegarde
        tasks = delete_task(tasks, task_id)
        save_tasks(tasks)
        
        print("\nTâche supprimée avec succès!")
        
    except ValueError:
        print("\nErreur: Veuillez entrer un ID valide (nombre entier)!")
    
    input("\nAppuyez sur Entrée pour continuer...")
    return tasks

def main():
    """Fonction principale qui gère la boucle du programme"""
    # Charge les tâches existantes
    tasks = load_tasks()
    
    while True:
        clear_screen()
        print_header()
        choice = print_menu()
        
        if choice == '1':
            tasks = handle_add_task(tasks)
        elif choice == '2':
            tasks = handle_view_tasks(tasks)
        elif choice == '3':
            tasks = handle_update_task(tasks)
        elif choice == '4':
            tasks = handle_delete_task(tasks)
        elif choice == '5':
            clear_screen()
            print("Merci d'avoir utilisé mon gestionnaire de tâches!")
            print("À bientôt!")
            sys.exit(0)
        else:
            print("\nChoix invalide! Veuillez réessayer.")
            input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
