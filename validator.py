'''
Credit card numbers follow certain patterns: It must have between 13 and 16 digits, 
and the number must start with:
■ 4 for Visa cards
■ 5 for MasterCard credit cards
■ 37, 34 for American Express cards

In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. The
algorithm is useful to determine whether a card number is entered correctly or whether
a credit card is scanned correctly by a scanner. The validation steps are as the following:
1. Double every second digit from right to left. If doubling of a digit results in a
two digit number, add up the two digits to get a single-digit number. 
2. Add the original numbers and the odd position new numbers together.
5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is
invalid
'''
def double(account):
    new = []
    for i in range(1, len(account)+1):
        if i % 2 == 0:
            doubled = (int(account[-i])) * 2
            if doubled >= 10:
                doubled_s = str(doubled)
                doubled = int(doubled_s[0]) + int(doubled_s[1])
            new.append(doubled)
        else:
            new.append(int(account[-i]))
    return new

def sum_all(digits: list):
    sum = 0
    for i in digits:
        sum += i
    return sum

if __name__ == "__main__":
    account = str(input("Please enter your credit card number:"))
    mastercard = ["51", "52", "53", "54", "55"]
    if account[0] == "4":
        card_type = "Visa Card"
    elif account[:1] in mastercard:
        card_type = "MasterCard Credit Cards"
    elif account[:1] == "37" or account[:1] == "34":
        card_type = "American Express Cards"
    else:
        card_type = "invalid"
        print("The card format is invalid.")
        quit()
    
    doubled = double(account)
    sum_step_2 = sum_all(doubled)
    if sum_step_2 % 10 == 0:
        print(f"The card number is a valid {card_type} number")
    else:
        print(f"The card number is a invalid {card_type} number")