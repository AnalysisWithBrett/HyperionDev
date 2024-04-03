# Creating a calculator for holiday
# Assuming you live in London, you will fly from Heathrow

# Asking your holiday destination
city_flight = input("""Where is your holiday destination? 
                    \n- Paris\n- Berlin\n- Rome\n - Barcelona\n - Athens\n - Lisbon\n - New York\n - Casablanca\n - Istanbul\n - Other
                    \n Type here: """)

# Prints out your destination within a friendly sentence
print(f'Great choice! You are flying to {city_flight}. \n ') # \n creates a blank line underneath this sentence to keep the output tidy


# Asking you how many nights you are staying at your destination
num_nights = int(input(f'How many nights are you staying at {city_flight}? '))

# Printing out your number of stays at your preferred destination
print(f'You are staying at {city_flight} for {str(num_nights)} nights. Great! \n ')


# Asking you to input how many days you want to use a car rental
rental_days = int(input(f'How many days do you want to use a rental car at {city_flight}? '))

# Printing out the number of days you will use the rental car
print(f'Great! You will use the rental car for {str(rental_days)} days in {city_flight}. \n ')


# Printing out the break down of the holiday cost
print("Here is the breakdown of your holiday cost:")

# Creating a function for plane cost. This includes using if/else statements depending on destination
def plane_cost(destination):
    if destination == "Paris":
        ticket = 24
    elif destination == "Berlin" or destination == "Rome" or destination == "Barcelona":
        ticket = 30
    elif destination == "Athens" or destination == "Lisbon":
        ticket = 37
    elif destination == "Istanbul" or destination == "Casablanca":
        ticket = 46
    elif destination == "New York":
        ticket = 270
    else:
        ticket = 300
    return ticket


# Printing out the plane ticket
print(f'The ticket to {city_flight} is worth £{plane_cost(city_flight)}.')



# Creating a function for days spent at hotel in your preferred destination
# The hotel cost depends on the destination as well
def hotel_cost(nights):
    if city_flight == "Paris" or city_flight == "New York":
        stay_cost = nights * 80
    elif city_flight == "Rome" or city_flight == "Barcelona" or city_flight == "Berlin":
        stay_cost = nights * 72
    elif city_flight == "Athens" or city_flight == "Lisbon" or city_flight == "Istanbul":
        stay_cost = nights * 46
    elif city_flight == "Casablanca":
        stay_cost = nights * 37
    else:
        stay_cost = nights * 28
    return stay_cost


# Printing out the total cost of hotel
print(f'For {str(num_nights)} nights at {city_flight}, the hotel cost is £{str(hotel_cost(num_nights))}.')



# Creating a function for days spent using a rental car in your preferred destination
# The car rental cost depends on the destination as well
def car_rental(days):
    if city_flight == "Paris" or city_flight == "New York":
        rental_cost = days * 20
    elif city_flight == "Rome" or city_flight == "Barcelona" or city_flight == "Berlin":
        rental_cost = days * 16
    elif city_flight == "Athens" or city_flight == "Lisbon" or city_flight == "Istanbul":
        rental_cost = days * 13
    elif city_flight == "Casablanca":
        rental_cost = days * 10
    else:
        rental_cost = days * 8
    return rental_cost

# Printing out the total cost of car rental
print(f'For {str(rental_days)} days at {city_flight}, the car rental cost is £{str(car_rental(rental_days))}.')



# Creating a function that calculates the total cost of holiday
def holiday_cost(plane, hotel, car):
    total_cost = plane_cost(plane) + hotel_cost(hotel) + car_rental(car)
    return total_cost

# Printing out the total cost of the holiday
print(f'The total cost of your holiday: £{holiday_cost(city_flight, num_nights, rental_days)}')
