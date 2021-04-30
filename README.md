**Branch cachewb:**

This branch demonstrates our extended version of pickled in the form of an interaction between front end Query Engine and the storage system along with a **Read-Through, Write-Back cache** implementation.

**Folder Structure:**

PICKLEDB

```
.
├── LICENSE
├── README.md
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
    │   ├── atomicON_cache_latencies_AV.json
    │   ├── atomicOff_writeBack_latencies.json
    │   ├── atomicOnConfig.json
    │   ├── atomicOnOffTest.py
    │   ├── atomicOnTest_trial.py
    │   ├── atomicOn_latencies.json
    │   ├── atomicOn_writeBack_latencies.json
    │   ├── config.json
    │   ├── generateWriteWorkload.py
    │   ├── latencies.json
    │   ├── query.py
    │   ├── readWorkload.json
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

        atomicOnOffTest.py

5. picklesrc: original pickled code base

6. storage: backend storage code

        variable.py

**Configure paths to run the code from this branch:**

1. In variable.py - Change the &#39;databaseStorageFilePath&#39; to an appropriate file path.
2. In atomicOnOffTest.py - Change the &#39;configFile&#39; to a json file where the configuration for the workload is present.
3. In atomicOnOffTest.py - Change the &#39;workloadFile&#39; to a json file where the workload is present.
4. In atomicOnOffTest.py - Change the &#39;latencyRecordFile&#39; to a json file where the latencies of the workload can be recorded.

**To run the code from cache branch:**

1. We can also run a workload from atomicOnOffTest.py. This calls the APIs from the queryEngine.py and runs the given workload to produce latency records for each workload.