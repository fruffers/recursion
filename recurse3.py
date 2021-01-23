# double recurse
# draw a recurse tree/trace to understand

houses = ["house1","house2","house3","house4"]

def deliver_presents(houses):
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        deliver_presents(first_half)
        deliver_presents(second_half)

