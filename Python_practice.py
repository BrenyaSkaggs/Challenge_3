x=0
while x <=5:
    print (x)
    x=x+1


count = 7
while count < 1:
    print ("Hello World")

 
  
numbers = [ 0,1,2,3,4]
for num in numbers:
    print(num)

for num in range (5):
    print(num)

counties_dict= {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:   
    print(counties_dict.get(county))
for county,voters in counties_dict.items():
    print (county,voters)
for county,voters in counties_dict.items():
    print(county + " county has"+ str("voters") + "registered voters")
    







