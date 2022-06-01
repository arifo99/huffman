from node import *

class Heap:

    def __init__(self, nodes = []):

        self.nodes = nodes

    def checkUp(self, nodeIndex):

        if nodeIndex == 0:
            return

        if self.nodes[nodeIndex].weight < self.nodes[int(nodeIndex / 2)].weight:

            self.nodes[nodeIndex], self.nodes[int(nodeIndex / 2)]  = self.nodes[int(nodeIndex / 2)], self.nodes[nodeIndex]
            self.checkUp(int(nodeIndex / 2))            

    def checkDown(self, nodeIndex):

        smallestWeight = self.nodes[nodeIndex].weight
        smallestWeightLocation = "current"


        if 2 * nodeIndex < self.size() and smallestWeight > self.nodes[2 * nodeIndex].weight:

            smallestWeight = self.nodes[2 * nodeIndex].weight
            smallestWeightLocation = "left"

        if 2 * nodeIndex + 1 < self.size() and smallestWeight > self.nodes[2 * nodeIndex + 1].weight:

            smallestWeight = self.nodes[2 * nodeIndex + 1].weight
            smallestWeightLocation = "right"

        if smallestWeightLocation == "left":

            self.nodes[nodeIndex], self.nodes[2 * nodeIndex] = self.nodes[2 * nodeIndex], self.nodes[nodeIndex]
            self.checkDown(2 * nodeIndex)

        elif smallestWeightLocation == "right":

            self.nodes[nodeIndex], self.nodes[2 * nodeIndex + 1] = self.nodes[2 * nodeIndex + 1], self.nodes[nodeIndex]
            self.checkDown(2 * nodeIndex + 1)
        
    def push(self, node):

        self.nodes.append(node)
        self.checkUp(len(self.nodes) - 1)
    
    def pop(self, index = 0):

        self.nodes[index], self.nodes[self.size() - 1] = self.nodes[self.size() - 1], self.nodes[index]
        poppedNode = self.nodes[self.size() - 1]
        self.nodes.pop()

        if self.size() != 0:
            self.checkDown(index)
            self.checkUp(index)

        return poppedNode

    def size(self):
        return len(self.nodes)
        