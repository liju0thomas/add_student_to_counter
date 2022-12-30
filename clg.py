class College:
    def __init__(self, c, n):
        self.n = n #total number of people in each queue
        self.c = c #total counters
        self.queues = [[None for i in range(n)] for j in range(c)]
        self.starts = [0 for i in range(c)] # queue start number
        self.ends = [0 for i in range(c)] # queue end number
        self.sizes = [0 for i in range(c)] # queue size
        self.open = [False for i in range(c)] # Which all queues are open
        self.open[0] = True # By default first queue will be true
        self.admission_count = 0 #by default starting count is at zero
        
    def getCounter (self, counterId):
        opFile = open('outputPS08.txt', 'a+')
        counterId-=1
        if counterId < self.c and self.open[counterId]:
            queuess = []
            for val in self.queues[counterId]:
                if val:
                    queuess.append(val)
            # s = self.queues[counterId]
 #           opFile.write(s)
            s = queuess
        else:
            s = []
 #           opFile.write(s)
        self.write_to_output_file('getCounter', str(counterId+1), str(s))
        return s

    def addStudent (self, studentID: int):
        """ This function takes studentid as argument and returns corresponding counter id
        StudentID(arg): Student id of each student
        CounterID(return): Counter id to which the student is assigned
        """
        min_pos = 0
        position_found = False
        last_visited = 0
        for i in range(len(self.open)):
            if  (self.open[i]):
                if  (self.sizes[min_pos] > self.sizes[i]) and (self.sizes[i] < self.n):
                    min_pos = i
                    position_found = True
                last_visited = i

        if (last_visited == 0 and self.sizes[last_visited]  < self.n):
            position_found = True
        if (not position_found) and (last_visited == (self.c -1)):
            file = open("outputPS08.txt","a")
            text = str(studentID) + '\n'
            file.write(text)
            file.close()
            counterId = -1

        elif (not position_found) and (last_visited < (self.c -1)):
            self.queues[last_visited + 1] [0] = studentID
            self.ends[last_visited + 1] = self.ends[last_visited + 1] + 1
            self.sizes[last_visited + 1] = self.sizes[last_visited + 1] + 1
            self.open[last_visited + 1] = True
            counterId = last_visited + 1 + 1
        elif position_found:
            
            self.queues[min_pos] [self.ends[min_pos]] = studentID
            self.ends[min_pos] = self.ends[min_pos] + 1
            self.sizes[min_pos] = self.sizes[min_pos] + 1
            counterId = min_pos + 1

        else:
            self.queues[min_pos] [self.ends[min_pos]] = studentID
            self.sizes[min_pos] = self.sizes[min_pos] + 1
            counterId = min_pos + 1
        
        if counterId != -1:
            self.write_to_output_file('addStudent', str(studentID), str(counterId))
        else:
            self.write_to_output_file('addStudent', str(studentID), 'all queues are full')
        return counterId

    def giveAdmissionTicket (self):
        admission = 0
        #print("1st length : " + str(self.sizes))
        for i in range(self.c):
            if self.open[i] and self.sizes[i]:
                # print("length : " + str(self.sizes))
                admission =admission+1
                    # admission count for single run in all counters
                self.queues[i].pop(0)
                self.sizes[i]-=1
                self.ends[i]-=1
                # print("length after loop: " + str(self.sizes))
        self.write_to_output_file('giveAdmissionTicket','',str(admission))
        return admission
    def isOpen(self, counterId):

        counterId -= 1

        if self.open[counterId]:

            status = True

        else:

            status = False

    
        self.write_to_output_file('isOpen', str(counterId+1), str(status))
        return status

    def write_to_output_file(self, func:str, input_val, out_val):
        file = open("outputPS08.txt","a")
        text = func +':'+input_val + '>>' + out_val+ '\n'
        file.write(text)
        file.close()

if __name__ == "__main__":
    sampleArray = open("inputPS08.txt", "r")
    first_iteration = True

    for lineText in sampleArray:
        if first_iteration:
            inputTxt = lineText.split(':')
            c = College(int(inputTxt[1]), int(inputTxt[2]))
            first_iteration = False
        else:
            inputTxt = lineText.split(':')

        if(inputTxt[0] == "getCounter"):

            #calling isOpen function

            c.getCounter(int(inputTxt[1].strip("\n")))
        if(inputTxt[0] == "addStudent"):

            #calling isOpen function

            c.addStudent(int(inputTxt[1].strip("\n")))

        if(inputTxt[0] == "isOpen"):

            #calling isOpen function

            c.isOpen(int(inputTxt[1].strip("\n")))

        if(inputTxt[0]== "giveAdmissionTicket"):

            #calling isOpen function

            c.giveAdmissionTicket()

# 2 students in each counter and total 5 counters
# c = College(3,5)
# print(c.addStudent(1))
# print(c.addStudent(2))
# print(c.addStudent(3))
# print(c.addStudent(4))
# print(c.addStudent(5))
# print("DM" + str(c.getCounter(1)))
# print("DM" + str(c.getCounter(2)))
# print("status : " + str(c.isOpen(1)))
# print("status : " + str(c.isOpen(2)))
# print(c.addStudent(6))
# print("DM" + str(c.getCounter(1)))
# print("DM" + str(c.getCounter(2)))
# print("Admission : " + str(c.giveAdmissionTicket()))
# print("DM" + str(c.getCounter(1)))
# print("DM" + str(c.getCounter(2)))
# print("Admission : " + str(c.giveAdmissionTicket()))
# print("DM" + str(c.getCounter(1)))
# print("DM" + str(c.getCounter(2)))
# print("Admission : " + str(c.giveAdmissionTicket()))
# print("DM" + str(c.getCounter(1)))
# print("DM" + str(c.getCounter(2)))
# print(c.addStudent(7))
# print("DM" + str(c.getCounter(1)))
# print("DM" + str(c.getCounter(2)))
