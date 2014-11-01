###Summaries
---
[1]	Cardosa. M., Wang. C., Nangia. A., Chandra. A., and Weissman. J., Exploring MapReduce Efficiency with highly – distributed data, MapReduce’11, June 8, 2011, San Jose, California, USA, Pg: 27-33.
---
___Summary:___
	In this paper authors explained how efficiently mapreduce could search in the data while distributing them. Few architectural approaches were given to know the performance of mapreduce.
The architecture approaches given are: Local MapReduce (LMR), Global MapReduce (GMR), and Distributed MapReduce (DMR). They have done experiments on two platforms : PlanetLab and Amazon EC2. Both platforms undergone three experiments namely: High-aggregation, Zero-aggregation and Ballooning-data experiments. Incase of zero-aggregation LMR performed well and incase of high-aggregation DMR performed well.

---
[2]	Fadika. Z., Dede. E., Ramakrishnan. L., and Govindaraju. M., MARIANE: MApReduce Implementation Adapted for HPC Environments, 12th IEEE/ACM International conference on Grid Computing, Washington, DC, USA, 2011, Pg: 82-89.
---
___Summary:___
	The authors of this paper introduced MARIANE (MApReduce Implementation Adapted for HPC Environments), an implementation designed for clustered and shared-disk file systems and as such not dedicated to a specific MapReduce Solution. MARIANE is an extension of MapReduce, so it uses most of the MapReduce functionalities.They have performed experiments of the model on the Magellan testbed at the National Energy Research Scientific Computing Center (NERSC) over Apache Hadoop. From their experiments MARIANE found that they have high performance under working and failing conditions than a regular MapReduce.

---
[3]	Fadika. Z., Dede. E., Hartog. J., and Govindaraju. M., MARLA: MapReduce for heterogeneous clusters, 12th IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing,  2012, Pg: 49-56.
---
___Summary:___
	In this paper the authors introduced a new framework of mapreduce that can perform well even with the clusters that have heterogeneous properties. The architecture of MARLA have three principal modules: Splitter for I/O management, TaskController for managing concurrency, and FaultTracker for fault-tolerance. To get the results of performance authors have done tests on two different clusters: NERSC Magellan cluster and Grid and Cloud Computing Research Lab Cluster. MARLA divides input splits to many nodes.

---
[4]	Kondikoppa. P., Chiu. C., Cui. C., Xue. L., and Park. S., Network-aware scheduling of mapreduce framework on distributed clusters over high speed networks, FederatedClounds’12, September 21, 2012, San Jose, California, USA, Pg: 38-43.
---
___Summary:___
	The authors of this paper states that if the scheduling of map tasks over the cluster is performed well, then mapreduce can work on distributed clusters over high-speed network. The distributed cluster specified is federated cluster. Authors have done experiments on both native hadoop and network aware hadoop using CRON, an Emulab based testbed. FIFO and FAIR schedulers have been used to place the map tasks. While performing the experiments authors found that performance is increased from 12% to 15%.

---	
[5]	Mantha. P., Luckow. A., and Jha. S., Pilot-MapReduce: An extensible and flexible mapreduce implementation for distributed data, MapReduce’12, June 18-19, 2012, Delft, The Netherlands, Pg: 17-24.
---
___Summary:___
	The authors in this paper discusses about Pilot-MapReduce (PMR), a runtime environment for mapreduce. Pilot-MapReduce is infrastructure independent mapreduce. PMR is completely based on the abstraction of computing pilot-jobs and pilot-data. Pilot-jobs are utilized to combine the map phase computation to the nearby source data. Pilot-data is used to transfer data from intermediate data to the reduce phase using parallel data. PMR uses finer-grain specification to compute and place data.
