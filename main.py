from tkinter import *
import requests




def hållbar_kurs():
        response = requests.get('https://www.skagenfondene.no/api/FundGathering/GetGraphSeriesList?isin=SE0005965688&currency=NOK')
        nyeste = response.json()
        # Iterates list and finds latest index, multiplies it with input value and puts it in a label
        for i in nyeste:
            hållbarCurrent_label = Label(MainFrame, text = i["data"][-1]["y"] * float(handel_entry.get()))
            hållbarCurrent_label.place(x = 90, y = 60)


        

def blackrock_kurs():
    response = requests.get("https://www.skagenfondene.no/api/FundGathering/GetGraphSeriesList?isin=LU0056508442&currency=NOK")
    nyeste = response.json()
    for i in nyeste:
        blackrockCurrent_label = Label(MainFrame, text = i["data"][-1]["y"] * float(blackrock_entry.get()))
        blackrockCurrent_label.place(x = 90, y = 140)


window = Tk()
window.geometry("300x500")
window.title("Oljebarna")


MainFrame = Frame(window)
MainFrame.place(x = 0, y = 0, width = 300, height = 500)




#button
hållbar_button = Button(text = "Update", command = hållbar_kurs)
hållbar_button.place(x = 140, y = 35)

blackrock_button = Button(text = "Update", command = blackrock_kurs)
blackrock_button.place(x = 140, y = 115)




# Labels
handel_label = Label(MainFrame, text = "Handelsbanken Hållbar Energi", font = 'Helvetica 10 bold')
handel_label.place(x = 0, y =0)

blackrock_label = Label(MainFrame, text = "Blackrock World Technology", font = 'Helvetica 10 bold')
blackrock_label.place(x = 0, y = 80)

handelInsert = Label(MainFrame, text = "Enter amount of stocks:")
handelInsert.place(x = 0, y = 20)

blackrockInsert = Label(MainFrame, text = "Enter amount of stocks:")
blackrockInsert.place(x = 0, y = 100)

current_label1 = Label(MainFrame, text = "Current worth:")
current_label1.place(x = 0, y = 60)
current_label1.configure(fg = "orange")

current_label2 = Label(MainFrame, text = "Current worth:")
current_label2.place(x = 0, y = 140)
current_label2.configure(fg = "orange")


#label end

# entry
handel_entry = Entry(MainFrame)
handel_entry.place(x = 0, y = 40)
handel_entry.insert(END, "181")


blackrock_entry = Entry(MainFrame)
blackrock_entry.place(x = 0, y = 120)
blackrock_entry.insert(END, "110")
# entry end



# profit label start
profit_hållbar = Label(MainFrame, text = "Profit hållbar:", font = 'Helvetica 10 bold')
profit_hållbar.place(x= 0, y = 200)



profit_blackrock = Label(MainFrame, text = "Profit blackrock:", font = 'Helvetica 10 bold')
profit_blackrock.place(x= 0, y = 280)


profit_total = Label(MainFrame, text = "Total profit:", font = 'Helvetica 12 bold')
profit_total.place(x= 0, y = 360)
#profit label end



def hållbar_profit():
    response = requests.get('https://www.skagenfondene.no/api/FundGathering/GetGraphSeriesList?isin=SE0005965688&currency=NOK')
    nyeste = response.json()
    # Iterates list and finds latest index, multiplies it with input value and puts it in a label
    for i in nyeste:
        hållbarTotal_label = Label(MainFrame, text = i["data"][-1]["y"] * float(handel_entry.get()) - 74753)
        hållbarTotal_label.place(x = 0, y = 220)
        hållbarTotal_label.configure(fg = "green")

hållbarprofit_button = Button(MainFrame, text = "Update", command = hållbar_profit)
hållbarprofit_button.place(x = 120, y = 220)




def blackrock_profit():
    response = requests.get('https://www.skagenfondene.no/api/FundGathering/GetGraphSeriesList?isin=LU0056508442&currency=NOK')
    nyeste = response.json()
    # Iterates list and finds latest index, multiplies it with input value and puts it in a label
    for i in nyeste:
        blackrockTotal_label = Label(MainFrame, text = i["data"][-1]["y"] * float(blackrock_entry.get()) - 75240)
        blackrockTotal_label.place(x = 0, y = 300)
        blackrockTotal_label.configure(fg = "green")

blackrockprofit_button = Button(MainFrame, text = "update", command = blackrock_profit)
blackrockprofit_button.place(x = 120, y = 300)



def total():
    response1 = requests.get('https://www.skagenfondene.no/api/FundGathering/GetGraphSeriesList?isin=SE0005965688&currency=NOK')
    nyeste1 = response1.json()
    response2 = requests.get('https://www.skagenfondene.no/api/FundGathering/GetGraphSeriesList?isin=LU0056508442&currency=NOK')
    nyeste2 = response2.json()
    # Iterates list and finds latest index, multiplies it with input value and puts it in a label
    total_list = []
    for i in nyeste1:
        total_list.append(i["data"][-1]["y"] * float(handel_entry.get()))

    for y in nyeste2:
        total_list.append(y["data"][-1]["y"] * float(blackrock_entry.get()))
    total_label = Label(MainFrame, text = total_list[0] + total_list[1] - 149993)
    total_label.configure(fg = "green")
    total_label.place(x = 0, y = 380)




totalprofit_button = Button(MainFrame, text = "update", command = total)
totalprofit_button.place(x = 120, y = 380)

'''
exit_button = Button(MainFrame, text = "lukk", command = exit)
exit_button.place(x = 130, y = 450)
exit_button.configure(bg = "red", fg = "blue")
'''

window.mainloop()