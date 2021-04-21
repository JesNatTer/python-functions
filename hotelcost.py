def hotel_cost(nights):
    return 140*nights  # hotel cost per day is R140


def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500  # ride to Cape Town is R2500
    elif city == "Durban":
        return 2300  # ride to Durban is R2300
    elif city == "JHB":
        return 2000  # ride to Johannesburg is R2000
    elif city == "BFN":
        return 1800  # ride to Bloemfontein is R1800
    else:
        return "Location unavailable."  # Only has options for Cape Town, Durban, JHB and BFN


def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        return cost - 50  # if car is rented for 7 or more days, R50 is removed from total cost
    elif 3 <= days < 7:
        return cost - 20  # if car is rented for 3 or more days (up till 6 days), R20 is removed from total cost
    else:
        return cost  # if car is rented for less than 3 days, no discount is given for total cost


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money  # total cost of trip


location = input("Where did you go: ")  # user inputs city
time = int(input("How many days were you there: "))  # user inputs days
extras = float(input("How much did you spend on extras: "))  # user inputs spending money

print(trip_cost(location, time, extras))
