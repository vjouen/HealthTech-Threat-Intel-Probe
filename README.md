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

Cloner le dépôt.

Insérer votre clé API VirusTotal dans le fichier AUTOMATIQUE.py.

Dans le même dossier que le script Python, crée un nouveau fichier texte simple
Nomme-le : "ips_suspectes.txt"

Ajouter quelques IPs (une par ligne) pour tester, par exemple :

8.8.8.8

185.220.101.43

1.1.1.1

Lancer le script Python.

