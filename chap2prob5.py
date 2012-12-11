# Chapter 2 Problem 5 - robot distance travelled - math.pi version
import math
RADIUS = 2.7 # of wheel, in cm
rotations = 2
#robot will travel the circumference of its wheel (pi * d) with each rotation
distance = math.pi * RADIUS * 2 * rotations
print("Rotations:", rotations)
print("Distance travelled:", distance,"cm")