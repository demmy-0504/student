V=int(input("input velocity:"))
c=299792458
r=1/(1-(V**2/c**2))**0.5
a=4.3
b=6.0
c=309
d=2000000
p=V/c
print("percentage of light speed="+str(p))
print("travel time to alpha centauri="+str(a/r))
print("travel time to barnard's star="+str(b/r))
print("travel time to betelgeuse="+str(c/r) )
print("travel time to andromeda="+str(d/r))