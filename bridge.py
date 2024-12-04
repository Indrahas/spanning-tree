class Bridge():

    def __init__(self,id):
        self.root = id
        self.cur_id = id
        self.best_msg=[id,-1,float("inf"),0]
        self.root_dist = 0
        self.nodeToRoot=""
        self.received_messages=[]
        self.nodesOfBridge = dict() #[ [node id,best message from that node], .... ]
        self.changedStatus = False
    def getNodes(self):
        return self.nodesOfBridge
    def addNode(self,node):
        self.nodesOfBridge[node] = [float("inf"),float("inf"),float("inf"),"z"]
    
    def addMessage(self,message):
        self.received_messages.append(message.copy())

    def compare(self,message,check=True):
        if self.root!=message[0]:
            return self.root<message[0]
        elif self.root_dist!=message[1]:
            return self.root_dist<message[1]
        elif self.cur_id!=message[2]:
            return self.cur_id<message[2]
        elif (self.nodeToRoot!=message[3]) and check:
            return self.nodeToRoot<message[3]
        
        return False

            
    def getDP(self):
        designated_ports = []
        for node in self.nodesOfBridge:
            if self.compare(self.nodesOfBridge[node],check=False):
                designated_ports.append(node)
        return designated_ports

    def sendMessages(self,time,trace):
        messages = []
        designated_ports = self.getDP()
        for i in designated_ports:
            messages.append([time+1,[self.root,self.root_dist,self.cur_id, i] ])
            #message = rootPort | distance to root port | current id of bridge | LAN to which message is forwarded
        
        if trace:
            print(time," B{}".format(self.cur_id)," s (B{} ,{} ,B{})".format(self.root,self.root_dist,self.cur_id))
        
        return messages
    def compareMessages(self,cur_message,old_message):
        if cur_message[0]!=old_message[0]:
            return cur_message[0]<old_message[0]
        elif cur_message[1]!=old_message[1]:
            return cur_message[1]<old_message[1]
        elif cur_message[2]!=old_message[2]:
            return cur_message[2]<old_message[2]
        elif cur_message[3]!=old_message[3]:
            return cur_message[3]<old_message[3]
        else:
            return False

    def checkReceive(self,time,trace):
        temp = []
        for i in self.received_messages:
            cur_time = i[0]
            cur_message = i[1]
            if cur_time==time:
                if self.compareMessages(cur_message,self.nodesOfBridge[cur_message[-1]]):
                    self.nodesOfBridge[cur_message[-1]] = cur_message
                if self.compareMessages(cur_message,self.best_msg):
                    self.changedStatus=True
                    self.best_msg = cur_message
                    self.root = cur_message[0]
                    self.root_dist = cur_message[1]+1
                    self.nodeToRoot = cur_message[-1]
                if trace==1:
                    print(time," B{}".format(self.cur_id)," r (B{} ,{} ,B{})".format(cur_message[0], cur_message[1],cur_message[2] ))
            else:
                temp.append(i)
        self.received_messages[:] = temp.copy()
