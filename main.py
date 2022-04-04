print("Hiya!Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
tip = int(input("what percentage of tip would you like to give? 10,12 or 15 ?"))
people = int(input("How many people to split the bill with ?"))

bill_tip_result = tip/100 * bill + bill
split_total = bill_tip_result / people 
final_amount = round(split_total, 2)

print(f"Each person should pay: {final_amount}")