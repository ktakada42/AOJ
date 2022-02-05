class Dice():
	def __init__(self, ary):
		self.__top = ary[0]
		self.__front = ary[1]
		self.__right = ary[2]
		self.__left = ary[3]
		self.__back = ary[4]
		self.__bottom = ary[5]

	def turn_e(self):
		self.__top, self.__left, self.__bottom, self.__right = \
		self.__left, self.__bottom, self.__right, self.__top

	def turn_w(self):
		self.__top, self.__left, self.__bottom, self.__right = \
		self.__right, self.__top, self.__left, self.__bottom

	def turn_n(self):
		self.__top, self.__back, self.__bottom, self.__front = \
		self.__front, self.__top, self.__back, self.__bottom

	def turn_s(self):
		self.__top, self.__back, self.__bottom, self.__front = \
		self.__back, self.__bottom, self.__front, self.__top

	# def is_same_setting(self, ary):
	# 	if self.top == ary[0] and self.front == ary[1], self.right == ary[2] and \
	# 		self.left == arry[3] and self.back == ary[4] and self.bottom == ary[5]:
	# 		return True

	def show_top(self):
		return self.__top

number = list(map(int, input().split()))
turn = input()

dice = Dice(number)

for i in range(len(turn)):
	if turn[i] == 'E':
		dice.turn_e()
	if turn[i] == 'W':
		dice.turn_w()
	if turn[i] == 'N':
		dice.turn_n()
	if turn[i] == 'S':
		dice.turn_s()

print(dice.show_top())
