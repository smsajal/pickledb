**Branch work1:**

This branch demonstrates our extended version of pickled in the form of an interaction between front end Query Engine and the storage system **without any cache** implementation.

**Folder Structure:**

PICKLEDB
```
.
├── LICENSE
├── README.md
├── data
│   ├── atomicOFF_cache_latencies.json
│   ├── atomicON_cache_latencies.json
│   ├── atomicOff_nonCache_latencies.json
│   ├── atomicOff_writeBack_latencies.json
│   ├── atomicOn_nonCache_latencies.json
│   └── atomicOn_writeBack_latencies.json
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
    │   └── __pycache__
    │       ├── cache.cpython-37.pyc
    │       └── caheDict.cpython-37.pyc
    ├── graph
    │   ├── __init__.py
    │   ├── generateGraph.py
    │   └── graph
    │       ├── atomicOnOff_WB_workload1.png
    │       ├── atomicOnOff_WB_workload2.png
    │       ├── atomicOnOff_WB_workload3.png
    │       ├── atomicOnOff_cache_Reportworkload1.png
    │       ├── atomicOnOff_cache_Reportworkload2.png
    │       ├── atomicOnOff_cache_Reportworkload3.png
    │       ├── atomicOnOff_cache_workload1.png
    │       ├── atomicOnOff_cache_workload2.png
    │       ├── atomicOnOff_cache_workload3.png
    │       ├── atomicOnOff_noncache_workload1.png
    │       ├── atomicOnOff_noncache_workload2.png
    │       ├── atomicOnOff_noncache_workload3.png
    │       ├── atomic_workload1.png
    │       ├── atomic_workload2.png
    │       ├── atomic_workload3.png
    │       ├── cacheOnOff_atomicON_Reportworkload1.png
    │       ├── cacheOnOff_atomicON_Reportworkload2.png
    │       ├── cacheOnOff_atomicON_Reportworkload3.png
    │       ├── cacheOnOff_atomicOn_workload1.png
    │       ├── cacheOnOff_atomicOn_workload2.png
    │       ├── cacheOnOff_atomicOn_workload3.png
    │       ├── cacheWB_atomicON_Reportworkload1.png
    │       ├── cacheWB_atomicON_Reportworkload2.png
    │       ├── cacheWB_atomicON_Reportworkload3.png
    │       ├── cacheWB_atomicOn_workload1.png
    │       ├── cacheWB_atomicOn_workload2.png
    │       ├── cacheWB_atomicOn_workload3.png
    │       └── joinTest3.png
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
    │   ├── atomicOff_nonCache_latencies.json
    │   ├── atomicOnConfig.json
    │   ├── atomicOnOffTest.py
    │   ├── atomicOnTest_trial.py
    │   ├── atomicOn_latencies.json
    │   ├── atomicOn_nonCache_latencies.json
    │   ├── config.json
    │   ├── generateWriteWorkload.py
    │   ├── joinConfig.json
    │   ├── joinLatency.json
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

2. graph: graphs generated from the workloads

3. interface: interface code

        queryEngine.py

4. perf\_eval: performance evaluation code

        atomicOnOffTest.py

5. picklesrc: original pickled code base

6. storage: backend storage code

        variable.py

**Configure Paths to run the code from this branch:**

1. In variable.py - Change the &#39;databaseStorageFilePath&#39; to an appropriate file path.
2. In atomicOnOffTest.py - Change the &#39;configFile&#39; to a json file where the configuration for the workload is present.
3. In atomicOnOffTest.py - Change the &#39;workloadFile&#39; to a json file where the workload is present.
4. In atomicOnOffTest.py - Change the &#39;latencyRecordFile&#39; to a json file where the latencies of the workload can be recorded.

**There are two ways to run the implementation from the work1 branch:**

1. We can run it directly from the queryEngine.py. This will give us a menu driven interface to choose a query to run from. The query descriptions are mentioned in comments below every function.
2. We can also run a workload from atomicOnOffTest.py. This calls the APIs from the queryEngine.py and runs the given workload to produce latency records for each workload.