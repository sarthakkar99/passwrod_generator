"""with open("data.json", "w") as f:
        json.dump(new_data,f,indent=4)
        #f.write(f"{input.get()}|{input1.get()}|{input3.get()}\n")
    input.delete(0, END)
    input3.delete(0, END)"""

"""with open("data.json", "r") as f:
    data = json.load(f)
    print(data)
    #f.write(f"{input.get()}|{input1.get()}|{input3.get()}\n")
        nput.delete(0, END)
input3.delete(0, END)"""

"""is_ok=messagebox.askokcancel(title=input.get(),
                                message=f"The details are \n Website : {input.get()} \n Password : {input3.get()} \n Is it ok to save")"""
# if is_ok:
with open("data.json", "r") as f:
    data=json.load(f)
    print(data)
    input.delete(0, END)
    input3.delete(0, END)