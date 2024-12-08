# EvaTech

## Description
EvaTech est une plateforme web développée avec Django permettant de créer, gérer et évaluer des tests en ligne. Elle est destinée aux enseignants qui souhaitent évaluer les compétences des étudiants en proposant des tests interactifs. Les étudiants peuvent s'inscrire, passer les tests et consulter leurs résultats.

---

## Fonctionnalités
### Utilisateur :
- **Enseignant (Teacher)** :
  - Créer un compte enseignant.
  - Créer des tests.
  - Ajouter des questions à un test.
  - Voir les soumissions des étudiants.

- **Étudiant (Student)** :
  - Créer un compte étudiant.
  - Passer les tests disponibles.
  - Consulter les résultats des tests.

### Administrateur :
- Gérer les enseignants, les étudiants, les tests et les questions via une interface d'administration intuitive.

---

## Prérequis
- Python 3.10 ou supérieur
- Django 5.1.4
- SQLite (par défaut, ou une autre base de données configurée)
- Environnement virtuel Python (`venv`)

---

## Installation

### Étape 1 : Cloner le projet
```bash
git clone <repository_url>
cd EvaTech
