#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 5-dars string
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
print(kocha,'ko\'chasi', mahalla, 'mahallasi', tuman, 'tumani', viloyat, 'viloyati')


# In[3]:


print('Iltimos quyidagi malumotlarni kiriting:')
kocha=input('ko\'changiz: ')
mahalla=input('mahallangiz: ')
tuman=input('tumaningiz: ')
viloyat=input('viloyatingiz: ')
print(kocha,'ko\'chasi\n', mahalla, 'mahallasi\n', tuman, 'tumani\n', viloyat, 'viloyati')


# In[4]:


manzil=f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)


# In[9]:


print(manzil.title())
print(manzil.capitalize())
print(manzil.upper())
print(manzil.lower())


# In[10]:


# takrorlash
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
print(f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")


# In[14]:


print('iltimos quyidagilarni kiriting:')
kocha=input('kochasi: ')
mahalla=input('mahallasi:')
tuman=input('tumani: ')
viloyat=input('viloyati:')
print((f"{kocha} kochasi,\n {mahalla} mahallasi,\n {tuman} tumani,\n {viloyat} viloyati").title())


# In[16]:


#6-dars mashqlar
n=int(input('Istalgan sonni kiriting:\n>>>'))
print(n, 'ning kvadrati', n**2,'ga teng.')
print(n, 'ning kubi', n**3, 'ga teng.')


# In[18]:


n=int(input('Yoshingiz nechida?\n>>>'))
m=2021-n
print('Siz', m, 'yili tugilgansiz.')


# In[19]:


n=int(input('Birinchi sonni kiriting:\n>>>'))
m=int(input('Ikkinchi sonni kiriting:\n>>>'))
print(n,'+',m,'=',n+m)
print(n,'-',m,'=',n-m)
print(n,'*',m,'=',n*m)
print(n,'/',m,'=',n/m)


# In[20]:


#7 lists
fruits=['apples','figs', 'apricots', 'pomegranates', 'cherries']
print('first fruits:',fruits[0])
print('second fruits:', fruits[1])


# In[23]:


fruits=['apples','figs', 'apricots', 'pomegranates', 'cherries']
print('first fruits:',fruits[0].title())
print('second fruits:', fruits[1].upper())


# In[25]:


prices=[12000, 13000, 15000, 23000]
print('new price=',prices[0]+prices[3])


# In[28]:


#yangi royhat qoshish
fruits=['apples', 'melons', 'peach']
fruits.append('bananas')
print(fruits)


# In[31]:


cars=[]
cars.append('lacetti')
cars.append('nexia 3')
cars.append('damas')
print(cars)


# In[32]:


cars=['nexia', 'lacetti', 'spark']
cars.insert(0, 'malibu')
print(cars)


# In[33]:


fruits=['apples', 'figs', 'apricots', 'melons']
del fruits[0]
fruits.insert(0,'bananas')
print(fruits)


# In[34]:


fruits=['apples', 'figs', 'apricots', 'melons']
fruits.remove('figs')
print(fruits)


# In[40]:


fruits=['apples', 'figs', 'apricots', 'melons']
sugirish=fruits.pop(3)
print(f"men {sugirish} mevasini sotib oldim.".capitalize())


# In[44]:


#lists mashqlar
names=['John','Ali','Mike','Tyson']
a=names[0]
print('Hello', a,'.', f"{names[1]}, will you come to the class tomorrow?")
print(names[-1].upper(), 'was the best boxer in the world.')


# In[45]:


numbers=[100,-200, 0.4, -900, 120, 450]
numbers[1]=200
numbers[0]=numbers[1]+numbers[-1]
numbers[3]=numbers[4]-100
del numbers[-1]
numbers.insert(0, 1000)
print(numbers)


# In[56]:


t_shahslar=['Beruniy','Buxoriy', 'Ibn Sino', 'Farobiy', 'Termiziy']
z_shahslar=['Bill Gates', 'Robert Kyosaki', 'Jack Ma', 'Elon Musk']
print(f" Men tarixiy shahslardan {t_shahslar[1].title()} va zamonaviy shahslardan {z_shahslar[2].title()} bilan suhbat qurishni istardim.")


# In[67]:


friends=[]
friends.append('Ali')
friends.append('Temur')
friends.append('Zombie')
friends.append('John')
friends.append('Tom')
friends.append('Jack')
print(friends)
friends.remove('Ali')
friends.remove('John')
print(friends)
friends.insert(0,'White')
friends.insert(2, 'Cruise')
friends.insert(-1, 'Thomson')
print(friends)


# In[68]:


new_friends=['White', 'Temur', 'Cruise', 'Zombie', 'Tom', 'Thomson', 'Jack']
print(f" There are some new friends. They are {new_friends[0]}, {new_friends[2]}, and {new_friends[-1]}. Welcome to our party. Enjoy it")


# In[1]:


#8 sorting list
cars=['jeep', 'malibu', 'kia', 'BMW', 'mercedes benz', 'sonata', 'hundai']
cars.sort()
print(cars)


# In[2]:


#teskari royhat
cars=['jeep', 'malibu', 'kia', 'BMW', 'mercedes benz', 'sonata', 'hundai']
cars.sort(reverse=True)
print(cars)


# In[4]:


cars=['jeep', 'malibu', 'kia', 'BMW', 'mercedes benz', 'sonata', 'hundai']

print(sorted(cars))
print(cars)


# In[5]:


numbers=[12,34,67,45,23,98]
numbers.sort()
print(numbers)
print(sorted(numbers, reverse=True))


# In[6]:


fruits=['banana', 'apples', 'peaches', 'melons', 'figs']
fruits.reverse()
print(fruits)


# In[8]:


fruits=['apples', 'pears', 'peaches', 'bananas', 'tangerines', 'lemons']
print('elementlar soni=',len(fruits))


# In[10]:


numbers=list(range(0,10))
print(numbers)


# In[13]:


prices=[12000, 45000, 65000, 34000, 12300, 11000, 98000]
cheapest=min(prices)
most_expensive=max(prices)
total=sum(prices)
print('the cheapest is',cheapest, 'and the most expensive is', most_expensive, 'total is', total)


# In[17]:


cars=['BMW', 'damas', 'tico', 'gentra', 'nexia 2', 'malibu', 'captiva']
my_cars=cars[0:3]
print(my_cars)
print(cars[:4])
print(cars[2:])


# In[19]:


numbers=[1,2,3,4,5]
numbers2=numbers[:]
numbers2.append(6)
numbers2.append(7)
print('numbers list=', numbers)
print('numbers2 lis=', numbers2)


# In[20]:


#ozgarmas royhat tuples
sides=(15,20,25)
print(sides)


# In[21]:


toys = ('bus','car','bear','dino','snake','lizard')
toys[3] = 'dragon'


# In[22]:


toys=('teddy', 'tiger', 'lizard', 'rabbit', 'dragon')
print(toys[0])
print(toys[:2])
print(toys[-1])


# In[23]:


toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)


# In[28]:


#8 mashqlar
countries=['Uzbekistan', 'Turkey', 'Germany', 'Japan', "South Korea", 'Russia']
print(countries)
print('countries=', len(countries))


# In[29]:


print(sorted(countries))


# In[30]:


print(sorted(countries, reverse=True))


# In[31]:


countries.reverse()
print(countries)


# In[32]:


countries.sort()
print(countries)


# In[33]:


countries.sort(reverse=True)
print(countries)


# In[38]:


numbers=list(range(2,120,2))
print(numbers)


# In[39]:


print(sum(numbers))


# In[41]:


ayirma=max(numbers)-min(numbers)
print('max-min=',ayirma)


# In[43]:


print('raqamlar soni=',len(numbers))


# In[49]:


print(numbers[:10])
print(numbers[-20:])


# In[60]:


foods=['kimchi', 'osh', 'norin', 'mastava', 'shorva', 'dimlama', 'shavla']
breakfast=foods[:]
del breakfast[-2:]
del breakfast[1:3]
breakfast.append('quymoq')
breakfast.append('kofe')
print(breakfast)
print(foods)
breakfast=tuple(breakfast)
print(breakfast)

breakfast=list(breakfast)
breakfast[0]='cream and bread'
print(breakfast)


# In[1]:


#9 for
guests=['Akbar', 'Temur', 'Xerox', "Dilyor", "Mahmud"]
for i in guests:
    print(i,end=' ')


# In[2]:


guests=['Akbar', 'Temur', 'Xerox', "Dilyor", "Mahmud"]
for j in guests:
    print(f" Dear, {j} we would like to invite you to our next week party. Thank you.")


# In[3]:


numbers=list(range(1,11))
for i in numbers:
    print(f' {i} ning kvadrati {i**2} ga teng.')


# In[7]:


sonlar=list(range(1,11))
sonlar_kvadrati=[]
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)


# In[9]:


names=["Ali", 'Vali', "Sanjar", 'Temur', "Dilyor"]
for name in names:
    print(f' Assalomu alaykum {name}. Keling dostim.')


# In[10]:


print(f' Kod {len(name)} marta takrorlandi.')


# In[13]:


odd_numbers=list(range(11,101,2))
cube=[]
for i in odd_numbers:
    cube.append(i**3)

print(cube)


# In[16]:


cinemas=['Titanic', "Gladiator", "Salahiddin Ayyubiy", 'Hobbit']
print(cinemas)


# In[19]:


print('How many people have you talked today?')
people=['Ali', "Zakir", "Elyor", "Bahtiyor"]
s=0
for i in people:
    s+=1
    
    print(f'who was the {s}- person?= {i}')


# In[21]:


#10 if else
autos=['bmw', 'hundai', 'mercedes benz', 'toyota', 'cruise', 'x5']
for auto in autos:
    if auto=='bmw':
        print(auto.upper(), end=' ')
    else:
        print(auto.title(), end=' ')


# In[28]:


name=input('Please enter your name:\n>>>')
if name.lower()!='john':
    print(f' Sorry {name.title()}, we are waiting for John')
else:
    print(f' Welcome John.')


# In[30]:


answer=float(input('12*6=?\n>>>'))
if answer!=72:
    print('mistake')


# In[33]:


age=int(input('How old are you?\n>>>'))
if age>=18:
    print('Welcome')
else:
    print('Not allowed')


# In[35]:


login=input('choose a new login:\n>>>')
if len(login)<=5:
    print('login must be more than 5 characters')


# In[39]:


age=int(input('Enter your birth year:\n>>>'))
if 2021-age<18:
    print(f' you are {2021-age}.')
    print('Not allowed.')
else:
    print('Welcome.')


# In[43]:


age=int(input('enter your age:\n>>>'))
if age>65:      print('you are in a COVID age group.')


# In[45]:


#10 mashqlar
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for i in cars:
    if i=='gm':
        print(i.upper())
    else:
        print(i.title())


# In[46]:


#11
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for m in cars:
    if m!='gm':
        print(m.title())
    else:
        print(m.upper())


# In[50]:


login=input('Enter you login:\n>>>')
if login.lower()=='admin':
    print('Xush kelibsiz Admin, foydalanuvchilar royhatini korasizmi?')
else:
    print(f' Xush kelibsiz {login.title()}')


# In[52]:


print('Ikkita son kiritinig:')
a=input('1-sonni kiriting:\n>>>')
b=input('2-sonni kiriting:\n>>>')
if a==b:
    print('sonlar ozaro teng ekan.')


# In[4]:


#11 if elif else
n=int(input('yoshingizni kiriting:\n>>>'))
if n<4:
    price=0
elif n<12:
    price=5000
elif n<65:
    price=10000
else:
    price=8000
print(f' sizga kirish {price} som')


# In[5]:


n=input('Bugun kun nima?\n>>>')
if n.lower()=='shanba' or n.lower()=='yakshanba':
    print('Bugun dam olish kuni')
else:
    print('Bugun ish kuni')


# In[6]:


kun=input('Bugun kun nima?\n>>>')
harorat=int(input('Havo harorati qanday?\n>>>'))
if kun.lower()=='yakshanba' and harorat>=30:
    print('Chomilgani ketdik.')
elif kun.lower()=='yakshanba' and harorat<30:
    print('Bugun uyda qolamiz.')


# In[1]:


foods=['manti', 'somsa', 'non', 'norin', 'mastava', 'shavla']
'osh' in foods


# In[2]:


menu=['osh', 'manti', 'shavla', 'dimlama', 'norin', 'burger']
ovqat=input('Nima ovqat yeysiz?\n>>>')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi.')
else:
    print('Afsus, bizda bunday taom yoq.')


# In[5]:


menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f' {taom} bor')
        else:
            print(f' {taom} yoq')
else:
    print('savatiz bosh')


# In[7]:


n=int(input('juft son kiriting:\n>>>'))
if n%2==0:
    print('Rahmat')
else:
    print('Bu juft son emas.')


# In[9]:


n=int(input('Yoshingiz nechida?\n>>>'))
if n<4 or 60<n:
    price=0
elif n<18:
    price=10000
elif n>=18:
    price=20000
print('sizga kirish', price, 'so\'m')    


# In[13]:


n=int(input('Istalgan sonni kiriting=\n>>>'))
m=range(2,11)
for k in m:
    if n%k==0:
        print(f'{n} {k} ga qoldiqsiz bolinadi.')


# In[14]:


son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")


# In[ ]:





# In[ ]:





# In[ ]:




