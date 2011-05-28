# Python the Hard Way
# Ex. 5
# Kyle Wanamaker
# www.klowell.com
#

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

my_weight_kg = my_weight * 2.241
my_height_cm = my_height * 2.54
my_age_dog_yrs = my_age * 7

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I'd get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)

print "If I were a dog, I would be %d years old." % my_age_dog_yrs
print "In Europe I would weigh %fkg and be %fcm tall." % (my_weight_kg, my_height_cm)