from multiprocessing.dummy import Array
from linkedQFile import LinkedQ

#Ordning som krävs för att det ska bli rätt är [7 1 12 2 8 3 11 4 9 5 13 6 10]

def ask_user():
#Ask user to select a specific order of cards 1-13
    kortlek=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    ordning_kortlek=LinkedQ()
    
    for i in range (0,len(kortlek)):

        print(kortlek)    

        kort=int(input("Select a card: "))  

        ordning_kortlek.enqueue(kort)

        kortlek.remove(kort)
    return ordning_kortlek

def wizard(ordning_kortlek):
#Method for compiling the order which the wizard will read the cards as    
    list=[]
    while ordning_kortlek.isEmpty()==False:

        card=ordning_kortlek.dequeue()

        ordning_kortlek.enqueue(card)

        card=ordning_kortlek.dequeue()

        list.append(card)
    return list

def main():
    random_cardstack=ask_user()
    order=wizard(random_cardstack)
    print(order)

if __name__ == "__main__":
    main()
