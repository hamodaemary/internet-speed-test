import speedtest
from tkinter import *
def down():
	c = round(st.download()/(1024*1024),2)
	lbl1.config(text=c)
def uploud():
	z = round(st.upload()/(1024*1024),2)
	lbl2.config(text=z)
def bing():
	server = []
	st.get_servers(server)
	lbl3.config(text=st.results.ping)
x = Tk()
st = speedtest.Speedtest()
x.config(bg='black')
x.title('Internet speed test')
lbl = Label(text='internet speed test')
lbl.pack(fill=X)
lbl1 = Label(text='')
lbl1.pack()
lbl2 = Label(text='')
lbl2.pack()
lbl3 = Label(text='')
lbl3.pack()
but = Button(text='download',command=down)
but.pack()
but1 = Button(text='uploud',command=uploud)
but1.pack()
but2 = Button(text='ping',command=bing)
but2.pack()






x.mainloop()