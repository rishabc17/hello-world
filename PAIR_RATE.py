import math
d=2.4*10**(-12)
p=1*10**-3
l=30*10**-3
c=3*10**8
w=2*math.pi*c/(405*10**-9)
W=6*10**-5
e=8.85*10**-12

L1=405
L2=L1*2

Az=2.25411
Bz=1.06543
Cz=0.05486
Dz=0.02140
Ay=2.19229
By=0.83547
Cy=0.0497
Dy=0.01641

n1=(Ay+(By/(1-Cy*(L1**-2)))-Dy*(L1**2))**0.5 #for pump
n2=(Ay+(By/(1-Cy*(L2**-2)))-Dy*(L2**2))**0.5 #rishab
kbgugubj=88888
tefehgeg=00

a0=9.9587*10**-6    #n1(Z) values
a1=9.9228*10**-6
a2=-8.9603*10**-6
a3=4.1010*10**-6
b0=-1.1882*10**-8   #n2(Z) values
b1=10.459*10**-8
b2=-9.8136*10**-8
b3=3.1481*10**-8
c0=6.2897*10**-6  #n1(Y) values
c1=6.3061*10**-6
c2=-6.0629*10**-6
c3=2.6486*10**-6
d0=-0.14445*10**-8 #n2(Y) values
d1=2.2244*10**-8
d2=-3.5770*10**-8
d3=1.3457*10**-8


N1=(n1)+15*(c0+(c1/L1)+(c2/L1**2)+(c3/L1**3))+225*(d0+(d1/L1)+(d2/L1**2)+(d3/L1**3))
N2=(n2)+15*(c0+(c1/L2)+(c2/L2**2)+(c3/L2**3))+225*(d0+(d1/L2)+(d2/L2**2)+(d3/L2**3))
N3=(n3)+15*(a0+(a1/L2)+(a2/L2**2)+(a3/L2**3))+225*(b0+(a1/L2)+(b2/L2**2)+(b3/L2**3))

num=4*d**2*p*l*w**2
den=9*N1*N2*N3*e*math.pi*W**2*(N3-N2)*c**2

rate = num/den
print("the pair rate is : ", rate)


