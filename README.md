## Parking Lot
Design a parking lot using Python.

## Dependencies

1. Python. Visit the link https://www.python.org/downloads/ to install Python. 

2. tabulate. After cloning the repository, use the command `pip install -r requirements.txt`

## Description

The aim of this project is to design a basic parking lot in Python. It creates parking lot with given number of slots. The cars follow Greedy(nearest slot first) approach while being parked in the slots.

The project accepts the following commands in the exact format -

1. `exit` - Exits the interactive terminal.

2. `file_name.txt` - Executes all the valid commands provided in the text file.

3. `create_parking_lot slots` - Create a parking lot with given number of slots.

4. `park registration_no color` - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".

5. `leave slot` - Removes vehicle from given slot.

6. `status` - Prints the slot number, registration number and color of the parked vehicles.

7. `registration_numbers_for_cars_with_color color` - Prints all the registration numbers of cars of a given color.

8. `slot_numbers_for_cars_with_color` - Prints all the slot numbers currently occupied by the cars of a given color.

9. `slot_number_for_cars_with_registration_number` - Prints the slot/slots currently occupied by a car of a given registration number.


main.py can be run through shell. commands can be entered manually or through the file containing test cases. An example file `test_case.txt` has been provided in repo.


## Setup

To create your own ParkingLot - 

1. Clone the repository

2. Run `python main.py`. This opens a shell where you can write your commands.
  
3. To run with a file enter, the name of the file, i.e.. `test_case.txt` in the shell . You can modify the test cases.