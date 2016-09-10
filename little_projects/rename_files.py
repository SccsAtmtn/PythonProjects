import os

def rename_files():
    file_names = os.listdir(r"C:\Users\asus-pc\Pictures\桌面壁纸")
    save_path = os.getcwd()
    os.chdir(r"C:\Users\asus-pc\Pictures\桌面壁纸")
    count = 0
    for file_name in file_names:
        os.rename(file_name, "Robin"+str(count)+".jpg")
        count = count+1
    os.chdir(save_path)
    
rename_files()
