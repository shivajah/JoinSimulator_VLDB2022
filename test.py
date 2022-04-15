# import math
#
# def getNumberOfPartitions(buildSize, memoryInFrames):
#         return  math.ceil((buildSize*fudge - memoryInFrames) / (memoryInFrames - 1)) + 1
#         #return max(1, math.ceil((buildSize * fudge - memoryInFrames) / (memoryInFrames - 1)))+1000
# class ophhj:
#     def __init__(self, buildSize, probeSize, memoryInFrames, numberOfPartitions):
#         self.totalRandomWrites = 0;
#         self.totalSequentialWrites = 0;
#         self.total_reads_seq = 0;
#         self.total_reads_rand = 0;
#         self.buildSize = buildSize
#         self.probeSize = probeSize
#         self.memoryInFrames = memoryInFrames
#         self.numberOfPartitions = numberOfPartitions
#         self.numberOfInMemoryPartitions=-1
#         self.level=-1
#         self.inMemoryData = 0
#         self.joins=[]
#
#     def run(self):
#         j = Join(self.buildSize,self.probeSize,self.memoryInFrames,self.numberOfPartitions,self,0)
#         self.joins.append(j)
#         j.start()
#
#     def printRes(self):
#         for j in self.joins:
#             self.total_reads_rand+= j.reads_rand
#             self.total_reads_seq+=j.reads_seq
#             self.totalSequentialWrites+=j.sequentialWrites
#             self.totalRandomWrites += j.randomWrites
#             self.level= max(j.level, self.level)
#             self.level= max(j.level, self.level)
#         print str(self.memoryInFrames*frameSize/1024)+"\t" + str(self.buildSize*frameSize/1024)+ "\t"+str(self.numberOfPartitions)+ "\t"+str(self.totalRandomWrites*frameSize/1024)+"\t"+str(self.totalSequentialWrites*frameSize/1024)+"\t"+str(self.inMemoryData*frameSize/1024) +"\t"+str(self.total_reads_seq*frameSize/1024)+"\t"+str(self.total_reads_rand*frameSize/1024)+"\t"+str(self.numberOfInMemoryPartitions)+"\t"+str(self.level)
#
# class Join:
#     def __init__(self, buildSize, probeSize, memoryInFrames, numberOfPartitions, ophhj,level):
#         self.randomWrites = 0;
#         self.sequentialWrites = 0;
#         self.reads_seq = 0;
#         self.reads_rand = 0;
#         self.buildSize = buildSize
#         self.probeSize= probeSize
#         self.memoryInFrames = memoryInFrames
#         self.numberOfPartitions = numberOfPartitions
#         self.ophhj=ophhj
#         self.level=level
#         self.numberOfSpillingPartitions=0
#
#
#
#     def start(self):
#         self.build()
#         if self.ophhj.numberOfInMemoryPartitions < 0:
#             self.ophhj.numberOfInMemoryPartitions = self.numberOfPartitions-self.numberOfSpillingPartitions
#         self.probe()
#         s=0
#         while s < self.numberOfSpillingPartitions:
#             buildSpilledSizePerPartition = self.buildSize*(self.numberOfSpillingPartitions/self.numberOfPartitions)/self.numberOfSpillingPartitions
#             probeSpilledSizePerPartition = self.probeSize*(self.numberOfSpillingPartitions/self.numberOfPartitions)/self.numberOfSpillingPartitions
#             j=Join(buildSpilledSizePerPartition,probeSpilledSizePerPartition,self.memoryInFrames,getNumberOfPartitions(buildSpilledSizePerPartition,self.memoryInFrames),self.ophhj,self.level+1)
#             self.ophhj.joins.append(j)
#             j.start()
#             s+=1
#
#
#     def build(self):
#         a=math.ceil(self.buildSize*real_expansion / self.numberOfPartitions*1.0)
#         numberOfInMemoryPartitions = min(self.numberOfPartitions,math.floor((self.memoryInFrames*1.0) / (a*1.0)))
#         self.numberOfSpillingPartitions = self.numberOfPartitions - numberOfInMemoryPartitions
#         totalWritesInThisBuild=0;
#         totalRandWritesInThisBuild=0;
#
#         x = 1;
#         while x <= self.numberOfSpillingPartitions:
#             randWrite=math.floor((((self.buildSize*real_expansion / (self.numberOfPartitions*1.0)) - ((self.memoryInFrames - x + 1))*1.0) / ((self.numberOfPartitions - x + 1)*1.0))+1)
#             seqWrite = math.ceil((self.memoryInFrames - x + 1)*1.0 / ((self.numberOfPartitions - x + 1)*1.0)-1)
#             self.randomWrites += randWrite
#             self.sequentialWrites += seqWrite
#             totalWritesInThisBuild += randWrite+seqWrite
#             totalRandWritesInThisBuild += randWrite
#             x += 1;
#         totalReads = self.buildSize*real_expansion
#         self.reads_seq +=(totalReads-totalRandWritesInThisBuild)#each rand write causes the next read to be random.
#         self.reads_rand += totalRandWritesInThisBuild
#
#         if (self.level ==0):
#             self.ophhj.inMemoryData = self.buildSize*real_expansion - (totalWritesInThisBuild)
#             if self.ophhj.inMemoryData > self.memoryInFrames:
#                 print "here"
#
#
#
#
#     def probe(self):
#         #####Probe's reads and writes
#         # Initial read: all of the buildSize is read into memory. Data is read sequentillay until the point that memory is full, then partitions write to disk randomly, so the rest of the reads are random.
#         randReads = self.probeSize*real_expansion - min(self.memoryInFrames, self.probeSize*real_expansion);
#         self.reads_rand += randReads;
#         self.reads_seq += self.probeSize*real_expansion - randReads;
#         val=(self.probeSize)*real_expansion * (self.numberOfSpillingPartitions / self.numberOfPartitions)  # probe writes. All random.
#         self.randomWrites += val
#
#
#
#
# if __name__ == '__main__':
#     fudge=1.0
#     real_expansion=1.0
#     #memory=[2048,5120,10240,20480] #MB
#     memory=10240
#     frameSize=32 #KB
#     #memInFrames = memory * 1024 / frameSize
#     buildSizes = [x*memory for x in [2,5,10,50,100,500,1000,15,20,30,40,50] ]
#     #buildSizes=[102400]
#     #numberOfPartitions = [2, 5, 10, 15, 20, 30, 40, 50, 60, 70,80,90,100,200,300,400,500,600,700,800,900,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,15000,20000,25000,30000,35000,40000,50000,55000,60000,65000,70000,75000,80000,85000,90000,95000,100000,125000,150000,175000,200000,225000,250000,275000,300000,325000,350000,375000,393210]
#     #numberOfPartitions = [2, 5, 10, 15, 20, 30, 40, 50, 60, 70,80,90,100,200,300,400,500,600,700,800,900,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,15000,20000,25000,30000,35000,40000,50000,55000,60000,65000,70000,75000,80000,85000,90000,95000, 98300]
#     #numberOfPartitions = [2, 5, 10, 15, 20, 30, 40, 50, 60, 70,80,90,100,200,300,400,500,600,700,800,900,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,15000,20000,25000,30000,35000,40000,50000,55000,60000,65000,70000,75000,80000,85000,90000,95000,100000,125000,150000,175000,200000,225000,250000,275000,300000,325000, 327670]
#     numberOfPartitions=[x for x in range(2,101,1)]
#     n = [101,1000]
#     n1=[x for x in range(1000,327670,10000)]
#     #n1 = [x for x in range(1000, 81920, 10000)]
#     for x in n1:
#          n.append(x)
#     for x in n:
#          numberOfPartitions.append(x)
#     #numberOfPartitions.append(81900)
#     # buildSizes=[122880]
#     #numberOfPartitions=[311000]
#     print("MemorySize(MB)\tBuildSize(MB)\tNumberOfPartitions\tRandomWrites(MB)\tSequentialWrites(MB)\tIn Memory Data(MB)\treads_seq(MB)\treads_rand(MB)\tnumberOfInMemoryPartitions\tlevels")
#     for b in buildSizes:
#         bIFrames = b* 1024 / frameSize
#         memInFrames = memory*1024/frameSize
#         for p in numberOfPartitions:
#             _ophhj  =  ophhj(bIFrames,bIFrames,memInFrames,p)
#             _ophhj.run()
#             _ophhj.printRes()
#         # p = getNumberOfPartitions(bIFrames,memInFrames)
#         # _ophhj  =  ophhj(bIFrames,bIFrames,memInFrames,p)
#         # _ophhj.run()
#         # _ophhj.printRes()