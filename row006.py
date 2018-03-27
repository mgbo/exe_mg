
from card006 import Card006
from container import Container

class Row(Container):

	Max_LEN = 5
	def __init__(self):
		pass

	def put_katy(self, other_c):
		self.cards.append(other_c)

	def check(self):
		"""good row or not good True/False"""

	def cut(self):
		"""cut all cards except the last, return cutted cards or score of all cutted cards"""
		pass

	def need_cut(self):
		return len(self.row_kat) >= Row.Max_LEN


	def __str__(self):
		s =' '.join([str(n) for n in self.cards])
		return s

class Table(object):
	MAX_ROW = 4

	def __init__(self):
		#self.rows = [Row() for i in range (Table.MAX_ROW)]
		self.all_card = []
		self.rows = [Row(Table.row1), Row(Table.row2), Row(Table.row3), Row(Table.row4)]

	def find_row(self, card):
		"""Find appropriate row for the card or None if card is too small"""
		# a = filter rows
		# if a == [] return None 
		# min(a, key=)

	def drawCard(self, ind):
		ans = self.rows[ind]
		print (ans)
		#return self.rows[ind].pop()

	def __str__(self):
		return '\n'.join([str(r) for r in self.rows])


class Player(object):
	def __init__(self, name=''):
		self.name = name
		self.hand = Hand()

	def draw(self, table):
		self.hand.append(table.drawCard())
		#return self

	def discard(self):
		return self.hand.pop()

class GameCow006(Game):
	def __init__(self, player_list):
		deck = Card006.all_card(105)
		self.players = player_list
		self.table = Table()
		self.hidden_cards = []
		for p in self.players:
			p.

	def play(self):


def test_row():

	r1 = Row(Table.row1)

	r1.put_katy(Card006(3))
	r1.put_katy(Card006(12))
	r1.put_katy(Card006(104))
	print(r1)


	r2 = Row(Table.row2)
	r2.put_katy(Card006(55))
	r2.put_katy(Card006(37))

	print ('----------')

	t = Table()
	print (t)

if __name__ == '__main__':
	
	test_row()

	print ("---------")

	g = GameCow006([Player("alla"), Player("bob")])   # GameCow006.__init__
	g.play()





