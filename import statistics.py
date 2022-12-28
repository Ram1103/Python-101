'''import statistics

def cont():
    dataList = []
    print("Enter tvalues,enter \"End\" in observation to stop entering")   
    temp = "Yes"
    while temp != "End":
        print("Observation:")
        temp = input()
        if temp == "End":
            break
        o = int(temp)
        print("Frequency")
        f = int(input())
        for x in range(0,f):
            dataList.append(o)    
    return dataList  

def disc():
    dataList = [] 
    print("Enter tvalues,enter \"End\" in observation to stop entering")   
    temp = "Yes"
    while temp != "End":
        print("Observation:")
        temp = input()
        if temp == "End":
            break
        o = int(temp)
        dataList.extend(temp)    
    return dataList  

print("Discrete(d) or continuous(c)(Data with frequency)")
response = input()
dataList = []
if response == 'd':
    dataList = disc()
elif response == 'c':
    dataList = cont() 
standardDeviation = statistics.stdev(dataList)
variance = statistics.variance(dataList)
print("Sample Standard Deviation is:",standardDeviation)
print("Sample Variance is:",variance)
print("Population Standard Deviation is:",(standardDeviation *len(dataList))/(len(dataList)-1))
print("Population Variance is:",(variance *len(dataList))/(len(dataList)-1))'''




import statistics

def cont():
    dataList = []
    print("Enter tvalues,enter \"End\" in observation to stop entering")   
    temp = "Yes"
    while temp != "End":
        print("Observation:")
        temp = input()
        if temp == "End":
            break
        o = int(temp)
        print("Frequency")
        f = int(input())
        for x in range(0,f):
            dataList.append(o)    
    return dataList  

def disc():
    dataList = [] 
    print("Enter tvalues,enter \"End\" in observation to stop entering")   
    temp = "Yes"
    while temp != "End":
        print("Observation:")
        temp = input()
        if temp == "End":
            break
        o = int(temp)
        dataList.extend(temp)    
    return dataList  

print("Discrete(d) or continuous(c)(Data with frequency)")
response = input()
dataList = []
if response == 'd':
    dataList = disc()
elif response == 'c':
    dataList = cont() 
standardDeviation = statistics.stdev(dataList)
variance = statistics.variance(dataList)
print("Sample Standard Deviation is:",standardDeviation)
print("Sample Variance is:",variance)
print("Population Standard Deviation is:",(standardDeviation *(len(dataList)-1))/(len(dataList)))
print("Population Variance is:",(variance *(len(dataList)-1))/(len(dataList)))