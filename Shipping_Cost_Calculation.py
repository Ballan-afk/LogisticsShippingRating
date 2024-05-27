#Shipping Cost Calculator

#input package  weight and shipping rate


weight = float(input("Enter the package weight in kilograms: "))
Shipping_rate =float(input("Enter the shipping rate in kilograms: "))

#Calculate the shipping cost
shipping_cost = weight * shipping_rate

#Display the results
print(f"Shipping Cost:{shipping_cost} USD")


