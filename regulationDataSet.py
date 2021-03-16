# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件


def file_nameOnSp(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpeg':
                L.append(os.path.join(root, file))
    return L

def ListPicFile(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        #print(root)
        for file in files:
            #print(file)
            #print(file_dir)
            if os.path.splitext(file)[1] =='.jpeg' or os.path.splitext(file)[1] =='.jpg':
               # L.append(os.path.join(root, file))
                #L.append(os.path.splitext(file)[0])
                L.append(file)
                #print(os.path.splitext(file)[0])
    return L

def ListXmlFile(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] =='.xml' or os.path.splitext(file)[1] =='.xaml':
                #L.append(os.path.join(root, file))
                L.append(os.path.splitext(file)[0])
    return L

def ListFileAndWriteInTxt(PicfileList,XmlFile,PicPath,xmlPath,txtPath):
    nub = 0;
    with open(txtPath, "a") as f:
        #f.write("这是个测试！/r")
        for file in PicfileList:
            print(os.path.splitext(file)[0])
            if os.path.splitext(file)[0] in XmlFile:
                f.write(PicPath+"/"+file+" "+xmlPath+"/"+file+".xml\n")
                nub=nub+1
    return nub

def ttc(txtPath):
    #print("路径不存在")
    res=False
    if os.path.exists(txtPath):
        print("已存在文件train.txt,删除请按1，退出请按2，append 请按3")
        userOrder = input()
        if userOrder == '1':
            os.remove(txtPath)
            print("删除完成")
            res = True
        if userOrder == '2':
            res = False
        if userOrder == '3':
            res = True
    else:
        print("路径不存在")
        res = True

    return res



def main():
    picFoderName = "JPEGImages"     #文件夹名称
    xmlFoderName = "Annotations"  #文件夹名称
    txtPath = "train.txt"           #保存的txt
    ress = ttc(txtPath)
    print(ress)
    if ress:
        picFileNameList = ListPicFile(picFoderName)
        xmlFileNameList = ListXmlFile(xmlFoderName)
        print(picFileNameList)
        print(xmlFileNameList)
        fileNub=ListFileAndWriteInTxt(picFileNameList,xmlFileNameList,picFoderName,xmlFoderName,txtPath)
        print(fileNub,"个文件名字写入完成")


if __name__ == '__main__':
    main()
