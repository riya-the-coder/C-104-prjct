from collections import Counter 
import csv
def getMean(TotalWeight,TotalEntries):
    mean=TotalWeight/TotalEntries
    print(mean)

def getMedian(TotalEntries,SortedData):
    if TotalEntries%2==0:
        median1=float(SortedData[TotalEntries//2])
        median2=float(SortedData[TotalEntries//2-1])       
        median=(median1+median2)/2
    else:
        median=float(SortedData[TotalEntries//2])
    print(median)

def getMode(SortedData):
    data=Counter(SortedData)
    modeDataForRange={
        "75-85":0,
        "85-95":0,
        "95-105":0,
        "105-115":0,
        "115-125":0,
        "125-135":0,
        "135-145":0,
        "145-155":0,
        "155-165":0,
        "165-175":0,
    }
    for Weight,Occurence in data.item():
        if 75<Weight<85:
            modeDataForRange["75-85"]+=Occurence
        elif 85<Weight<95:
             modeDataForRange["85-95"]+=Occurence
        elif 95<Weight<105:
             modeDataForRange["95-105"]+=Occurence
        elif 105<Weight<115:
             modeDataForRange["105-115"]+=Occurence
        elif 115<Weight<125:
             modeDataForRange["115-125"]+=Occurence
        elif 125<Weight<135:
             modeDataForRange["125-135"]+=Occurence
        elif 135<Weight<145:
             modeDataForRange["135-145"]+=Occurence
        elif 145<Weight<155:
             modeDataForRange["145-155"]+=Occurence
        elif 155<Weight<165:
             modeDataForRange["155-165"]+=Occurence
        elif 165<Weight<175:
             modeDataForRange["165-175"]+=Occurence



    modeRange,modeOccurence=0,0
    for range,Occurence in modeDataForRange.items():
        if Occurence>modeOccurence:
            modeRange,modeOccurence=[int(range.split("-")[0]),int(range.split("-")[1])],Occurence
    mode=float((modeRange[0]+modeRange[1])/2)
    print(f"mode=>{mode:2f}")
    print(mode)


