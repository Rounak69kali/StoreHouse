import tkinter as tk
from tkinter import ttk 
import time as tm
import threading

# ------------------------------------------------------------------Description & Use Case--------------------------------------------------------------
# A simple yet effective Typing Speed Calculator built using Python and Tkinter. 
# This project allows users to test and improve their typing speed in Words Per Minute (WPM) while also tracking accuracy. 
# Designed with a user-friendly interface, the app provides real-time feedback and helps enhance both typing speed and precision.

# Use Case
# Great for beginners or professionals who want to improve typing skills, measure typing performance, or simply practice for fun.
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# *********************************************************************************************************Complete-Backend*******************************************************************************
# Initial Variables

timelimit = 10
remainingtime = timelimit
elpasedtime = 0
elpasedtimeInMinute = 0
totalwords = 0
wrong_words = 0
wpm = 0
accuracy = 0

def start_timer():
    global elpasedtime, remainingtime

    try:
        entry.focus()
        entry.config(state='normal')
        btn_start.config(state='disabled')
    except Exception as e:
        print("Error accessing entry or button widgets:", e)
        return

    for time in range(1, (timelimit + 1)):
        try:
            elpasedtime = time
            lbl_elpasedTimer['text'] = elpasedtime

            updatedRemainingtime = remainingtime - elpasedtime
            lbl_remainingTimer['text'] = updatedRemainingtime

            tm.sleep(1)
            window.update()
        except Exception as e:
            print("Runtime error during timer update:", e)
            break

    try:
        entry.config(state='disabled')
        btn_reset.config(state='normal')
    except Exception as e:
        print("Error updating widgets at end of timer:", e)


# To Count the Wrong Words
def count():
    global wrong_words
    global elpasedtime
    global elpasedtimeInMinute

    try:
        para_words = lbl_paragraph['text'].split()
    except Exception as e:
        print("Error accessing paragraph label text:", e)
        return

    try:
        while elpasedtime != timelimit:
            enteredParagraph = entry.get(1.0, 'end-1c').split()
            totalwords = len(enteredParagraph)
    except Exception as e:
        print("Error getting user input from text widget:", e)
        return

    try:
        for pair in list(zip(para_words, enteredParagraph)):
            if pair[0] != pair[1]:
                wrong_words += 1

        elpasedtimeInMinute = elpasedtime / 60

        wpm = (totalwords - wrong_words) / elpasedtimeInMinute
        gross_wpm = totalwords / elpasedtimeInMinute
        accuracy = (wpm / gross_wpm) * 100

        lbl_wpm['text'] = round(wpm)
        lbl_totalwords['text'] = totalwords
        lbl_accuracy['text'] = str(round(accuracy, 2)) + "%"
        lbl_wrongwords['text'] = wrong_words

    except ZeroDivisionError:
        print("Elapsed time is zero. Avoiding division by zero.")
    except Exception as e:
        print("Error during WPM and accuracy calculation or label updates:", e)



def reset():
    global remainingtime
    global elpasedtime
    global wrong_words

    try:
        btn_reset.config(state='disabled')
        btn_start.config(state='normal')
    except Exception as e:
        print("Error configuring buttons during reset:", e)

    try:
        entry.config(state='normal')
        entry.delete(1.0, tk.END)
        entry.config(state='disabled')
    except Exception as e:
        print("Error resetting the entry widget:", e)

    try:
        remainingtime = timelimit
        elpasedtime = 0
        wrong_words = 0

        lbl_remainingTimer['text'] = timelimit
        lbl_elpasedTimer['text'] = 0
        lbl_wpm['text'] = 0
        lbl_accuracy['text'] = "0%"
        lbl_totalwords['text'] = 0
        lbl_wrongwords['text'] = 0
    except Exception as e:
        print("Error resetting labels or variables:", e)


      

# -------------------------------------------------------------------------------------------------------------------------------
# To Count Wrong Words by Chat gpt
# def count():
#     global wrong_words, elpasedtime, elpasedtimeInMinute
#     global wpm, totalwords

#     para_words = lbl_paragraph['text'].split()
#     enteredPara = entry.get(1.0, 'end-1c').split()
#     totalwords = len(enteredPara)

#     for pair in zip(para_words, enteredPara):
#         if pair[0] != pair[1]:
#             wrong_words += 1

#     elpasedtimeInMinute = elpasedtime / 60
#     wpm = (totalwords - wrong_words) / elpasedtimeInMinute

#     lbl_wpm['text'] = wpm
#     lbl_totalwords['text'] = totalwords
#     lbl_wrongwords['text'] = wrong_words

# -------------------------------------------------------------------------------------------------------------------------------

# Funtion Using Thread Operation for Smooth working
def star():
    thread1 = threading.Thread(target=start_timer)
    thread1.start()
    thread2 = threading.Thread(target=count)
    thread2.start()


# ********************************************************************************************* Complete-GUI ****************************************************************************

window = tk.Tk()
window.title("Typing Speed Calculator")
window.geometry("1000x998+250+0")
window.resizable(False,False)

#Maine Frame
main_frame = tk.Frame(window,bg='Yellow',bd=9)

#Title Frame
frame_title = tk.Frame(main_frame,bg='orange',relief='flat')
lable = tk.Label(frame_title,text='Typing Speed Calculator',font='algerian 35 bold',bg='blue',fg='Red',relief='flat',bd=10,width=30)
lable.grid(pady=10)
frame_title.grid()


#Test Frame
selected_paragraph = "In a world that moves at an increasingly fast pace, taking a moment to pause and reflect can make all the difference. Imagine waking up early on a crisp morning, the sun gently streaming through the curtains, and the air still tinged with the coolness of dawn. The kettle whistles softly in the kitchen, promising the comfort of a warm cup of tea. Outside, the streets begin to stir—footsteps echo, distant conversations hum, and the world slowly comes to life. In that moment, there's a sense of calm, of clarity, of purpose. It reminds us that while we chase deadlines and dreams, the quiet in-between moments often hold the deepest meaning. Speaking clearly, listening intently, and choosing your words carefully—these are the marks of a thoughtful speaker. And in the art of communication, it's not only what you say, but how you say it, that truly leaves a lasting impression."
frame_taste = tk.LabelFrame(main_frame,text="Type From Here...",font='algerian 25 bold',bg='white',relief='groove')
#Paragraph
lbl_paragraph = tk.Label(frame_taste,text=selected_paragraph,font='Tahoma 13 bold',wraplength=990,justify='left')
lbl_paragraph.grid(row=0,column=0,pady=15)
#InputBox
entry = tk.Text(frame_taste,height=3,width=110,bd=5,relief='groove',font='Tahoma 10 bold')
entry.grid(row=1,column=0,pady=1,padx=5)
entry.config(state='disabled')

frame_taste.grid(row=1,column=0)

#Output Frame
frame_output = tk.Frame(main_frame,bg='Yellow')
frame_labels = tk.Frame(frame_output,bg='yellow')

#Elpased Time
lbl_elpasedTime = tk.Label(frame_labels,text="Elpased Time",fg='red',bg='yellow',font='Algerian 15 bold')
lbl_elpasedTimer = tk.Label(frame_labels,text='0',font='Algerian 15 bold',fg='black',bg='yellow')
lbl_elpasedTime.grid(row=0,column=0)
lbl_elpasedTimer.grid(row=0,column=1,padx=4,pady=3)
#Remaining Time
lbl_remainingTime = tk.Label(frame_labels,text="Remaining Time",fg='red',bg='Yellow',font='Algerian 15 bold')
lbl_remainingTimer = tk.Label(frame_labels,text=remainingtime,font='Algerian 15 bold',fg='black',bg='Yellow')
lbl_remainingTime.grid(row=0,column=2)
lbl_remainingTimer.grid(row=0,column=3,padx=4,pady=3)
#WPM
lbl_wpmtitle = tk.Label(frame_labels,text="WPM",fg='red',bg='Yellow',font='Algerian 15 bold')
lbl_wpm = tk.Label(frame_labels,text='0',font='Algerian 15 bold',fg='black',bg='Yellow')
lbl_wpmtitle.grid(row=0,column=4)
lbl_wpm.grid(row=0,column=5,padx=4,pady=3)
#Accuracy
lbl_accuracytitle = tk.Label(frame_labels,text="Accuracy",fg='red',bg='Yellow',font='Algerian 15 bold')
lbl_accuracy = tk.Label(frame_labels,text='0%',font='Algerian 15 bold',fg='black',bg='Yellow')
lbl_accuracytitle.grid(row=0,column=6)
lbl_accuracy.grid(row=0,column=7,padx=4,pady=3)
#Total Words
lbl_totalwordstitle = tk.Label(frame_labels,text="Total Words",fg='red',bg='Yellow',font='Algerian 15 bold')
lbl_totalwords = tk.Label(frame_labels,text='0',font='Algerian 15 bold',fg='black',bg='Yellow')
lbl_totalwordstitle.grid(row=0,column=8)
lbl_totalwords.grid(row=0,column=9,padx=4,pady=3)
#Wrong Words
lbl_wrongwordstitle = tk.Label(frame_labels,text="Wrong Words",fg='red',bg='Yellow',font='Algerian 15 bold')
lbl_wrongwords = tk.Label(frame_labels,text='0',font='Algerian 15 bold',fg='black',bg='Yellow')
lbl_wrongwordstitle.grid(row=0,column=8)
lbl_wrongwords.grid(row=0,column=9,padx=4,pady=3)


frame_labels.grid(row=0)

#Control Frame
frame_control = tk.Frame(frame_output,bg='yellow')

#Start Button
btn_start = ttk.Button(frame_control,text='START',width=47,command=star)
btn_start.grid(row=0,column=0,padx=90,pady=15)

#Reset Button
btn_reset = ttk.Button(frame_control,text='RESET',width=47,command=reset)
btn_reset.grid(row=0,column=1,padx=90,pady=15)
btn_reset.config(state='disabled')

frame_control.grid(row=1)

frame_output.grid(row=2,column=0)

#Keyboard Frame

frame_keyboard = tk.Frame(main_frame,bg='Yellow')

# 1 to 0
frame_1to0 = tk.Frame(frame_keyboard,bg='Yellow')
lbl_1 = tk.Label(frame_1to0,text='1',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_2 = tk.Label(frame_1to0,text='2',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_3 = tk.Label(frame_1to0,text='3',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_4 = tk.Label(frame_1to0,text='4',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_5 = tk.Label(frame_1to0,text='5',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_6 = tk.Label(frame_1to0,text='6',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_7 = tk.Label(frame_1to0,text='7',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_8 = tk.Label(frame_1to0,text='8',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_9 = tk.Label(frame_1to0,text='9',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_0 = tk.Label(frame_1to0,text='0',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)

lbl_1.grid(row=0,column=0,padx=15,pady=5)
lbl_2.grid(row=0,column=1,padx=15,pady=5)
lbl_3.grid(row=0,column=2,padx=15,pady=5)
lbl_4.grid(row=0,column=3,padx=15,pady=5)
lbl_5.grid(row=0,column=4,padx=15,pady=5)
lbl_6.grid(row=0,column=5,padx=15,pady=5)
lbl_7.grid(row=0,column=6,padx=15,pady=5)
lbl_8.grid(row=0,column=7,padx=15,pady=5)
lbl_9.grid(row=0,column=8,padx=15,pady=5)
lbl_0.grid(row=0,column=9,padx=15,pady=5)
frame_1to0.grid(row=0)
# Q to P
frame_QtoP = tk.Frame(frame_keyboard,bg='Yellow')
lbl_Q = tk.Label(frame_QtoP,text='Q',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_W = tk.Label(frame_QtoP,text='W',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_E = tk.Label(frame_QtoP,text='E',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_R = tk.Label(frame_QtoP,text='R',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_T = tk.Label(frame_QtoP,text='T',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_Y = tk.Label(frame_QtoP,text='Y',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_U = tk.Label(frame_QtoP,text='U',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_I = tk.Label(frame_QtoP,text='I',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_O = tk.Label(frame_QtoP,text='O',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_P = tk.Label(frame_QtoP,text='P',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)

lbl_Q.grid(row=0,column=0,padx=12,pady=5)
lbl_W.grid(row=0,column=1,padx=12,pady=5)
lbl_E.grid(row=0,column=2,padx=12,pady=5)
lbl_R.grid(row=0,column=3,padx=12,pady=5)
lbl_T.grid(row=0,column=4,padx=12,pady=5)
lbl_Y.grid(row=0,column=5,padx=12,pady=5)
lbl_U.grid(row=0,column=6,padx=12,pady=5)
lbl_I.grid(row=0,column=7,padx=12,pady=5)
lbl_O.grid(row=0,column=8,padx=12,pady=5)
lbl_P.grid(row=0,column=9,padx=12,pady=5)
frame_QtoP.grid(row=1)
# A to L
frame_AtoL = tk.Frame(frame_keyboard,bg='Yellow')
lbl_A = tk.Label(frame_AtoL,text='A',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_S = tk.Label(frame_AtoL,text='S',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_D = tk.Label(frame_AtoL,text='D',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_F = tk.Label(frame_AtoL,text='F',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_G = tk.Label(frame_AtoL,text='G',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_H = tk.Label(frame_AtoL,text='H',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_J = tk.Label(frame_AtoL,text='J',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_K = tk.Label(frame_AtoL,text='K',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_L = tk.Label(frame_AtoL,text='L',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)

lbl_A.grid(row=0,column=0,padx=11,pady=5)
lbl_S.grid(row=0,column=1,padx=11,pady=5)
lbl_D.grid(row=0,column=2,padx=11,pady=5)
lbl_F.grid(row=0,column=3,padx=11,pady=5)
lbl_G.grid(row=0,column=4,padx=11,pady=5)
lbl_H.grid(row=0,column=5,padx=11,pady=5)
lbl_J.grid(row=0,column=6,padx=11,pady=5)
lbl_K.grid(row=0,column=7,padx=11,pady=5)
lbl_L.grid(row=0,column=8,padx=11,pady=5)
frame_AtoL.grid(row=2)
# Z to M
frame_ZtoM = tk.Frame(frame_keyboard,bg='Yellow')
lbl_Z = tk.Label(frame_ZtoM,text='Z',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_X = tk.Label(frame_ZtoM,text='X',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_C = tk.Label(frame_ZtoM,text='C',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_V = tk.Label(frame_ZtoM,text='V',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_B = tk.Label(frame_ZtoM,text='B',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_N = tk.Label(frame_ZtoM,text='N',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)
lbl_M = tk.Label(frame_ZtoM,text='M',font='algerian 12 bold',bg='black',fg='white',width=4,height=2,relief='groove',bd=10)

lbl_Z.grid(row=0,column=0,padx=10,pady=5)
lbl_X.grid(row=0,column=1,padx=10,pady=5)
lbl_C.grid(row=0,column=2,padx=10,pady=5)
lbl_V.grid(row=0,column=3,padx=10,pady=5)
lbl_B.grid(row=0,column=4,padx=10,pady=5)
lbl_N.grid(row=0,column=5,padx=10,pady=5)
lbl_M.grid(row=0,column=6,padx=10,pady=5)
frame_ZtoM.grid(row=3)
# Space Bar
fram_space = tk.Frame(frame_keyboard,bg='Yellow')
lbl_space = tk.Label(fram_space,bg='black',width=40,height=2,relief='groove',bd=10)
lbl_space.grid(row=0,column=0,padx=10,pady=5)
fram_space.grid(row=4)

frame_keyboard.grid(row=3)

main_frame.grid()


#Key Binding By My self
def changeBG(widget):
    bg = 'black'
    widget.configure(background = 'blue')
    widget.after(500,lambda color = bg : widget.configure(background=color))

label_numbers = [lbl_1,lbl_2,lbl_3,lbl_4,lbl_5,lbl_6,lbl_7,lbl_8,lbl_9,lbl_0]
label_alphabets = [lbl_A,lbl_B,lbl_C,lbl_D,lbl_E,lbl_F,lbl_G,lbl_H,lbl_I,lbl_J,lbl_K,lbl_L,lbl_M,lbl_N,lbl_O,lbl_P,lbl_Q,lbl_R,lbl_S,lbl_T,lbl_U,lbl_V,lbl_W,lbl_X,lbl_Y,lbl_Z]
label_space = [lbl_space]

binding_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9' , '0']
binding_small_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
binding_capital_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for number in range(len(binding_numbers)):
    window.bind(binding_numbers[number],lambda event,label=label_numbers[number]:changeBG(label))

for small_alpha in range(len(binding_small_alphabets)):
    window.bind(binding_small_alphabets[small_alpha],lambda event,label=label_alphabets[small_alpha]:changeBG(label))

for capital_alpha in range(len(binding_capital_alphabets)):
    window.bind(binding_capital_alphabets[capital_alpha],lambda event,label=label_alphabets[capital_alpha]:changeBG(label))

window.bind('<space>',lambda event,label=label_space[0] : changeBG(label))

# ----------------------------------------------------------------------------------------------------------------------------------------
# Function to change background color temporarily By Chat GPT
# def changeBG(widget):
#     bg = 'black'
#     widget.configure(background='blue')
#     widget.after(100, lambda color=bg: widget.configure(background=color))

# # Lists of label widgets
# label_numbers = [lbl_1, lbl_2, lbl_3, lbl_4, lbl_5, lbl_6, lbl_7, lbl_8, lbl_9, lbl_0]
# label_alphabets = [lbl_A, lbl_B, lbl_C, lbl_D, lbl_E, lbl_F, lbl_G, lbl_H, lbl_I, lbl_J, lbl_K, lbl_L,
#                    lbl_M, lbl_N, lbl_O, lbl_P, lbl_Q, lbl_R, lbl_S, lbl_T, lbl_U, lbl_V, lbl_W, lbl_X, lbl_Y, lbl_Z]

# # Key bindings
# binding_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# binding_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#                      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # Bind number keys to respective label widgets
# for i in range(len(binding_numbers)):
#     window.bind(binding_numbers[i], lambda event, lbl=label_numbers[i]: changeBG(lbl))

# # Bind small & capital letters to same labels
# for i in range(len(binding_alphabets)):
#     window.bind(binding_alphabets[i], lambda event, lbl=label_alphabets[i]: changeBG(lbl))
#     window.bind(binding_alphabets[i].upper(), lambda event, lbl=label_alphabets[i]: changeBG(lbl))
# ----------------------------------------------------------------------------------------------------------------------------------------
window.mainloop()