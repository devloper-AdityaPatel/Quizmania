
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import os
import pygame.mixer
from pygame import mixer
import pickle
from tkinter import scrolledtext as st
import math

#main window creation and its manipulation
main_window=Tk()
main_window.title('Quizmania')
#get the screen dimensions
screen_width=main_window.winfo_screenwidth()
screen_height=main_window.winfo_screenheight()
#window dimensions
window_width=1800
window_height=1000
#to find from tkinter import *
#centre point of the window
#centre_x=int((screen_width-mainwindow_width)/2)
#centre_y=int((screen_height-mainwindow_height)/2)
#set the position of the window int the centre of screen
main_window.geometry(f'{screen_width}x{screen_height}')
main_window.resizable(True,True)
#imported library work here
#pygame work here
# music creation work here
pygame.mixer.init()
def smouseclick(event):
    pygame.mixer.music.load('Mouse-Click-sound.mp3')
    pygame.mixer.music.play(loops=1)

#os work
#folder creation work done here
cwd=os.getcwd()
dir_list=os.listdir()
if 'quizfolder' not in dir_list:
    os.mkdir('quizfolder',mode=0o666)

quizfolder_path=cwd+'\\quizfolder'
qff_list=os.listdir(quizfolder_path) #listcontains question ,answer and option folder
print(qff_list)
quizfolder_qpath=cwd+'\\quizfolder\\qquizfolder' #question folder path
quizfolder_opath=cwd+'\\quizfolder\\oquizfolder' #option folder path
quizfolder_apath=cwd+'\\quizfolder\\aquizfolder' #answer folder path


if 'qquizfolder' not in qff_list:    #'''creating the question folder'''
    os.mkdir(quizfolder_qpath,mode=0o666)
    print('directory created')
if 'oquizfolder' not in qff_list:    #'''creating the option folder'''
    os.mkdir(quizfolder_opath,mode=0o666)
    print('directory created')
if 'aquizfolder' not in qff_list:    #'''creating the ans folder'''
    os.mkdir(quizfolder_apath,mode=0o666)
    print('directory created')

qquiz_list=os.listdir(quizfolder_qpath) #'''retireving list of files in question folder'''
oquiz_list=os.listdir(quizfolder_opath) #'''retireving list of files in option folder'''
aquiz_list=os.listdir(quizfolder_apath) #'''retireving list of files in ans folder'''



#folder creation work complete here


#-----------------------------LOGINWINDOW CREATION----------------------------------
loginwindow=Toplevel(bg='#6698ff',height=250,width=250)
loginwindow.title('Login')
#login window dimensions
loginwindow_width=450
loginwindow_height=450
#to place the login window in the centre
loginwindow_centre_x=int((screen_width-loginwindow_width)/2)
loginwindow_centre_y=int((screen_height-loginwindow_height)/2)
#set the geometry of login window
loginwindow.geometry(f'{loginwindow_width}x{loginwindow_height}+{loginwindow_centre_x}+{loginwindow_centre_y}')
loginwindow.lift(main_window)
#----------------login func start----------
#def exit func for login window
def exit_login():
    loginwindow.iconify()
    main_window.deiconify()


#program for login window
def login():
    main_window.iconify()
    label_head.config(text='LOGIN')
    frame_1.pack(side=TOP, anchor='n', fill=X)
    #user login widget definition
    username_label = Label(frame_1, text='Username',
                          bg='#404040', fg='#2ce68c',
                          width=12, height=1, font='comicsansms 10 bold', padx=3, pady=2, relief=SUNKEN)
    username_entry=Entry(frame_1,bg='#def2ff',fg='#6698ff',width=30,bd=1)
    password_label = Label(frame_1, text='Password',
                          bg='#404040', fg='#2ce68c',
                          width=12, height=1, font='comicsansms 10 bold', padx=3, pady=2, relief=SUNKEN)
    password_entry=Entry(frame_1,bg='#def2ff',fg='#6698ff',width=30,bd=1,show='*')

    #login button widget insert
    login_button=Button(frame_1,text='Login',bg='#910303',fg='white',font='comicsansms 10 bold',padx=1,pady=1,
                        width=8,height=1,command=exit_login)
    login_button.grid(column=1,row=3)
    #labeladjust b/w login and username
    label_adjust=Label(frame_1,bg='#6698ff')

    # new usr?
    label_rynu=Label(frame_1,text='ARE YOU NEW USR?',font='comicsansms 10 bold',bg='#6698ff',fg='white')
    label_rynu.grid(column=0,row=4)

    #sign up button
    signup_button=Button(frame_1,text='Singup',bg='#3b56cc',fg='white',font='comicsansms 10 bold',padx=1,pady=1,
                        width=8,height=1)
    signup_button.bind('<Button-1>',signup)
    signup_button.grid(column=1,row=5)
    label_adjust.grid(column=0,row=0,padx=50,pady=2)
    username_label.grid(column=0,row=1,padx=50,pady=2);username_entry.grid(column=1,row=1)
    password_label.grid(column=0,row=2,padx=50,pady=2);password_entry.grid(column=1,row=2)



#----------------login func end-----------------
#----------------signup func start--------------
def signup(event):
    # feame destroyed
    frame_1.pack_forget()
    label_head.config(text='SIGNUP')
    # frame_2 packed
    frame_2.pack(side=TOP,anchor='n',fill=X)
    # gap adjusted
    label_adjust = Label(frame_2, bg='#6698ff')
    label_adjust.grid(column=0,row=0,padx=50,pady=2)
    # name
    name_label = Label(frame_2, text='Name',
                           bg='#404040', fg='#2ce68c',
                           width=12, height=1, font='comicsansms 10 bold', padx=3, pady=2, relief=SUNKEN)
    name_entry = Entry(frame_2, bg='#def2ff', fg='#6698ff', width=30, bd=1)
    name_label.grid(column=0,row=1,padx=50,pady=2)
    name_entry.grid(column=1,row=1,padx=50,pady=2)
    #class
    class_label = Label(frame_2, text='Class',
                           bg='#404040', fg='#2ce68c',
                           width=12, height=1, font='comicsansms 10 bold', padx=3, pady=2, relief=SUNKEN)
    class_entry = Entry(frame_2, bg='#def2ff', fg='#6698ff', width=30, bd=1)
    class_label.grid(column=0,row=2,padx=50,pady=2)
    class_entry.grid(column=1,row=2,padx=50,pady=2)
    #section
    section_label = Label(frame_2, text='Section',
                           bg='#404040', fg='#2ce68c',
                           width=12, height=1, font='comicsansms 10 bold', padx=3, pady=2, relief=SUNKEN)
    section_entry = Entry(frame_2, bg='#def2ff', fg='#6698ff', width=30, bd=1)
    section_label.grid(column=0,row=3,padx=50,pady=2)
    section_entry.grid(column=1,row=3,padx=50,pady=2)
    #roll no
    rollno_label = Label(frame_2, text='Roll No',
                           bg='#404040', fg='#2ce68c',
                           width=12, height=1, font='comicsansms 10 bold', padx=3, pady=2, relief=SUNKEN)
    rollno_entry = Entry(frame_2, bg='#def2ff', fg='#6698ff', width=30, bd=1)
    rollno_label.grid(column=0,row=4,padx=50,pady=2)
    rollno_entry.grid(column=1,row=4,padx=50,pady=2)
    #stuid
    stuid_label = Label(frame_2, text='Student ID',
                           bg='#404040', fg='#2ce68c',
                           width=12, height=1, font='comicsansms 10 bold', padx=3, pady=2, relief=SUNKEN)
    stuid_entry = Entry(frame_2, bg='#def2ff', fg='#6698ff', width=30, bd=1)
    stuid_label.grid(column=0,row=5,padx=50,pady=2)
    stuid_entry.grid(column=1,row=5,padx=50,pady=2)
    #school
    school_label = Label(frame_2, text='School',
                           bg='#404040', fg='#2ce68c',
                           width=12, height=1, font='comicsansms 10 bold', padx=3, pady=2, relief=SUNKEN)
    school_entry = Entry(frame_2, bg='#def2ff', fg='#6698ff', width=30, bd=1)
    school_label.grid(column=0,row=6,padx=50,pady=2)
    school_entry.grid(column=1,row=6,padx=50,pady=2)

    back_button = Button(frame_2, text='Back to login ', bg='#3b56cc', fg='white', font='comicsansms 10 bold', padx=1, pady=1,
                           width=8, height=1)
    back_button.bind('<Button-1>', back_login)
    back_button.grid(column=0, row=7)
    # sign up button to go signup page from login page
    signup_button=Button(frame_2,text='Singup',bg='#910303',fg='white',font='comicsansms 10 bold',padx=1,pady=1,
                        width=8,height=1)
   # signup_button.bind('<Button-1>',signup)
    signup_button.grid(column=1,row=7)

#define back to login from signup window
def back_login(event):
    frame_2.pack_forget()
    frame_1.config()
    login()

#------------------login window __main program__------------------

#label for  login and sign up defined here
label_head=Label(loginwindow,bg='#3b56cc',fg='white',font='dongle 10 bold',
                 width=80,height=2,padx=3,pady=2)
label_head.pack()
#frame from login func defined here
frame_1=Frame(loginwindow,bg='#6698ff',
              height=8,width=80)

#frame for signup func defined here
frame_2=Frame(loginwindow,bg='#6698ff',
              height=8,width=80)
frame_2.pack(side=TOP,anchor='n',fill=X)

login()

#---------------mainwindow program start here ---------
back_img=PhotoImage(file='icons8-back-to-30.png')
# --------------button 1 func define here-----------
def btn1_func(event):

    def playquiz_func(event):
        '''getting questionn, answer,option file '''
        qquiz_list = os.listdir(quizfolder_qpath)  # '''retireving list of files in question folder'''
        oquiz_list = os.listdir(quizfolder_opath)  # '''retireving list of files in option folder'''
        aquiz_list = os.listdir(quizfolder_apath)  # '''retireving list of files in ans folder'''

        def startquiz_func(x):
            nonlocal qquiz_list;oquiz_list;aquiz_list
            '''getting file name from folders '''
            pq_scrn2.pack_forget()
            '''packing  pq_scrn3 to show questions '''
            pq_scrn3.pack()

            ques_filenam=qquiz_list[x]
            ques_filenam1=ques_filenam.split('.')
            ques_filenam2=ques_filenam1[0]
            option_filenam=oquiz_list[x]
            ans_filenam=aquiz_list[x]
            '''confugring pq_screen 1'''
            lbl_sno.grid_forget()
            lbl_qnam.config(text='Name of quiz  : '+ques_filenam2)
            lbl_ply.grid_forget()
            entry_qcode.grid_forget()
            btnply.grid_forget()
            lbl_qcode.grid_forget()

            '''opening files here to show quiz'''
            ques_filehandle=open('.\\quizfolder\\qquizfolder\\'+ ques_filenam,'rb')
            option_filehandle = open('.\\quizfolder\\oquizfolder\\' + option_filenam, 'rb')
            ans_filehandle = open('.\\quizfolder\\aquizfolder\\' + ans_filenam, 'rb')

            '''getting list of questions,answers and option'''
            ques_list=pickle.load(ques_filehandle)
            option_list=pickle.load(option_filehandle)
            ans_list=pickle.load(ans_filehandle)

            '''no of questions count'''
            ques_no=len(ques_list)

            '''getting option a,b,c,d list'''
            option_a_list=option_list[0]
            option_b_list=option_list[1]
            option_c_list=option_list[2]
            option_d_list=option_list[3]

            '''user anser list here'''
            usr_ans=[]
            '''defining instruction label and start btn to show quiz'''
            label_instr=Label(pq_scrn3,text=f'1.This quiz contain {ques_no} questions'+'\n'+f'2.All questions are compulsory.'+'\n'+'3.Each questions is of 4 points.'+'\n'+'4.Total weightge of quiz {ques_no*4}'+'\n'+'5.All the best',
                              height=10,width=100,font='comicsansms 12 ',anchor=W)
            label_instr.grid(column=0,row=0,sticky=W)
            startbtn=Button(pq_scrn3,text="START",bg='#f5b120',fg='black',width=20,height=2,bd=0)
            startbtn.grid(column=0,row=1,sticky=N,pady=10)
            z=1    # it is a variable


            def startbtn_func(event):
                nonlocal z
                '''forgetting  start btn and instruction label here '''
                startbtn.grid_forget()
                label_instr.grid_forget()

                '''defining question label frame here to show questions to user '''
                ques_labelframe=ttk.Labelframe(pq_scrn3,text=f'Question- {z}',height=10,width=140)
                ques_labelframe.grid(column=0,row=0,sticky=W)

                '''defining question label and ans label'''
                ques_label=Label(ques_labelframe,text=ques_list[z-1],bg='white',fg='black',font='comicsansms 10 bold',
                                 anchor=NW,width=140,height=10)
                ques_label.grid(column=0,row=0,sticky='w')
                ans_label=Label(ques_labelframe, bg='#353c4d',width=140,height=2)
                ans_label.grid(column=0,row=1,sticky=W)
                more_label=Label(pq_scrn3, bg='#353c4d',width=130,height=2)
                more_label.grid(column=0,row=2,sticky=W)

                '''show option to user code here'''
                usrinput_var=StringVar()
                usrinput_var.set(None)
                '''defining dictionary here'''
                option_dict={'(A)'+option_a_list[z-1]:'A',
                             '(B)'+option_b_list[z-1]:'B',
                             '(C)'+option_c_list[z-1]:'C',
                            '(D)'+option_d_list[z-1]:'D',
                             }
                dumvar=-1 #definig a dummy variable here
                #ans_label.columnconfigure([0,1,2,3],weight=1,minsize=20) #configuring columns of ans label

                '''applying loop to cfeate loop for ans options'''
                for (text,value) in option_dict.items():
                    dumvar+=1
                    option_radiobtn=Radiobutton(ans_label,text=text,variable=usrinput_var,value=value,
                                                bg='white',fg='black',width=27,bd=0,font='comicsansms 10 bold',
                                                activebackground='#353c4d',activeforeground='White',anchor=W)
                    option_radiobtn.grid(row=0,column=dumvar,sticky='w',pady=5,padx=10,ipadx=5,ipady=5)

                def back_contraint ():
                    backques_btn.pack_forget()

                '''defining nextques_btn func here'''
                def nextquesbtn_func(event):
                    usrinput_get = usrinput_var.get()
                    usr_ans.append(usrinput_get)
                    nonlocal z
                    z+=1
                    nonlocal ques_no
                    nonlocal ans_list
                    if z>=ques_no+1:
                        nextques_btn.config(text='Save')
                        reply=messagebox.askyesno('Submit',"Do you want the Save?")


                        if reply==True:
                            marks=0
                            nonlocal ans_list
                            print(ans_list)
                            print(usr_ans)

                            for i in range(0,ques_no):
                                if usr_ans[i]==None :
                                    marks+=0
                                elif usr_ans[i]==ans_list[i] and usr_ans[i]!=None:
                                    marks+=1
                                else:
                                    pass
                            correct_ans=marks
                            incorrect_ans=ques_no-marks
                            messagebox.showinfo('Score',
f' Total correct answer:{correct_ans} \n Incorrect answer: {incorrect_ans} \n Total marks :{ques_no*4} \n You scored : {correct_ans*4}')
                            lbl_sno.grid(column=0, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
                            lbl_sno.config(text='S No.')
                            lbl_qnam.config(text='Name of Quiz ')
                            lbl_ply.grid(column=2, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
                            pq_scrn3.pack_forget()
                            entry_qcode.grid(column=4, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
                            btnply.grid(column=5, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
                            lbl_qcode.grid(column=3, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
                            ques_labelframe.grid_forget()
                            more_label.grid_forget()
                            nextques_btn.grid_forget()
                            pq_scrn2.pack(fill=BOTH,anchor=E,expand=True)

                    else:

                        ques_labelframe.config(text=f'Question- {z}')
                        nextques_btn.unbind('<Button-1>')
                        #nextques_btn.bind('<Button-1>',startbtn_func)
                        startbtn_func('<Button-1>')

                '''defining last ques btn'''
                def backquesbtn_func(event):
                    nonlocal z
                    z-=1
                    if z==0 :
                        back_contraint()
                    else:
                        usrinput_get=usrinput_var.get()
                        usr_ans.insert(z-1,usrinput_get)
                        ques_labelframe.config(text=f'Question- {z}')
                        backques_btn.unbind('<Button-1>')
                        #backques_btn.bind('<Button-1>',startbtn_func)
                        startbtn_func('<Button-1>')
                        print('kelo')

                '''defining next question and back question button'''
                nextques_btn=Button(more_label,text='Next',width=15,height=2,bg='#f5b120',fg='white',bd=0)
                nextques_btn.pack(side=RIGHT,anchor='e',padx=5,pady=3)
                nextques_btn.bind('<Button-1>',nextquesbtn_func)
                nextques_btn.bind('<Button-1>',smouseclick,add='+')
                backques_btn=Button(more_label, text='Back', width=15, height=2, bg='#f5b120', fg='white',bd=0)
                #backques_btn.pack(side=RIGHT, anchor='e',padx=5,pady=3)
                #lbl_fake = Label(more_label, width=15, height=2, bg='#353c4d', fg='white', bd=0)
                #lbl_fake.pack(side=LEFT, anchor='w', padx=15, pady=3)
                #backques_btn.bind('<Button-1>',backquesbtn_func)
                #backques_btn.bind('<Button-1>',smouseclick,add='+')

            '''startbtn bind here top func to startbtn_func'''
            startbtn.bind('<Button-1>',startbtn_func)
            startbtn.bind('<Button-1>',smouseclick,add='+')

        #----------play quiz main program
        '''main program of start vquiz'''
        playquizbtn.unbind('<Button-1>')
        # configuring status bar and quiz screen
        menu_label.config(text='>> Home >> Play quiz >> Start quiz  ')
        pq_scrn1= Canvas(playquiz_rframe, bg='#353c4d', height=4) # title screen
        pq_scrn1.pack(fill=X)
        pq_scrn2_scroll = Scrollbar(playquiz_rframe,orient=VERTICAL)
        pq_scrn2_scroll.pack(side=RIGHT,anchor=NW,fill=Y,padx=5)
        pq_scrn2 = Canvas(playquiz_rframe, bg='#353c4d',height=100,scrollregion=(0,0,700,700))
        pq_scrn2.pack(fill=BOTH,anchor=E,expand=True)
        pq_scrn2_scroll.config(command=pq_scrn2.yview)

        pq_scrn3 = Frame(playquiz_rframe, bg='#353c4d', height=100)
        pq_scrn3.pack(fill=BOTH, anchor=E, expand=True)
        pq_scrn3.pack_forget()


        #pq_scrn1 labels here
        lbl_sno = Label(pq_scrn1, text='S No.', font="comicsansms 10 bold", fg='white', bg='#353c4d',
                          height=1, width=20,pady=5)
        lbl_sno.grid(column=0, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
        lbl_qnam = Label(pq_scrn1, text='Name of Quiz ', font="comicsansms 10 bold", fg='white', bg='#353c4d',
                          height=1, width=20)#quiz name label
        lbl_qnam.grid(column=1, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
        lbl_ply= Label(pq_scrn1, text=' QuizCode', font="comicsansms 10 bold", fg='white', bg='#353c4d',
                          height=1, width=20,anchor='e') # play
        lbl_ply.grid(column=2, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
        lbl_qcode = Label(pq_scrn1, text='Enter quizcode here:', font="comicsansms 10 bold", fg='white', bg='#353c4d',
                        height=1, width=20, anchor='e')  # play
        lbl_qcode.grid(column=3, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
        qcode_var=IntVar()
        entry_qcode = Entry(pq_scrn1, bd=0, bg='#cfdee6', width=30,textvariable=qcode_var)
        entry_qcode.grid(column=4, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
        entry_qcode.focus()
        a=None
        def btnply_func(event):
            nonlocal a
            a=qcode_var.get()


        btnply = Button(pq_scrn1, text='   Play', font="comicsansms 10 bold", fg='white', bg='red', bd=0,
                         width=5, command= lambda : startquiz_func(a))
        btnply.grid(column=5, row=0, ipadx=5, ipady=2, pady=10, padx=30, sticky='e')
        btnply.bind('<Button-1>',btnply_func)

        #pq scrn 2 code defined here
        #qquiz_list is that list which contain all the quiz txt file name
        qfile_list=[] #creating list to save file name to print
        for i in qquiz_list:
            file_split=i.split('.')
            fil_nm=file_split[0]
            qfile_list.append(fil_nm)
        print(qfile_list)

        no_of_file=len(qquiz_list) # no of files in question folder


        for i in range(1,no_of_file):
            nam_of_file=qfile_list[i]
            lbl_strip = Label(pq_scrn2, fg='white', bg='#353c4d',  # 353c4d
                              height=2)  # it is defined to place the lbl sno,qnam,lby.play
            lbl_strip.pack(side=TOP, anchor=N,fill=X)
            lbl_sno1 = Label(lbl_strip, text=i, font="comicsansms 10 bold", fg='white', bg='#353c4d',
                             width=25)
            lbl_sno1.grid(column=0, row=0, ipadx=5, ipady=5, pady=10, sticky='w')
            lbl_qnam1 = Label(lbl_strip, text=nam_of_file, font="comicsansms 10 bold", fg='white', bg='#353c4d',
                              width=20)
            lbl_qnam1.grid(column=1, row=0, ipadx=5, ipady=5, pady=10, sticky='e')
            lbl_qcode1 = Label(lbl_strip, text=i, font="comicsansms 10 bold", fg='white', bg='#353c4d',
                             width=20)
            lbl_qcode1.grid(column=2, row=0, ipadx=5, ipady=5, pady=10, sticky='e')



        #definig option menu pq_scrn1
        #var_file = StringVar()
        #var_file.set(None)
        #set_var = var_file.set('Search...')
        #optionmenu_file = OptionMenu(pq_scrn1, set_var, *qfile_list)
        #optionmenu_file.config(width=30, bg='#353c4d', fg='white', bd=0, anchor=E)
        #optionmenu_file.grid(column=3, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='n')



    # function for bact to home menu defined hetre from addquiz feame
    def backbtn_func():
        menu_label.config(text="HOME")
        playquiz_lframe.pack_forget()
        playquiz_rframe.pack_forget()
        base_frame.pack(fill=BOTH, expand=True)
        backbtn.grid_forget()
        exit_btn.grid()

    # quiting home menu
    menu_label.config(text=">> Home >> Play quiz")
    base_frame.pack_forget()
    exit_btn.grid_forget()

    # craete new frame
    playquiz_lframe = Frame(main_window, bg='#353c4d', width=30)
    playquiz_lframe.pack(side=LEFT, fill=Y)
    playquiz_rframe = Frame(main_window, bg='#353c4d')
    playquiz_rframe.pack(fill=BOTH, expand=True)
    playquiz_lframe.columnconfigure(0, weight=1, minsize=25)
    status2_frame = Frame(playquiz_rframe, bg='#e8de80', height=20)
    status2_frame.pack(fill=X)
    status2_frame = Frame(playquiz_rframe, bg='#e8de80', width=2)
    status2_frame.pack(side=LEFT, fill=Y)

    # back btn definrd to go back in main menu
    backbtn = Button(status_frame, text='  Back', anchor=CENTER, bd=0, bg='#353c4d', font='comicsansms 10 bold',
                     width=80, image=back_img, compound=LEFT, command=backbtn_func)
    backbtn.grid(column=0, row=1, ipady=5, ipadx=5, pady=3, padx=3, sticky='e')
    backbtn.bind('<Button-1>', smouseclick)
    # button 1 tempororary
    playquizbtn = Button(playquiz_lframe, text='PLAY QUIZ', anchor=CENTER, width=20, height=2,
                           font='comicsansms 10 bold', bd=0, bg='#f5b120')
    playquizbtn.grid(column=0, row=0, ipady=1, ipadx=3, pady=5, padx=8, sticky='e')
    playquizbtn.bind('<Button-1>', playquiz_func)
    playquizbtn.bind('<Button-1>',smouseclick,add='+')
#-----------------btn1 function end here
#-----------------btn2 function start here----
def btn2_func(event):
    # defining eempty list
    ques_list = []
    option_a_list = []
    option_b_list = []
    option_c_list = []
    option_d_list = []
    option_list=[option_a_list,option_b_list,option_c_list,option_d_list]
    ans_list = []
    len1=len(ques_list)

    # --------define add quiz function here
    def create_quiz_func(event):
        nonlocal createquizbtn;editquizbtn;showqzbtn
        createquizbtn.unbind('<Button-1>')
        editquizbtn.unbind('<Button-1>')
        showqzbtn.unbind('<Button-1>')

        #configuring status bar and quiz screen
        menu_label.config(text='>> Home >> Add quiz >> Create quiz  ')
        cq_scrn1=Frame(addquiz_rframe, bg='#353c4d',height=4)
        cq_scrn1.pack(fill=X)
        cq_scrn2= Frame(addquiz_rframe, bg='#893c4d')
        cq_scrn2.pack(fill=BOTH, expand=True,anchor='e')
        #scrollbar insert code
        cq_scrn2_scrollbar=ttk.Scrollbar(cq_scrn2,orient=VERTICAL)
        cq_scrn2_scrollbar.pack(side=RIGHT,fill=Y,anchor=N,padx=7)




        def bk2_editquiz(event): #back to edit quiz menu
            menu_label.config(text='>> Home >> Add quiz >> Edit Quiz  ')
            cq_scrn1.pack_forget()
            cq_scrn2.pack_forget()
            edit_quiz_func('<Button-1')
        editquizbtn.bind('<Button-1>',bk2_editquiz)# going edit quiz menu
        editquizbtn.bind('<Button-1>', smouseclick, add='+')

        def bk2_showquiz(event):  # back to show quiz menu
            menu_label.config(text='>> Home >> Add quiz >> Edit Quiz  ')
            cq_scrn1.pack_forget()
            cq_scrn2.pack_forget()
            show_quiz_func('<Button-1')
        showqzbtn.bind('<Button-1>', bk2_showquiz)
        showqzbtn.bind('<Button-1>', smouseclick, add='+')


        #program to create quiz file

        #filnm=filename
        lbl_filnm=Label(cq_scrn1,text='Enter quiz title   :',font="comicsansms 10 bold",fg='white',bg='#353c4d',
                        height=1,width=20)
        lbl_filnm.grid(column=0,row=0,ipadx=5,ipady=5,pady=10,padx=5,sticky='w')
        filnm_var=StringVar()
        entry_filnm=Entry(cq_scrn1,bd=0,bg='#cfdee6',width=30,textvariable=filnm_var)
        entry_filnm.grid(column=1, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
        entry_filnm.focus()
        def sav_filnm(event):
            gfilnm=filnm_var.get() #gfilnm=get file from string var
            filtyp=gfilnm+'.bin' # file type is created only to crate if loop
            ques_gfilnm='\\'+gfilnm+'.bin' #giving text format file
            option_gfilnm = '\\o' + gfilnm + '.bin'  # giving text format
            ans_gfilnm='\\a'+gfilnm+'.bin' #giving text format file
            ques_path=quizfolder_qpath+ques_gfilnm # creating path for question file
            option_path=quizfolder_opath+option_gfilnm # creating path for question file
            ans_path=quizfolder_apath+ans_gfilnm # creating path for question file

            try:
                ques_filehandle=open(ques_path,'x')
                ques_filehandle.close()
                option_filehandle=open(option_path,'x')
                option_filehandle.close()
                ans_filehandle=open(ans_path,'x')
                ans_filehandle.close()
                addques_btn.grid(column=3, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
                messagebox.showinfo('Quiz created ', 'quiz created!')
            except:
                messagebox.showerror('Already exist','Please enter new quiz name')

        def add_question(event):
            nonlocal ques_list
            gfilnm = filnm_var.get()  # gfilnm=get file from string var
            filtyp = gfilnm + '.bin'  # file type is created only to crate if loop
            ques_gfilnm = '\\' + gfilnm + '.bin'  # giving text format file
            option_gfilnm = '\\o' + gfilnm + '.bin'  # giving text format
            ans_gfilnm = '\\a' + gfilnm + '.bin'  # giving text format file
            ques_path = quizfolder_qpath + ques_gfilnm  # creating path for question file
            option_path = quizfolder_opath + option_gfilnm  # creating path for question file
            ans_path = quizfolder_apath + ans_gfilnm  # creating path for question file

            #open the binary file in append mode
            ques_filehandle=open(ques_path,'a+b')
            option_filehandle=open(option_path,'a+b')
            ans_filehandle=open(ans_path,'a+b')
            '''defining some variables'''

            ques_labelframe=ttk.Labelframe(cq_scrn2,text=f'Question - {len(ques_list)+1}',labelanchor='nw')
            ques_labelframe.pack(side=RIGHT,anchor=N)
            qry_frame=Frame(ques_labelframe,bg='#353c4d')
            qry_frame.pack(side=BOTTOM,anchor=E,fill=X)


            #question input
            ques_input=st.ScrolledText(ques_labelframe,width=150,height=10)
            ques_input.pack()
            ques_input.focus()
            #option entry
            #option A entry code here
            option_a=StringVar()
            label_a=Label(ques_labelframe,text="[A]")
            label_a.pack(side=LEFT,ipady=3,ipadx=3,pady=3,padx=6)
            entry_a=Entry(ques_labelframe,textvariable=option_a,width=35)
            entry_a.pack(side=LEFT,ipady=3,ipadx=3,pady=3,padx=6)
            #option b entry code here
            option_b = StringVar()
            label_b= Label(ques_labelframe, text="[B]")
            label_b.pack(side=LEFT, ipady=3, ipadx=3, pady=3, padx=6)
            entry_b = Entry(ques_labelframe,textvariable=option_b, width=35)
            entry_b.pack(side=LEFT,ipady=3,ipadx=3,pady=3,padx=6)

            #option c entry code here
            option_c = StringVar()
            label_c= Label(ques_labelframe, text="[C]")
            label_c.pack(side=LEFT, ipady=3, ipadx=3, pady=3, padx=6)
            entry_c = Entry(ques_labelframe,textvariable=option_c, width=35)
            entry_c.pack(side=LEFT,ipady=3,ipadx=3,pady=3,padx=6)

            #option d entry  code here
            option_d= StringVar()
            label_d= Label(ques_labelframe, text="[D]")
            label_d.pack(side=LEFT, ipady=3, ipadx=3, pady=3, padx=6)
            entry_d = Entry(ques_labelframe,textvariable=option_d, width=35)
            entry_d.pack(side=LEFT,ipady=3,ipadx=3,pady=3,padx=6)

            #correct answer entry code
            option1_list=['A','B','C','D']  #another option_list already defined thats why here option1_list defined
            option_ans = StringVar()
            option_ans.set(None)
            label_ans = Label(qry_frame, text="[Correct answer]",bg='#353c4d',fg='white')
            label_ans.pack(side=LEFT, ipady=3, ipadx=3, pady=3, padx=6)
            optionmenu_ans=OptionMenu(qry_frame,option_ans,*option1_list)
            optionmenu_ans. config(width=10,bg='#353c4d',fg='white',bd=0)
            optionmenu_ans.pack(side=LEFT, ipady=3, ipadx=3, pady=3, padx=6)
            #define function for to add more question
            def addmore_func(event):
                nonlocal addmore_btn;addques_btn
                nonlocal ques_list;option_a_list;option_b_list;option_c_list;option_d_list;ans_list
                #get input that user has givem
                get_ques=ques_input.get('0.0',END)
                get_option_a=option_a.get()
                get_option_b=option_b.get()
                get_option_c=option_c.get()
                get_option_d=option_d.get()
                get_option_ans=option_ans.get()


                #appending list given by user
                try:
                    ques_list.append(get_ques)
                    option_a_list.append(get_option_a)
                    option_b_list.append(get_option_b)
                    option_c_list.append(get_option_c)
                    option_d_list.append(get_option_d)
                    ans_list.append(get_option_ans)
                    len1=len(ques_list)+1
                    ques_labelframe.config(text=f'Question - {len1}')

                    ques_input.delete('0.0',END)
                    entry_a.delete('0',END)
                    entry_b.delete('0', END)
                    entry_c.delete('0', END)
                    entry_d.delete('0', END)
                    #ques_labelframe.pack_forget()
                    optionmenu_ans.config(option_ans.set(None))
                except:
                    messagebox.showerror('error','error')

                addques_btn.unbind('Button-1')
                addmore_btn.unbind('Button-1')
                addmore_btn.bind('Button-1', add_question)


            def save_func(event):
                nonlocal addmore_btn;
                addques_btn
                nonlocal ques_list;
                option_a_list;
                option_b_list;
                option_c_list;
                option_d_list;
                ans_list
                # get input that user has givem
                get_ques = ques_input.get('0.0', END)
                get_option_a = option_a.get()
                get_option_b = option_b.get()
                get_option_c = option_c.get()
                get_option_d = option_d.get()
                get_option_ans = option_ans.get()

                # appending list given by user
                try:
                    ques_list.append(get_ques)
                    option_a_list.append(get_option_a)
                    option_b_list.append(get_option_b)
                    option_c_list.append(get_option_c)
                    option_d_list.append(get_option_d)
                    ans_list.append(get_option_ans)
                    #erasing
                    ques_input.delete('0.0', END)
                    entry_a.delete('0', END)
                    entry_b.delete('0', END)
                    entry_c.delete('0', END)
                    entry_d.delete('0', END)
                    optionmenu_ans.config(option_ans.set(None))
                    reply=messagebox.askyesno('Save',"Do you want save the  Quiz?")
                    if reply==True :
                        pickle.dump(ques_list,ques_filehandle)
                        pickle.dump(option_list,option_filehandle)
                        pickle.dump(ans_list,ans_filehandle)
                        ques_filehandle.close()
                        option_filehandle.close()
                        ans_filehandle.close()
                    else:
                        pass


                except:
                    pass


            #code for save and add more button
            addmore_btn = Button(qry_frame, text='+ Add more', font='comicsansms 10 bold', width=10,
                                height=1, bd=0, bg='#e63535', fg='white')
            addmore_btn.pack(side=RIGHT, anchor=N, pady=5, padx=10, ipadx=15, ipady=5)
            addmore_btn.bind('<Button-1>',addmore_func)
            addmore_btn.bind('<Button-1>',smouseclick,add='+')

            save_btn = Button(qry_frame, text='Save', font='comicsansms 10 bold', width=10,
                             height=1, bd=0, bg='#e63535', fg='white')
            save_btn.pack(side=RIGHT, anchor=N, pady=5, padx=10, ipadx=15, ipady=5)
            save_btn.bind('<Button-1>',save_func)
            save_btn.bind('<Button-1>',smouseclick,add='+')


        # ---------------
        addques_btn = Button(cq_scrn1, text='add question', font='comicsansms 10 bold', width=10,
                                     height=1, bd=0,bg='#e63535', fg='white')
        addques_btn.grid(column=3, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
        addques_btn.grid_forget()
        addques_btn.bind('<Button-1>', add_question)
        addques_btn.bind('<Button-1>',smouseclick,add='+')

        crt_btn=Button(cq_scrn1,text='Create',font='comicsansms 10 bold',width=8,height=1,bd=0,
                       bg='#e63535',fg='white')
        crt_btn.grid(column=2, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
        crt_btn.bind('<Button-1>',sav_filnm)
        crt_btn.bind('<Button-1>',smouseclick,add='+')

    #---------defining edit quiz function here
    def edit_quiz_func(event):

        nonlocal createquizbtn;editquizbtn;showqzbtn ; ques_list

        createquizbtn.unbind('<Button-1>')
        editquizbtn.unbind('<Button-1>')
        showqzbtn.unbind('<Button-1>')

        #configuring status bar and quiz screen
        menu_label.config(text='>> Home >> Add quiz >> Edit Quiz  ')

        cq_scrn=Frame(addquiz_rframe, bg='#353c4d')
        cq_scrn.pack(fill=BOTH,expand=True)

        def bk2_createquiz(event):  # back to create quiz menu
            menu_label.config(text='>> Home >> Add quiz >> Create Quiz  ')
            cq_scrn.pack_forget()
            create_quiz_func('<Button-1')

        createquizbtn.bind('<Button-1>', bk2_createquiz)  # going edit quiz menu
        createquizbtn.bind('<Button-1>', smouseclick, add='+')

        def bk2_showquiz(event):  # back to show quiz menu
            menu_label.config(text='>> Home >> Add quiz >> Show Quiz  ')
            cq_scrn.pack_forget()
            show_quiz_func('<Button-1')
        showqzbtn.bind('<Button-1>', bk2_showquiz)
        showqzbtn.bind('<Button-1>', smouseclick, add='+')


        # edit scren program start here
        lbl_filnm = Label(cq_scrn, text=' edit quiz screen    :', font="comicsansms 10 bold", fg='white', bg='#353c4d',
                          height=1, width=20)
        lbl_filnm.grid(column=0, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')
    # edit quiz function end here
    #________________

    #---------definig show quiz function here

    def show_quiz_func(event):
        #undindind here thre function
        nonlocal createquizbtn;editquizbtn;showqzbtn
        createquizbtn.unbind('<Button-1>')
        editquizbtn.unbind('<Button-1>')
        showqzbtn.unbind('<Button-1>')

        #configuring status bar and quiz screen
        menu_label.config(text='>> Home >> Add quiz >> Show Quiz ')
        cq_scrn=Frame(addquiz_rframe, bg='#353c4d')
        cq_scrn.pack(fill=BOTH,expand=True)
        # interchanging b/w add,edit,show quiz
        def bk2_createquiz(event):  # back to create quiz menu
            menu_label.config(text='>> Home >> Add quiz >> Create Quiz  ')
            cq_scrn.pack_forget()
            create_quiz_func('<Button-1')

        createquizbtn.bind('<Button-1>', bk2_createquiz)  # going edit quiz menu
        createquizbtn.bind('<Button-1>', smouseclick, add='+')

        def bk2_editquiz(event):  # back to edit quiz menu
            menu_label.config(text='>> Home >> Add quiz >> Edit Quiz  ')
            cq_scrn.pack_forget()
            edit_quiz_func('<Button-1')

        editquizbtn.bind('<Button-1>', bk2_editquiz)
        editquizbtn.bind('<Button-1>',smouseclick,add='+')


        lbl_filnm = Label(cq_scrn, text=' show quiz screen    :', font="comicsansms 10 bold", fg='white', bg='#353c4d',
                          height=1, width=20)
        lbl_filnm.grid(column=0, row=0, ipadx=5, ipady=5, pady=10, padx=5, sticky='w')

   #-----function definition of three buttons end above i.e add ,edit , show

  #function for bact to home menu defined hetre from addquiz feame
    def backbtn_func(event):
        menu_label.config(text="HOME")
        addquiz_lframe.pack_forget()
        addquiz_rframe.pack_forget()
        base_frame.pack(fill=BOTH,expand=True)
        backbtn.grid_forget()
        exit_btn.grid()

    #quiting home menu
    menu_label.config(text=">> Home >> Add quiz")
    base_frame.pack_forget()
    exit_btn.grid_forget()

    #craete new frame
    addquiz_lframe=Frame(main_window, bg='#353c4d',width=30)
    addquiz_lframe.pack(side=LEFT,fill=Y)
    addquiz_rframe = Frame(main_window, bg='#353c4d')
    addquiz_rframe.pack(fill=BOTH, expand=True)
    addquiz_lframe.columnconfigure(0,weight=1,minsize=25)
    status2_frame = Frame(addquiz_rframe, bg='#e8de80', height=20)
    status2_frame.pack(fill=X)
    status2_frame = Frame(addquiz_rframe, bg='#e8de80', width=2)
    status2_frame.pack(side=LEFT, fill=Y)

    #back btn definrd to go back in main menu
    backbtn=Button(status_frame, text='  Back', anchor=CENTER, bd=0, bg='#353c4d',font='comicsansms 10 bold',
                   width=80,image=back_img,compound=LEFT)
    backbtn.bind('<Button-1>',backbtn_func)
    backbtn.bind('<Button-1>',smouseclick,add='+')
    backbtn.grid(column=0, row=1, ipady=5, ipadx=5, pady=3, padx=3,sticky='e')
    #cretequit button inserted
    createquizbtn = Button(addquiz_lframe, text='CEREATE QUIZ', anchor=CENTER, width=20, height=2,
                           font='comicsansms 10 bold',bd=0, bg='#f5b120')
    createquizbtn.grid(column=0, row=0, ipady=1, ipadx=3, pady=5, padx=8,sticky='e')
    createquizbtn.bind('<Button-1>',create_quiz_func)
    createquizbtn.bind('<Button-1>', smouseclick, add='+')
    #edit quiz button
    editquizbtn = Button(addquiz_lframe, text='EDIT QUIZ', anchor=CENTER, width=20, height=2,
                         font='comicsansms 10 bold',bd=0, bg='#f5b120')
    editquizbtn.grid(column=0, row=1, ipady=1, ipadx=3, pady=5, padx=8, sticky='e')
    editquizbtn.bind('<Button-1>', edit_quiz_func)
    editquizbtn.bind('<Button-1>', smouseclick, add='+')
    #show quiz btn
    showqzbtn= Button(addquiz_lframe, text='SHOW QUIZ', anchor=CENTER, width=20, height=2,
                         font='comicsansms 10 bold', bd=0, bg='#f5b120')
    showqzbtn.grid(column=0, row=2, ipady=1, ipadx=3, pady=3, padx=8, sticky='e')
    showqzbtn.bind('<Button-1>',show_quiz_func)
    showqzbtn.bind('<Button-1>', smouseclick,add='+')
#--------------------------------------btn2 func ends here------------------

# --------------button 3 func define here-----------
def btn3_func(event):
    # function for bact to home menu defined hetre from addquiz feame
    def backbtn_func():
        menu_label.config(text="HOME")
        rcdquiz_lframe.pack_forget()
        rcdquiz_rframe.pack_forget()
        base_frame.pack(fill=BOTH, expand=True)
        backbtn.grid_forget()
        exit_btn.grid()

    # quiting home menu
    menu_label.config(text=">> Home >> Records")
    base_frame.pack_forget()
    exit_btn.grid_forget()

    # craete new frame
    #rcd=record
    rcdquiz_lframe = Frame(main_window, bg='#353c4d', width=30)
    rcdquiz_lframe.pack(side=LEFT, fill=Y)
    rcdquiz_rframe = Frame(main_window, bg='#353c4d')
    rcdquiz_rframe.pack(fill=BOTH, expand=True)
    rcdquiz_lframe.columnconfigure(0, weight=1, minsize=25)
    status2_frame = Frame(rcdquiz_rframe, bg='#e8de80', height=20)
    status2_frame.pack(fill=X)
    status2_frame = Frame(rcdquiz_rframe, bg='#e8de80', width=2)
    status2_frame.pack(side=LEFT, fill=Y)

    # back btn definrd to go back in main menu
    backbtn = Button(status_frame, text='  Back', anchor=CENTER, bd=0, bg='#353c4d', font='comicsansms 10 bold',
                     width=80, image=back_img, compound=LEFT, command=backbtn_func)
    backbtn.bind('<Button-1>', smouseclick)
    backbtn.grid(column=0, row=1, ipady=5, ipadx=5, pady=3, padx=3, sticky='e')
    # button 1 tempororary
    createquizbtn = Button(rcdquiz_lframe, text='PLAY QUIZ', anchor=CENTER, width=20, height=2,
                           font='comicsansms 10 bold', bd=0, bg='#f5b120')
    createquizbtn.grid(column=0, row=0, ipady=1, ipadx=3, pady=5, padx=8, sticky='e')
#-----------------btn3 function end here

# --------------button 4 func define here-----------
def btn4_func(event):
    # function for bact to home menu defined hetre from addquiz feame
    def backbtn_func():
        menu_label.config(text="HOME")
        helpquiz_lframe.pack_forget()
        helpquiz_rframe.pack_forget()
        base_frame.pack(fill=BOTH, expand=True)
        backbtn.grid_forget()
        exit_btn.grid()

    # quiting home menu
    menu_label.config(text=">> Home >> Help")
    base_frame.pack_forget()
    exit_btn.grid_forget()

    # craete new frame
    helpquiz_lframe = Frame(main_window, bg='#353c4d', width=30)
    helpquiz_lframe.pack(side=LEFT, fill=Y)
    helpquiz_rframe = Frame(main_window, bg='#353c4d')
    helpquiz_rframe.pack(fill=BOTH, expand=True)
    helpquiz_lframe.columnconfigure(0, weight=1, minsize=25)
    status2_frame = Frame(helpquiz_rframe, bg='#e8de80', height=20)
    status2_frame.pack(fill=X)
    status2_frame = Frame(helpquiz_rframe, bg='#e8de80', width=2)
    status2_frame.pack(side=LEFT, fill=Y)

    # back btn definrd to go back in main menu
    backbtn = Button(status_frame, text='  Back', anchor=CENTER, bd=0, bg='#353c4d', font='comicsansms 10 bold',
                     width=80, image=back_img, compound=LEFT, command=backbtn_func)
    backbtn.bind('<Button-1>', smouseclick)
    backbtn.grid(column=0, row=1, ipady=5, ipadx=5, pady=3, padx=3, sticky='e')

    # button 1 tempororary
    createquizbtn = Button(helpquiz_lframe, text='Help', anchor=CENTER, width=20, height=2,
                           font='comicsansms 10 bold', bd=0, bg='#f5b120')
    createquizbtn.grid(column=0, row=0, ipady=1, ipadx=3, pady=5, padx=8, sticky='e')
#-----------------btn1 function end here

#app label code here
#icon image here
app_icon=PhotoImage(file='icons8-machine-learning-30.png')
#app label here
app_label=Label(main_window,text='        𝐐𝐔𝐈𝐙𝐌𝐀𝐍𝐈𝐀',
                bg='#ebac26',fg='#000000',font="comicsansms 25 bold",anchor='w'
                )
app_label.pack(fill=X)
#app icon defined here
app_ic=Label(app_label,image=app_icon,anchor='w',bg='#ebac26',)
app_ic.pack(side=LEFT,ipady=8)
#btn others and contact defined here to applabel
btn_5=Button(app_label,text='others',anchor=CENTER,width=10,height=2,bd=0,bg='#f5b120')
btn_5.pack(side=RIGHT,ipady=1,ipadx=3,pady=3,padx=3)
btn_6=Button(app_label,text='Contact us',anchor=CENTER,width=10,height=2,bd=0,bg='#f5b120')
btn_6.pack(side=RIGHT,ipady=1,ipadx=3,pady=3,padx=3)
btn_7=Button(app_label,text='About us',anchor=CENTER,width=10,height=2,bd=0,bg='#f5b120')
btn_7.pack(side=RIGHT,ipady=1,ipadx=3,pady=3,padx=3)



#menu label defined here
menu_label=Label(main_window,text='>> Home',anchor=W,bg='#e8de80',fg="black",font='comicsansms 10 ')
menu_label.pack(fill=X,ipady=5)
#status frame defined here
status_frame=Frame(main_window,bg='#353c4d',height=30)
status_frame.pack(fill=X)
sep_frame=ttk.Separator(status_frame,orient='horizontal')
sep_frame.grid(sticky=S)
##------exit func here
def exit_func(event):
    answer=messagebox.askyesno('Quit','do you want to quit?')
    if answer==True:
        main_window.destroy()
# exit button defined here
exit_btn=Button(status_frame,text='  Exit',bg='#353c4d',fg='white',font='comicsansms 15 bold',
                image=back_img,compound=LEFT,width=80,bd=0)
exit_btn.grid(column=0,row=0,sticky='nw')
exit_btn.bind('<Button-1>',exit_func)
exit_btn.bind('<Button-1>',smouseclick,add='+')
#base frame defined here
base_frame=Frame(main_window,bg='#353c4d')
base_frame.pack(fill=BOTH,expand=True)
#----------code for base frame here
base_frame.columnconfigure(0,weight=2,minsize=10)
base_frame.columnconfigure(1,weight=5,minsize=10)
base_frame.rowconfigure([0,1,2,3,4,5],weight=1,minsize=10)


fimg1=PhotoImage(file='business-3d-task.png')
fimg2=PhotoImage(file='icons8-puzzle-60.png')#btn1
fimg3=PhotoImage(file='icons8-plus-+-60.png')#btn2
fimg4=PhotoImage(file='icons8-icons8-50.png')#btn3
fimg5=PhotoImage(file='icons8-support-60.png')#btn4


lbl_fimg1=Label(base_frame,bg='#353c4d',image=fimg1)
lbl_fimg1.grid(column=1,row=0,columnspan=5,rowspan=7)

btn_1=Button(base_frame,image=fimg2,width=50,height=50,bd=0,bg='#f5b120')
btn_1.bind('<Button-1>',btn1_func)
btn_1.grid(column=0,row=1,ipady=1,ipadx=3,pady=3,padx=3,sticky='ne')
btn_1.bind('<Button-1>',btn1_func)
btn_1.bind('<Button-1>',smouseclick,add='+')
btn_2=Button(base_frame,image=fimg3,width=50,height=50,bd=0,bg='#f5b120')
btn_2.grid(column=0,row=2,ipady=1,ipadx=3,pady=3,padx=3,sticky='ne')
btn_2.bind('<Button-1>',btn2_func)
btn_2.bind('<Button-1>',smouseclick,add='+')
btn_3=Button(base_frame,image=fimg4,width=50,height=50,bd=0,bg='#f5b120',command=smouseclick)
btn_3.grid(column=0,row=3,ipady=1,ipadx=3,pady=3,padx=3,sticky='ne')
btn_3.bind('<Button-1>',btn3_func)
btn_3.bind('<Button-1>',smouseclick,add='+')
btn_4=Button(base_frame,image=fimg5,width=50,height=50,bd=0,bg='#f5b120')
btn_4.grid(column=0,row=4,ipady=1,ipadx=3,pady=3,padx=3,sticky='ne')
btn_4.bind('<Button-1>',btn4_func)
btn_4.bind('<Button-1>',smouseclick,add='+')





loginwindow.mainloop()
main_window.mainloop()
