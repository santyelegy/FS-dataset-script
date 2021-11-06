import os


path = "./"

for file in os.listdir(path):
    if file.startswith("2019_MS_WC_"):
        os.rename(os.path.join(path,file),os.path.join(path,file.replace("2019_MS_WC_","2019_WC_MS_")))