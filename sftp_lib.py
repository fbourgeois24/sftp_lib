import paramiko

class sftp_client():
	def __init__(self, server_addr, username, key_file, key_type, key_passwd=None, host_verify=True):
		self.server_addr = server_addr
		self.username = username
		# self.key_file = key_file
		# self.key_type = key_type
		# self.key_passwd = key_passwd
		self.ssh = paramiko.SSHClient()

		# Si on ne vérifie pas l'hôte
		if not host_verify:
			self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		# Si clé de type ed25519
		if key_type == "ed25519":
			self.key = paramiko.Ed25519Key.from_private_key_file(key_file, password=key_passwd)
		else:
			raise ValueError("Wrong key type")



	def connect(self, username=None, pkey=None):
		""" Connexion au serveur """
		# Si pas d'username ou de pkey définie on prend ceux définis à la création
		if username is None:
			username = self.username
		if pkey is None:
			pkey = self.key

		# Connexion au serveur en ssh
		self.ssh.connect(self.server_addr, username=username, pkey = pkey)

	def disconnect(self):
		# Déconnexion du serveur ssh
		self.ssh.disconnect()


	def open_sftp(self):
		""" Ouverture du sftp """
		self.sftp = self.ssh.open_sftp()


	def close_sftp(self):
		""" Fermeture du sftp """
		self.sftp.close_sftp()


	def __enter__(self):
		# Ouverture avec WITH
		self.connect()
		self.open_sftp()
		return self.sftp

	def __exit__(self):
		# Fermeture après WITH
		self.close_sftp()
		self.disconnect()