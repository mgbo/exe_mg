
from card import Card
from container import Container

class Card006(Card):
	point = {1:1, 5:2,10:3, 11:5, 55:7}

	def __init__(self, chislo=0):
		self.chislo = Card006.get_chislo(chislo)
		self.all_card = []

    @staticmethod
    def all_cards():
    	return [Card006(x) for x in range(1, 105)].shuffle()
    	
	@staticmethod
	def get_chislo(chislo):
		if chislo in range(0,105):
			return chislo
		else:
			raise ValueError("Число Карты {} не должно превышать 104".format(chislo))

	def score(self):
		for n in sorted(Card006.point.keys(), reverse=True):
			if self.chislo % n == 0:
				return Card006.point[n]

	def __str__(self):
		return ('Число Карты : {} --> Очков : {} '.format(self.chislo,self.score()))

	def __gt__(self, other):
		return self.chislo>other.chislo

	def __lt__(self, other):
		return self.chislo<other.chislo



if __name__ == "__main__":
	c1 = Card006(15)
	print (c1)
	score_c1 = c1.score()
	#print (type(score_c1))

	c2 = Card006(55)
	print (c2)
	score_c2 = c2.score()

	c3 = Card006(22)
	print (c3)

	print (c1<c2)
	print (c1>c2)
	#assert (c1.score()==2),"Score больше два"




























