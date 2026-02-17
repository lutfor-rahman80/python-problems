start_balance = 10000

balance = start_balance

while True:

    print("""
        Menu:
        1. Check Balance
        2. Withdraw
        3. Deposit
        4. Exit
        """)
    menu = int(input("Enter the number which you want to do: "))

    if menu==1:
        print("Your Current Balance is: ",balance)
        
    elif menu==2:
        withdraw=int(input("How Many Amount You Want To Withdraw: "))
        if balance>=withdraw:
            balance= balance - withdraw
            print(withdraw,"Withdraw is Successful.\n""Your New Balance is: ", balance)
            
        else:
            print("Insuficient balance.")
            
    elif menu==3:
        deposit= int(input("Enter How many amount you want to Deposit: "))
        balance = balance+deposit
        print(deposit,"Deposit is Successful.\n""Your New Balance is: ", balance)
        
    elif menu==4:
        print("Thank you for using ATM.")
        break
    else:
        print("You Enter wrong number. Please Enter the right number from the menu.")