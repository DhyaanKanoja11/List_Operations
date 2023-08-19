#Menu driven program to perform various tasks operations of list

#Declaring list
q=[]

#Range of the list
n=int(input("RANGE OF THE LIST:"))

#Getting input of elements for a list

for i in range(n):
    E=int(input("Enter ELEMENTS of the LIST:"))
    q.append(E)

#Checking The List
print("LIST:",q,'\n')

#Menu Of List Operations
while True:
    print("\n L I S T   O P E R A T I O N S")
    print("1 | Append an Element")
    print("2 | Insert an Element at desired position")
    print("3 | Append a List To Given List")
    print("4 | Modify an Existing Element")
    print("5 | Delete an Existing Element by its Position")
    print("6 | Delete an Existing Element by its Value")
    print("7 | Sort The List In Ascending Order")
    print("8 | Sort The List In Ascending Order")
    print("9 | Display The List")
    print("10| EXIT")
    choice=int(input("Enter Your Choice(1-10): "))

#To make the List Operations Work

#List Operation-1 {Append an Element}
    if choice==1:
        g=int(input("Enter The Element To Append:"))
        q.append(g)
        print("New List:",q,"\n")

#List Operation-2 {Insert an Element at desired position}
    elif choice==2:
        g=int(input("Enter The Element To Be Inserted:"))
        pos=int(input("Enter Position of The Element:"))
        q.insert(pos,g)
        print("Updated List",q,"\n")

#List Operation-3 {Append a List To Given List}
    elif choice==3:
        nl=list(eval(input("Enter New List:")))
        q.extend(nl)
        print("Extended List:",q,"\n")

#List Operation-4 {Modify an Existing Element}
    elif choice==4:
        pos1=int(input("Enter Position To Be Modified:"))
        ne=int(input("Enter New Element:"))
        q[pos]=ne
        print("Modified List:",q,"\n")

#List Operation-5 {Delete an Existing Element by its Position}
    elif choice==5:
        pos2=int(input("Enter Position Of the Number To be Deleted:"))
        q.pop(pos2)
        print("Updated List:",q,"\n")

#List Operation-6 {Delete an Existing Element by its Value}
    elif choice==6:
        el=int(input("Enter Element To Be Deleted: "))
        q.remove(el)
        print("Updated List: ",q,"\n")

#List Operation-7 {Sort The List In Ascending Order}
    elif choice==7:
        q.sort()
        print("\nThe List Has Been Sorted")

#List Operation-8 {Sort The List In Descending Order}
    elif choice==8:
        q.sort(reverse=True)
        print("\n The List Has Been Sorted")

#List Operation-9 {Display The List}
    elif choice==9:
        print("\nThe List Is:",q)

#List Operation-10 {EXIT/BREAK}
    elif choice==10:
        break

#Else
    else:
        print("*****Invalid Choice*****")
        print("\n Press Any Key To Continue............")
        ch=input()



#END OF THE CODE
