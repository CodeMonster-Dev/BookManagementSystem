# This is a Tkinter Project
import tkinter as tk
from tkinter import *
import csv
import pandas as pd
from tabulate import tabulate

root = Tk()
var = tk.IntVar()
root.geometry("500x400")
frame = Frame(root)
frame.pack()

def CheckLogin():
    loginButton.pack_forget()
    LogOutBtn.pack(side=RIGHT)
    addUser["state"] = ACTIVE
    searchUsers["state"] = ACTIVE
    addBook["state"] = ACTIVE
    searchBooks["state"] = ACTIVE
    sortBooks["state"] = ACTIVE
    cancel()

def Logout():
    cancel()
    loginButton.pack(side=RIGHT)
    LogOutBtn.pack_forget()
    addUser["state"] = DISABLED
    searchUsers["state"] = DISABLED
    addBook["state"] = DISABLED
    searchBooks["state"] = DISABLED
    sortBooks["state"] = DISABLED


def LoggedIn():
    with open('Users.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        username = userNameInput.get()
        password = passInput.get()

        for row in csv_reader:
            if row[1] == username and row[2] == password:
                login = True
                break
            else:
                login = False

    if login == True:
        CheckLogin()
    else:
        HideLoginData()
        LoginFunction()

def hideAddUser():
    cancel()

def LoginFunction():
    cancel()
    userNameLabel.pack(pady=5)
    userNameInput.pack()
    userNameInput.insert(0, "")
    passLabel.pack(pady=5)
    passInput.pack()
    loginBtn.pack(pady=10)

def HideLoginData():
    cancel()

def BtnAddUser():
    cancel()
    CityLabel.pack(pady=5)
    CityInput.pack()
    StateLabel.pack(pady=5)
    StateInput.pack()
    CountryLabel.pack(pady=5)
    CountryInput.pack()
    AgeLabel.pack()
    AgeInput.pack()
    CancelBtn.pack()
    AddBtn.pack()

def AddUser():
    City = CityInput.get()
    State = StateInput.get()
    Country = CountryInput.get()
    Age = AgeInput.get()
    data = pd.read_csv('Users.csv')
    df = data.UserID
    print(df)
    id = df.iloc[-1]
    id = id+1
    location = City + ", " + State + ", " + Country
    UserList = [id, "", "", location, Age]
#    data.to_append(UserList)
    a_series = pd.Series(UserList, index=data.columns)
    data = data.append(a_series, ignore_index=True)
    print(data.Age)
    data.to_csv('Users.csv', index=False)
    Success = Label(bottomframe, text="User Added Successfully!", bg="Green", fg="White")
    Success.pack()

def DisplaySearch():
    cancel()
    IdLabel.pack(pady=5)
    IdInput.pack()
    CityLabel.pack(pady=5)
    CityInput.pack()
    StateLabel.pack(pady=5)
    StateInput.pack()
    CountryLabel.pack(pady=5)
    CountryInput.pack()
    AgeLabel.pack(pady=5)
    AgeInput.pack()
    SearchBtn.pack()
    CancelUserBtn.pack()

def SearchUser():
    Id = IdInput.get()
    City = CityInput.get()
    State = StateInput.get()
    Country = CountryInput.get()
    Age = AgeInput.get()
    location = City + ", " + State + ", " + Country
    df = pd.read_csv("Users.csv")
    search = df.UserID
    r = 0
    for row in search:
        if(str(search[r]) == str(Id)):
            message = ""
            print("User ID: " + str(search[r]))
            if(str(df["Location"][r] == location)):
                print("Location: " + str(df["Location"][r]))
                if (str(df["Age"][r] == Age)):
                    print("Age: " + str(df["Age"][r]))
            break
        else:
            r = r+1
            message = "User Not Found | Please Enter Correct Details"
    print(message)

def HideSearch():
    cancel()

def ShowBook():
    cancel()
    IsbnLabel.pack(pady=5)
    IsbnInput.pack()
    TitleLable.pack(pady=5)
    TitleInput.pack()
    AuthorLabel.pack(pady=5)
    AuthorInput.pack()
    YearLabel.pack(pady=5)
    YearInput.pack()
    PublisherLabel.pack(pady=5)
    PublisherInput.pack()
    CancelBookBtn.pack()
    AddBookBtn.pack()

def AddBooks():
    Isbn = IsbnInput.get()
    Title = TitleInput.get()
    Author = AuthorInput.get()
    Year = YearInput.get()
    Publisher = PublisherInput.get()
    books = pd.read_csv('Books.csv')
    BookList = [Isbn, Title, Author, Year, Publisher]
    #    data.to_append(UserList)
    a_series = pd.Series(BookList, index=books.columns)
    books = books.append(a_series, ignore_index=True)
    books.to_csv('Books.csv', index=False)
    Success = Label(bottomframe, text="Book Added Successfully!", bg="Green", fg="White")
    Success.pack()

def CancelBook():
    cancel()

def ShowSearchBook():
    cancel()
    IsbnLabel.pack(pady=5)
    IsbnInput.pack()
    TitleLable.pack(pady=5)
    TitleInput.pack()
    AuthorLabel.pack(pady=5)
    AuthorInput.pack()
    YearLabel.pack(pady=5)
    YearInput.pack()
    PublisherLabel.pack(pady=5)
    PublisherInput.pack()
    CancelBookBtn.pack()
    SearchBookBtn.pack()

def SearchBook():
    Isbn = IsbnInput.get()
    Title = TitleInput.get()
    Author = AuthorInput.get()
    Year = YearInput.get()
    Publisher = PublisherInput.get()
    df = pd.read_csv("Books.csv")
    r = 0
    ISBNMatch = df["ISBN"]
    TitleMatch = df["Book-Title"]
    AuthorMatch = df["Book-Author"]
    YearMatch = df["Year-Of-Publication"]
    PublisherMatch = df["Publisher"]
    mask = (df["ISBN"] == Isbn) | (df["Book-Title"] == Title) | (df["Book-Author"] == Author) | (df["Year-Of-Publication"] == Year) | (df["Publisher"] == Publisher)
    res = df[mask]
    print(tabulate(res, headers='keys', tablefmt='psql'))

def ShowSort():
    cancel()
    IsbnSort.pack(side=LEFT)
    TitleSort.pack(side=LEFT)
    AuthorSort.pack(side=LEFT)
    PublisherSort.pack(side=LEFT)
    RatingSort.pack(side=LEFT)
    RatingCountSort.pack(side=LEFT)
    SortBtn.pack(side=LEFT, padx=5)
    CancelSortBtn.pack(side=LEFT)

def SortBooks():
    value = var.get()
    df = pd.read_csv("Books.csv")
    newdf = pd.read_csv("Review_small.csv")
    merged = df = pd.merge(df, newdf, on="ISBN")
    if value == 1:
        sorted_df = merged.sort_values(by=["ISBN"], ascending=True)
        print(sorted_df)
    elif value == 2:
        sorted_df = merged.sort_values(by=["Book-Title"], ascending=True)
        print(sorted_df)
    elif value == 3:
        sorted_df = merged.sort_values(by=["Book-Author"], ascending=True)
        print(sorted_df)
    elif value == 4:
        sorted_df = merged.sort_values(by=["Year-Of-Publication"], ascending=True)
        print(sorted_df)
    elif value == 5:
        sorted_df = merged.sort_values(by=["Publisher"], ascending=True)
        print(sorted_df)
    elif value == 6:
        sorted_df = merged.sort_values(by=["Book-Rating"], ascending=True)
        print(sorted_df)
    elif value == 7:
        sorted_df = merged.sort_values(by=["Book-Rating"], ascending=False)
        print(sorted_df)
    else:
        print('No option selected')


def cancel():
    userNameLabel.pack_forget()
    userNameInput.pack_forget()
    passPrev.pack_forget()
    passLabel.pack_forget()
    passInput.pack_forget()
    loginBtn.pack_forget()
    CityLabel.pack_forget()
    CityInput.pack_forget()
    StateLabel.pack_forget()
    StateInput.pack_forget()
    CountryLabel.pack_forget()
    CountryInput.pack_forget()
    AgeLabel.pack_forget()
    AgeInput.pack_forget()
    CancelBtn.pack_forget()
    AddBtn.pack_forget()
    IdLabel.pack_forget()
    IdInput.pack_forget()
    SearchBtn.pack_forget()
    CancelUserBtn.pack_forget()
    IsbnLabel.pack_forget()
    IsbnInput.pack_forget()
    TitleLable.pack_forget()
    TitleInput.pack_forget()
    AuthorLabel.pack_forget()
    AuthorInput.pack_forget()
    YearLabel.pack_forget()
    YearInput.pack_forget()
    PublisherLabel.pack_forget()
    PublisherInput.pack_forget()
    AddBookBtn.pack_forget()
    CancelBookBtn.pack_forget()
    SearchBookBtn.pack_forget()
    IsbnSort.pack_forget()
    TitleSort.pack_forget()
    AuthorSort.pack_forget()
    YearSort.pack_forget()
    PublisherSort.pack_forget()
    RatingSort.pack_forget()
    RatingCountSort.pack_forget()
    SortBtn.pack_forget()
    CancelSortBtn.pack_forget()
    userNameInput.delete(0, END)
    passInput.delete(0, END)
    CityInput.delete(0, END)
    StateInput.delete(0, END)
    CountryInput.delete(0, END)
    AgeInput.delete(0, END)
    IdInput.delete(0, END)
    IsbnInput.delete(0, END)
    TitleInput.delete(0, END)
    AuthorInput.delete(0, END)
    YearInput.delete(0, END)
    PublisherInput.delete(0, END)

bottomframe = Frame(root)


bottomframe.pack(side=BOTTOM)

LogOutBtn = Button(frame, text="Logout", fg="black", command=Logout)
LogOutBtn.pack_forget()

loginButton = Button(frame, text="Login", fg="black", command=LoginFunction)
loginButton.pack(side=LEFT)

addUser = Button(frame, text="Add User", fg="black", command=BtnAddUser, state=DISABLED)
addUser.pack(side=LEFT)

searchUsers = Button(frame, text="Search Users", fg="black", command=DisplaySearch, state=DISABLED)
searchUsers.pack(side=LEFT)

addBook = Button(frame, text="Add Book", fg="black", command=ShowBook, state=DISABLED)
addBook.pack(side=LEFT)

searchBooks = Button(frame, text="Search Books", fg="black", command=ShowSearchBook, state=DISABLED)
searchBooks.pack(side=LEFT)

sortBooks = Button(frame, text="Sort Books", fg="black", command=ShowSort, state=DISABLED)
sortBooks.pack(side=LEFT)

quitWindow = Button(frame, text="Quit", fg="black", command=exit)
quitWindow.pack(side=LEFT)

userNameLabel = Label(text="Username:")
userNameLabel.pack_forget()
userNameInput = Entry()
userNameInput.pack_forget()

passPrev = Label(text="\n\n\n")
passPrev.pack_forget()
passLabel = Label(text="Password:")
passLabel.pack_forget()
passInput = Entry()
passInput.pack_forget()

loginBtn = Button(text="Login", command=LoggedIn)
loginBtn.pack_forget()

# Add User Data

CityLabel = Label(text="City")
CityLabel.pack_forget()
CityInput = Entry()
CityInput.pack_forget()


StateLabel = Label(text="State")
StateLabel.pack_forget()
StateInput = Entry()
StateInput.pack_forget()

CountryLabel = Label(text="Country")
CountryLabel.pack_forget()
CountryInput = Entry()
CountryInput.pack_forget()

AgeLabel = Label(text="Age")
AgeLabel.pack_forget()
AgeInput = Entry()
AgeInput.pack_forget()

CancelBtn = Button(text="Cancel", command=hideAddUser)
CancelBtn.pack_forget()

AddBtn = Button(text="Add", command=AddUser)
AddBtn.pack_forget()


IdLabel = Label(text="ID")
IdLabel.pack_forget()
IdInput = Entry()
IdInput.pack_forget()

SearchBtn = Button(text="Search", command=SearchUser)
SearchBtn.pack_forget()

CancelUserBtn = Button(text="Cancel", command=HideSearch)
CancelUserBtn.pack_forget()

# Book Labels and Inputs

IsbnLabel = Label(text="ISBN")
IsbnLabel.pack_forget()
IsbnInput = Entry()
IsbnInput.pack_forget()

TitleLable = Label(text="Title")
TitleLable.pack_forget()
TitleInput = Entry()
TitleInput.pack_forget()

AuthorLabel = Label(text="Author")
AuthorLabel.pack_forget()
AuthorInput = Entry()
AuthorInput.pack_forget()

YearLabel = Label(text="Year")
YearLabel.pack_forget()
YearInput = Entry()
YearInput.pack_forget()

PublisherLabel = Label(text="Publisher")
PublisherLabel.pack_forget()
PublisherInput = Entry()
PublisherInput.pack_forget()

AddBookBtn = Button(text="Add", command=AddBooks)
AddBookBtn.pack_forget()

CancelBookBtn = Button(text="Cancel", command=CancelBook)
CancelBookBtn.pack_forget()

SearchBookBtn = Button(text="Search", command=SearchBook)
SearchBookBtn.pack_forget()

# Radio Buttons
IsbnSort = Radiobutton(root, text="ISBN", variable=var, value=1)
IsbnSort.pack_forget()

TitleSort = Radiobutton(root, text="Title", variable=var, value=2)
TitleSort.pack_forget()

AuthorSort = Radiobutton(root, text="Author", variable=var, value=3)
AuthorSort.pack_forget()

YearSort = Radiobutton(root, text="Year", variable=var, value=4)
YearSort.pack_forget()

PublisherSort = Radiobutton(root, text="Publisher", variable=var, value=5)
PublisherSort.pack_forget()

RatingSort = Radiobutton(root, text="Rating", variable=var, value=6)
RatingSort.pack_forget()

RatingCountSort = Radiobutton(root, text="Rating Count", variable=var, value=7)
RatingCountSort.pack_forget()

SortBtn = Button(text="Sort", command=SortBooks)
SortBtn.pack_forget()

CancelSortBtn = Button(text="Cancel", command=cancel)
CancelSortBtn.pack_forget()

root.mainloop()