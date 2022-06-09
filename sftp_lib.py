import paramiko

class sftp_client():
	def __init__(self, server_addr, username, key_file, key_type, key_passwd=None, host_verify=True):
		self.server_addr = server_addr
		self.username = username
		self.ssh = paramiko.SSHClient()

		# Si on ne vérifie pas l'hôte
		if not host_verify:
			self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		# Si clé de type ed25519
		if key_type == "ed25519":
			self.key = paramiko.Ed25519Key.from_private_key_file(key_file, password=key_passwd)
		elif key_type == "rsa":
			self.key = paramiko.RSAKey.from_private_key_file(key_file, password=key_passwd)
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
		""" Déconnexion du ssh """
		self.ssh.close()


	def open(self, auto_connect=True):
		""" Ouverture du sftp """
		self.auto_connect = auto_connect
		if auto_connect:
			self.connect()
		self.sftp = self.ssh.open_sftp()


	def close(self, auto_connect=True):
		""" Fermeture du sftp """
		self.sftp.close()
		if auto_connect:
			self.disconnect()


	def __enter__(self):
		# Ouverture avec WITH
		self.connect()
		self.open()
		return self.sftp

	def __exit__(self, *args, **kwargs):
		# Fermeture après WITH
		self.close()