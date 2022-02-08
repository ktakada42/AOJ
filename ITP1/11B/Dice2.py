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

	def spin_r(self):
		self.__right, self.__front, self.__left, self.__back = \
		self.__back, self.__right, self.__front, self.__left

	def spin_l(self):
		self.__right, self.__front, self.__left, self.__back = \
		self.__front, self.__left, self.__back, self.__right

	def is_same_top_front(self, ary):
		if ary[0] == self.__top and ary[1] == self.__front:
			return True

	def top_front_right(self, ary):
		right = 0
		for _ in range(2):
			for _ in range(3):
				for _ in range(4):
					if self.is_same_top_front(ary):
						right = self.__right
					self.spin_r()
				self.turn_n()
			self.spin_r()
			self.turn_s()
		return right

number = list(map(int, input().split()))
q = int(input())

dice = Dice(number)

for i in range(q):
	top_and_front = list(map(int, input().split()))
	right = dice.top_front_right(top_and_front)
	print(right)
