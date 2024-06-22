r=float(input("Please input a Richter scale value:"))
energy=10**(1.5*r+4.8)
tons=energy/(4.184*10**9)
lunch=energy/2930200 
print("Richter scale value:"+str(r))
print("Equivalence in Joules:"+str(energy))
print("Equivalence in tons of TNT: "+str(tons))
print("Equivalence in the number of nutritious lunches:"+str(lunch))