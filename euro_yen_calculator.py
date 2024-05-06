from import_exchange_rate import get_exchange_rate, link1


close = False

try:
    one_jpy_in_euro, rate_date = get_exchange_rate(link1)
    one_euro_in_jpy = 1 / one_jpy_in_euro

except:
    print("Could not gather the exchange-rate.")
    close = True
    input()


def jpy_to_euro(one_jpy_in_euro):  # function that turns the entered JPY-value into Euro
    calc_jpy = input("\nEnter the number of 'JPY' you want to convert to 'EURO':     ").replace(",",".")
    
    if calc_jpy == "m":
        menu = True
        negative_error = False
        number_error = False
        calc_jpy = "stop"
        return calc_jpy, negative_error, number_error, menu
    
    else:
        menu = False
        try:
            calc_jpy = float(calc_jpy)
            negative_error = False
            number_error = False

            if calc_jpy <= 0:
                negative_error = True
                number_error = False
                return calc_jpy, negative_error, number_error, menu

            else:
                result_euro = f"¥ {calc_jpy:.2f} JPY  ->  € {(calc_jpy * one_jpy_in_euro):.2f} EURO"
                return result_euro, negative_error, number_error, menu

        except:
            number_error = True
            negative_error = False

            return calc_jpy, negative_error, number_error, menu



def euro_to_jpy(one_euro_in_jpy):  # function that turns the entered EURO-value into Yen
    calc_euro = input("\nEnter the number of 'EURO' you want to convert to 'JPY':     ").replace(",",".")
    try:
        calc_euro = float(calc_euro)
        negative_error = False
        number_error = False

        if calc_euro <= 0:
            negative_error = True
            number_error = False
            return calc_euro, negative_error, number_error
        else:
            result_jpy = f"€ {calc_euro:.2f} EURO  ->  ¥ {(calc_euro * one_euro_in_jpy):.2f} JPY"
            return result_jpy, negative_error, number_error

    except:
        number_error = True
        negative_error = False

        return (calc_euro, negative_error, number_error)
    


def try_again ():  # function that lets the user decide what they want to do next
    repeat_input = input("\n\nDo you want to try again (y/n) or do you want to return to the menu (m)?  ")
    print("\n")
    if repeat_input == "y":
        close = False
        menu = False
    elif repeat_input == "n":
        close = True
        menu = False
    elif repeat_input == "m":
        close = False
        menu = True
    else:
        close, menu = try_again_invalid()

    return close, menu
        
  
def try_again_invalid():  # function that tells the user, their previous action was not correct
    
    close = False
    while close == False:
        eingabe = input("\nInvalid input, please press (y) to try again. Press (n) to close the program or press (m) to return to the menu!  ")
        print()
        if eingabe == "y":
            close = False
            menu = False
            return close, menu
        elif eingabe == "n":
            close = True
            menu = False
            return close, menu
        elif eingabe == "m":
            close = False
            menu = True
            return close, menu
        else:
            close = False
            menu = False


negative_error = False
number_error = False

while close != True:  # keeps the program running until the user decides otherwise
    choose_operation = input("Press (1) to convert JPY to EURO.\n\nPress (2) to convert EURO to JPY.\n\nPress (3) to view the current exchange rate.\n\nPress (4) to end this program.\n")
    menu = False
    add_list = []
    list_calc = []
    list_show = []

    while menu != True and close != True:  # execution and error handling of all the other actions

        if choose_operation == "1":
            result_euro, negative_error, number_error, menu = jpy_to_euro(one_jpy_in_euro)
            if not negative_error and not number_error and not menu:
                print(f"\n   ¥ 1 JPY   ->     {one_jpy_in_euro:.6f} EURO\n   € 1 EURO  ->   {one_euro_in_jpy:.6f} JPY \n\n-------------------------------------\n   {result_euro}\n-------------------------------------")
                close, menu = try_again()
        
            elif menu == True:
                break

            elif negative_error == True:
                    error = True
                    print("\nInput can't be a negative number!")
                    close, menu = try_again()

            elif number_error == True:
                    error = True
                    print("\nValue is not a valid number!")
                    close, menu = try_again()


        elif choose_operation =="2":
            result_jpy, negative_error, number_error = euro_to_jpy(one_euro_in_jpy)
            if not negative_error and not number_error:
                print(f"\n   € 1 EURO  ->   {one_euro_in_jpy:.6f} JPY \n   ¥ 1 JPY   ->     {one_jpy_in_euro:.6f} EURO\n\n-------------------------------------\n   {result_jpy} \n-------------------------------------\n")
                close = try_again()
        
            elif menu == True:
                break

            elif negative_error == True:
                    error = True
                    print("\nInput can't be a negative number!")
                    close, menu = try_again()

            elif number_error == True:
                    error = True
                    print("\nValue is not a valid number!")
                    close, menu = try_again()


        elif choose_operation == "3":
            print(f"\n--------------------------------------------------------------------------\nThe following exchange rates are the official up-to-date rates, \nas presented on the website of the European Central Bank (ECB).\n\n   ¥ 1 JPY   ->     {one_jpy_in_euro:.6f} EURO\n   € 1 EURO  ->   {one_euro_in_jpy:.6f} JPY \n\nThe latest date of an exchange rate update on the ECB website was:\n\n   {rate_date}\n--------------------------------------------------------------------------\n")
            input("Press Enter to continue.")
            break

        elif choose_operation == "4":
            close = True

        
        else:
            print("\nInvalid input.\n\n")
            break


