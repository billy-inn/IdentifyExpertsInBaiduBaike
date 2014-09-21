# coding=utf-8
from Tkinter import *
import geturl
import read
import socket

fr = open("fileList.txt","r")
fileList = fr.readlines()
fr.close()

class Application(Frame):
	def nextEntry(self):
		#name = self.entry.get()
		#info = self.entry2.get()
		name, title, org, keyword = read.read('reviewer/'+fileList[self.cnt].strip())
		wordList = str()
		for word in keyword:
			wordList += " " + word
		self.entry.delete(0,len(self.entry.get()))
		self.entry2.delete(0,len(self.entry2.get()))
		self.entry3.delete(0,len(self.entry3.get()))
		self.entry4.delete(0,len(self.entry4.get()))
		self.entry.insert(0,name)
		self.entry2.insert(0,org)
		self.entry3.insert(0,title)
		self.entry4.insert(0,wordList.strip())
		self.cnt = self.cnt + 1
		#geturl.search(name, info)
	
	def identify(self):
		print self.cnt
		name = self.entry.get()
		org = self.entry2.get()
		title = self.entry3.get()
		keyword = self.entry4.get().split()
		ans = geturl.search(name, org, title, keyword)
		print ans
		res = input()
		if res == 1: self.A += 1
		elif res == 2: self.B += 1
		elif res == 3: self.C += 1
		else: self.D +=1
		print self.A,self.B,self.C,self.D

	def createWidgets(self):
		self.title = Label(self)
		self.title["text"] = "Identify Experts in Baidu Baike"

		self.title.grid(row = 0, columnspan = 3)

		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["command"] = self.quit

		self.QUIT.grid(row = 5, column = 1, sticky = E)

		self.go = Button(self)
		self.go["text"] = "Go"
		self.go["command"] = self.identify

		self.go.grid(row = 5, column = 1)

		self.nextE = Button(self)
		self.nextE["text"] = "Next"
		self.nextE["command"] = self.nextEntry

		self.nextE.grid(row = 5, column = 1, sticky = W)

		self.entry = Entry(self)
		self.entry["width"] = 50

		self.entry.grid(row = 1, column = 1)

		self.hint = Label(self)
		self.hint["text"] = "Please enter the name of the expert:"
		
		self.hint.grid(row = 1, column = 0)
		
		self.hint2 = Label(self)
		self.hint2["text"] = "Please enter the organization of the expert:"
		
		self.hint2.grid(row = 3, column = 0)

		self.entry2 = Entry(self)
		self.entry2["width"] = 50

		self.entry2.grid(row = 3, column = 1)

		self.hint3 = Label(self)
		self.hint3["text"] = "Please enter the title of the expert:"

		self.hint3.grid(row = 2, column = 0)
		
		self.entry3 = Entry(self)
		self.entry3["width"] = 50
		
		self.entry3.grid(row = 2, column = 1)
		
		self.hint4 = Label(self)
		self.hint4["text"] = "Please enter the research area of the expert:"

		self.hint4.grid(row = 4, column = 0)
		
		self.entry4 = Entry(self)
		self.entry4["width"] = 50
		
		self.entry4.grid(row = 4, column = 1)
		#im = Image.open("capture.png")
		#self.image = ImageTk.PhotoImage(self,im)
		
		#self.canvas = Canvas(self)
		#self.canvas.create_image(0,0,image=self.image)

		#self.canvas.grid(row = 2, column = 0, rowspan = 3, columnspan = 3, padx=5, pady=5)

	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.grid()
		self.createWidgets()
		self.cnt = 584
		self.A = 130
		self.B = 2
		self.C = 13
		self.D = 355

socket.setdefaulttimeout(5)
root = Tk()
app = Application(master = root)
app.mainloop()
root.destroy()
