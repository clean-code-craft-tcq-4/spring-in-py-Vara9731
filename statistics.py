import math

if __name__ == "__main__":
def calculateStats(numbers):
    n=[numbers]
    avg=sum(n)/len(n)
    min1=min(n)
    max1=max(n)
    computedStats={}
    computedStats["avg"]=avg
    computedStats["min"]=min1
    computedStats["max"]=max1
    print(computedStats)
    if math.isnan(numbers):
        print("NaN")
        return true