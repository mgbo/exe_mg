
from card006 import Card006

class Row(Card006):
	Max_LEN = 5
	def __int__(self, row_kat=[]):
		self.row_kat = row_kat

	def __str__(self):
		return ' '.join(self.row_kat)

	def put_katy(self, other_card):
		self.row_kat.append(other_card)

	def check(self):
		"""good row or not good True/False"""

	def cut(self):
		"""cut all cards except the last, return cutted cards or score of all cutted cards"""

	def need_cut(self):
		return len(self.row_kat) == Row.Max_LEN


class Table(object):
	MAX_ROW = 4
	def __init__(self):
		self.rows = [Row() for i in range (MAX_ROW)]

	def find_row(self, card):
		"""Find appropriate row for the card or None if card is too small"""
		# a = filter rows
		# if a == [] return None 
		# min(a, key=)

	def __str__(self):
		return '\n'.join(self.rows)


def test_row():
	r1 = Row()
	#r1.put_katy(3)
	#r1.put_katy(Card006(3))
	#r1.put_katy(Card006(12))
	#r1.put_katy(Card006(35))

	print(r1)

	'''
	c1 = Card006(37)
	assert(r1.check(c1) == True)

	c2 = Card006(30)
	assert(r1.check(c2) == False)

	assert(r1.need_cut() == False)
	'''


if __name__ == '__main__':
	test_row()

