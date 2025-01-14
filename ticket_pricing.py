age = int(input("Please enter your age: "))

if age < 5:
    ticket_price = "Free"
elif 5 <= age <= 17:
    ticket_price = "$10"
elif 18 <= age <= 60:
    ticket_price = "$20"
else:
    ticket_price = "$15"

print(f"Your ticket price is: {ticket_price}")