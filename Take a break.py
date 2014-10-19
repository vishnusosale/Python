import webbrowser
import time

total_breaks = 3
break_count = 1


print ("Start time of program is : " + time.ctime())
while (break_count <= total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.facebook.com")
    print ("Break number : " + str(break_count) + " at time : "+ time.ctime())
    break_count = break_count + 1
