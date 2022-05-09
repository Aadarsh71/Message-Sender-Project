import requests

from tkinter import *
from tkinter.messagebox import showinfo,showerror

def send_sms(num,message):

    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"XnGHQa1KFTu7jwvz8Il6YRd3eUckhEfqs9VmPJCyS4NoDgLrW2c0GZE4gn5dVhjbiBSyk9LIu718ewNr",
               "sender_id":"TXTIND",
               "message":message,
               "route":"v3",
               "numbers":num}

    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

    dic=response.json()
    print(dic)
    return dic.get('return')

    #print("---- messeage send succesfully -----")
    #send_sms("8085033557", "my first project")

def btn_click():
    num=textnum.get()
    msg=textmsg.get("1.0",END)
    r=send_sms(num,msg)
    if r==True:
        showinfo("Send Success","Successfully Sent")
    else:
        showerror("Error","Something went wrong..")


#Gui create

root=Tk()
root.title("--- MESSAGE SENDER ---")
root.geometry("400x500")
font = ("Helvetica",22,"bold")

textnum = Entry(root, font=font)
textnum.pack(fill=X)

textmsg=Text(root)
textmsg.pack(fill=X,pady=20)

sendbtn=Button(root,text="SEND MSG",command=btn_click)
sendbtn.pack()

root.mainloop()