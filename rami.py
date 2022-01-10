#Input

bill= float(input("enter the bill amount "))
num_f = int(input("Enter total friends excluding Leaane:"))
isExcellentService = bool(input("Was the service excellent? True or False"))

if (isExcellentService ==True):
    tip = bill * 0.2
else:
    tip = bill * 0.15

total_bill = bill + tip
split = total_bill/(num_f+1)

print("Initial Bill:",bill)
print("Total Bill including tip:",total_bill)
print("Was the service excelent or average?", isExcellentService)
print("Split Amount",split)
