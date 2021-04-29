**Branch cache:**

This branch demonstrates our extended version of pickled in the form of an interaction between front end Query Engine and the storage system along with a **Read-Through, Write-Around cache** implementation.

**Folder Structure:**

PICKLEDB

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