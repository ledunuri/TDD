from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('what is your product: ')
    unit_price = Invoice().inputNumber("Please enter unit price: ")
    qnt = Invoice().inputNumber("Please enter quantity of product: ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")
    student=Invoice().inputAnswer("Student? (y,n) : ")
    print("Oh WOW!You are getting additional 5% discount Baby")
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break

total_amount = Invoice().totalPurePrice(products,student)

print("Your total pure price is: ", total_amount)
