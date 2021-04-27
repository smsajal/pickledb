import src.storage.fileUtility as FileUtility
import numpy as np
import matplotlib.pyplot as plt

def readData(filename, workloadName):
    data = FileUtility.readJsonFile(filename)
    latencies = data[workloadName]
    print(type(latencies))
    mean = np.mean(latencies)
    percentile50 = np.percentile(latencies, 50)
    percentile90 = np.percentile(latencies, 90)
    percentile95 = np.percentile(latencies, 95)
    percentile99 = np.percentile(latencies, 99)
    return [mean, percentile50, percentile90, percentile95, percentile99]

'''data1= atomic off, data2= atomic on'''
def makeGraphAtomic(data1, data2, outfilename):
    percentiles = ['mean', '50P', '90P', '95P', '99P']
    X = np.arange(len(percentiles))
    # ax = plt.subplot(111)
    plt.bar(X-0.2, data1, width=0.4, color='c', label='atomic off')
    plt.bar(X+0.2, data2, width=0.4, color='m', label='atomic on')
    plt.xticks(X, percentiles)
    plt.xlabel("Percentiles")
    plt.ylabel("Latency(nanosec)")
    # plt.title("Number of Students in each group")
    plt.legend()
    # plt.show()
    plt.savefig(outfilename)

'''data1= cache absent, data2= cache present'''
def makeGraphCache(data1, data2, outfilename):
    percentiles = ['mean', '50P', '90P', '95P', '99P']
    X = np.arange(len(percentiles))
    # ax = plt.subplot(111)
    plt.bar(X-0.2, data1, width=0.4, color='c', label='Cache absent')
    plt.bar(X+0.2, data2, width=0.4, color='m', label='Cache present')
    plt.xticks(X, percentiles)
    plt.xlabel("Percentiles")
    plt.ylabel("Latency(nanosec)")
    # plt.title("Number of Students in each group")
    plt.legend()
    # plt.show()
    plt.savefig(outfilename)

'''data1= base implementation, data2= writeback'''
def makeGraphWB(data1, data2, outfilename):
    percentiles = ['mean', '50P', '90P', '95P', '99P']
    X = np.arange(len(percentiles))
    # ax = plt.subplot(111)
    plt.bar(X-0.2, data1, width=0.4, color='c', label='Base implementation')
    plt.bar(X+0.2, data2, width=0.4, color='m', label='Writeback implementation')
    plt.xticks(X, percentiles)
    plt.xlabel("Percentiles")
    plt.ylabel("Latency(nanosec)")
    # plt.title("Number of Students in each group")
    plt.legend()
    # plt.show()
    plt.savefig(outfilename)

'''data1 = sort-merge, data2=hash join, data3= inner loop'''
def makeGraphJoin(data1, data2, data3, outfilename):
    percentiles = ['mean', '50P', '90P', '95P', '99P']
    X = np.arange(len(percentiles))
    width=0.25
    # ax = plt.subplot(111)
    plt.bar(X-width, data1, width=width, color='y', label='Sort-Merge')
    plt.bar(X, data2, width=width, color='m', label='Hash Join')
    plt.bar(X+width, data3, width=width, color='c', label='Inner Loop')
    plt.xticks(X, percentiles)
    plt.xlabel("Percentiles")
    plt.ylabel("Latency(nanosec)")
    # plt.title("Number of Students in each group")
    plt.legend()
    # plt.show()
    plt.savefig(outfilename)

if __name__ == '__main__':
    file1 = "/Users/rxh655/Documents/Spring 2021/CSE 541/Project/pickledb/data/atomicOff_nonCache_latencies.json"
    file2 = "/Users/rxh655/Documents/Spring 2021/CSE 541/Project/pickledb/data/atomicOn_nonCache_latencies.json"
    workload = 3
    data1 = readData(file1, str(workload))
    data2 = readData(file2, str(workload))
    makeGraphAtomic(data1=data1, data2=data2, outfilename='graph/atomic_workload' + str(workload) + '.png')
    # makeGraphJoin(data1=data1, data2=data2, data3=data2, outfilename='graph/joinTest' + str(workload) + '.png')