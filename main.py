import sys
from heap import *
from helpful import *

PATH = "example.txt"
BLOCK_SIZE = 4

if len(sys.argv) > 1:
    PATH = str(sys.argv[1])

if len(sys.argv) > 2:
    BLOCK_SIZE = int(sys.argv[2])


    
class Huffman:

    def __init__(self, inputBits, blockSize = BLOCK_SIZE):

        self.inputBits = inputBits
        self.blockSize = blockSize
        self.codesDict = {}

    def getFrequencyDict(self):
        
        print ("Started computing frequency dict")
        
        bitIndex = 0
        blockResult = 0
        frequencyDict = {}
        
        for bit in self.inputBits:

            if bit:
                blockResult += (1 << bitIndex)

            bitIndex += 1

            if bitIndex == self.blockSize:
                
                if blockResult not in frequencyDict.keys():
                    frequencyDict[blockResult] = 0

                frequencyDict[blockResult] += 1

                bitIndex = 0
                blockResult = 0

        if bitIndex != 0:
            
                if blockResult not in frequencyDict.keys():
                    frequencyDict[blockResult] = 0

                frequencyDict[blockResult] += 1
            
        print ("Done computing frequency dict")
        
        return frequencyDict

    def getHuffmanTreeRoot(self):

        frequencyDict = self.getFrequencyDict()

        print ("Started computing huffman tree")
        
        heap = Heap()
        
        for key in frequencyDict.keys():
            heap.push(Node(weight = frequencyDict[key], value = key))

        while heap.size() > 1:

            #for node in heap.nodes:
                #print(node.value, node.weight)
            #print("----------------")
            lightestNode = heap.pop()
            secondLightestNode = heap.pop()

            mergedNode = Node(lightestNode.weight + secondLightestNode.weight, leftSon = lightestNode, rightSon = secondLightestNode)
            heap.push(mergedNode)

        print ("Done computing huffman tree")

        return heap.nodes[0]

    def depthFirstSearch(self, node, code = ""):

        if node.value != None:

            self.codesDict[node.value] = code
            return

        if node.leftSon != None:

            self.depthFirstSearch(node.leftSon, code + "0")

        if node.rightSon != None:

            self.depthFirstSearch(node.rightSon, code + "1")

    def computeCodesDict(self):

        print ("Started computing encoding blocks")

        self.depthFirstSearch(self.getHuffmanTreeRoot())

        print ("Done computing encoding blocks")

    def getTranslationDictionary(self):
        
        print ("Started computing translation dictionary")
        
        translationDictionary = ""
        
        for key in range(1 << self.blockSize):

            keyLength = 0
            
            if key in self.codesDict.keys():
            
                keyLength = len(self.codesDict[key])
            
            #print(key, keyLength, self.codesDict[key])
            
            for bitIndex in range(self.blockSize):
                
                if (1 << bitIndex) & keyLength:
                    translationDictionary += "1"
                    
                else:
                    translationDictionary += "0"

            if key in self.codesDict.keys():
                
                translationDictionary += self.codesDict[key]

        print ("Done computing translation dictionary")

        return translationDictionary

    def getTranslatedText(self):

        print ("Started computing traslating text")

        translatedText = ""
        
        bitIndex = 0
        blockResult = 0
        
        for bit in self.inputBits:

            if bit:
                blockResult += (1 << bitIndex)

            bitIndex += 1

            if bitIndex == self.blockSize:

                translatedText += self.codesDict[blockResult]
                blockResult = 0
                bitIndex = 0

        
        if bitIndex != 0:

                translatedText += self.codesDict[blockResult]

        print ("Done computing traslating text")

        return translatedText

    def writeCompressedFile(self):
        
      
        if len(self.codesDict.keys()) == 0:
            self.computeCodesDict()

            if len(self.codesDict.keys()) == 0:
                raise ValueError('No huffman codes. Check input') 

        print ("Started writing compressed file")
        
        compressedTextBits = self.getTranslationDictionary() + self.getTranslatedText() 
        
        f = open(PATH + '.huff', 'wb')

        """
        for byteIndex in range(0, len(compressedTextBits), 8):

            number = 0

            for bitIndex in range(byteIndex, min(byteIndex + 8, len(compressedTextBits))):
                #print(self.inputBits[bitIndex], bitIndex, "AAAAA")
                if compressedTextBits[bitIndex] == '1':
                    
                    number += (1 << (bitIndex - byteIndex))
            print(number, chr(number))
        """
        f.write(bytes(int(compressedTextBits[i : i + 8], 2) for i in range(0, len(compressedTextBits), 8)))

        f.close()

        print ("Done writing compressed file")
    

huffman = Huffman(getBitwise())

#huffman.computeCodesDict()
huffman.writeCompressedFile()
