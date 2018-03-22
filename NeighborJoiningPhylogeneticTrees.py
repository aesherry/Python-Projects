from hivDist import *
from njHelper import *

def nodeSep(node,nodeL,distD):
    '''A measure of the separation between a node of interest and
    the other nodes.'''
    distSum=0
    for iternode in nodeL:
        if node != iternode:
            distSum+=distD[(node,iternode)]
    return(float(distSum)/(len(nodeL)-2))

def njMetric(node1,node2,nodeL,distD):
    '''Calculates the neighbor joining metric between two nodes.'''
    d=distD[(node1,node2)]
    s1=nodeSep(node1,nodeL,distD)
    s2=nodeSep(node2,nodeL,distD)
    return(d-s1-s2)

def branchLength(nodeA,nodeB,nodeL,distD):
    '''Takes two nodes we're planning to merge, nodeA and nodeB. Calculates the
branch lengths from their common ancestor to each.'''
    dist=distD[(nodeA,nodeB)]
    sepA=nodeSep(nodeA,nodeL,distD)
    sepB=nodeSep(nodeB,nodeL,distD)
    branchA=0.5*(dist+(sepA-sepB))
    branchB=0.5*(dist+(sepB-sepA))
    return(branchA,branchB)

def bestPair(nodeL,distD): 
    """input: list of nodes, dictionary of distances
    output: compares every pair in list of nodes and 
    finds he pair with the minimum value for the 
    neighbor-joining metric"""
    keys = (nodeL[0],nodeL[1])
    minVal = njMetric(nodeL[0],nodeL[1],nodeL,distD)
    for node1 in nodeL:
        for node2 in nodeL:
            if node1 != node2:
                nj= njMetric(node1,node2,nodeL,distD)
                if nj < minVal:
                    minVal = nj
                    keys = (node1,node2)
    return keys



def mergeNodes(nodeA,nodeB,branchLenA,branchLenB):
    """merges nodeA and nodeB into new node which will
    follow our 4-tuple tree format"""
    newNodeA = (nodeA[0], nodeA[1], nodeA[2], branchLenA)
    newNodeB = (nodeB[0], nodeB[1], nodeB[2], branchLenB)
    new = ('anc',newNodeA,newNodeB,0)
    return new

def updateDistances(nodeA,nodeB,newNode,nodeL,distD):
    """input: distance dictionary
    output: updates distD assing distances to a newly created node"""
    for node in nodeL:
        if node not in (nodeA, nodeB):
            dis = 0.5 * (distD[(node,nodeA)]+distD[(node,nodeB)]-distD[(nodeA,nodeB)])
            distD[(newNode,node)]=dis
            distD[(node,newNode)]=dis
            
def terminate(nodeL,distD):
    """takes a list of nodes (which has now been reduced to 
    two nodes) and a distance dictionary as input. It 
    calculates the distance between these two nodes, and then 
    calls mergeNodes to merge them. It returns the final merged node"""
    b= 0.5 * distD[(nodeL[0],nodeL[1])]
    newNode = mergeNodes(nodeL[0], nodeL[1], b, b)
    return newNode

def nj(nodeL,distD):
    """which takes a node list and a distance dictionary as input. 
    It then reconstructs and returns a phylogenetic tree in tuple 
    tree format"""
    while len(nodeL) > 2:
        nodeA,nodeB = bestPair(nodeL,distD)
        bA, bB = branchLength(nodeA,nodeB,nodeL,distD)
        newNode= mergeNodes(nodeA, nodeB, bA, bB)
        updateDistances(nodeA,nodeB,newNode,nodeL,distD)
        nodeL.remove(nodeA)
        nodeL.remove(nodeB)
        nodeL.append(newNode)
    return terminate(nodeL,distD)



