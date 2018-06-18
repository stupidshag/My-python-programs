report_type = ""

while report_type.lower() == "":
    report_type = input('Choose Report Type ("A" or "T")')
    if report_type.lower() != 'a':
        if report_type.lower() != 't':
            print(report_type,"is invalid input")
            report_type = ""
        else:
            break
    else:
        break

def adding_report():

    integer = ""
    integerx = 0
    integery = ""

    while True:
        integer = input('Enter an integer or "Q":')
        if integer.isdigit():
            integerx = int(integer)+integerx
            integery = integery+integer + '\n'
        elif integer.lower() == 'q':
            break
        else:
            print (integer,"is invalid input")

    if report_type.lower() == 'a':
        print ("\nItems\n"+integery+"\nTotal\n"+str(integerx)+'\n')
    else:
        print("\nTotal\n"+str(integerx)+'\n')

adding_report()
