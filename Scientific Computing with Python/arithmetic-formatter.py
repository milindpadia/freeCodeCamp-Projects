# def arithmetic_arranger(problems):
#     pass
#     #return arranged_problems

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

for i in range(len(problems)):
    dashes = 0
    first_number = f"{problems[i].split()[0]}"
    operand = f"{problems[i].split()[1]}"
    second_number = f"{problems[i].split()[2]}"
    if len(first_number) > len(second_number):
        dashes = len(first_number) + 2
        print(f"  {first_number}")
        space = " " * (dashes - (len(second_number) + 1))
        print(f"{operand}{space}{second_number}")
        print("-"*dashes)
    else:
        dashes = len(second_number) + 2
        print(f"{first_number:>{dashes}}")
        print(f"{operand} {second_number}")
        print("-"*dashes)