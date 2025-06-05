def items_purchased():
   
    shirt = 10
    pant = 15
    socks = 5
    Tax = 1.06

    total_cost_notax = shirt + pant + socks

    print(total_cost_notax)

    total_cost_withtax = total_cost_notax * Tax
    print(total_cost_withtax)

items_purchased()    