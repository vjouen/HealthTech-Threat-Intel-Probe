#  AWS CSPM Auditor (Compliance as Code)

> **Outil d'audit automatisé de la posture de sécurité Cloud (AWS) et vérification de la conformité ISO 27001.**

##  Contexte du Projet (Gouvernance & ISO 27001)
Dans le cadre de la sécurisation des infrastructures Cloud, la rédaction de politiques de sécurité (PSSI) ne suffit pas ; il est crucial d'en vérifier l'application technique. 

Ce projet est un outil de **CSPM (Cloud Security Posture Management)**. Il permet de traduire les exigences de la norme **ISO 27001** en requêtes techniques automatisées afin d'identifier les écarts de conformité sur un environnement Amazon Web Services (AWS).

##  Périmètre d'Audit (Contrôles techniques)
Le script interroge l'API AWS pour vérifier les points de contrôle suivants :
* **Contrôle d'accès (ISO 27001 - Annexe A.9) :** Vérification de l'activation de l'authentification multifacteur (MFA) pour l'ensemble des utilisateurs IAM.
* **Sécurité des données (ISO 27001 - Annexe A.10 / RGPD) :** Détection des espaces de stockage (Buckets S3) exposés publiquement ("Block Public Access" manquant).
* **Reporting GRC :** Génération automatique d'un rapport CSV exploitable par les directions métiers, classant les actifs en statuts "CONFORME" ou "NON CONFORME" avec recommandations de remédiation.

##  Technologies & Stack
* **Langage :** Python 3
* **Bibliothèque Cloud :** `boto3` (AWS SDK for Python)
* **Services audités :** AWS IAM, AWS S3
* **Domaines :** Cloud Security / Compliance / Audit IT

---

##  Instructions d'utilisation

### 1. Prérequis et Sécurité
Ce script respecte le principe de moindre privilège. Il nécessite un compte AWS configuré avec des droits en **Lecture Seule** (politique `SecurityAudit`). Le script ne modifie en aucun cas l'infrastructure.

Assurez-vous d'avoir installé le SDK AWS pour Python :
```bash
pip install boto3 ```

2. Configuration des accès
Configurez vos identifiants AWS via l'interface en ligne de commande (CLI) :

```Bash
aws configure ```
(Fournissez votre Access Key et Secret Key associées au compte d'audit).

3. Exécution de l'audit
Lancez la sonde depuis votre terminal :

```Bash
python auditeur_cloud.py ```
4. Livrable
Le script générera un fichier nommé rapport_conformite_aws.csv dans le répertoire courant. Ce fichier utilise le séparateur point-virgule (;) et l'encodage UTF-8-SIG pour une intégration native et sans perte de données dans Microsoft Excel.
