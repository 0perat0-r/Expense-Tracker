import tkinter as tk

root = tk.Tk()
root.title("Budget Tracker")
root.iconbitmap("logo.ico")
root.geometry(f"300x300")

####

def add_balance():
    amount = add_balance_entry.get()

    logFile = open("action_log.txt", "a")
    logFile.write(f"[+] Added {amount}\n")

    dataFile = open("balance.txt", "r")
    amount = int(dataFile.read()) + int(amount)
    dataFile.close()

    dataFile = open("balance.txt", "w")
    dataFile.write(str(amount))
    dataFile.close()

add_balance_entry = tk.Entry(root, width=20)
add_balance_entry.pack(anchor="center")

add_balance_button = tk.Button(root, text="Add balance", command=add_balance, width=16)
add_balance_button.pack(anchor="center")

####
def remove_balance():
    amount = remove_balance_entry.get()

    logFile = open("action_log.txt", "a")
    logFile.write(f"[-] Removed {amount}\n")

    dataFile = open("balance.txt", "r")
    amount = int(dataFile.read()) - int(amount)
    dataFile.close()

    dataFile = open("balance.txt", "w")
    dataFile.write(str(amount))
    dataFile.close()

remove_balance_entry = tk.Entry(root, width=20)
remove_balance_entry.pack(anchor="center")

remove_balance_button = tk.Button(root, text="Remove balance", command=remove_balance, width=16)
remove_balance_button.pack(anchor="center")

####

def get_balance():
    x = open("balance.txt")
    balance = x.read()
    x.close()
    return balance

def upd_balance():
    balance_label.config(text=get_balance())

balance_label = tk.Label(root, text=get_balance(), width=15, borderwidth=5, background="#87CEEB")
balance_label.pack(anchor="center", pady=10)

refresh_balance_buttion = tk.Button(root, text="Refresh balance", width=16, command=upd_balance, background="#87CEEB", borderwidth=4)
refresh_balance_buttion.pack(anchor="center")

root.mainloop()