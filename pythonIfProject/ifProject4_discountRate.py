shoppingAmount = int(input("Please enter your shopping amount (₺): "))
customerCard = str(input("Do you have customer card ?  YES / NO: "))

if shoppingAmount >= 500 and customerCard == "YES":
    print("%20 Discount")
elif shoppingAmount >= 500 and customerCard == "NO":
    print("%10 Discount")
elif shoppingAmount >=100 and shoppingAmount < 500 and customerCard == "YES":
    PRİNT("%20 Discount")
else:
    print("No Discount")

