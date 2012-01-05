import random
COLOURS = ['A', 'B', 'C', 'D']
WIDTH = 4

class Mastermind(object):
	def __init__(self):
		self.problem = [random.choice(COLOURS) for n in range(WIDTH)]
		self.score = [0]*WIDTH

	def check_answer(self):
		for i,x in enumerate(self.guess):
			if x == self.problem[i]:
				self.score[i] = 2
			elif x in self.problem:
				self.score[i] = 1
			else:
				self.score[i] = 0
	def print_score(self):
		print self.score

	def get_input(self):
		while True:
			print "Enter your guess: (up to %d letters of %s)" % (WIDTH, COLOURS)
			self.guess = raw_input().upper()
			if len(self.guess.strip()) == WIDTH:
				break

	def run(self):
		while True:
			self.get_input()
			print self.problem
			self.check_answer()
			self.print_score()
			if self.score == [2]*WIDTH:
				print "you are a mastermind"
				break


if __name__ == '__main__':
	game = Mastermind()
	game.run()
