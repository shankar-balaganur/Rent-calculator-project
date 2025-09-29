rent=int(input("Enter the room rent amount :"))
food=int(input("Enter the food Expendature:"))
unit=int(input("Enter the unit of electricity spent:"))
cost_perunit=int(input("Enter the cost per unit:"))
ele_bill=unit*cost_perunit
per=int(input("Enter the total nunber of persoin:"))
total_bill=rent+food+ele_bill/per
day=int(input("Enter today date:"))
time=30-day
print("\n Your rent:",rent,"\n Food Expendature:",food,"\n You spent ",unit,"unit electricty","\n Total persons:",per)
print("\n Rent per person is:",total_bill,"your rent paying dete is come in ",time,"Days.")