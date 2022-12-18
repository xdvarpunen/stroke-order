from tkinter import *
import tkinter
from tkinter.ttk import *

features = ["horizontal_line","vertical_line"]

rules = {
  "I": ["vertical_line"],
  "T": ["horizontal_line","vertical_line"],
  "L": ["vertical_line","horizontal_line"],
}

class App(tkinter.Tk):
  def __init__(self):
    super().__init__()

    self.input_text = "Last result: None"
    self.temp_input = []

    self.title('Stroke Order')
    self.geometry('250x300')

    self.eval('tk::PlaceWindow . center')

    self.label = Label(self, text=self.input_text)
    self.label.grid(row=0,rowspan=3,column=1)
    
    self.button1 = Button(self, text ="Process Input", command = self.process_input)
    self.button1.grid(row=1,column=0)

    self.button1 = Button(self, text ="Remove Last Stroke", command = self.remoteLastStroke)
    self.button1.grid(row=2,column=0)

    self.button1 = Button(self, text ="Clear", command = self.clear)
    self.button1.grid(row=3,column=0)

    self.b1 = Listbox(self)
    self.b1.grid(row=4,rowspan=10,column=1)

    row = 5
    for index in range(len(features)):
      button = Button(self, text=features[index], command = lambda index=index: self.addStroke(features[index]) )
      button.grid(row=row,column=0)
      row+=1

  def clear(self):
    self.input_text = ""
    self.temp_input=[]
    self.b1.delete(0,"end")

  def remoteLastStroke(self):
    if len(self.temp_input) > 0:
      self.temp_input.pop()
      self.b1.delete("end","end")

  def addStroke(self,feature):
    self.temp_input.append(feature)
    self.b1.insert("end",feature)

  def process_input(self):
    self.input_text="Last result: "
    key_list = list(rules.keys())
    val_list = list(rules.values())
    try:
      position = val_list.index(self.temp_input)
      key = key_list[position]
      print(key)
      self.input_text+=key
    except:
      print("None")
      self.input_text+="None"
    self.label.config(text=self.input_text)
    self.temp_input=[]
    self.b1.delete(0,"end")


if __name__ == "__main__":
  app = App()
  app.mainloop()