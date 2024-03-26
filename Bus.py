#python has preinstalled libraries but you have to import them to be able to use them
from time import sleep
from random import randint
import numpy as np

class Passenger:

    def __init__(self, passenger_id, name, last_name, age, gender, seat):
        self.id = passenger_id
        self.name = name
        self.last_name = last_name
        self.seat = seat
        self.ticket = False

        if gender.upper() != 'F' and gender.upper() != 'M': # Before assigning gender we check if it's F or M
            self.gender = None # If not gender is None
            print("\n\n[!][!] Gender must be either F - Female or M - Male...Setting default value to - None[!][!]\n** You may change this value in the card configurations **\n\n")
            sleep(2)#creates a delay in the code so everything doesnt print out at once it looks prettier,you gotta import it from time
        else:
            self.gender = gender.upper()#If yes then we add gender.upper() it gets addes as upper case

        try:#incase it breaks while converting try will save it
            self.age = int(age)
        except: # if the exception is thrown then we set age to 1 (default value)
            self.age = 1
            print("\n\n[!][!] Age must not containt characters, setting default value to - 1[!][!]\n** You may change this value in the card configurations **\n\n")
            sleep(2) 

    def __str__(self):#magic method: when u create an object it will show u the address of the memory 
        return f'--- Passenger Card ---\n| ID: {self.id}\n| Name: {self.name + " " + self.last_name}\n| Age: {self.age}\n| Gender: {self.gender}\n| Ticket Poked: {self.ticket}\n{"-"*22}'

    def talk(self):

        sentence_picker = randint(0,5) # generate random number from 0 to 5
        quotes = [] # initialize quotes so we can access it outside "if"

        if self.age >= 15: # Create quotes for 15+ years old
            quotes = ["Quite a warm day today! I wonder how I can open this window", "Please stop poking me...", "Hey! How can I help you?", "*i'm on the phone here, just a moment...*", "zzzZZZzzz😴😴😴"]
        else: # Create quotes for 15- years old
            quotes = ["Sir have you seen my train?", "I like your watch 😊 reminds me of my dad's", "What is your name sir?", "Poke me again I will tell dad...", "Wanna play a game?!", "*Pew Pew*🎮👾"]
        
        sentence_picked = quotes[sentence_picker] # pick sentence

        if not self.ticket: # Check if ticket has been poked
            self.ticket = True # If not then poke it
            print("""
                ##############
                #Ticket Poked#
                ##############
            """)

        # Display quote from the passenger
        print(f"""
        ----------------------------------------------------
        {self.name + " " + self.last_name}: {sentence_picked}
        ----------------------------------------------------
        """)

        sleep(2)

class Bus:

    def __init__(self):
        self.max_passengers = 20
        self.passengers = []
        self.passenger_count = 0
        #shape the array to 2D because i need a line for each passenger side by side
        self.bus_seats = np.empty((self.max_passengers, 2), dtype=str)
        #itirates through each seat to change the first seat with empty spaces
        # :: <-- will go from position 0 to the last position 
        self.bus_seats[::] = " "

        self.passenger_ages = np.array([], dtype=int)


    def menu(self):
        print(f"""
        Menu:

        1 - Add a new passenger
        2 - See all passengers
        3 - Change passenger card
        4 - Total age of passengers
        5 - Average age
        6 - Check oldest passenger
        7 - Filter passengers per age
        8 - Sort passengers
        9 - Poke a passenger
        10 - Print M/F positions
        11 - Make a passenger get off
              
              ---------------
        
        0 - Quit
        """)

    # seat = None in case the passenger doesn't have a seat yet
    # When we push the passengers 1 position we have to reassign the whole array
    def add_passenger_to_seat(self, gender, seat = None): 
        if seat:# (if seat is not none)if seat exists then it is same as saying if seat then true
            row = seat[0] # the row is the first position of the seat (seat is an array)
            chair = seat[1] # the chair is the second position of the seat (seat is an array)
            self.bus_seats[row, chair] = gender.upper() #reasign same person to the same seat
            return #return to previous function
        else:
            for i, row in enumerate(self.bus_seats): # returns the value(row) and the index(i) of the bus seat
                for j, seat in enumerate(row): # returns the value(seat) and the index(j) of each row
                    if seat == " ": # Check if the seat is free
                        if gender:
                            self.bus_seats[i, j] = gender # Assignes passenger gender to seat
                        else:
                            self.bus_seats[i, j] = 'N' # Assignes 'N' if the gender is None
                        return i, j # returns index chair(i) seat and index of row(j)
        
            

    def add_passenger(self):

        if self.max_passengers == self.passenger_count:
            message = "Bus is full! Remove a passengers before you can add new ones!"
            print("#" * (len(message) + 2))#print # times the lenght of the message so it has the exact amount of #
            print(f"#{message}#")
            print("#" * (len(message) + 2))
            return#then it returns to previous function which is menu/while loop

        # Make Passenger Card
        print("\n### Create a new passenger ### \n")

        
        first_name = str(input('Name: '))
        last_name = str(input('Last Name: '))
        age = str(input('Age: '))
        gender = str(input('Gender [ M/F ]: '))
        

        #call add_passenger_to_seat function and save the returned results (row and seat)
        row, seat = self.add_passenger_to_seat(gender.upper()) # calls function add_passenger_to_seat and receives 2 values returned from it
                                                               # row and seat

        # Create instance from class Passenger
        new_passenger = Passenger(name=first_name, last_name=last_name, age=age, gender=gender, passenger_id=self.passenger_count + 1, seat=[row, seat])

        self.passengers.append(new_passenger)
        self.passenger_count += 1
        self.passenger_ages = np.append(self.passenger_ages, int(new_passenger.age))

        success_message = f"Passenger: {new_passenger.name} as been added!"
        
        print("#" * len(success_message))
        print(f"Passenger: {new_passenger.name} as been added!")
        print("#" * len(success_message))
        print(f"\n\n{new_passenger}\n")


        choice = str(input("Would you like to add another passanger (n/Y): "))
        if choice.lower() == 'y':
            self.add_passenger() # call function add_passenger()
        else:
            return # if we don't want to add other passengers we return to the previous function

    def print_bus(self):
        # If there's no passangers it throws an error
        if self.passenger_count <= 0:
            print("\n")
            message = "# No passengers added yet! #"
            print("#" * len(message))
            print(message)
            print("#" * len(message))
            print("\n")
            return False

        print("\n\n### Passengers ###")
        print("-" * 15)
        for passenger in self.passengers: # iterates through each existing passenger
            print(f"ID: {passenger.id}")
            print(f"Name: {passenger.name + ' ' + passenger.last_name}")
            print(f"Age: {str(passenger.age)}")
            print(f"Gender: {passenger.gender}")
            print(f"Ticket Poked: {passenger.ticket}")
            print("- " * 10)
        return True

    def edit_passenger_card_menu(self, passenger_index): # Receives passenger_index from the self.passengers var
        while True:
            passenger = self.passengers[passenger_index] # Gets the passengers object
            message = f"### Passenger {passenger.id} selected ! ###"
            print("\n")
            print("#" * len(message))
            print(f"{message}")
            print("#" * len(message))
            print("\n")
            print("- What changes would you like to make:\n")
            print(f"1 - Name = {passenger.name}")
            print(f"2 - Last name = {passenger.last_name}")
            print(f"3 - Age = {passenger.age}")
            print(f"4 - Gender = {passenger.gender}")
            print(f"0 - Exit")
            change = str(input(": "))

            if change == '1':
                new_value = str(input('New name: ')) # get new name
                if any(char.isdigit() for char in new_value): # if any of the characters in new name is a digit throw an error
                    print("\n\n[!][!]Name must not contain numbers...[!][!]\n\n")
                    sleep(2)
                else:
                    passenger.name = new_value # add new name
                    print("\n[+][+]Name has been changed![+][+]")

            elif change == '2':
                new_value = str(input('New last name: '))
                if any(char.isdigit() for char in new_value): # if any of the characters in new last name is a digit throw an error
                    print("\n\n[!][!]Last name must not contain numbers...[!][!]\n\n")
                    sleep(2)
                else:
                    passenger.last_name = new_value # add new last name
                    print("\n[+][+]Last name has been changed![+][+]")

            elif change == '3':
                try:
                    new_value = int(input('New age: ')) # try to convert to int
                    #recycle old age in vector

                    #find an index of a number that is equal to the age, [0] <-- because it returns a tuple
                    age_index = np.where(self.passenger_ages == passenger.age)[0]

                    self.passenger_ages = np.delete(self.passenger_ages, age_index[0])  # remove old age from vector

                    self.passenger_ages = np.append(self.passenger_ages, new_value)  # add new age to vector

                    
                    passenger.age = new_value # add new age to passenger
                    
                    print("\n[+][+]Age has been changed![+][+]")
                except: # if it can't convert it means it wasn't a full number
                    print("\n\n[!][!]Age must be a number...[!][!\n")

            elif change == '4':
                new_value = str(input('New gender: '))
                if new_value.upper() != 'F' and new_value.upper() != 'M': # check if new gender is F or M
                    print("\n\n[!][!]Value must be F - Feminine or M - Masculine[!][!]\n") # if not throws this error
                else:
                    passenger.gender = new_value.upper() # add new gender 
                    self.add_passenger_to_seat(passenger.gender.upper(), passenger.seat) # add passenger to new seat, pass as arguments gender and current seat
                    print("\n[+][+]Gender has been changed![+][+]")

            elif change == '0':
                break # if the choice is 0 then exit
            else:
                print("\n\n[-][-]Invalid choice...[-][-]\n\n")

            choice = str(input("\nWould you like to make more changes [ N/y ]: "))
            if choice.upper() != 'Y':
                break # If the choice is differente from Y then exit

    def edit_passenger_card(self):

        while True:
            ID_FOUND = False # Set ID_FOUND to false

            if self.print_bus() == 0: # if the print_bus function returns False it means there's no passenger, therefore we can just exit
                break
            
            # if there are passengers the code won't break and we add "0 - Exit" as an option to the output of print_bus()
            print("0 - Exit")

            try:
                choice = input("\nWhich passenger would you like to edit (select by ID): ")
                if choice == "": # If the choice is blank throw error
                    print("\n\n[-][-]Invalid selection.[-][-]\n- Please enter a number or '0' to exit. -\n\n")
                    sleep(2)
                    continue # since this is a while True loop we can just continue and the code will go to the beggining of the function

                choice = int(choice) # try to convert choice to number

                if choice == 0:
                    break   

            except: # if we can't convert the choice to an integer than it's not a valid ID and we throw an error
                print("\n\n[-][-]Invalid selection.[-][-]\n- Please enter a number or '0' to exit. -\n\n")
                sleep(2)
                continue

            for passenger in self.passengers: #iterate through each passenger
                if passenger.id == choice: #if the id matches the choice
                    ID_FOUND = True # set ID_FOUND to true
                    self.edit_passenger_card_menu(self.passengers.index(passenger)) # call edit_passenger_card_menu and pass passenger index as argument

            if choice == 0 and not ID_FOUND: # if choice is 0 and ID_FOUND is falsew we break the while true loop
                break
            elif not ID_FOUND:  # if ID_FOUND is false but the user selects another ID we throw another error
                print("\n\n[-][-]No card found with that ID...[-][-]\n\n")
                sleep(2)
                continue

    def calc_total_age(self):

        # use np to find the total age with np.sum
        
        print(f"""

        The total age is : {np.sum(self.passenger_ages)}

        """)

    def calc_average_age(self):

        # use np to calculate average and np.round to round the value
        print(f"""

        The average age is : {np.round(np.average(self.passenger_ages))}

        """)
        pass

    def max_age(self):
        
        # use np to find the max age with np.max
        print(f"""

        The oldest passenger's age is : {np.max(self.passenger_ages)}

        """)

    def find_age(self):
        if self.passenger_count == 0:
            print("\n\n[-][-] No passengers have been added yet. [-][-]\n")
            return

        try:
            print("### Filter by Age ###")
            initial_age = int(input("Initial age: ")) # try to convert input to int

            final_age_input = int(input("End age (leave blank if you only want to get the passengers with the initial age): ")) # try to convert final age to int

            # this checkes if the user put a final age or not, so we know if we should return the users that match the age in between
            if final_age_input:
                final_age = int(final_age_input)
            else:
                final_age = initial_age

            for passenger in self.passengers:
                if initial_age <= passenger.age <= final_age: # if intial_age is smaller or equal to passenger age, and if passenger age is smaller of equal to final_age
                    print(f"\t{passenger}")                   # print the passengers that match this
        except:
            print("\n\n[!][!] Age must be a number [!][!]\n")

    def sort_bus(self):

        if self.passenger_count == 0: # if there's no passengers than no need to sort
            print("\n\n[-][-] No passengers have been added yet. [-][-]\n")
            return

        # Bubble Sort
        for _ in range(len(self.passengers)):
            for j in range(len(self.passengers) - 1):
                if self.passengers[j].age < self.passengers[j + 1].age:
                    temp = self.passengers[j]
                    self.passengers[j] = self.passengers[j + 1]
                    self.passengers[j + 1] = temp
                    print(self.passengers[j])
        # end of bubble sort

        print("""
              
              #########################
              ### Passengers sorted ###
              #########################
              
              """)
        
        self.print_bus() # Print the users sorted

    def print_sex(self):

        for passenger in self.passengers:
            if passenger.gender == None: #if a passenger has a gender set as None than the bus view gets locked
                print("""
                    ######################################
                      A passenger has a None type gender.
            Make sure you correct this before you try to access this view.
                    ######################################
                      """)
                return

        # Styling of the bus
        print("\t  ## Bus seats ##\n\n")
        print("\t      _________")
        print("\t     /         \\")
        print("\t     ----------- ")
        for sit in self.bus_seats:# prints each seat in the array bus_seats
            print("\t    | ", end="")
            print(sit, end="")
            print(" |")


        print("\t     -___---___-\n\n")


        print(f"\t# Total seats used: {self.passenger_count}")
        

    def poke(self):

        is_not_empty = self.print_bus() #gets return value from print_bus()

        if is_not_empty: # if there are passengers

            passenger = str(input("Select a passenger: "))
            for p in self.passengers: 
                if p.id == int(passenger): #if the passenger ID is equal to the choice of the user
                    p.talk() # we call talk function from the Passenger class
        else:
            return # else we return to the previous function

    def getting_off(self):

        self.print_bus() # print entire bus

        message = "Select a passenger to get off: "
        print("\n")
        print("#" * len(message))
        passenger_id = str(input(message)) #get passenger ID from user
        print("#" * len(message))

        for passenger in self.passengers:   #iterate through each passenger
            if passenger.id == int(passenger_id):   #check if passenger ID is the same as the user input
                self.passengers.remove(passenger)   #remove passenger from array
                self.passenger_count = len(self.passengers) #change passenger count to the lenght of the passenger array (all passengers)
                
                self.bus_seats = np.empty((self.max_passengers, 2), dtype=str) # create new bus with np.empty
                self.bus_seats[::] = " "    # set all seats to " "
                for passenger in self.passengers:   # iterate through each passenger
                    self.add_passenger_to_seat(passenger.gender)    # call add_passenger_to_seat so we add each passenger again 1 seat ahead
                                                                    # note we only use gender because we want to reassign seats, not keep the passengers in place
                print("### Passenger Removed ###")
                return  # return to previous function
            
        print("No passenger with that ID...")
        return # return to previous function

if __name__ == "__main__":
    #create instance from class Bus
    bus = Bus()

    message = "Welcome to Bus Simulator"
    m = "\t"
    print("\n")
    for i in message:# iterates through the message
        m += i  #appends each character to the variable (each one at the time) 
        print(f"\r{m}",end="") # end="" will happend each character to the same line
        sleep(0.1) # sleep for 0.1 sec
    print("\n"+"\t"+("#" * len(message)))

    while True:
        bus.menu() # Call function menu from the class bus
        choice = str(input("--> "))

        # Select an option on the menu
        if choice == '1':
            bus.add_passenger()
        elif choice == '2':
            bus.print_bus()
        elif choice == '3':
            bus.edit_passenger_card()
        elif choice == '4':
            bus.calc_total_age()
        elif choice == '5':
            bus.calc_average_age()
        elif choice == '6':
            bus.max_age()
        elif choice == '7':
            bus.find_age()
        elif choice == '8':
            bus.sort_bus()
        elif choice == '9':
            bus.poke()
        elif choice == '10':
            bus.print_sex()
        elif choice == '11':
            bus.getting_off()
        elif choice == '0': # Exists the code
            exit_message = "Thank you for using Bus Simulator ^.^ !!!"
            print("-" * len(exit_message))
            print(f"\n\n{exit_message}\n\n")
            print("-" * len(exit_message))
            exit()

        # Everytime we return to this main function we fall here
        input("\n\nClick any key to go back to the menu...")