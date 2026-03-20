# HealthTech-Threat-Intel-Probe
Sonde Python connectée à l'API VirusTotal dans le cadre d'un scénario EBIOS RM

Sonde de détection Threat Intel (Scénario HealthTech)

Contexte du Projet

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

Comment l'utiliser :

Cloner le dépôt "Sonde python"

Insérer votre clé API VirusTotal dans le fichier AUTOMATIQUE.py.

Lancer le script Python.

Pour aller plus loin :
Le déclenchement sans intervention humaine (Windows)

Si tu es sous Windows, tu peux utiliser le Planificateur de tâches :

Appuie sur la touche Windows, tape Planificateur de tâches et ouvre-le.

Clique sur Créer une tâche de base.

Nomme-la "Threat Intel Scanner".

Choisis un déclencheur (ex: "Tous les jours" à "08:00").

Action : Démarrer un programme.

Dans "Programme/script", tape "python".

Dans "Ajouter des arguments", mets le nom de ton script : AUTOMATIQUE.py.

Dans "Commencer dans", mets le chemin du dossier où se trouve ton script

Ce dépôt ne contient pas seulement du code, mais la réponse technique à une analyse de risques formelle.
Vous trouverez dans le dossier "Livrable GRC" l'étude EBIOS RM complète

