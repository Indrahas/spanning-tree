This project implements a simulation of the **Spanning Tree Protocol (STP)**, which is used in computer networks to prevent loops in Layer 2 network topologies. The simulator mimics the behavior of network bridges, message exchanges, and the formation of a spanning tree.  

Key functionalities include:  
- Simulating bridges and their behavior as per STP protocols.  
- Demonstrating how messages propagate through the network topology to establish a loop-free spanning tree.  
- Verifying results using predefined test cases for various topologies.  

## Features  
- **Bridge Simulation**: Implements the logic for network bridges, including message handling and protocol execution.  
- **Network Simulation**: Simulates the flow of messages between bridges in a given topology.  
- **Test Cases**: Provides pre-defined network topologies with expected outputs for validation.  

## Directory Structure  
```  
├── bridge.py         # Code to mimic an actual bridge and STP behavior  
├── bridgesim.py      # Main script to simulate message flow and spanning tree formation  
├── test/             # Test cases for different topologies with input and expected output
```

## How to Run  


### Steps  
1. **Clone the Repository**  
   Clone the repository to your local machine and run the file:  
   ```plaintext
     git clone https://github.com/Indrahas/spanning-tree.git 
     cd spanning-tree
     python3 bridgesim.py
2. **Provide Input**  
   The simulator expects input specifying the network topology. Input files are available in the test/ directory.

## Examples  

### Input (from `test/2_inp_practice_tc2`)  
```plaintext  
1
5
B1: A G B
B2: G F
B3: B C
B4: C F E
B5: C D E
```
### Output   
```plaintext  
0  B1  s (B1 ,0 ,B1)
0  B2  s (B2 ,0 ,B2)
0  B3  s (B3 ,0 ,B3)
0  B4  s (B4 ,0 ,B4)
0  B5  s (B5 ,0 ,B5)
1  B1  r (B2 ,0 ,B2)
1  B1  r (B3 ,0 ,B3)
1  B2  r (B1 ,0 ,B1)
1  B2  r (B4 ,0 ,B4)
1  B3  r (B1 ,0 ,B1)
1  B3  r (B4 ,0 ,B4)
1  B3  r (B5 ,0 ,B5)
1  B4  r (B2 ,0 ,B2)
1  B4  r (B3 ,0 ,B3)
1  B4  r (B5 ,0 ,B5)
1  B4  r (B5 ,0 ,B5)
1  B5  r (B3 ,0 ,B3)
1  B5  r (B4 ,0 ,B4)
1  B5  r (B4 ,0 ,B4)
1  B1  s (B1 ,0 ,B1)
1  B2  s (B1 ,1 ,B2)
1  B3  s (B1 ,1 ,B3)
1  B4  s (B2 ,1 ,B4)
1  B5  s (B3 ,1 ,B5)
2  B2  r (B1 ,0 ,B1)
2  B3  r (B1 ,0 ,B1)
2  B3  r (B2 ,1 ,B4)
2  B4  r (B1 ,1 ,B2)
2  B4  r (B1 ,1 ,B3)
2  B4  r (B3 ,1 ,B5)
2  B5  r (B1 ,1 ,B3)
2  B5  r (B2 ,1 ,B4)
2  B5  r (B2 ,1 ,B4)
2  B1  s (B1 ,0 ,B1)
2  B2  s (B1 ,1 ,B2)
2  B3  s (B1 ,1 ,B3)
2  B4  s (B1 ,2 ,B4)
2  B5  s (B1 ,2 ,B5)
3  B2  r (B1 ,0 ,B1)
3  B3  r (B1 ,0 ,B1)
3  B4  r (B1 ,1 ,B2)
3  B4  r (B1 ,1 ,B3)
3  B4  r (B1 ,2 ,B5)
3  B5  r (B1 ,1 ,B3)
3  B5  r (B1 ,2 ,B4)
3  B1  s (B1 ,0 ,B1)
3  B2  s (B1 ,1 ,B2)
3  B3  s (B1 ,1 ,B3)
3  B4  s (B1 ,2 ,B4)
3  B5  s (B1 ,2 ,B5)
B1: A-DP B-DP G-DP
B2: F-DP G-RP 
B3: B-RP C-DP 
B4: C-NP E-DP F-RP 
B5: C-RP D-DP E-NP
