# HealthTech-Threat-Intel-Probe
Sonde Python connectée à l'API VirusTotal dans le cadre d'un scénario EBIOS RM

Sonde de détection Threat Intel (Scénario HealthTech)

Ce dépôt ne contient pas seulement du code, mais la réponse technique à une analyse de risques formelle.
Vous trouverez dans le dossier "Livrable GRC" l'étude EBIOS RM complète



Contexte du Projet :

Ce projet a été réalisé dans le cadre d'une étude de risques (méthode EBIOS RM) pour une infrastructure de santé fictive. 
L'objectif était de réduire le risque résiduel face aux menaces de type Ransomware et compromission de la Supply Chain.



Fonctionnalités du script :

Ce script Python agit comme une sonde d'analyse :

Extraction automatique des adresses IP / Domaines suspects.

Connexion à l'API VirusTotal pour automatiser l'audit des flux sortants.

Génération d'un rapport de conformité/alerte.



Technologies utilisées :

Python 3

API REST (VirusTotal)

OSINT / Threat Intelligence



Instructions d'utilisation :

Téléchargez le dépôt nommé « Sonde python ».

Insérez votre clé API VirusTotal au sein du fichier threat_intel_probe.py.

Exécutez le script Python.

Fonctionnalités avancées : Automatisation de l'exécution (Windows)
Si vous évoluez dans un environnement Windows, vous avez la possibilité de recourir au Planificateur de tâches pour un déclenchement sans intervention humaine :

Appuyez sur la touche Windows, saisissez « Planificateur de tâches » dans la barre de recherche, puis ouvrez l'application.

Cliquez sur l'option « Créer une tâche de base... ».

Attribuez-lui l'intitulé « Threat Intel Scanner ».

Sélectionnez un déclencheur (par exemple : « Tous les jours » à 08h00).

À l'étape des actions, optez pour « Démarrer un programme ».

Dans le champ « Programme/script », saisissez la commande python.

Dans la section « Ajouter des arguments (facultatif) », renseignez le nom du script : threat_intel_probe.py.

Dans "Commencer dans", indiquez le chemin du dossier où se trouve le script



