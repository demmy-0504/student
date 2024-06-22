height=float(input("input the height of the 1st ball:"))
mass1=float(input("input the mass of the 1st ball:"))
mass2=float(input("input the mass of the 2st ball:"))
g=9.8
u=mass1*g*height
v1=(2*u/mass1)**0.5
v2=(2*u/mass2)**0.5
print("the velocity of the 1st ball after slide:",v1,"m/s")
print("the velocity of the 2st ball after slide:",v2,"m/s")
