print("Welcome to the Binary Hexadecimal Converter App")

#user input for max value and create lists
max_value = int(input("\nWhat is the maximum binary and hexadecimal value you would like to compute: "))

decimals = list(range(1,max_value+1))
bnry = []
hexa = []

for num in decimals:
  bnry.append(bin(num))
  hexa.append(hex(num))  

print("\nGenerating lists.....complete.")

print("\nUsing slices, we will now show a portion of each list.")

#get min and max value to slice lists
num_start = int(input("\nWhat decimal number would you like to start at: "))
num_stop = int(input("What decimal number would you like to stop at: "))

#print values for each number type
print("\nDecimal values from " + str(num_start) + " to " + str(num_stop) + ":")
for num in decimals[num_start-1:num_stop]:
  print(num)

print("\nBinary values from " + str(num_start) + " to " + str(num_stop) + ":")
for num in bnry[num_start-1:num_stop]:
  print(num)

print("\nHexadecimal values from " + str(num_start) + " to " + str(num_stop) + ":")
for num in hexa[num_start-1:num_stop]:
  print(num)

#print overall list using zip method
input("\nHit enter to see all the values from 1 to " + str(max_value) + ".")

print("\nDecimal----Binary----Hexadecimal")
print("--------------------------------")

for d, b, h in zip(decimals,bnry,hexa):
  print(str(d) + "----" + str(b) + "----" + str(h))

