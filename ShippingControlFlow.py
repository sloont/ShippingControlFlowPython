ground_flat = 20.00
ground_premium = 125.00
def normal_ground(weight):
  if weight <= 2.00:
    return weight * 1.50 + ground_flat
  elif weight > 2.00 and weight <= 6.00:
    return weight * 3.00 + ground_flat
  elif weight > 6.00 and weight <= 10.00:
    return weight * 4.00 + ground_flat
  else:
    return weight * 4.75 + ground_flat

print(normal_ground(8.4))

def drone(weight):
  if weight <= 2.00:
    return weight * 4.50
  elif weight > 2.00 and weight <= 6.00:
    return weight * 9.00
  elif weight > 6.00 and weight <= 10.00:
    return weight * 12.00
  else:
    return weight * 14.25

print(drone(1.5))

def cheapest(weight):
  if drone(weight) <= ground_premium and drone(weight) <= normal_ground(weight):
    if drone(weight) == ground_premium:
      return "Drone shipping and Premium ground shipping are the same price and the cheapest option."
    elif drone(weight) == normal_ground(weight):
      return "Drone shipping and Normal ground shipping are the same price and the cheapest options."
    else:
      return "Drone shipping is cheapest!"
  elif normal_ground(weight) <= drone(weight) and normal_ground(weight) <= ground_premium:
    if normal_ground(weight) == ground_premium:
      return "Normal ground shipping and Premium ground shipping are the same price and the cheapest options."
    else:
      return "Normal ground shipping is cheapest!"
  else:
    return "Premium ground shipping is cheapest!"


print(cheapest(4.8))
print(cheapest(41.5))
