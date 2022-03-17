weight = int(input("Enter the weight please \n"))

def ground_shipping() :
    cost = 5 * weight
    taxe = 50
    totalCost = cost + taxe
    return totalCost

def air_shipping() :
    cost = 5 *weight
    taxe = (2/10) *cost
    totalCost = cost  + taxe
    return int(totalCost)
premium_shpping = 800
if ground_shipping() > air_shipping() < premium_shpping :
    print("the most suitable method is air shipping with  " + str(air_shipping()) +"$")
elif air_shipping() > ground_shipping() < premium_shpping :
    print("the most suitable method is gournd shipping with  " + str(ground_shipping())+"$")
elif air_shipping() > premium_shpping < ground_shipping() :
    print("the most suitable method is premium shipping with  " +str( premium_shpping)+"$")
input()

