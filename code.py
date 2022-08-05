
x = 0
while x < 3:
	password = input("請輸入密碼: ")
	if password == "a123456":
		print("登入成功")
		break
	else:
		if  x == 0:
			print("密碼錯誤 你還有2次機會")
		elif x == 1:
			print("密碼錯誤 你還有1次機會")
		else:
			print("密碼錯誤 你沒機會了")
	x+=1


