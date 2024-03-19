 #Write a program to create Student class with data members student rollno, name, address, course. Include a constructor to initialize data members. Add a method to print the student details.
class student:
  def __init__ (self,rollno,name,address,course) :
    self.rollno=rollno
    self.name=name
    self.address=address
    self.course=course
  def display(self) :
    print("student roll no :",self.rollno)
    print("student name :",self.name)
    print("student address :",self.address)
    print("student course :",self.course)
stul=student("322010301047","CHARAN","TIRUPATHI","CSE")
stul.display()
#Write a program to create Book class with data members book_id, name, cost and publisher. Include constructor and a method to display the book details. Create 3 objects and display their details.
class book:
    def __init__ (self,id,name,cost,publisher):
        self.id = id
        self.name = name
        self.cost = cost
        self.publisher = publisher
    def book(self):
            print("Book ID number: ",self.id)
            print("Book Name: ",self.name)
            print("Book Cost: ",self.cost)
            print("Book Publisher: ",self.publisher)
b1 = book ("1234","Half Girlfriend","Rs.180","Rupa")
b1.book()
b2 = book("5678","Intensions","Rs.650","Justin")
b2.book()
print("\n")
 #Write a program to create Account class with data members acc_no, name, balance. Include a constructor and methods to perform deposit and withdraw operations on account. Create account object perform some operations and display the account details.
class account:

  def __init__ (self, accno, accname, accbalance) :
    self.accno = accno
    self.name = accname
    self.balance = accbalance
  def procedure(self) :
    self.new_bal = 0
    a = input("Deposit or withdrawl?")
    if a=="deposit":
      self.b = int(input("How much would you want to deposit?"))
      self.new_bal = self.balance + self.b
    elif a=="withdrawl":
      self.b = int(input("How much would you like to withdraw"))
      self.new_bal = self.balance - self.b
  def display(self) :
    print("account number: ",self.accno)
    print("account holder name: ",self.name)
    print("account balance: ",self.balance)
    print("account new balance: ",self.new_bal)
acc1 = account("8769234362","CHARAN",6000)
acc1.procedure()
acc1.display()
print("\n")
 #Write a program to create Product class with data members product_id, product_name, price, expiry_date. Include constructor to initialize data members and a method to print products details.
class product:
  def __init__(self,proid,proname,proprice,prodate):
    self.proid = proid
    self.proname = proname
    self.proprice = proprice
    self.prodate = prodate
  def display(self):
    print("product ID number :",self.proid)
    print("product name : ",self.proname)
    print("product price : ",self.proprice)
    print("product expiry date : ",self.prodate)
p1= product("978456","Paneer","Rs.70","26th August 2080")
p1.display()
 #Write a program to create Employee class with data members eno, ename, sal, designation. Include constructor to initialize employee details and count the number of employee objects created.
class employee:
  e_count=0
  def __init__ (self,eno,ename,sal,designation) :
    self.eno=eno
    self.ename=ename
    self.esal=sal
    self.edes=designation
    employee.e_count+=1
  def display(self) :
    print("employee no",self.eno)
    print("employee name",self.ename)
    print("emplyee salary",self.esal)
    print("employee designation",self.edes)
    print("total objects created:",employee.e_count)
e1=employee("1047","CHARAN","140000","ARTIST")
e1.display()
print("\n")
 #Write a program to create Complex_Number with data members real_part and imaginary_part. Include constructor to initialize complex number. Add a method which adds two complex numbers.
class complex:
  j=(-1)**0.5
  def __init__ (self, r_part, i_part,r_part2, i_part2) :
    self.real = r_part
    self.imag = i_part
    self.real2 = r_part2
    self.imag2 = i_part2
  def comp(self) :
    self.x1=self.real+self.imag*self.j
    self.x2=self.real2+self.imag*self.j
  def display(self) :
    j=(-1)**0.5
    print(self.x1)
    print(self.x2)
    print((self.real+self.real2)+((self.imag+self.imag2)*j))
    print(type((self.real+self.real2)+((self.imag+self.imag2)*j)))
c1=complex(56,46,78,90)
c1.comp()
c1.display()
