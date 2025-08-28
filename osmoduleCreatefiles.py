import os

if(not os.path.exists("icons")):
    os.mkdir("icons")

for i in range(0, 10):
    os.mkdir(f"icons/icon{i+1}.png")
    
