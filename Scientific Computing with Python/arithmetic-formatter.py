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
                first_line += (f"  {first_number}    ")
                space = " " * (dashes - (len(second_number) + 1))
                second_line += (f"{operand}{space}{second_number}    ")
                third_line += (("-"*dashes) + '    ')
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
        arranged_problems = first_line +"\n" + second_line + "\n" + third_line + "\n" + fourth_line
    else:
        arranged_problems = first_line +"\n" + second_line + "\n" + third_line
    print(arranged_problems)

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])