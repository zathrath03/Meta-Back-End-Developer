# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

def input_to_cents(dollars: str) -> int:
    return int(float(dollars) * 100)


# Modify the line below
coffee = input_to_cents(input('1 coffee @: $ '))
# Modify the line below
sandwich = input_to_cents(input('1 sandwich @: $ '))
# Modify the line below
cake = input_to_cents(input('1 cake @: $ '))

bill_total = coffee + sandwich + cake

print('Your total bill is $', bill_total/100, sep="")
