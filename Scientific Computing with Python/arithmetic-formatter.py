def arithmetic_arranger(problems, result=None):
    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    answer = 0

    if len(problems) > 5:
        return "Error: Too many problems." # if number of problems are more than 5, it return an error
    else:
        for i in range(len(problems)):
            dashes = 0
            # checks for the errors mentioned in the description of the problem
            if len(problems[i].split()[0]) > 4:
                return "Error: Numbers cannot be more than four digits."
                break
            elif not problems[i].split()[0].isdigit():
                return "Error: Numbers must only contain digits."
                break
            else:
                first_number = f"{problems[i].split()[0]}"
            if "*" == problems[i].split()[1] or "/" == problems[i].split()[1]:
                return "Error: Operator must be '+' or '-'."
                break
            else:
                operand = f"{problems[i].split()[1]}"
            if len(problems[i].split()[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
                break
            elif not problems[i].split()[2].isdigit():
                return "Error: Numbers must only contain digits."
                break
            else:
                second_number = f"{problems[i].split()[2]}"
            
            # arranging problems as per required specifications
            if len(first_number) > len(second_number):
                dashes = len(first_number) + 2
                space = " " * (dashes - (len(second_number) + 1))
                first_line += (f"  {first_number}    ")
                second_line += (f"{operand}{space}{second_number}    ")
                third_line += (("-"*dashes) + '    ')
                # if result was set to 'True' the following code will calculate the answer
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
                # if result was set to 'True' the following code will calculate the answer
                if result == True and operand == "+":
                    answer = str(int(first_number) + int(second_number))
                elif result == True and operand == "-":
                    answer = str(int(first_number) - int(second_number))
                fourth_line += f"{answer:>{dashes}}    "

    # first and second line of the arranged problems.
    first_line = first_line.rstrip() + "\n"
    second_line = second_line.rstrip() + "\n"

    # if result was 'True' it will print an additional line of calculated answers
    if result == True:
        third_line = third_line.rstrip() + "\n"
        arranged_problems = first_line + second_line + third_line + fourth_line.rstrip()
        return arranged_problems
    else:
        arranged_problems = first_line + second_line + third_line.rstrip()
        return arranged_problems
