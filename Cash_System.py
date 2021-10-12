import random
import turtle
import func_module



def main():
    func_module.art_2()
    print("Life is a never ending state of constant suffering")

def cost(): #Function for cost
    x = float(input("Enter it's cost "))
    return x

allcost = 0
a = int(input("How many things are you buying? ")) #USED FOR THE LOOP
discount = random.choice([10, 20, 30])
print ("Our current discount is", discount, "%")
b = 0

for reciept in range(a): #For the receipt

    name_of_item = input("What is the item name? ")
    from_cost = cost() * 1.05

#randomization
    if discount == 10:
        discount = 0.10
        disccost = from_cost * discount
        print("You saved", disccost, "dollars")
    elif discount == 20:
        discount = 0.20
        disccost = from_cost * discount
        print("You saved", disccost, "dollars")
    elif discount == 30:
        discount = 0.30
        disccost = from_cost * discount
        print("You saved", disccost, "dollars")

    totalcost = from_cost - disccost
    print ("Item", name_of_item, "Cost", totalcost)
    allcost = totalcost + allcost
    print("All the items added up cost (ACCOUNTED FOR GST)", allcost, "currently.") #all the cost of the items added up
    b = b + 1
    if b == a:
        input("Thank you for shopping at H! ")
        main()







