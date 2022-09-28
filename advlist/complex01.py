ii#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    #displaylist[1] which should only display arista_eos
    print(list1[1])

    # create a new list containing a single item
    list2 = ["juniper"]

    #extend list1 by list 2 (combine both list together into a single list)
    list1.extend(list2)

    #display list1, whichnow contains juniper
    print(list1)

    #create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

 i   #user the append operation to append list 1 by list3
    list1.append(list3)
i
    #display the new complex list1
    print(list1)

main()


##### NEED TO FINISHTO ADD TOGIT HUB###
