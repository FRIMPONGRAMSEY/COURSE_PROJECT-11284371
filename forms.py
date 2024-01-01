# This is my first python code please do well to check it out
A=input('What is your surname name? ')
O=input('Enter your firse name- ')
M=input('Enter your other name- ')
B=input('Enter your email address- ')
C=int(input('Enter password- '))
D=int(input('Confirm password- '))
if C==D:
    print('Please confirm from your gmail')
elif C!=D:
    print('Kindly check there is an error in your input')
E=int(input('Enter your date of birth- '))
Z=2023-E
print('Then you are',Z)
F=input('What is the name of your home -town? ')
G=input('Enter your parent/guardians name- ')
H=input('Enter your gender- ')
K=input('Are you a male or female? ')
if H==K:
    print('Thank you for signing up with us')
elif H!=K:
    print('Thank you for signing up with us but input a correct gender')
I=input('Have you read and accepted our terms and conditions? ')
L=input('yes/no- ')
if I==L:
    print('Click here to summit')
elif I!=L:
    print('Go to www.ramsey.com to accept and agree to our conditions')
print(A,O,M)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)
print(K)
print(I)
print('Please we  are very happy for your contribution in filling this form',A,'.We shall send you an e-mail notification upon your submission','.Please cross check',B,'.Kindly send the telephone number of',G,'to our serial caller')
from tkinter import *
from tkinter import messagebox
def login():
    username=entry1.get()
    password=entry2.get()
    if (username=="" and password==""):
        messagebox.showinfo("","Blank Not Allowed")
    elif (username==A and password==C):
        messagebox.showinfo("","login successful")
    else:
        messagebox.showinfo("","Incorrect username and password")
root=Tk()
root.title("Login")
global entry1
global entry2
Label(root,text="Username").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=70)
entry1=Entry(root,bd=5)
entry1.place(x=140,y=20)
entry2=Entry(root,bd=5)
entry2.place(x=140,y=70)
Button(root,text="Login",command=login,height=3,width=13,bd=6).place(x=100,y=120)
root.mainloop()