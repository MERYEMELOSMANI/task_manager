# Task Manager CLI

Un simple gestionnaire de tâches en ligne de commande que j'ai créé pour rester organisé(e) au quotidien.

## Pourquoi j'ai créé ce projet

J'avais besoin d'un moyen rapide et efficace de gérer mes tâches quotidiennes directement depuis le terminal, sans avoir à ouvrir d'applications graphiques ou de navigateur. Ce projet me permet de:
- Noter rapidement des tâches à faire
- Les organiser par priorité
- Les consulter facilement
- Les mettre à jour ou les supprimer quand nécessaire

C'est un outil que j'utilise personnellement et qui m'aide à rester productif/productive.

## Installation

### Prérequis
- Python 3.x installé sur votre système

### Étapes d'installation
1. Clonez ce dépôt ou téléchargez les fichiers
2. Aucune dépendance externe n'est nécessaire, j'ai utilisé uniquement des bibliothèques standard de Python

## Utilisation

Pour lancer l'application:
```
python main.py
```

### Fonctionnalités
- **Ajouter une tâche**: Sélectionnez l'option 1, puis entrez la description et la priorité
- **Voir les tâches**: Sélectionnez l'option 2 pour afficher toutes vos tâches triées par priorité
- **Mettre à jour une tâche**: Sélectionnez l'option 3, choisissez l'ID de la tâche, puis modifiez sa description ou sa priorité
- **Supprimer une tâche**: Sélectionnez l'option 4, puis choisissez l'ID de la tâche à supprimer
- **Quitter**: Sélectionnez l'option 5 pour quitter l'application

### Exemple d'utilisation
1. Lancez l'application
2. Sélectionnez "1" pour ajouter une tâche
3. Entrez "Finir le rapport de projet" comme description
4. Sélectionnez "1" pour une priorité Haute
5. Sélectionnez "2" pour voir votre nouvelle tâche dans la liste

## Structure du projet

J'ai organisé le code en trois fichiers principaux pour le rendre plus modulaire:
- `main.py`: Gère l'interface utilisateur et les interactions
- `tasks.py`: Contient la logique de gestion des tâches (ajout, affichage, mise à jour, suppression)
- `storage.py`: S'occupe de la persistance des données via JSON

## Améliorations futures

Quelques idées que j'aimerais implémenter quand j'aurai plus de temps:
- Ajouter des dates d'échéance aux tâches
- Implémenter des catégories/tags pour mieux organiser les tâches
- Ajouter des notifications pour les tâches urgentes
- Créer une interface web simple

N'hésitez pas à utiliser ce code, à le modifier selon vos besoins ou à proposer des améliorations!
