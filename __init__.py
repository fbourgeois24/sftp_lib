import os

try:
	# On importe tout
	from sftp_lib.sftp_lib import sftp_client
except ModuleNotFoundError:
	# Si module non trouvé, on installe les dépendances
	os.popen(f"pip install --no-cache-dir -r {os.path.dirname(os.path.realpath(__file__))}/requirements.txt").read()
	from sftp_lib.sftp_lib import sftp_client