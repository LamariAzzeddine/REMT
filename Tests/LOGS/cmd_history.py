import paramiko
from transfert import Transfer
from fabric import Connection
import subprocess
import csv

def ssh_client_creation(host, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    return ssh_client



def test_cron(ssh_client, commands, password):
    results2 = []  # Liste pour stocker les résultats des commandes
    
    for command in commands:
        # Exécute la commande spécifiée sur le serveur distant sans sudo
        stdin, stdout, stderr = ssh_client.exec_command(command, get_pty=True)
        
        # Récupère le résultat de la commande
        result2 = stdout.read().decode().strip()
        
        # Vérifie s'il y a eu des erreurs
        error = stderr.read().decode().strip()
        if error:
            results2.append(error)
        else:
            # Stocke le résultat dans la liste des résultats
            results2.append(result2)
    
    return results2



if __name__ == "__main__":
    
    csv_file = "Tests/LOGS/users.csv"

    # Liste pour stocker les données lues depuis le fichier CSV
    data_from_csv = []

    # Lire les données depuis le fichier CSV
    with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                data_from_csv.append(row)

    # Vérifier si des données ont été lues depuis le fichier CSV
    if len(data_from_csv) > 1:  # Vérifier si des données autres que l'en-tête ont été lues
            host, port, username, password, hostname = data_from_csv[1]  # Récupérer les valeurs depuis la deuxième ligne (première ligne étant l'en-tête)
    
    # Connexion SSH
    ssh_client = ssh_client_creation(host, port, username, password)
    
    # Établir une connexion avec les informations fournies
    conn = Connection(host, user=username, port=port, connect_kwargs={"password": password})
    
    
    # Exécute le script Python config.py
    script_path = 'Tests/LOGS/config.py'
    subprocess.run(["python", script_path])
    
        
    commands9= [f'touch /home/{username}/Bureau/test.sh']
    # Exécution des commandes sans sudo 
    results9 = test_cron(ssh_client, commands9, password)
    print(results9)
    
    # Utiliser la méthode sudo() pour exécuter la commande avec les privilèges sudo,
    # en spécifiant le mot de passe
    result000 = conn.sudo('chmod a+w Bureau/test.sh && chmod +x Bureau/test.sh', password=password, warn=True)


    
    commands2 = [f"echo '#!/bin/bash' > /home/{username}/Bureau/test.sh"]

    # Exécution des commandes sans sudo 
    results2 = test_cron(ssh_client, commands2, password)
    print(results2)
    
    commands3 = [f"echo 'bash -i <<EOF' >> /home/{username}/Bureau/test.sh"]
    # Exécution des commandes sans sudo 
    results3 = test_cron(ssh_client, commands3, password)
    print(results3)
    
    commands4 = [f"echo 'HISTTIMEFORMAT=\"%F %T - \$USER - \" history > /home/{username}/Bureau/cmd_history.txt' >> /home/{username}/Bureau/test.sh"]

    # Exécution des commandes sans sudo 
    results4 = test_cron(ssh_client, commands4, password)
    print(results4)
    
    commands5 = [f"echo 'EOF' >> /home/{username}/Bureau/test.sh"]
    # Exécution des commandes sans sudo 
    results5 = test_cron(ssh_client, commands5, password)
    print(results5)
    
    commands6 = [f'./Bureau/test.sh']
    # Exécution des commandes sans sudo 
    results6 = test_cron(ssh_client, commands6, password)
    print(results6)

    # Création d'une instance de la classe Transfer
    transfer = Transfer()


    
    commands33 = ['hostname -f']
    # Exécution des commandes sans sudo 
    results33 = test_cron(ssh_client, commands33, password)
    # Récupérer le nom de la machine 
    machine_name = results33[0]

    # Chemin local où vous souhaitez télécharger le fichier
    localpath = rf'Tests/LOGS/var/logs/{machine_name}/journal/cmd_history.txt'
    

    # Chemin distant du fichier que vous souhaitez télécharger
    remotepath = f"/home/{username}/Bureau/cmd_history.txt"

    # Appel de la méthode GET pour télécharger le fichier
    result = transfer.GET(hostname, username, password, localpath, remotepath)

    # Affichage du résultat
    print(result)

    commands7 = [f'rm  Bureau/test.sh']
    # Exécution des commandes sans sudo 
    results7 = test_cron(ssh_client, commands7, password)
    print(results7)
    
    commands8= [f'rm Bureau/cmd_history.txt']
    # Exécution des commandes sans sudo 
    results8 = test_cron(ssh_client, commands8, password)
    print(results8)
    





