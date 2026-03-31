# HealthTech-Threat-Intel-Probe

HealthTech Threat Intel Probe (EBIOS RM)
Sonde Python connectée à l'API VirusTotal : De l'analyse de risques à la remédiation technique.

Ce dépôt ne contient pas seulement du code, mais la réponse technique à une analyse de risques formelle. Vous trouverez dans le dossier Livrable GRC l'étude EBIOS RM complète ayant motivé le développement de cet outil.

# Contexte du Projet (Gouvernance)
Ce projet a été réalisé dans le cadre d'une étude de risques (méthode EBIOS RM) pour une infrastructure de santé fictive. L'objectif stratégique était de réduire le risque résiduel face aux menaces de type :

Déploiement de Ransomware.

Compromission de la Supply Chain (Prestataires).

# Fonctionnalités Techniques
Ce script Python agit comme une sonde d'analyse OSINT et d'audit des flux :

Extraction automatisée : Identification des adresses IP et Domaines suspects dans les journaux (logs).

Threat Intelligence : Connexion à l'API REST de VirusTotal pour évaluer la réputation des indicateurs de compromission (IoC).

Reporting GRC : Génération d'un rapport de conformité et d'alerte au format CSV (encodage UTF-8-SIG, exploitable directement sur Excel pour les reportings de direction).

# Technologies & Stack
Langage : Python 3

API : REST (VirusTotal)

Domaines : OSINT / Threat Intelligence / Risk Management

# Instructions d'utilisation

1. Installation
Clonez ou téléchargez ce dépôt sur votre machine locale, puis ouvrez le dossier.

2. Configuration de l'API
Ouvrez le fichier threat_intel_probe.py avec votre éditeur de code.
Insérez votre clé API VirusTotal à l'endroit indiqué :

```Python
API_KEY = "CLE_API" ```

3. Exécution manuelle
Ouvrez un terminal dans le dossier du projet et lancez la commande :
```python threat_intel_probe.py```

# Déploiement Continu (Automatisation Windows)

Pour transformer ce script en véritable sonde de surveillance continue sans intervention humaine, vous pouvez utiliser le Planificateur de tâches Windows :

Ouvrez le Planificateur de tâches (via la barre de recherche Windows).

Cliquez sur Créer une tâche de base... et nommez-la Threat Intel Scanner.

Définissez le déclencheur (ex: Tous les jours à 08h00).

Dans l'onglet Action, choisissez Démarrer un programme.

Dans le champ Programme/script, tapez python.

Dans le champ Ajouter des arguments, tapez le nom du script : threat_intel_probe.py.

Dans le champ Commencer dans, collez le chemin d'accès complet du dossier contenant le script (ex: C:\Users\Valerian\Documents\Projet_Cyber).



