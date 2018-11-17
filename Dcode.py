fullName = "Cody Summers"
age = 22

myArray = []
myArray.append(fullName)
myArray.append(age)
print myArray

def sayHello():
    print "Hello Cody!"
sayHello()    

split_Name = fullName
print fullName.split(" ");

def sayName():
    print "Hello, "+fullName;
sayName()

def myAge(year_born):
    print 2018-year_born;
myAge(1995);

def sum_odd_numbers():
    sum = 0;
    for i in range(1,5001,2):
        if(i % 2 == 1):
            sum += i;
            return sum;
print sum_odd_numbers();

