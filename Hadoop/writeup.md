-----
screenshot for jps command:
-----

![alt tag](http://104.131.135.146/BigData/jps.png)


-----
1. Adding nodes to the Hadoop cluster
-----

Thought of writing pages and pages of description on adding cluster but thought if something is present online why doing it again.

so here is the link to how to add the nodes:

http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/


-----
2. Multi-node Hadoop cluster
-----

Yes we can simultaneously run a hadoop cluster and be a slave to another hadoop cluster.

The tutorial for making multi-node hadoop cluster is:

http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-multi-node-cluster/

-----
3. Speculating Hadoop
-----

The memory available is 512 MB is not sufficient to store huge amount of data we are going to use for our projects.

The code we are going to write will fetch large amount of data from different data Nodes and digital ocean provides a restriction of 1 TB on transfer of data

If most of the multi threads of Hadoop are been used by a single Node then rest of the clusters would be waiting in the network to complete the task. so thats the reason we cannot use our servers.
