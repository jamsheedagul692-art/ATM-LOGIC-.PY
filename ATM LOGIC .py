print("====🤠LANGUAGE🤠====")
print("1:","english")
print("2:","urdu")
print("3:","hinddi")
lan=input("chiose the language:")
if lan=="english":
	print("your chiose the english")
elif lan=="hinddi":
	print("your chiose the hinddi")
elif lan=="urdu":
	print("your language is urdu")
else:
	print("invalid language")
	exit()
transactions=["withdraw amount",]
deposit_transactions=["deposit amount"]
pin=int(input("enter the  pin :"))
balance=10000
if pin==12345:
	print("login secussfully 🤗🤗👍")
else:
	print("pin wrong stop 😧😧😂")
	exit()
print("\n😀😃😃welcome to this menu😀😃😃")
print("\n1.check balance")
print("2.withdraw money")
print("3.deposit money")
print("4.exit")
choice=input("enter your choice:")
if choice=="check balance":
	print("current balance:",balance)
elif choice=="withdraw money":
	amount=int(input("enter your amount:"))
	if amount>10000:
		print("not balance aviable")
		exit()
	else:
		print("invalid amount")
	z=balance-amount
	print("withdraw amount:",amount,"   new balance:",z)
	print("witdraw is secussfully")
	transactions.append(amount) 
elif choice=="deposit money":
	amount1=int(input("enter your amount:",))
	d=balance+amount1
	print("deposit amount:",amount1,"new balance:",d)
	deposit_transactions.append(amount1)
else:
	print("thank u visit for this atm system")
	






