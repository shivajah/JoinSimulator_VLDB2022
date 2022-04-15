# JoinSimulator_VLDB2022
This is the source code for the join simulator used calculating the amount of I/O(read and write) and their pattern (random, sequential) during a Dynamic Hybrid Hash Join.

For running, just run: python main.py

In the source code you can set the build size, number of partitions (or you can set it to use Equation 2 in our paper instead), the amount of memory and the fudge factor. The output will look like as below:

MemorySize(MB)	BuildSize(MB)	NumberOfPartitions	RandomWrites(MB)	SequentialWrites(MB)	In Memory Data(MB)	reads_seq(MB)	reads_rand(MB)	numberOfInMemoryPartitions	levels
10240	512000	2	1934800.1587	73814.34375	0	1108842.91822	1923772.46639	0.0	2
