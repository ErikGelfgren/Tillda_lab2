from arrayQFile import ArrayQ
from linkedQFile import LinkedQ
import sys

#Ordning som krävs för att det ska bli rätt är [7 1 12 2 8 3 11 4 9 5 13 6 10]

def ask_user():
#Ask user to select a specific order of cards 1-13
    ordning_kortlek=LinkedQ()
    
    indata = sys.stdin.readline()
    list=indata.split()

    for i in range(0,len(list)):
        ordning_kortlek.enqueue((list[i]))
    
    return ordning_kortlek

def wizard(ordning_kortlek):
#Method for compiling the order which the wizard will read the cards as    
    list=[]
    while ordning_kortlek.isEmpty()==False:

        card=ordning_kortlek.dequeue()

        ordning_kortlek.enqueue(card)

        card=ordning_kortlek.dequeue()

        list.append(card)
    list=' '.join(list)
    return list

def main():
    random_cardstack=ask_user()
    order=wizard(random_cardstack)
    print(order)

if __name__ == "__main__":
    main()
