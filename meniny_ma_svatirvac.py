import math
pi=math.pi

##1
##x=int(input("kolko mas cukrikov?:"))
##y=int(input("medzi kolko deti ich rozdelis?"))
##print("kazde dieta dostane",int(x/y),"cukrikov a tebe ich ostane",x-int(x/y)*y)

##2
##x=int(input("zadaj stranu: "))
##print("obvod = ",4*x,"\n obsah = ",x*x)

##3
##a=int(input("strana_a: "))
##b=int(input("strana_b: "))
##c=int(input("strana_c: "))
##print(print("objem = ",a*b*c,"\n povrch = ",2*(a*b+a*c+b*c)))

##4
##r=int(input("zadaj polomer: "))
##print("obvod kruhu  = ",2*pi*r,"\n obsah kruhu = ",pi*r*r,"\n objem gule = ",(4/3)*pi*r**3)

##5
##x=int(input("zadaj cislo: "))
##print("jeho treria mocnina: ",x**3,"\n","jeho siesta mocnina: ",x**6)

##6
##x=float(input("vklad: "))
##m=float(input("urok: "))
##print("o rok neskor.... ",float(x+x*m/100))

##7
##h=int(input("pocet hodin: "))
##m=int(input("pocet minut: "))
##s=int(input("pocet sekund: "))
##print("do smrti mas este: ",int(h*3600+m*60+s),"sekund")
##
####8
##s=int(input("pocet sekund: "))
##H= int(s/3600)
##M= int((s-H*3600)/60)
##print("do smrti mas este: ",int(s/3600),"hodin",int(s/60-int(int(s/3600)*60)),"minut",s - H*3600 - M*60,"sekund a 0 tercii")

##9
##c=int(input("vase peniaze nadobudnute kontroverznym podnikanim: "))
##b_500 = int(c/500)
##b_200 = int((c-b_500*500)/200)
##b_100 = int((c-b_500*500 - b_200*200)/100)
##b_50 = int((c - b_500*500 - b_200*200 - b_100*100)/50)
##b_20 = int((c - b_500*500 - b_200*200 - b_100*100 - b_50*50)/20)
##b_10 = int((c - b_500*500 - b_200*2 - b_100*100 - b_50*50 - b_20*20)/10)
##b_5 = int((c - b_500*500 - b_200*2 - b_100*100 - b_50*50 - b_20*20 - b_10*10)/5)
##print("mate: ",b_500,"patstoviek, ",b_200,"dvestoviek, ",b_100,"stovak, ",b_50,"pajd, ",b_20,"dvaciek, ",b_10,"desiek a ",b_5,"patiek")

####10
##s = float(input("spotreba vasho sukromneho lietadla: "))
##c = float(input("cena za liter benzinu: "))
##v = float(input("vzdialenost vasej destinacie: "))
##print("na vasu cestu potrebujete ",c*s/100*v)

##11
##x=float(input("x = "))
##y=float(input("y = "))
##if x<y:
##    print("vacsie je ",y,"a mensie ",x)
##elif x>y:
##    print("vacsie je ",x,"a mensie ",y)
##elif x==y:
##    print(x," a ",y,"su rovnake")
    
##12   
##a = float(input("a = "))
##b = float(input("b = "))
##if a==0:
##    print("rovnica nema koren do pixe")
##else:
##    print("vas zazvorovy koren je",-b/a)

##13
##a = float(input("a = "))
##b = float(input("b = "))
##c = float(input("c = "))
##if a>b and a>c:
##    print("najvacsie cislo je ",a)
##elif c>b and c>a:
##    print("najvacsie cislo je ",c)
##elif b>a and b>c:
##    print("najvacsie cislo je ",b)

##14, 15
##k = float(input("k = "))
##l = float(input("l = "))
##m = float(input("m = "))
##if k+l>m and k+m>l and m+l>k:
##    if k == l == m:
##        print("vas epic trojuholnik je rovnostranny")
##    elif k==l or k==m or l==m:
##        print("vas epic trojuholnik je rovnoramenny")
##    elif m == (k**2 + l**2)**(1/2) or k == (l**2 + m**2)**(1/2) or l == (k**2 + m**2)**(1/2):
##        print("vas epic trojuholnik je pravouhly")
##    else:
##        print("vas epic trojuholnik je proste epic")
##else:        
##    print("vas trojuholnik sa neda urobit pixe")

##16
##v = float(input("vasa vyska v metroch: "))
##h = float(input("vasa hmotnost v kilogramoch: "))
##b = float(h/v**2)
##if b < 18.5:
##    print("lala ho, aky je chudy frixe")
##elif 18.5<= b <25:
##    print("lala ho, aku ma epic postavu")
##elif 25<= b <30:
##    print("lala ho, prilis je chlapec")
##elif 30<b:
##    print("u r horizontaly overmatured")

##17
##a = float(input("kolko mate cukrikov? "))
##if int(a/2) == float(a/2) and int(a/3) == float(a/3) :
##    print("vase cukriky mozte rozdelit medzi 2 aj medzi 3 deti")
##elif int(a/2) == float(a/2) and int(a/3) != float(a/3) :
##    print("vase cukriky mozte rozdelit medzi 2 deti")
##elif int(a/2) != float(a/2) and int(a/3) == float(a/3) :
##    print("vase cukriky mozte rozdelit medzi 3 deti")
##else:
##    print("vyhrali ste, lebo vase cukriky sa nedaju rozdelit medzi 2 ani 3 deti a mozte ich zjest")

##18
##print("tento epic program vam zoradi vase cisla vzostupne")
##a = float(input("a = "))
##b = float(input("b = "))
##c = float(input("c = "))
##if a<b <c:
##    print(a,b,c)
##if a<c <b :
##    print(a,c,b)
##if b< a<c :
##    print(b,a,c)
##if b<c <a :
##    print(b,c,a)
##if c<b <a :
##    print(c,b,a)
##if c<a <b :
##    print(c,a,b)

##19

##20
##a = float(input("a = "))
##b = float(input("b = "))
##c = float(input("c = "))
##if a == b == c :
##    print("vase cisla su rovnake")
##elif a == b or a == c or b == c :
##    print("dve z vasich cisla su rovnake")
##elif a != b and a != c and b != c :
##    print("vase cisla nie su rovnake") 

##21
##p = float(input("vas cash? "))
##d = float(input("vas volny den? "))
##h = float(input("vas volny cas? "))
##if h > 20:
##	print("chod uz spat")
##elif p < 7 :
##	print("nemas dost penazi")
##elif d == 1 :
##	if h < 17 :
##		if p >= 14:
##			print("pojdes do kina o 17 aj o 20")
##		elif p < 14:
##			print("pojdes do kina o 17 alebo o 20")
##	if h < 17 :
##		print("pojdes do kina o 20")
##elif d != 1 :
##	if h >= 17:
##		if p >= 18:
##			print("pojdes do divadla o osmej")
##		elif p < 18:
##			print("pojdes do kina o osmej")
##	elif h < 17:
##		if p >= 25:
##			print("pojdes do kina o piatej a do divadla o osmej")
##		elif 14 <= p < 25:
##			print("pojdes do kina o piatej a o osmej")
##		elif p < 14:
##			print("pojdes do kina o piatej alebo o osmej")

##26
##x=0
##for i in range(50):
##    x += 2
##    print(x)

##28
##a = int(input("a = "))
##b = int(input("b = "))
##x = a+1
##n = 0
##while x < b:
##    if int(x/3) == float(x/3):
##        n += x
##    else:
##        pass
##    x += 1
##print("suctom je ",n)

##31
##n = int(input("n = "))
##k = int(input("k = "))
##print("n na k = ",n**k)

##33
##n = int(input("vase sestciferne cislo: "))
##a = int(n/100000)
##b = int((n - a*100000)/10000)
##c = int((n - a*100000 - b*10000)/1000)
##d = int((n - a*100000 - b*10000 - c*1000)/100)
##e = int((n - a*100000 - b*10000 - c*1000 - d*100)/10)
##f = int(n - a*100000 - b*10000 - c*1000 - d*100 - e*10)
##print(str(a)+"\n",str(b)+"\n",str(c)+"\n",str(d)+"\n",str(e)+"\n",str(f)+"\n")

##n = int(input("vase sestciferne cislo: "))
##for i in range(6):
##    a = n%10
##    n = n//10
##    print(a)

##35
##x = int(input("veduceho cislo (2-9): "))
##n = 1
##z = 0
##for i in range(100):
##    z += n
##    if int(z/x) == float(z/x) or z%10 == x or (z//10)%10 == x or z == x:
##        print("*")
##    else:
##        print(z)

##37
##x=0
##for i in range(10000):
##    d=i+1
##    for n in range(i):
##        k=n+1
##        if int(d/k) == d/k :
##            x =x+ k 
##            
##    if x == d :
##        print(d)
##    x=0

##38
##n = int(input("cislo n: "))
##x = 0
##for i in range(n*2):
##    
##    if int(i/2) != i/2 :
##        x = x+i
##       
##print(x)
    
##41

##42
##x = int(input("x = "))
##y = int(input("y = "))
##a = y - 1
##b = x - 1
##if x >= y:
##    while x%a != 0 or y%a != 0 :
##        a-=1
##    print(a)
##else:
##    while y%b != 0 or x%b != 0 :
##        b-=1
##    print(b)

##45
n = int(input("n = "))
x = 2
som = True
while x<n :
    if n%x != 0 :
        som = False  
    x+=1
        

       
if som == True:
    print("n je prvocislo")
else:
    print("n nie je prvocislo")
























