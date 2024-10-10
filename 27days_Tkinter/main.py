from tkinter import *



window = Tk()
#코드사이에 있어야함
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=20)

#Label
my_label = Label(text="I am label", font=("Arial",24,"bold"))
#my_label["text"] = "New Text"
my_label.config(text ="New Text")
#my_label.pack(side="left") #라벨 보이게 하기
#my_label.place(x=100,y=200)
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)


#button
def button_clicked():
    print("I get clicked")
    new_text = input.get()
    my_label.config(text = new_text)

button = Button(text ="Click Me" ,command =button_clicked)
#button.pack(side="left")
button.grid(column =1, row=1)

new_button = Button(text ="New Button")
new_button.grid(column =2, row=0)


#Entry(텍스트박스)
input = Entry(width=10)
#input.pack(side="left")
#print(input.get())
input.grid(column =3, row=2)



window.mainloop()