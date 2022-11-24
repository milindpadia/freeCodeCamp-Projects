def arithmetic_arranger(problems, result=None):
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    answer = 0

    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for i in range(len(problems)):
            dashes = 0
            first_number = f"{problems[i].split()[0]}"
            operand = f"{problems[i].split()[1]}"
            second_number = f"{problems[i].split()[2]}"
            
            if len(first_number) > len(second_number):
                dashes = len(first_number) + 2
                space = " " * (dashes - (len(second_number) + 1))
                if i == len(problems) - 1:
                    first_line += (f"  {first_number}\n")
                    second_line += (f"{operand}{space}{second_number}\n")
                    third_line += (("-"*dashes))
                else:
                    first_line += (f"  {first_number}    ")
                    second_line += (f"{operand}{space}{second_number}    ")
                    third_line += (("-"*dashes) + '    ')
                space = " " * (dashes - (len(second_number) + 1))
                if result == True and operand == "+":
                    answer = str(int(first_number) + int(second_number))
                elif result == True and operand == "-":
                    answer = str(int(first_number) - int(second_number))
                fourth_line += f"{answer:>{dashes}}    "

            else:
                dashes = len(second_number) + 2
                first_line += f"{first_number:>{dashes}}    "
                second_line += f"{operand} {second_number}    "
                third_line += (("-"*dashes) + '    ')
                if result == True and operand == "+":
                    answer = str(int(first_number) + int(second_number))
                elif result == True and operand == "-":
                    answer = str(int(first_number) - int(second_number))
                fourth_line += f"{answer:>{dashes}}    "
                
    if result == True:
        third_line += "\n"
        arranged_problems = first_line + second_line + third_line + fourth_line
        print(arranged_problems)
    else:
        arranged_problems = first_line + second_line + third_line
        first_line
        second_line
        third_line
        print(arranged_problems)

arithmetic_arranger(['3801 - 2', '123 + 49'])

