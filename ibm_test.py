list1 = {}

class commodity:
    def __init__(self, _name, _price):
        self.name = _name
        self.price = _price
		
def introduce():
	print("\n    -----------------------ovo----------------------- \n")
	print("   ·add     输入商品的编号 名称 价格 。添加该商品。")
	print("   ·del     输入商品编号 。删除该商品")
	print("   ·calc    开始收银")
	print("   ·break   结束程序")
	print("\n    -----------------------ovo----------------------- \n")
	return

def add(_id, _name, _price):
	if _id in list1.keys():
		print("Please don't add the commodity again!")
	else:
		list1[_id] = commodity(_name, _price)
		print("You have added the commodity successfully!")
	return
def delete(_id):
	if _id in list1.keys():
		del list1[_id]
		print("You have deleted the commodity successfully!")
	else: print("Can't find the commodity!")
	return
def calc():
	print("   ·buy     输入所需商品编号 数量")
	print("   ·over    结账。结束本次收银。")
	sum = 0
	while(True):
		test = input().split()
		c = test[0]
		if (len(test) < 1): continue
		if(c == 'over'):
			print("The sum is: ", sum)
		else:
			_id = int(test[1]); _number = int(test[2]);
			if _id in list1.keys():
				sum = sum + list1[_id].price * _number
			else: print("Can't find the commodity!")
	return

def main():
	introduce()
	while(True): 
		test = input().split()
		if (len(test) < 1): continue
		c = test[0];
		if (c == 'break'): break
		if (c == 'add'): add(int(test[1]), test[2], int(test[3]))
		elif (c == 'del'): delete(int(test[1]))
		elif (c == 'calc'): calc()
		else: print("Your input is wrong!")

main()
