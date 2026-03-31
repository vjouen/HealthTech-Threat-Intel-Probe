"""
------------------------------------------------------------------------
AUDITEUR CLOUD AWS - COMPLIANCE AS CODE (CSPM)
------------------------------------------------------------------------
Description : Audite automatiquement la configuration de sécurité d'AWS
              (MFA des utilisateurs, Exposition des buckets S3) et 
              génère un rapport CSV de conformité.
------------------------------------------------------------------------
"""

import boto3
import csv
from datetime import datetime
import os

# Nom du rapport qui sera généré
FICHIER_RAPPORT = "rapport_conformite_aws.csv"

def auditer_mfa_utilisateurs(resultats_audit):
    print("\n[1/2] Audit des identités (IAM) : Vérification du MFA...")
    iam = boto3.client('iam')
    
    try:
        utilisateurs = iam.list_users()['Users']
        for user in utilisateurs:
            nom = user['UserName']
            # On demande à AWS si cet utilisateur a un MFA activé
            mfa = iam.list_mfa_devices(UserName=nom)['MFADevices']
            
            if len(mfa) > 0:
                statut = "CONFORME"
                reco = "N/A"
                print(f"  ✅ {nom} : MFA Activé")
            else:
                statut = "NON CONFORME"
                reco = "Activer immédiatement le MFA (ISO 27001 - A.9)"
                print(f"  ❌ {nom} : Aucun MFA !")
                
            # On ajoute le résultat dans notre tableau mémoire
            resultats_audit.append(["Contrôle d'accès IAM", f"Utilisateur: {nom}", statut, reco])
            
    except Exception as e:
        print(f"  ⚠️ Erreur lors de l'audit IAM : {e}")

def auditer_stockage_s3(resultats_audit):
    print("\n[2/2] Audit du stockage (S3) : Vérification de l'accès public...")
    s3 = boto3.client('s3')
    
    try:
        buckets = s3.list_buckets()['Buckets']
        if not buckets:
            print("  ℹ️ Aucun bucket de stockage trouvé sur ce compte.")
            return

        for bucket in buckets:
            nom_bucket = bucket['Name']
            try:
                # On vérifie la configuration de blocage public
                acces = s3.get_public_access_block(Bucket=nom_bucket)
                config = acces['PublicAccessBlockConfiguration']
                
                # Si toutes les sécurités publiques sont activées (bloquées)
                if config.get('BlockPublicAcls') and config.get('BlockPublicPolicy'):
                    statut = "CONFORME"
                    reco = "N/A"
                    print(f"  ✅ {nom_bucket} : Accès public bloqué")
                else:
                    statut = "NON CONFORME"
                    reco = "Activer 'Block All Public Access' (Fuite RGPD potentielle)"
                    print(f"  ❌ {nom_bucket} : Risque d'accès public !")
            
            except Exception:
                # Si la configuration n'existe pas, par défaut c'est un risque
                statut = "NON CONFORME"
                reco = "Activer 'Block All Public Access' (Configuration absente)"
                print(f"  ❌ {nom_bucket} : Configuration de sécurité absente !")

            resultats_audit.append(["Sécurité des Données S3", f"Bucket: {nom_bucket}", statut, reco])

    except Exception as e:
        print(f"  ⚠️ Erreur lors de l'audit S3 : {e}")

def generer_rapport(resultats):
    print("\n💾 Génération du rapport CSV...")
    entetes = ["Domaine_Audit", "Cible", "Statut_Conformite", "Recommandation"]
    
    # 1. utf-8-sig : dit à Excel "C'est de l'UTF-8 avec des accents"
    with open(FICHIER_RAPPORT, 'w', newline='', encoding='utf-8-sig') as f:
        
        writer = csv.writer(f, delimiter=';') 
        writer.writerow(entetes)
        writer.writerows(resultats)

    chemin_complet = os.path.abspath(FICHIER_RAPPORT)    
    print(f"🎉 Terminé ! Le rapport a été sauvegardé EXACTEMENT ici :\n➡️ {chemin_complet}\n")

def main():
    print(f"=== Début de l'Audit Cloud AWS ({datetime.now().strftime('%H:%M:%S')}) ===")
    
    # Liste qui va stocker tous nos résultats avant de les mettre dans le fichier
    resultats_audit = []
    
    # Lancement des contrôles
    auditer_mfa_utilisateurs(resultats_audit)
    auditer_stockage_s3(resultats_audit)
    
    # Création de la "preuve" d'audit
    generer_rapport(resultats_audit)

if __name__ == "__main__":
    main()