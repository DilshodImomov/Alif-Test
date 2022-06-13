class Grocery():
	items = {}
	Total = 0

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

	def encode(self, filename):
		file = open(filename, 'w', encoding = 'utf-8')
		for item in self.items:
			file.write(item + " - " + str(self.items[item]) + '\n')
		file.close()

	def read(self):
		filename, action = map(str, input().split(" "));
		file = open(filename, 'r', encoding = 'utf-8')
		for item in file:
			name, price = self.decode(item);
			self.items[name] = price
			self.Total += price
		file.close()

		if action == "Add":
			self.Add()
		elif action == "Change":
			self.Change()
		elif action == "Delete":
			self.Delete()
		elif action == "Sum":
			self.Sum()

		self.encode(filename)

	def Add(self):
		item = input()
		name, price = self.decode(item)
		self.items[name] = price
		self.Total += price;

	def Change(self):
		item = input()
		name, price = self.decode(item)
		self.Total -= self.items[name]
		self.items[name] = price
		self.Total += price

	def Delete(self):
		name = input()
		self.Total -= self.items[name]
		del self.items[name]

	def Sum(self):
		print(self.Total)

G = Grocery()