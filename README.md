**Branch joinBranch:**

This branch demonstrates our extended version of pickleDB in the form of an interaction between front end Query Engine and the storage system along with a **Read-Through, Write-Around cache** implementation to make a comparison study between **Nested Loop join, Sort Merged join and Hash join**.

**Folder Structure:**

PICKLEDB



```
├── LICENSE
├── README.md
├── data
│   ├── atomicOff_nonCache_latencies.json
│   └── atomicOn_nonCache_latencies.json
├── docs
│   ├── commands.html
│   ├── favicon.ico
│   ├── index.html
│   └── logo.png
├── inputs
│   ├── atomic_tester_data.json
│   ├── name_basics.json
│   └── name_basics_first_10k.json
└── src
    ├── cache
    │   ├── __pycache__
    │   │   ├── cache.cpython-37.pyc
    │   │   └── caheDict.cpython-37.pyc
    │   ├── cache.py
    │   └── caheDict.py
    ├── graph
    │   ├── __init__.py
    │   ├── generateGraph.py
    │   └── graph
    │       ├── atomic_workload1.png
    │       ├── atomic_workload2.png
    │       ├── atomic_workload3.png
    │       ├── cacheSize_workload1.png
    │       ├── cacheSize_workload2.png
    │       ├── cacheSize_workload3.png
    │       ├── join5000_cache_atomicOn.png
    │       ├── join5000_cache_atomicOn_base.png
    │       ├── join5000_cache_atomicOn_legend.png
    │       ├── joinTest3.png
    │       ├── join_cache_atomicOn.png
    │       └── join_cache_atomicOn_MH.png
    ├── interfaces
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   ├── queryEngine.cpython-37.pyc
    │   │   └── storageInterface.cpython-37.pyc
    │   ├── interfaceTester.py
    │   ├── queryEngine.py
    │   └── storageInterface.py
    ├── perf_eval
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   └── query.cpython-37.pyc
    │   ├── atomicOFF_cache_latencies__cacheClear.json
    │   ├── atomicOFF_cache_latencies__noCacheClear.json
    │   ├── atomicON_cache_latencies_100.json
    │   ├── atomicON_cache_latencies_40.json
    │   ├── atomicON_cache_latencies_70.json
    │   ├── atomicON_cache_latencies_AV.json
    │   ├── atomicOnConfig.json
    │   ├── atomicOnOffTest.py
    │   ├── atomicOnTest_trial.py
    │   ├── atomicOn_latencies.json
    │   ├── config.json
    │   ├── generateWriteWorkload.py
    │   ├── joinConfig.json
    │   ├── joinConfig1000.json
    │   ├── joinLatency.json
    │   ├── joinLatency1000.json
    │   ├── joinLatency500.json
    │   ├── joinLatency5000.json
    │   ├── joinLatencyTest.json
    │   ├── joinWorkload.json
    │   ├── joinWorkloadTest.py
    │   ├── latencies.json
    │   ├── query.py
    │   ├── readWorkload.json
    │   ├── temp.json
    │   ├── tempWorkload.json
    │   ├── writeWorkload.json
    │   └── writeWorkload_pretty.json
    ├── pickleSrc
    │   ├── pickledb.py
    │   ├── setup.py
    │   └── tests.py
    └── storage
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-37.pyc
        │   ├── dataFile.cpython-37.pyc
        │   ├── database.cpython-37.pyc
        │   ├── fileTracker.cpython-37.pyc
        │   ├── fileUtility.cpython-37.pyc
        │   ├── join.cpython-37.pyc
        │   ├── table.cpython-37.pyc
        │   ├── tempResult.cpython-37.pyc
        │   └── variables.cpython-37.pyc
        ├── dataFile.py
        ├── database.py
        ├── dump
        ├── fileTracker.py
        ├── fileUtility.py
        ├── imdbInputParser.py
        ├── join.py
        ├── runner.py
        ├── table.py
        ├── tempResult.py
        └── variables.py

```



src

1. cache: FIFO cache code

        cacheDict.py

2. graph: graphs generated from the workloads

3. interface: interface code

        queryEngine.py

4. perf\_eval: performance evaluation code

       joinWorkloadTest.py

5. picklesrc: original pickled code base

6. storage: backend storage code

        variable.py

**Configure paths to run the code from this branch:**

1. In variable.py - Change the &#39;databaseStorageFilePath&#39; to an appropriate file path.
2. In joinWorkloadTest.py - Change the &#39;configFile&#39; to a json file where the configuration for the workload is present.
3. In joinWorkloadTest.py - Change the &#39;workloadFile&#39; to a json file where the workload is present.
4. In joinWorkloadTest.py - Change the &#39;latencyRecordFile&#39; to a json file where the latencies of the workload can be recorded.

**To run the code from cache branch:**

1. We can also run a workload from joinWorkloadTest.py. This calls the APIs from the queryEngine.py and runs the given workload to produce latency records for each workload.