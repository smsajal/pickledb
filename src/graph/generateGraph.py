import src.storage.fileUtility as FileUtility
import numpy as np
import matplotlib.pyplot as plt

def readData(filename, workloadName):
    data = FileUtility.readJsonFile(filename)
    latencies = data[workloadName]

    mean = np.mean(latencies)
    percentile50 = np.percentile(latencies, 50)
    percentile90 = np.percentile(latencies, 90)
    percentile95 = np.percentile(latencies, 95)
    percentile99 = np.percentile(latencies, 99)
    print(mean, percentile50, percentile90, percentile95, percentile99)
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
    plt.clf()

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
    plt.clf()

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
    plt.clf()

'''data1 = sort-merge, data2=hash join, data3= inner loop'''
def makeGraphJoin(data1, data2, data3, outfilename):
    percentiles = ['mean', '50P', '90P', '95P', '99P']
    X = np.arange(len(percentiles))
    width=0.25
    # ax = plt.subplot(111)
    plt.rcParams.update({'font.size': 16})
    plt.bar(X-width, data1, width=width, color='y', label='SM')
    plt.bar(X, data2, width=width, color='m', label='Hash')
    plt.bar(X+width, data3, width=width, color='c', label='Loop')
    plt.ylim(top=100000000)
    plt.xticks(X, percentiles)
    plt.xlabel("Percentiles")
    plt.ylabel("Latency(nanosec)")
    # plt.title("Number of Students in each group")
    plt.legend(bbox_to_anchor=(0.18,0.68), loc=3)
    # plt.show()
    plt.savefig(outfilename)
    plt.clf()

'''data1 = sort-merge, data2=hash join'''
def makeGraphJoinMergeHash(data1, data2, outfilename):
    percentiles = ['mean', '50P', '90P', '95P', '99P']
    X = np.arange(len(percentiles))
    width=0.2
    # ax = plt.subplot(111)
    plt.bar(X-width, data1, width=width*2, color='y', label='Sort-Merge')
    plt.bar(X+width, data2, width=width*2, color='m', label='Hash Join')
    # plt.ylim(top=300000)
    plt.xticks(X, percentiles)
    plt.xlabel("Percentiles")
    plt.ylabel("Latency(nanosec)")
    # plt.title("Number of Students in each group")
    plt.legend()
    # plt.show()
    plt.savefig(outfilename)
    plt.clf()

'''data1 = sort-merge, data2=hash join, data3= inner loop'''
def makeGraphCacheSize(data1, data2, data3, outfilename):
    percentiles = ['mean', '50P', '90P', '95P', '99P']
    X = np.arange(len(percentiles))
    width=0.25
    # ax = plt.subplot(111)
    plt.rcParams.update({'font.size': 16})
    plt.bar(X-width, data1, width=width, color='y', label='Size=40')
    plt.bar(X, data2, width=width, color='m', label='Size=70')
    plt.bar(X+width, data3, width=width, color='c', label='Size=100')
    # plt.ylim(top=100000000)
    plt.xticks(X, percentiles)
    plt.xlabel("Percentiles")
    plt.ylabel("Latency(nanosec)")
    # plt.title("Number of Students in each group")
    plt.legend()
    # plt.show()
    plt.savefig(outfilename)
    plt.clf()

def makeGraphJoinFile():
    file1 = "/Users/rxh655/Documents/Spring 2021/CSE 541/Project/pickledb/src/perf_eval/joinLatency5000_det2.json"
    datasortmerge = readData(file1, "1")
    datahashjoin = readData(file1, "2")
    # datanestedloop = readData(file1, "3")

    # makeGraphJoin(data1=datasortmerge, data2=datahashjoin, data3=datanestedloop, outfilename = 'graph/join5000Report_cache_atomicOn_legend.png')


if __name__ == '__main__':
    makeGraphJoinFile()
    # file1 = "/Users/rxh655/Documents/Spring 2021/CSE 541/Project/pickledb/src/perf_eval/atomicON_cache_latencies_40.json"
    # file2 = "/Users/rxh655/Documents/Spring 2021/CSE 541/Project/pickledb/src/perf_eval/atomicON_cache_latencies_70.json"
    # file3 = "/Users/rxh655/Documents/Spring 2021/CSE 541/Project/pickledb/src/perf_eval/atomicON_cache_latencies_100.json"
    # makeGraphAtomic(data1=data1, data2=data2, outfilename='graph/atomicOnOff_noncache_workload' + str(workload) + '.png')
    # makeGraphJoin(data1=data1, data2=data2, data3=data2, outfilename='graph/joinTest' + str(workload) + '.png')
    # for i in range(1, 4):
    #     print(i)
    #     workload = i
    #     data1 = readData ( file1, str ( workload ) )
    #     data2 = readData ( file2, str ( workload ) )
    #     # makeGraphCache(data1=data1, data2=data2, outfilename='graph/cacheOnOff_atomicOn_workload' + str(workload) + '.png')
    #     makeGraphAtomic ( data1 = data1, data2 = data2, outfilename = 'graph/atomicOnOff_noncache_workload' + str ( workload ) + '.png' )
    #     # makeGraphWB ( data1 = data1, data2 = data2, outfilename = 'graph/cacheWB_atomicOn_workload' + str ( workload ) + '.png' )

    # datasortmerge = readData(file1, "1")
    # datahashjoin = readData(file1, "2")
    # datanestedloop = readData(file1, "3")

    # makeGraphJoin(data1=datasortmerge, data2=datahashjoin, data3=datanestedloop, outfilename = 'graph/join5000_cache_atomicOn_legend.png')
    # makeGraphJoinMergeHash(data1=datasortmerge, data2=datahashjoin, outfilename='graph/join5000_cache_atomicOn_MH.png')

    # for i in range(1, 4):
    #     print(i)
    #     workload = i
    #     data1 = readData ( file1, str ( workload ) )
    #     data2 = readData ( file2, str ( workload ) )
    #     data3 = readData ( file3, str ( workload ) )
    #     makeGraphCacheSize(data1, data2, data3, 'graph/cacheSize_Report_workload' + str ( workload ) + '.png')