# Program to analyse a dataset on Iris
# Author: Breeda Herlihy

filename = "iris.data"
def readText():
 with open(filename,"r") as f:
    chapter = str(f.read())
    return chapter
# test it
chapter = readText()

irisCount= readText().count("Iris")
print(irisCount)