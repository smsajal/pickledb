Branch work1:

This branch demonstrates our extended version of pickled in the form of an interaction between front end Query Engine and the storage system without any cache implementation.

Folder Structure:

PICKLEDB

1. src

2. cache: FIFO cache code

3. graph: graphs generated from the workloads

4. interface: interface code

        queryEngine.py

5. perf\_eval: performance evaluation code

        atomicOnOffTest.py

6. picklesrc: original pickled code base

7. storage: backend storage code

        variable.py

To run the code from this branch:

1. In variable.py  Change the &#39;databaseStorageFilePath&#39; to an appropriate file path.
2. In atomicOnOffTest.py  Change the &#39;configFile&#39; to a json file where the configuration for the workload is present.
3. In atomicOnOffTest.py  Change the &#39;workloadFile&#39; to a json file where the workload is present.
4. In atomicOnOffTest.py  Change the &#39;latencyRecordFile&#39; to a json file where the latencies of the workload can be recorded.

There are two ways to run the implementation from the work1 branch:

1. We can run it directly from the queryEngine.py. This will give us a menu driven interface to choose a query to run from. The query descriptions are mentioned in comments below every function.
2. We can also run a workload from atomicOnOffTest.py. This calls the APIs from the queryEngine.py and runs the given workload to produce latency records for each workload.