import time
import webbrowser

total_breaks = 3
total_count = 0
print("Take a Break starts at "+time.ctime())
while (total_count<total_breaks):
    time.sleep(45*60)
    webbrowser.open("http://v.yinyuetai.com/video/h5/115152")
    total_count = total_count+1
    
