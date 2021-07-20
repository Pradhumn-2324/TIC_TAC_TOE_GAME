from tkinter import *
from tkinter import messagebox

count=0
win=False
str1=' '
msg=' '
class tictactoe():
    
            
     count=0
     def __init__(self):
            
         vm=Tk()

         vm.geometry("500x500")
         vm.minsize(500,500)
         vm.maxsize(800,800)
         vm.title("TIC_TAC_TOE")

         def restart(vm):
            global msg
            msgbox=messagebox.askquestion("Alert"," DO YOU WANT TO CONTINUE")
            if msgbox=='yes':
                 print("restart Yes")
                 b1['text']=' '
                 b1['bg']='white'
                 b2['text']=' '
                 b2['bg']='white'
                 b3['text']=' '
                 b3['bg']='white'
                 b4['text']=' '
                 b4['bg']='white'
                 b5['text']=' '
                 b5['bg']='white'
                 b6['text']=' '
                 b6['bg']='white'
                 b7['text']=' '
                 b7['bg']='white'
                 b8['text']=' '
                 b8['bg']='white'
                 b9['text']=' '
                 b9['bg']='white'
                 global count
                 count=0
            else:
                 print("restart No")
                 vm.destroy()
         def whowins(vm):
                if win==True and str2=='X':
                     print("x wins")
                     messagebox.showinfo("Alert"," X Wins")
                     restart(vm)

                if str2=='O':
                     print("O wins")
                     messagebox.showinfo("Alert"," O Wins")
                     restart(vm)

        #  def winPossibilities():
        #         global win

        #         whowins(win)

         def actionPerformed(b):
                global count
                if count%2==0 and b["text"]==' ':
                    b["text"]='X'
                    b["font"]='Arial', '15'
                    b["bg"]="green"
                    count=count+1
                        
                elif count%2==1 and b["text"]==' ':
                    b["text"]='O'
                    b["font"]='Arial', '15'
                    b["bg"]="navy blue"
                    count=count+1
                else:
                     messagebox.showerror("tic tac toe ","re clicked button")
                     
                global str1,str2,win
                str1=b['text']
                print(str1)
                # for rows combinations
                if b1['text']==b2['text'] and b2['text']==b3['text']:
                    str2=b1['text']
                    win=True
                    whowins(vm)
                
                elif b4['text']==b5['text'] and b5['text']==b6['text'] and b7['text']!=' ':
                     str2=b4['text']
                     win=True
                     whowins(vm)

                elif b7['text']==b8['text'] and b8['text']==b9['text'] and b7['text']!=' ':
                     win=True
                     str2=b7['text']
                     whowins(vm)

                # column Possibilitites
                elif b1['text']==b4['text'] and b4['text']==b7['text'] and b1['text']!=' ':
                     str2=b1['text']
                     win=True
                     whowins(vm)

                elif b2['text']==b5['text'] and b5['text']==b8['text'] and b2['text']!=' ':
                     str2=b2['text']
                     win=True
                     whowins(vm)

                elif b3['text']==b6['text'] and b6['text']==b9['text'] and b3['text']!=' ':
                     str2=b3['text']
                     win=True
                     whowins(vm)
                    
                #diagonal Possibilities
                elif b1['text']==b5['text'] and b5['text']==b9['text'] and b1['text']!=' ':
                     str2=b1['text']

                     win=True
                     whowins(vm)
                
                elif b3['text']==b5['text'] and b5['text']==b7['text'] and b3['text']!=' ':
                     str2=b3['text']
                     win=True
                     whowins(vm)
                
                else:
                    win=False
                

         b1=Button(vm,bg='white',pady='5',text=' ',command=lambda:actionPerformed(b1))
         b2=Button(vm,bg='white',pady='5',text=' ',command=lambda:actionPerformed(b2))
         b3=Button(vm,bg='white',pady='5',text=' ',command=lambda:actionPerformed(b3))
         b4=Button(vm,bg='white',pady='5',text=' ',command=lambda:actionPerformed(b4))
         b5=Button(vm,bg='white',pady='5',text=' ',command=lambda:actionPerformed(b5))
         b6=Button(vm,bg='white',pady='5',text=' ',command=lambda:actionPerformed(b6))
         b7=Button(vm,bg='white',pady='5',text=' ',command=lambda:actionPerformed(b7))
         b8=Button(vm,bg='white',pady='5',text=' ',command=lambda:actionPerformed(b8))
         b9=Button(vm,bg='white',pady='5',text=' ',command=lambda:actionPerformed(b9))
         
    # specify grid
         Grid.rowconfigure(vm,0,weight=1) 
         Grid.columnconfigure(vm,0,weight=1)

         Grid.rowconfigure(vm,1,weight=1)
         Grid.columnconfigure(vm,1,weight=1)

         Grid.rowconfigure(vm,2,weight=1)
         Grid.columnconfigure(vm,2,weight=1)

         vm

         b1.grid(row=0,column=0,sticky="NSEW")
         b2.grid(row=0,column=1,sticky="NSEW")
         b3.grid(row=0,column=2,sticky="NSEW")
         b4.grid(row=1,column=0,sticky="NSEW")
         b5.grid(row=1,column=1,sticky="NSEW")
         b6.grid(row=1,column=2,sticky="NSEW")
         b7.grid(row=2,column=0,sticky="NSEW")
         b8.grid(row=2,column=1,sticky="NSEW")
         b9.grid(row=2,column=2,sticky="NSEW")

         vm.mainloop()

add=tictactoe()
