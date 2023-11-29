from tkinter import *
import socket
from tkinter import filedialog,Toplevel
from tkinter import messagebox
import os


root=Tk()
root.title("Sharing Files")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

def Send():
    print("Sending a file.....")
    window_send=Toplevel(root)
    window_send.title("Send")
    window_send.geometry('450x560+500+200')
    window_send.configure(bg="#f4fdfe")
    window_send.resizable(False,False)

    def select_file():
        global file_name
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",
                                            filetypes=(('file_types','*.txt'),('all files','*.*')))

    def sender_of():
        s=socket.socket()
        host=socket.gethostname()
        port=8081
        try:
            s.bind((host,port))
        except PermissionError as e:
            print(f"Error: {e}, Try running as administrator or using a different port.")
            return
        s.listen(1)
        print(host)
        print('waiting for any incoming connections.....')
        conn,addr=s.accept()

        try:
            with open(file_name,'rb') as file:
                file_data=file.read(1024)
                while file_data:
                    conn.send(file_data)
                    file_data = file.read(1024)
            print("Data has been sent successfully.")
        except Exception as e:
            print(f"The was an error while trying to send the file: {e}")
        finally:
            file.close()
            s.close()

        Send()
    # You might want to call select_file and sender_of appropriately in your GUI

    #icon
    image_icon1=PhotoImage(file="images/send.png")
    window_send.iconphoto(False,image_icon1)

    Sbackgorund=PhotoImage(file="images/sender.png")
    Label(window_send,image=Sbackgorund).place(x=-2,y=0)

    Mbackground=PhotoImage(file="images/id.png")
    Label(window_send,image=Mbackground,bg="#f4fdfe").place(x=100,y=260)

    host=socket.gethostname()
    Label(window_send,text=f'ID: {host}',bg='white',fg='black').place(x=140,y=290)

    Button(window_send,text="+ select a file",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window_send,text="SEND",width=8,height=1,font='arial 14 bold',fg="#fff",bg="#000",command=sender_of).place(x=150,y=300)

    window_send.mainloop()
def Receive():
    print("Receiving a file......")
    window_receive = Toplevel(root)
    window_receive.title("Send")
    window_receive.geometry('450x560+500+200')
    window_receive.configure(bg="#f4fdfe")
    window_receive.resizable(False, False)

    def send_receive():
        ID=Sender_ID.get()
        filename1=Rec_File_ID.get()
        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1624)
        file.write(file_data)
        file.close()
        print("The file has been received successfully")

    # icon
    image_icon2 = PhotoImage(file="images/receive.png")
    window_receive.iconphoto(False, image_icon2)

    Hbackground=PhotoImage(file="images/receiver.png")
    Label(window_receive,image=Hbackground).place(x=-2,y=0)

    logo=PhotoImage(file='images/profile.png')
    Label(window_receive,image=logo,bg="#f4fdfe").place(x=10,y=250)

    Label(window_receive,text="Receive",font=('arial',20),bg="#f4fdfe").place(x=100,y=280)


    Label(window_receive, text="Enter the Sender's ID : ",font=('arial', 10, 'bold'),bg='lightblue').place(x=20, y=340)
    Sender_ID = Entry(window_receive, width=25, fg="black", border=2, bg="white", font=('arial', 15))
    Sender_ID.place(x=20, y=370)
    Sender_ID.focus()


    Label(window_receive,text="Enter the file_name of the receiving file: ",font=('arial',10,'bold'),bg='#f4fdfe').place(x=20,y=420)
    Rec_File_ID = Entry(window_receive,width=25,fg="black",border=2,bg="white",font=('arial',15))
    Rec_File_ID.place(x=20,y=450)

    #image
    image_icon_r=PhotoImage(file="images/arrow.png")
    rr=Button(window_receive,text="Receive",compound=LEFT,image=image_icon_r,width=130,bg="#39c790",font="arial 14 bold",command=send_receive)
    rr.place(x=20,y=500)


    window_receive.mainloop()

#icon
image_icon=PhotoImage(file="images/icon.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=('Acumin Variable Concept',20,'bold'),bg="#f4fdf3").place(x=20,y=30)
Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image=PhotoImage(file="images/send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=50,y=100)

receive_image=PhotoImage(file="images/receive.png")
receive=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Receive)
receive.place(x=300,y=100)

#label
Label(root,text="Send",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="Receive",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=300,y=200)

background=PhotoImage(file="images/background.png")
Label(root,image=background).place(x=-2,y=323)




root.mainloop()