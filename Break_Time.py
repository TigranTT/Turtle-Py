import webbrowser
import time



count=0
while (count<3):
    time.sleep(2)
    webbrowser.open("http://google.com")
    print time.ctime()+'\n'+'Break-time!!!'
    count+=1

