"""
------------------------------------------------------------------------
IP REPUTATION SCANNER - MODE AUTOMATISÉ (BATCH)
------------------------------------------------------------------------
Description : Lit une liste d'IPs depuis un fichier texte, analyse
              chaque IP via VirusTotal, et enregistre les menaces
              dans un fichier CSV d'audit.
------------------------------------------------------------------------
"""

import requests
import json
import csv
import time  # Pour mettre le script en pause
import os    # Pour vérifier si les fichiers existent
from datetime import datetime

# --- CONFIGURATION ---
API_KEY = "CLE_API" # remplacer ici par la clé API obtenu sur VirusTotal
BASE_URL = "https://www.virustotal.com/api/v3/ip_addresses/"
LOG_FILE = "investigation_logs.csv"
INPUT_FILE = "ips_suspectes.txt"  # Le fichier que le script va lire tout seul

def initialiser_log():
    """Crée le fichier CSV avec les colonnes s'il n'existe pas."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["Date_Heure", "IP_Analysee", "Score_Malveillant", "Pays", "Proprietaire", "Verdict"])

def sauvegarder_dans_csv(ip, score, pays, proprio, verdict):
    """Écrit une menace dans le journal."""
    date_actuelle = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([date_actuelle, ip, score, pays, proprio, verdict])

def analyser_ip(ip_cible):
    """Envoie la requête pour une seule IP et traite le résultat."""
    url_complete = BASE_URL + ip_cible
    headers = {"x-apikey": API_KEY}
    
    print(f"[*] Analyse de {ip_cible}...")
    
    try:
        reponse = requests.get(url_complete, headers=headers)
        if reponse.status_code == 200:
            data = reponse.json()
            attrs = data['data']['attributes']
            stats = attrs['last_analysis_stats']
            
            pays = attrs.get('country', 'Inconnu')
            proprio = attrs.get('as_owner', 'Non identifié')
            score_bad = stats['malicious']
            
            if score_bad > 0:
                print(f"   ⚠️  DANGER ({score_bad}/90) -> Enregistrement CSV")
                sauvegarder_dans_csv(ip_cible, score_bad, pays, proprio, "DANGER")
            else:
                print("   ✅ SAFE -> Pas d'enregistrement.")
        else:
            print(f"   [-] Erreur de l'API (Code {reponse.status_code})")
    except Exception as e:
        print(f"   [!] Erreur système : {e}")

def main():
    print(f"=== Début du Scan Automatique ({datetime.now().strftime('%H:%M:%S')}) ===")
    initialiser_log()

    # 1. Vérifier si le fichier avec les IPs existe
    if not os.path.exists(INPUT_FILE):
        print(f"[ERREUR] Le fichier '{INPUT_FILE}' est introuvable.")
        print("Veuillez créer ce fichier et y mettre une IP par ligne.")
        return

    # 2. Lire les IPs dans le fichier
    with open(INPUT_FILE, 'r') as f:
        liste_ips = [ligne.strip() for ligne in f if ligne.strip()]

    if len(liste_ips) == 0:
        print("[INFO] Aucune IP à scanner dans le fichier.")
        return

    print(f"[INFO] {len(liste_ips)} IP(s) chargée(s) pour l'analyse.\n")

    # 3. La boucle automatique
    for ip in liste_ips:
        analyser_ip(ip)
        
        # Pause obligatoire pour ne pas exploser le quota API VirusTotal (4/min)
        print("   ⏳ Pause de 15s...")
        time.sleep(15)
        
    print(f"\n=== Fin du Scan Automatique ===")

if __name__ == "__main__":
    main()