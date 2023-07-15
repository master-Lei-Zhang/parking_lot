from datetime import datetime

def main():
    totLot = 100
    curCars = {}
    curTicket = 0
    while True:
        print('Welcome! Please choose an option\n' +
              '1: check-in\n' +
              '2: check-out')
        command = input('Enter a number:')
        
        if command == '1':
            # check if lots available
            if len(curCars) < totLot:
                # generate ticket number
                # record check-in time
                curCars[str(curTicket)] = datetime.now()
                print('\nPlease record your ticket number for later use.\n' + 
                      f'Ticket number: {curTicket}\n')
                curTicket += 1
            else:
                print('Lots full. Please check back later.\n')
        
        elif command == '2':
            # prompt for ticket number
            command_tn = input('Enter your ticket number:')
            # check if ticket number is valid
            # checkout ticket number if valid
            if command_tn in curCars.keys():
                parkTime = datetime.now() - curCars[command_tn]
                print(f'You have parked for {parkTime} hours.\n')
                curCars.pop(command_tn)
            # return to standby if invalid
            else:
                print('Invalid ticket number. Please start over.\n')
        
        else:
            print('Invalid operation. Please start over.\n')

if __name__ == '__main__':
    main()