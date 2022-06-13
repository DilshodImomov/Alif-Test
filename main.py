class Grocery():
	items = {}

	def __init__(self):
		self.read()

	def decode(self, item):
		item = item.split(' ')
		name = item[0]
		price = item[-1]
		if price[-1] == '\n':
			price = price[:-1]
		price = int(price)
		return name, price

	def read(self):
		filename, action = map(str, input().split(" "));
		file = open(filename, 'r', encoding = 'utf-8')
		for item in file:
			name, price = self.decode(item);
			self.items[name] = price
		file.close()
		print(self.items)

G = Grocery()