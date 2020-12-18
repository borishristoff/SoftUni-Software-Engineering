budget = float(input())
flour_price = float(input())

pack_of_eggs = 0.75 * flour_price

price_of_milk = 1.25 * flour_price

price_of_milk_per_cozonac = 0.25 * price_of_milk

total_cozonac_cost = flour_price + pack_of_eggs + price_of_milk_per_cozonac

 budget -= total_cozonac_cost

 if budget > 0:
    cozonac_counter += 1
    egss_counter += 3