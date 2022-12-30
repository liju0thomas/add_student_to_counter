# AddStudent
This function adds student to a counter.It works in the following way
1. Check for open counters and number of students waiting is less than maximum allowed value or not
    1.1. If yes check for minimum number of students waiting in each counter. Add student to that counter.
    1.2. If more than one counter has same number of students waiting allocate student to counter that has lowest counter id.
2. If all open counters opened contains maximum number of allowed students then check if counter limit is reached or not. 
    2.1. If counter limit not reached open a new counter and add student to the new counter.
    2.2. If counter limit is reached write queue is full to output file and return -1.

**Data Structure**

Data Structure used here is queue. Each counter is a seperate queue.

**Time Complexity**

This function used addition of students. It searches multiple queues and assigns student to each queue. Hence the time complexity should be of order O(n^2)

