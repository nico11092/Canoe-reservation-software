import sqlite3

class Database:
	def getConnexion(self):
		try:
			self.connection = sqlite3.connect("canoe.db")
		except ValueError:
			print("Erreur connextion base de données")

		return self.connection