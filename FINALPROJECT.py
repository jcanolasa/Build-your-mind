import statistics
from matplotlib import pyplot
from tkinter import *
import csv
import sys
import pandas as pd


def graph(x, y):
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    pyplot.xlim(-3, 3)
    pyplot.ylim(-3, 3)
    pyplot.axhline(2, color="red")
    pyplot.axhline(-2, color="red")
    pyplot.axvline(2, color="red")
    pyplot.axvline(-2, color="red")

    pyplot.grid()
    pyplot.title("YOUR POINT IN THE SPECTRUM IS:")
    pyplot.xlabel("Left(-2) to Right(2)")
    pyplot.ylabel("Liberal(-2) to Authoritarian(2)")

    # representar el punto
    pyplot.plot(x, y, linewidth=3, marker="o", markersize=20, color="red")

    pyplot.show()


def pr_inter():
    def validate_entry(text):
        return text.isdecimal()

    root = Tk()

    root.resizable(0,0)

    frame = Frame(root,width="700", height="480")
    frame.pack()
    frame.config(bg="white")

    frame.config(bd=15)
    frame.config(relief="groove")
    frame.config(cursor="arrow")

    #-----función hacer_click-----
    def hacer_click():
        xvalue=int(textone.get())
        yvalue=int(texttwo.get())
        if xvalue or yvalue > abs(2):
            output.config(text="TRY AGAIN! :(")
        if xvalue == -2:
            if yvalue == 2:
                output.config(text="1")
            if yvalue == 1:
                output.config(text="5")
            if yvalue == -1:
                output.config(text="9")
            if yvalue == -2:
                output.config(text="13")

        if xvalue == -1:
            if yvalue == 2:
                output.config(text="2")
            if yvalue == 1:
                output.config(text="6")
            if yvalue == -1:
                output.config(text="10")
            if yvalue == -2:
                output.config(text="14")

        if xvalue == 1:
            if yvalue == 2:
                output.config(text="3")
            if yvalue == 1:
                output.config(text="7")
            if yvalue == -1:
                output.config(text="11")
            if yvalue == -2:
                output.config(text="15")

        if xvalue == 2:
            if yvalue == 2:
                output.config(text="4")
            if yvalue == 1:
                output.config(text="8")
            if yvalue == -1:
                output.config(text="12")
            if yvalue == -2:
                output.config(text="16")

    #-----title-----
    labeltitle = Label(frame, text ="INTERACTIVE POLITICAL GRAPH", fg="orange")
    labeltitle.place(x=210, y=25)
    labeltitle.config(bg="white")

    #-----labels-----
    labelone= Label(frame, text ="X-AXIS COORDINATE (-2 TO 2):", fg="black")
    labelone.place(x=10, y=50)
    labelone.config(bg="white")

    labeltwo= Label(frame, text ="Y-AXIS COORDINATE (-2 TO 2):", fg="black")
    labeltwo.place(x=10, y=80)
    labeltwo.config(bg="white")

    labeltwo= Label(frame, text ="YOUR POSITION IN THE GRAPH IS AREA:", fg="black")
    labeltwo.place(x=10, y=110)
    labeltwo.config(bg="white")

    #-----texts-----
    textone=Entry(frame)
    textone.place(x=218, y=50)
    textone.config(fg="orange", justify="center")

    texttwo=Entry(frame)
    texttwo.place(x=218, y=80)
    texttwo.config(fg="orange", justify="center")

    output=Label(frame, text="OUTPUT")
    output.place(x=305, y=110)
    output.config(bg="white")

    #-----click button-----
    click= Label(frame, text ="CLICK SEND TO RECEIVE INFORMATION:", fg="black")
    click.place(x=180, y=350)
    click.config(bg="white")

    sendbutton=Button(frame, text="SEND", fg="red",height = 3,
            width = 3, command=hacer_click)
    sendbutton.place(x=280, y=380)
    sendbutton.config(bg="white")

    root.mainloop() #Debe estar en continua ejecución(SIEMPRE AL FINAL DEL CÓDIGO)



def interactive():
    root2=Tk()
    root2.resizable(0,0)
    root2.config(bg="peach puff")

    frame2 = Frame(root2)
    frame2.pack()
    frame2.config(bg="peach puff")
    frame2.config(bd=8)
    frame2.config(relief="groove")
    frame2.config(cursor="arrow")

    #------- título -----
    labeltitle2 = Label(frame2, text ="CLICK ON THE AREA WHERE YOU ARE LOCATED:", fg="indian red")
    labeltitle2.grid(row=1, column=1, padx=10, pady=10, columnspan=6)
    labeltitle2.config(bg="peach puff")

    #------- left -----
    xlabel = Label(frame2, text ="LEFT", fg="black")
    xlabel.grid(row=2, column=1, padx=10, pady=10, rowspan=6)
    xlabel.config(bg="peach puff")

    #------- liberal -----
    ylabel = Label(frame2, text ="LIBERAL", fg="black")
    ylabel.grid(row=7, column=1, padx=10, pady=10, columnspan=6)
    ylabel.config(bg="peach puff")

    #------- right -----
    ylabel = Label(frame2, text ="RIGHT", fg="black")
    ylabel.grid(row=2, column=6, padx=10, pady=10, rowspan=6)
    ylabel.config(bg="peach puff")

    #------- authoritarian -----
    ylabel = Label(frame2, text ="AUTHORITARIAN", fg="black")
    ylabel.grid(row=2, column=1, padx=10, pady=10, columnspan=6)
    ylabel.config(bg="peach puff")

    #------- primera fila de la gráfica-----
    def hacer_click2():
        t_label.config(text="GROUP ONE IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button1 = Button(frame2, text="1", width=3, fg="medium slate blue", command=hacer_click2)
    button1.grid(row=3, column=2)

    def hacer_click3():
        t_label.config(text="GROUP TWO IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button2 = Button(frame2, text="2", width=3,fg="medium slate blue", command=hacer_click3)
    button2.grid(row=3, column=3)

    def hacer_click4():
        t_label.config(text="GROUP THREE IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button3 = Button(frame2, text="3", width=3, fg="indian red", command=hacer_click4)
    button3.grid(row=3, column=4)

    def hacer_click5():
        t_label.config(text="GROUP FOUR IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button4 = Button(frame2, text="4", width=3, fg="indian red", command=hacer_click5)
    button4.grid(row=3, column=5)

    #------- segunda fila de la gráfica-----
    def hacer_click6():
        t_label.config(text="GROUP FIVE IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button5 = Button(frame2, text="5", width=3, fg="medium slate blue", command=hacer_click6)
    button5.grid(row=4, column=2)

    def hacer_click7():
        t_label.config(text="GROUP SIX IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button6 = Button(frame2, text="6", width=3, fg="medium slate blue", command=hacer_click7)
    button6.grid(row=4, column=3)

    def hacer_click8():
        t_label.config(text="GROUP SEVEN IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button7 = Button(frame2, text="7", width=3, fg="indian red", command=hacer_click8)
    button7.grid(row=4, column=4)

    def hacer_click9():
        t_label.config(text="GROUP EIGHT IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button8 = Button(frame2, text="8", width=3, fg="indian red", command=hacer_click9)
    button8.grid(row=4, column=5)

    #------- tercera fila de la gráfica-----
    def hacer_click10():
        t_label.config(text="GROUP NINE IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button9 = Button(frame2, text="9", width=3, fg="lime green", command=hacer_click10)
    button9.grid(row=5, column=2)

    def hacer_click11():
        t_label.config(text="GROUP TEN IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button10 = Button(frame2, text="10", width=3, fg="lime green", command=hacer_click11)
    button10.grid(row=5, column=3)

    def hacer_click12():
        t_label.config(text="GROUP ELEVEN IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button11 = Button(frame2, text="11", width=3, fg="dark orange", command=hacer_click12)
    button11.grid(row=5, column=4)

    def hacer_click13():
        t_label.config(text="GROUP TWELVE IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button12 = Button(frame2, text="12", width=3, fg="dark orange", command=hacer_click13)
    button12.grid(row=5, column=5)

    #------- cuarta fila de la gráfica-----
    def hacer_click14():
        t_label.config(text="GROUP THIRTEEN IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button13 = Button(frame2, text="13", width=3, fg="lime green", command=hacer_click14)
    button13.grid(row=6, column=2)

    def hacer_click15():
        t_label.config(text="GROUP FOURTEEN IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button14 = Button(frame2, text="14", width=3, fg="lime green", command=hacer_click15)
    button14.grid(row=6, column=3)

    def hacer_click16():
        t_label.config(text="GROUP FIFTEEN IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button15 = Button(frame2, text="15", width=3, fg="dark orange", command=hacer_click16)
    button15.grid(row=6, column=4)

    def hacer_click17():
        t_label.config(text="GROUP SIXTEEN IDENTIFIES YOU WITH PARTIES SUCH AS...")

    button16 = Button(frame2, text="16", width=3, fg="dark orange", command=hacer_click17)
    button16.grid(row=6, column=5)

    #-----mensaje recibido---
    output2=Label(frame2, text="OUTPUT")
    output2.place()
    output2.config(bg="white")

    #TEXT DISPLAY:
    frame3 = Frame(root2)
    frame3.pack()
    frame3.config(bg="peach puff")
    frame3.config(bd=8)
    frame3.config(relief="groove")
    frame3.config(cursor="arrow")

    # ------- título -----
    labeltitle3 = Label(frame3, text="THE INFORMATION OF YOUR AREA CLASSIFIES YOU AS...", fg="indian red")
    labeltitle3.grid(row=1, column=1, padx=10, pady=10, columnspan=3)
    labeltitle3.config(bg="peach puff")

    #Label with the information
    t_label = Label(frame3, text="GROUP INFORMATION", fg="black")
    t_label.grid(row=2, column=1, padx=10, pady=10, columnspan=3)
    t_label.config(bg="peach puff")

    root2.mainloop()


def questionare():
    x_list = []
    y_list = []
    instructions = 'For each one of the statements, answer from Completely Disagree to Completely Agree'
    print(instructions)

    # ROUND A:
    print('\nJust a few propositions concerning how you see countries and the world.')

    # q1
    print('\nI’d always support my country, whether it was right or wrong.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value1 = int(user_input) - 3
    y_list.append(value1)

    # q2
    print('\nNo one chooses their country of birth, however I see the logic of being proud of it.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value2 = int(user_input) - 3
    y_list.append(value2)

    # q3
    print('\nEconomic globalization is inevitable, and for me it is ok that it serves primarily the interest of\n' \
          'trans-national corporations rather than humanity.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value3 = int(user_input) - 3
    x_list.append(value3)

    # q4
    print('\nOur race has many superior qualities, compared with other races.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value4 = int(user_input) - 3
    y_list.append(value4)

    # q5
    print('\nThe enemy of my enemy is my friend')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value5 = int(user_input) - 3
    y_list.append(value5)

    # q6
    print('\nMilitary action that defies international law is justified.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value6 = int(user_input) - 3
    y_list.append(value6)

    # q7
    print('\nI don’t see a risk in the fusion of information and entertainment.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value7 = int(user_input) - 3
    y_list.append(value7)

    # ROUND B:
    print('\nNow, the economy, we are talking about  attitudes:')

    # q8
    print('\nControlling inflation is more important than controlling unemployment')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value8 = int(user_input) - 3
    x_list.append(value8)

    # q9
    print('\nThere’s no need for governmental regulations, corporation can be trusted to voluntarily protect the \n' \
          'environment')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value9 = int(user_input) - 3
    x_list.append(value9)

    # q10
    print('\nPeople are ultimately divided more by nationality than by social class')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value10 = int(user_input) - 3
    y_list.append(value10)

    # q11
    print('\n"From each according to his ability to each according to his needs” is an fundamentally erroneous \n' \
          'statement.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value11 = int(user_input) - 3
    x_list.append(value11)

    # q12
    print('\nThe freer the market, the freer the people.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value12 = int(user_input) - 3
    x_list.append(value12)

    # q13
    print('\nI don’t see it as a sad reflection that in our society, something as basic as drinking water is now \n' \
          'a bottle, branded consumer product. Actually, I find it quite interesting.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value13 = int(user_input) - 3
    x_list.append(value13)

    # q14
    print('\nLand is a commodity to be bought and sold')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value14 = int(user_input) - 3
    x_list.append(value14)

    # q15
    print('\nI don’t agree with the idea that some people believe that many personal fortunes are made by people\n' \
          'who simply manipulate money and contribute nothing to their society.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value15 = int(user_input) - 3
    x_list.append(value15)

    # q16
    print('\nProtectionism is hardly ever necessary in trade.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value16 = int(user_input) - 3
    x_list.append(value16)

    # q17
    print('\nThe only social responsibility of a company should be to deliver a profit to its shareholders.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value17 = int(user_input) - 3
    x_list.append(value17)

    # q18
    print('\nThe rich are too highly taxed.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value18 = int(user_input) - 3
    x_list.append(value18)

    # q19
    print('\nThose with the ability to pay should have access to higher standards of medical care.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value19 = int(user_input) - 3
    x_list.append(value19)

    # q20
    print('\nGovernments shouldn’t interfere and penalize businesses that mislead the public.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value20 = int(user_input) - 3
    x_list.append(value20)

    # q21
    print('\nA genuine free market does not require restrictions on the ability of predator multinationals to\n' \
          'create monopolies.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value21 = int(user_input) - 3
    x_list.append(value21)

    # ROUND B:
    print('\nNow let’s look at some social values:')

    # q22
    print('\nNot all authority should be questioned.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value22 = int(user_input) - 3
    y_list.append(value22)

    # q23
    print('\nTaxpayers should not be expected to prop up any theaters or museums that cannot survive on a\n' \
          'commercial basis.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value23 = int(user_input) - 3
    x_list.append(value23)

    # q24
    print('\nAttendance must be compulsory in the classroom.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value24 = int(user_input) - 3
    y_list.append(value24)

    # q26
    print('\nAbortion, when the woman’s life is  not threatned, should always be illegal.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value26 = int(user_input) - 3
    y_list.append(value26)

    # q27
    print('\nTAll people have their rights, but it is better for all of us that different sorts of people should\n' \
          'keep to their own kind.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value27 = int(user_input) - 3
    y_list.append(value27)

    # q28
    print('\nGood parents sometimes have to spank their children.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value28 = int(user_input) - 3
    y_list.append(value28)

    # q29
    print('\nIt’s not natural for children to keep some secrets from their parents.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value29 = int(user_input) - 3
    y_list.append(value29)

    # q30
    print('\nPossessing marijuana for personal use should be a criminal offense.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value30 = int(user_input) - 3
    y_list.append(value30)

    # q31
    print('\nThe prime function of schooling should be to equip the future generations to find jobs.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value31 = int(user_input) - 3
    x_list.append(value31)

    # q32
    print('\nPeople with serious inheritable disabilities should not be allowed to reproduce.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value32 = int(user_input) - 3
    y_list.append(value32)

    # q33
    print('\nThe most important thing for children to learn is to accept discipline.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value33 = int(user_input) - 3
    y_list.append(value33)

    # q34
    print('\nIt’s not just a cultural difference, some are more savage than others.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value34 = int(user_input) - 3
    y_list.append(value34)

    # q35
    print('\nThose who are able to work, and refuse the opportunity, should not expect society´s support.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value35 = int(user_input) - 3
    x_list.append(value35)

    # q36
    print('\nWhen you are troubled, you think it is worse to dot think about it and just think cheerful things.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value36 = int(user_input) - 3
    x_list.append(value36)

    # q37
    print('\nFirst-generation immigrants can never be fully integrated within their new country.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value37 = int(user_input) - 3
    y_list.append(value37)

    # q38
    print('\nWhat’s good for most successful corporations is always, ultimately, good for all of us.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value38 = int(user_input) - 3
    x_list.append(value38)

    # q39
    print('\nSome broadcasting institutions, depending on its content, should receive public funding.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value39 = int(user_input) - 3
    y_list.append(value39)

    # ROUND C:
    print('\n… and how you see the wider society.')

    # q40
    print('\nOur civil liberties are being excessively curbed in the name of the counter-terrorism.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value40 = int(user_input) - 3
    y_list.append(value40)

    # q41
    print('\nA significant advantage of a one-party state is that it avoids all the argument that delta progress \n' \
          'in a democratic political system.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value41 = int(user_input) - 3
    y_list.append(value41)

    # q42
    print('\nAlthough the electronic age makes official surveillance easier, only wrongdoers need to be worried.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value43 = int(user_input) - 3
    y_list.append(value43)

    # q44
    print('\nThe death penalty should be an option for the most serious crimes.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value44 = int(user_input) - 3
    y_list.append(value44)

    # q45
    print('\nIn a civilized society, one must have people about to be obeyed and people below to be commanded.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value45 = int(user_input) - 3
    y_list.append(value45)

    # q46
    print('\nAbstract art that does not represent anything should not be considered art at all.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value46 = int(user_input) - 3
    x_list.append(value46)

    # q47
    print('\nIn criminal justice, punishment should be more important than rehabilitation.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value47 = int(user_input) - 3
    y_list.append(value47)

    # q48
    print('\nIt is a waste of time to try to rehabilitate some criminals.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value48 = int(user_input) - 3
    y_list.append(value48)

    # q49
    print('\nThe business person and the manufacturer are more important than the writer and the artist.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value49 = int(user_input) - 3
    x_list.append(value49)

    # q50
    print('\nMothers may have careers, but their first duty is to be homemakers.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value50 = int(user_input) - 3
    y_list.append(value50)

    # q51
    print('\nMultinational companies shouldn’t be blamed for exploiting the plant genetic resources of \n' \
          'developing countries.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value51 = int(user_input) - 3
    x_list.append(value51)

    # q52
    print('\nMaking peace with the establishment is an important aspect of maturity.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value52 = int(user_input) - 3
    x_list.append(value52)

    # ROUND D:
    print('\nIf you got through that okay, you’ll find these propositions on religion a breeze.')

    # q53
    print('\nAstrology accurately explains nothing.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value53 = int(user_input) - 3
    y_list.append(value53)

    # q54
    print('\nYou cannot be moral without being religious.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value54 = int(user_input) - 3
    y_list.append(value54)

    # q54
    print('\nSocial security is better than charity as a means of helping the genuinely disadvantaged.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value54 = int(user_input) - 3
    x_list.append(value54)

    # q55
    print('\nThere is no such thing as “some people are naturally unlucky".')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value55 = int(user_input) - 3
    x_list.append(value55)

    # q56
    print('\nIt is important that my child’s school instills religious values.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value56 = int(user_input) - 3
    y_list.append(value56)

    # ROUND E:
    print('\nFinally, let’s look at sex:')

    # q57
    print('\nSex outside marriage is immoral.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value57 = int(user_input) - 3
    y_list.append(value57)

    # q58
    print('\nA same sex couple in a stable, loving relationship should be excluded from the possibility of \n' \
          'child adoption.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value58 = int(user_input) - 3
    y_list.append(value58)

    # q59
    print('\nPonography, depicting consenting adults, should not be legal for the adult population.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value59 = int(user_input) - 3
    y_list.append(value59)

    # q60
    print('\nWhat goes on in a private bedroom is not just between consenting adults and the state might have \n' \
          'some business on it.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value60 = int(user_input) - 3
    y_list.append(value60)

    # q62
    print('\nNo one can feel naturally homosexual.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value62 = int(user_input) - 3
    y_list.append(value62)

    # q63
    print('\nThese days openess about sex has gone too far.')
    likert_scale = ['Completely Disagree', 'Disagree', 'Neutral', 'Agree', 'Completely Agree']
    user_input = ''
    input_message = "Pick an option:\n"
    for index, item in enumerate(likert_scale):
        input_message += f'{index + 1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(likert_scale) + 1)):
        print('\nPlease, enter a valid option')
        user_input = input(input_message)
    value63 = int(user_input) - 3
    y_list.append(value63)

    x = statistics.mean(x_list)
    y = statistics.mean(y_list)
    print()
    print(x)
    print(y)
    graph(x,y)
    pr_inter()
    interactive()


def next_test1():
    print("(NEW TEST -- NOT CREATED)")


def next_test2():
    print("(NEW TEST -- NOT CREATED)")


def next_test3():
    print("(NEW TEST -- NOT CREATED)")


def new_results():
    print("Enter your results")
    nxaxis = float(input("Enter x axis: "))
    nyaxis = float(input("Enter y axis: "))

    # meter en el dataframe
    # df = pd.read_csv('results.csv')
    # print(df.loc["accesscode"==access_code, "xaxis"])
    # print(df.loc["accesscode"==access_code, "yaxis"])

    graph(nxaxis, nyaxis)
    pr_inter()
    interactive()


def next_quiz(access_code):
    ask = input("To perform the next quiz, press a key, EXCEPT <<enter to quit>> ")

    while ask != "":
        print("Select the text you want to complete:")
        available_tests = ["21/11/2022", "28/11/2022", "05/12/2022"]  # se irán añadiendo de forma semanal a medida que se vayan creando
        print(available_tests)
        response = input("Enter one of the options above: ")
        if response == available_tests[0]:
            next_test1()
            new_results()
            ask = input("To perform the next quiz, press a key, EXCEPT <<enter to quit>> ")
        if response == available_tests[1]:
            next_test2()
            new_results()
            ask = input("To perform the next quiz, press a key, EXCEPT <<enter to quit>> ")
        if response == available_tests[2]:
            next_test3()
            new_results()
            ask = input("To perform the next quiz, press a key, EXCEPT <<enter to quit>> ")
        else:
            break


def dataframe(x, y, user, password):
    with open("results.csv", mode="a", newline="") as f:
        results_writer = csv.writer(f, delimiter=",")
        access_code = user[:3] + password
        results_writer.writerow([access_code, x, y])


def account():
    with open("users.csv", mode="a", newline="") as f:

        users_writer = csv.writer(f, delimiter=",")
        user = input("Enter username: ")
        password = input("Enter password: ")
        password2 = input("Please, confirm password: ")

        if password == password2:
            users_writer.writerow([user, password])
            print("Registration is successful")
            print("Enter your results")
            x = eval(input("Enter x axis: "))
            y = eval(input("Enter y axis: "))
            dataframe(x, y, user, password)

        else:
            print("Please try again")
            sys.exit()


def login():
    user = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.csv", mode="r") as f:
        users_reader = csv.reader(f, delimiter=",")
        for row in users_reader:
            if row == [user, password]:
                access_code = str(user[:3] + password)
                print("You are logged in ")
                next_quiz(access_code)

                return True
    print("Please try again")
    return False


def main():
    print("WELCOME TO BUILD YOU MIND!")
    print("Build your Mind consists of an app that helps people discover their political positioning in terms of the current Spanish political parties.")
    decision = eval(input("Select an option <<register (1) or login (2)>> "))
    if decision == 1:
        questionare()
        print("Now create an account")
        account()
        print("Your data has successfully been saved! Now login to your account. ")
        login()

    if decision == 2:
        login()

    else:
        print("END")


main()
