
from Card006 import Card006

class Row(Card006):
	Max_LEN = 5
	def __int__(self, row_kat=[]):
		self.rkat = row_kat


	def put_katy(self, other):
		if len(self.row_kat) <= Row.Max_LEN:
			 self.ryad.append(other.chislo)

	def chack(self):
		pass