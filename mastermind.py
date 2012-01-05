import random
COLOURS = ['A', 'B', 'C', 'D']
WIDTH = 4

class Mastermind(object):
	def create_problem(self):
		random.shuffle(COLOURS)
	def check_answer(self):
		pass
	def print_board(self):
		pass
	def get_input(self):
		pass
	def run(self):
		pass	

if __name__ == '__main__':
	game = Mastermind()
	game.run()
