from bridge import Bridge


trace = int(input())
n = int(input())

bridge_list=[Bridge(i) for i in range(n+1)]
lan_list={}
for i in range(1,n+1):
    li = list(map(str,input().split()))
    li = li[1:]
    for j in li:
        bridge_list[i].addNode(j)
        if j not in lan_list:
            lan_list[j]=[i]
        else:
            lan_list[j].append(i)
time = 0
isChanged=True
while isChanged and time<100:
    tempChanged = False
    for i in range(1,n+1):
        bridge_list[i].changedStatus=False
        bridge_list[i].checkReceive(time,trace)
        tempChanged = (tempChanged or bridge_list[i].changedStatus)
    if time>1:
        isChanged = tempChanged
    for i in range(1,n+1):
        sent_messages = bridge_list[i].sendMessages(time,trace)
        for message in sent_messages:
            for j in lan_list[message[1][-1]]:
                if j!=i:
                    bridge_list[j].addMessage(message)
    time+=1


for i in range(1,n+1):
    port_status=[]
    designated_ports = bridge_list[i].getDP()
    print("B{}: ".format(i),end="")
    for node in sorted(bridge_list[i].nodesOfBridge):
        if node in designated_ports:
            port_status.append("DP")
        elif node==bridge_list[i].nodeToRoot:
            port_status.append("RP")
        else:
            port_status.append("NP")
    if "DP" not in port_status:
        for node in sorted(bridge_list[i].nodesOfBridge):
            print(node,end="")
            print("-{}".format("NP"),end=" ")
    else:
        for node in sorted(bridge_list[i].nodesOfBridge):
            print(node,end="")
            if node in designated_ports:
                # port_status.append("DP")
                print("-{}".format("DP"),end=" ")
            elif node==bridge_list[i].nodeToRoot:
                # port_status.append("RP")
                print("-{}".format("RP"),end=" ")
            else:
                # port_status.append("NP")
                print("-{}".format("NP"),end=" ")
        
    print()






#Initialize
# for i in range(1,n+1):
#     temp=[0,'s', [i,0,i] ,i]
#     for node in stp.bridges[i]:
#         for bridg in stp.nodes[node]:
#             if bridg>i:
#                 msgs.append(temp+[node,bridg])

# # for i in msgs:
# #     print(i)

# while len(msgs)!=0:
#     msg = msgs.pop(0)
#     # 0  s B1 (B1,0,B1)
#     # t   s|r  Bk   (Bi, d, Bj)
#     # [ [0,'s', [1,0,1] ,1,2], [0,'s', [2,0,2] , 2, 4] ] 
#     # print(msg)
#     #Check for root
#     if trace==1:
#         print(msg[0]," ",msg[1],)
#     info = msg[2]
#     cur_bridge = msg[-1]
#     if info[0]<cur_bridge:
#         info[1]+=1
#         info[2] = cur_bridge
#         msg[3] = cur_bridge
#         t = msg[0]+1
#         stp.solve(t,info,cur_bridge,msgs)
#         if info[0]==1:
#             stp.visited[msg[4]]=True
#             if not stp.rp_config[cur_bridge]:
#                 stp.status[cur_bridge][msg[4]]="RP"
#                 stp.rp_config[cur_bridge]=True
#             elif stp.status[cur_bridge][msg[4]]=="DP":
#                 stp.status[cur_bridge][msg[4]]="NP"

# for i in stp.status:
#     #check for availability of DP
#     num_dp = list(stp.status[i].values()).count("DP")
#     print("B"+str(i)+":",end=" ")
#     for key in sorted(stp.status[i]):
#         if num_dp==0:
#             print("{}-NP".format(key),end=" ")
#         else:
#             print("{}-{}".format(key,stp.status[i][key]),end=" ")
#     print()