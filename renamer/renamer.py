import os

path = '/home/anxiety/Documents/GitHub/bash/renamer/trash/'
files = os.listdir(path)
for file in files:
    new = file
    new = new.replace(' ','-')
    new = new.replace('_','-')

    new = new.replace('ı','i')
    new = new.replace('ü','u')
    new = new.replace('ğ','g')
    new = new.replace('ş','s')
    new = new.replace('ç','c')
    new = new.replace('ö','o')

    new = new.replace('İ','I')
    new = new.replace('Ü','U')
    new = new.replace('Ğ','G')
    new = new.replace('Ş','S')
    new = new.replace('Ç','C')
    new = new.replace('Ö','O')

    #new = new.replace('','')

    print('old - ' + file)
    print('new - ' + new + '\n')
    os.rename(path + file,path + new)