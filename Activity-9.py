# Write a python program to create a histogram
def histogram(item):
    for i in item:
        output =""
        times = i
        while(times>0):
            output+= "*"
            times = times-1
        print(output)
histogram([2,3,6,5])