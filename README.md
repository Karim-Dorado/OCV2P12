# Développez une architecture back-end sécurisée en utilisant Django ORM

### Contexte
Epic Events est une entreprise de conseil et de gestion dans l'événementiel qui répond aux besoins des start-up voulant organiser des « fêtes épiques ».

### Détails du projet
L'objectif de ce projet est de créer un CRM avec une interface web et une API pour la société Epic Events:

L'API doit respecter les directives suivantes :
- Les utilisateurs doivent pouvoir créer un compte et se connecter.
- L'accès global à l'API requiert une authentification.
- Mise en place d'un système de filtres de recherche sur tous les endpoints de l'API.
- Utiliser une base de données PostgreSQL.
- Les membres de l'équipe de vente doivent pouvoir effectuer des opérations CRUD sur les clients et les contrats qui leurs sont attribués.
- Les membres de l'équipe de support ont un accès en lecture seule à tous les clients, contrats ou événements ainsi q'un droit de modification/d'accès pour tous les événements dont ils sont responsables.
- Les membres de l'éuipe de gestion ont un droit de modification/d'accès à tous les clients contrats et événements.

### Installation
1. Installer Python 3
2. Cloner le repository :
    / git clone https://github.com/Karim-Dorado/V2P10.git