import tkinter as tk
from tkinter import filedialog
import EmailModule
from tkinter import messagebox
print('Your email:',end='')
email=input()
print('Your password(應用程式密碼):',end='')
password=input()
email=EmailModule.Email(email,password)

fontType=('Arial',10,'bold')

window=tk.Tk()
window.title('Mail Sender!')
innerFrame = tk.Frame(window, borderwidth=50)
Var_Image_text=''
Var_File_text=''

GUI_Title = tk.Label(window,font=fontType,text='wei 電子郵箱',height=2,width=15)
GUI_Title.grid(row=0,column=0,columnspan=3)
Receiever = tk.Label(window,font=fontType,text='收件者郵箱:',height=2,width=15)
Receiever.grid(row=1,column=0)
Receiever_text = tk.Text(window,font=fontType,height=1,width=30)
Receiever_text.grid(row=1,column=1,columnspan=2,padx=20)

Another = tk.Label(window,font=fontType,text='副本:\n(以，區隔',height=2,width=15)
Another.grid(row=2,column=0)
Another_text = tk.Text(window,font=fontType,height=1,width=30)
Another_text.grid(row=2,column=1,columnspan=2,padx=20)

Mail_Title = tk.Label(window,font=fontType,text='標題:',height=2,width=15)
Mail_Title.grid(row=3,column=0)
Mail_Title_text = tk.Text(window,font=fontType,height=1,width=30)
Mail_Title_text.grid(row=3,column=1,columnspan=2,padx=20)


Content = tk.Label(window,font=fontType,text='內文:',height=2,width=15)
Content.grid(row=4,column=0)
Content_text = tk.Text(window,font=fontType,height=10,width=30)
Content_text.grid(row=4,column=1,columnspan=2,rowspan=2,padx=20)

def GetImageFile():
    Var_Image_text = filedialog.askopenfilename(parent=window, title='選擇檔案', initialdir='./', filetypes=(("Image Files", ["*.png","*.jpg","*.jpeg"]),("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg")))
    email.attachImg(Var_Image_text)
    Image_text.config(text=Var_Image_text)


def GetFile():
    file_path = filedialog.askopenfilename(parent=window, title='選擇檔案', initialdir='./', filetypes=(("All Files","*.*"),("All Files","*.*")))
    email.attachFile(file_path)
    File_text.config(text=file_path)

Image = tk.Label(window,font=fontType,text='選擇照片',height=2,width=15)
Image.grid(row=6,column=0)

Image_btn = tk.Button(window,text='Open Image',font=fontType,command=GetImageFile)
Image_btn.grid(row=6,column=1,columnspan=2,pady=10)
Image_text=tk.Label(text=Var_Image_text,font=fontType)
Image_text.grid(row=7,column=1,columnspan=2)

File = tk.Label(window,font=fontType,text='選擇檔案',height=2,width=15)
File.grid(row=8,column=0)
File_btn = tk.Button(window,text='Open File',font=fontType,command=GetFile)
File_btn.grid(row=8,column=1,columnspan=2,pady=10)
File_text=tk.Label(text=Var_File_text,font=fontType)
File_text.grid(row=9,column=1,columnspan=2)

def SendMail():
    if(len(Receiever_text.get(1.0, "end"))==0):
        messagebox.showwarning('The Receiever Error','The content of receiever can\'t be Null')
        return
    email.setCc(Another_text.get(1.0, "end"))
    email.setReceive(Receiever_text.get(1.0, "end"))
    email.setTitile(Mail_Title_text.get(1.0, "end"))
    email.setContent(Content_text.get(1.0, "end"))
    email.Send()
    Receiever_text.delete('1.0','end')
    Another_text.delete('1.0','end')
    Mail_Title_text.delete('1.0','end')
    Content_text.delete('1.0','end')
    email.ImgRoute=''
    Var_Image_text=''
    Image_text.config(text=Var_Image_text)
    email.FileRoute = ''
    Var_File_text=''
    File_text.config(text=Var_File_text)


printButton = tk.Button(window,font=fontType, text="Send",command=SendMail)
printButton.grid(row=10,column=0,columnspan=3,pady=20)

window.mainloop()