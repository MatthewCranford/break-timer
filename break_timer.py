import time
import webbrowser

total_breaks =1


print ("This program started on "+time.ctime())
for i in range(0,total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=kxopViU98Xo")
