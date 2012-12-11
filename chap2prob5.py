# Chapter 2 Problem 5 - robot distance travelled - declare own PI version
PI = 3.142
RADIUS = 2.7 # of wheel, in cm
rotations = 2
#robot will travel the circumference of its wheel (pi * d) with each rotation
distance = PI * RADIUS * 2 * rotations
print("Rotations:",rotations)
print("Distance travelled:",distance,"cm")