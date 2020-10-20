class Movies:
        # Assing values to age and ticketPrice variables
        age = 0
        ticketPrice = 10.00

        # Define function called getPrice and pass ticketPrice as an argument
        def getPrice(ticketPrice):

                # Ask the user for their age
                age = int(input('Please enter your age: '))

                # Return $0.00 as the ticket price for people under age of 5
                if age < 5:
                        print('Ticket Price is: $' + str(ticketPrice - ticketPrice))

                # Return Half ticket price for people between ages of 5 and 18        
                elif age > 5 and age < 18:
                        print('Ticket Price is: $' + str(ticketPrice // 2))

                # Return Full ticket price for people between ages of 18 and 55       
                elif age >= 18 and age <= 55:
                        print('Ticket Price is: $' + str(ticketPrice))
                        
                # Return $2.00 of the ticket price for people over age of 55       
                elif age > 55:
                        print('Ticket Price is: $' + str(ticketPrice - 2))

        # Call the function with ticketPrice as the positional argument               
        getPrice(ticketPrice)

