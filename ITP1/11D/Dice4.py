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

	def is_same_setting(self, ary):
		if self.__top == ary[0] and self.__front == ary[1] and self.__right == ary[2] and \
			self.__left == ary[3] and self.__back == ary[4] and self.__bottom == ary[5]:
			return True

	def is_same_dice(self, ary):
		ret = 0
		for _ in range(2):
			for _ in range(3):
				for _ in range(4):
					if self.is_same_setting(ary):
						ret = 1
					self.spin_r()
				self.turn_n()
			self.spin_r()
			self.turn_s()
		return ret

n = int(input())
input_dice = [0] * n
same_flag = 0
for i in range(n):
	input_dice[i] = list(map(int, input().split()))
for i in range(n - 1):
	dicei = Dice(input_dice[i])
	for j in range(i + 1, n):
		ret = dicei.is_same_dice(input_dice[j])
		if ret == 1:
			same_flag = 1
			break
if same_flag == 1:
	print("No")
else:
	print("Yes")
