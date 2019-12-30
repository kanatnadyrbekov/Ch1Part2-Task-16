# If you were on the moon now, your weight will be 16,5% of your earth weight.
# To calculate it you have to multiple to 0,165. If next 15 years your weight will
# increase 1 kg each year. What will be your weight each year on the moon next
# 15 years?

weight = int(input("Your weight :"))

for x in range(1, 16):
    weight = weight + 1
    weight_in_moon = weight * 0.165
    
    print(weight_in_moon)
