
def puzels():

    while True:
        list_1 = []
        x = int(input("Enter your Nomper  :"))
        for n in range(x):
            list_1.append(2**n)
            if sum(list_1) > x/2:
                list_1.append(x - sum(list_1))
                break
        list_1.reverse()
        list_1.sort(reverse=True)
        print(list_1)
        nom = len(list_1)
        print("nom of packets = {} packets".format(nom))
        y = int(input("pls enter wanted nom from ( 1 ) :( {} ) :" .format(x)))
        list_2 = []
        #   1st case when we need nom existed in our list  #
        if y in list_1:
            print(" yor nom already exist on list ", y)
            puzels()
            #   2nd  case when we need nom bigger than twic max of list  #
        if x >= y >= 2*max(list_1):
            list_2.append(list_1[0])
            list_2.append(list_1[1])
            if (list_1[2]) < (list_1[1]):
                list_2.append(list_1[2])
            if (list_1[3]) < (list_1[2]):
                list_2.append(list_1[3])

        def calculate():
            i = 0
            a = 0
            while y-(sum(list_2)) <= int(list_1[a]):
                list_2.append(list_1[a+i])
                if y-(sum(list_2)) == 0:
                    print(list_2)
                    nom = len(list_2)
                    print("nom of packets = {} packets".format(nom))
                    puzels()

                if y-(sum(list_2)) < 0:
                    list_2.remove(list_1[a+i])
                    i = i+1
                    if i >= len(list_1):
                        print(list_2)
                        nom = len(list_2)
                        print("nom of packets = {} packets".format(nom))
                        puzels()

        calculate()
        a = 0
        #   3rd case when we need nom in between max & 2 max  #
        if max(list_1) <= y <= 2*max(list_1):
            list_2.append(list_1[a])
            calculate()
        list_2 = []
        #   last case when we need nom in smaller than max of list #
        if y < max(list_1):
            calculate()


puzels()
