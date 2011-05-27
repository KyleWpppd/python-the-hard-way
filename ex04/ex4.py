# Python the Hard Way
# Ex. 4
# Kyle Wanamaker
# www.klowell.com
#

# assign 100 to cars
cars = 100

# cars have space for people, drivers & passengers...
space_in_a_car = 4.0
drivers = 30
passengers = 90

#if there aren't enough drivers, a car doesn't get driven...
cars_not_driven = cars - drivers
cars_driven = drivers

# calc total capacity of all driven cars
carpool_capacity = cars_driven * space_in_a_car

# ok maybe I'm being silly here, but we aren't checking to make sure cars
# are actually below their capacity...bugs the easy way???
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in_each_car."




