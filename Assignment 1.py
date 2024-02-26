# Define a base class for a person
class Person:
    ''' A class representing a person'''
    def __init__(self, firstName, lastName, gender, phoneNum, age):
        # Initialize common attributes for all persons
        self._firstName = firstName
        self._lastName = lastName
        self._gender = gender
        self._phoneNum = phoneNum
        self._age = age  # Using a single underscore to indicate a protected attribute in parent class

    # using getter and setter methods for retrieving individual attributes
    def getFirstName(self):
        return self._firstName

    def getLastName(self):
        return self._lastName

    def getGender(self):
        return self._gender

    def getPhoneNum(self):
        return self._phoneNum

    def getAge(self):
        return self._age  # Accessing the protected attribute

# Defining a subclass for passengers, inheriting from Person
class Passenger(Person):
    ''' A class representing a passenger'''
    def __init__(self, firstName, lastName, gender, phoneNum, age, nationality, passengerID, passportNum):
        # Initializing attributes specific to passengers and calling the superclass constructor
        super().__init__(firstName, lastName, gender, phoneNum, age)
        self.__nationality = nationality
        self.__passengerID = passengerID
        self.__passportNum = passportNum  # Using double underscore to indicate a private attribute

    # using getter and setter for retrieving additional passenger-specific attributes
    def getNationality(self):
        return self.__nationality

    def getPassengerID(self):
        return self.__passengerID

    def getPassportNum(self):
        return self.__passportNum  # Accessing the private attribute

# Defining a class for airline staff
class AirlineStaff:
    ''' A class representing airline staff'''
    def __init__(self, empID, email, department, role, airline):
        # Initializing attributes specific to airline staff
        self.__empID = empID
        self.__email = email
        self.__department = department
        self.__role = role
        self.__airline = airline

    # using getter and setter for retrieving airline staff attributes
    def getEmpID(self):
        return self.__empID

    def getEmail(self):
        return self.__email

    def getDepartment(self):
        return self.__department

    def getRole(self):
        return self.__role

    def getAirline(self):
        return self.__airline  # Using double underscore to indicate a private attribute

# Define a class for baggage
class Baggage:
    ''' A class representing baggage'''
    def __init__(self, bagID, passengerName, weight, dimensions, securityScanR):
        # Initialize attributes specific to baggage
        self.__bagID = bagID  # Using double underscore to indicate a private attribute
        self.__passengerName = passengerName
        self.__weight = weight
        self.__dimensions = dimensions
        self.__securityScanR = securityScanR

    # using getter and setter for retrieving baggage attributes
    def getBagID(self):
        return self.__bagID  # Accessing the private attribute

    def getPassengerName(self):
        return self.__passengerName

    def getWeight(self):
        return self.__weight

    def getDimensions(self):
        return self.__dimensions

    def getSecurityScanR(self):
        return self.__securityScanR # Using double underscore to indicate a private attribute

# Defining a class for boarding passes
class BoardingPass:
    ''' A class representing boarding pass'''
    def __init__(self, boardingPID, boardingTime, departureTerminal, gate, flightNumber, fromLocation, toLocation,
                 flightDate, seatNum, classType):

        # Initialize attributes specific to boarding passes
        self.__boardingPID = boardingPID  # Using double underscore to indicate a private attribute
        self.__boardingTime = boardingTime
        self.__departureTerminal = departureTerminal
        self.__gate = gate
        self.__flightNumber = flightNumber
        self.__fromLocation = fromLocation
        self.__toLocation = toLocation
        self.__flightDate = flightDate
        self.__seatNum = seatNum
        self.__classType = classType

    # using getter and setter for retrieving boarding pass attributes
    def getBoardingPID(self):
        return self.__boardingPID  # Accessing the private attribute

    def getBoardingTime(self):
        return self.__boardingTime

    def getDepartureTerminal(self):
        return self.__departureTerminal

    def getGate(self):
        return self.__gate

    def getFlightNumber(self):
        return self.__flightNumber

    def getFromLocation(self):
        return self.__fromLocation

    def getToLocation(self):
        return self.__toLocation

    def getFlightDate(self):
        return self.__flightDate

    def getSeatNum(self):
        return self.__seatNum

    def getClassType(self):
        return self.__classType # Using double underscore to indicate a private attribute

# Defining functions for displaying details of different objects
# Displaying details of a person
def displayPerson(person):
    print("Person Details:")
    print("First Name:", person.getFirstName())
    print("Last Name:", person.getLastName())
    print("Gender:", person.getGender())
    print("Phone Number:", person.getPhoneNum())
    print("Age:", person.getAge())

# Displaying details of a passenger.
def displayPassenger(passenger):
    displayPerson(passenger)
    print("Nationality:", passenger.getNationality())
    print("Passenger ID:", passenger.getPassengerID())
    print("Passport Number:", passenger.getPassportNum())

# Displaying details of an airline staff
def displayAirlineStaff(airlineStaff):
    print("Airline Staff Details:")
    print("Employee ID:", airlineStaff.getEmpID())
    print("Email:", airlineStaff.getEmail())
    print("Department:", airlineStaff.getDepartment())
    print("Role:", airlineStaff.getRole())
    print("Airline:", airlineStaff.getAirline())

# Displaying details of a baggage
def displayBaggage(baggage):
    print("Baggage Details:")
    print("Bag ID:", baggage.getBagID())
    print("Passenger Name:", baggage.getPassengerName())
    print("Weight:", baggage.getWeight(), "kg")
    print("Dimensions:", baggage.getDimensions())
    print("Security Scan Result:", baggage.getSecurityScanR())

# Displaying details of a boarding pass.
def displayBoardingPass(boardingPass):
    print("Boarding Pass Details:")
    print("Boarding Pass ID:", boardingPass.getBoardingPID())
    print("Boarding Time:", boardingPass.getBoardingTime())
    print("Departure Terminal:", boardingPass.getDepartureTerminal())
    print("Gate:", boardingPass.getGate())
    print("Flight Number:", boardingPass.getFlightNumber())
    print("From Location:", boardingPass.getFromLocation())
    print("To Location:", boardingPass.getToLocation())
    print("Flight Date:", boardingPass.getFlightDate())
    print("Seat Number:", boardingPass.getSeatNum())
    print("Class Type:",boardingPass.getClassType())
# Example use:

# Creating sample objects
passenger1 = Passenger("Alyazia", "Mohamed", "Female", "050-123-456-9", 19, "UAE", "P12345", "A6789")
employee1 = AirlineStaff("E98765", "Salem@emiratesairlines.com", "Operations", "Manager", "Emirates Airlines")
baggage1 = Baggage("B789", "Alyazia Mohamed", 23, "30x40", "Passed")
boarding_pass1 = BoardingPass("BP567", "12:30 PM", "Terminal A", "Gate 3", "FL123", "London", "Dubai",
                               "2024-03-01", "12A", "Business Class")

# Displaying details
displayPassenger(passenger1)
displayAirlineStaff(employee1)
displayBaggage(baggage1)
displayBoardingPass(boarding_pass1)
