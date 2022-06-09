# SFTP lib
## Utilisation
Créer une instance de la classe

``` python
sftp = sftp_lib.sftp_client(server_addr, username, key_file, key_type, key_passwd=None, host_verify=True)
```

server_addr = adresse ip du serveur
username = nom d'utilisateur pour l'authentification
key_file = chemin vers le fichier de clé
key_type = type de clé
	Sont actuellement supportés
		- rsa
		- ed25519
key_passwd = mot de passe de la clé (None si aucun)
host_verify = vérification de l'hôte (utilisation du fichier .ssh/known_hosts) True ou False