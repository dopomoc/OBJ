'''
OBJData Class - v1.0

Utility class for OBJ Files
Written by Darren Cosker 2020

For info on the OBJ format, see:
    https://en.wikipedia.org/wiki/Wavefront_.obj_file

NB - not guarantee to cover all features! 
Simple OBJ display function included.

Example Usage:
    objFileName = 'neutralMesh.obj'
    objObject = OBJData()
    objObject.objRead(objFileName)
    objObject.objShow()    

'''


import numpy as np
import sys
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class OBJData:
    def __init__(self, objFileName='Empty'):
        self.vertices = []
        self.normals = []
        self.texture = []
        self.faces = []
        self.objFileName = objFileName
        self.allLines = []
        self.numVerts = 0
        self.numFaces = 0
        self.numTexture = 0
        self.numNormals = 0
        
    def objRead(self, objFileName):
        
        '''
        # Open OBJ file and read.         

        '''
        print('Reading OBJ File..', objFileName)
        
        objFile = open(objFileName)
                      
        self.allLines = objFile.read().split("\n") # Split each line by \n
        numLines = len(self.allLines) 
 
        lineIter = 0        
        while(lineIter<numLines-1):
                    
            line = self.allLines[lineIter].split()
            
            if(line[0]=='v'):
                self.vertices.append(line[1:])
                self.numVerts+=1
                
            if(line[0]=='vn'):
                self.normals.append(line[1:])
                self.numNormals+=1
            
            if(line[0]=='vt'):
                self.texture.append(line[1:])
                self.numTexture+=1
            
            if(line[0]=='f'):
                self.faces.append(line[1:])
                self.numFaces+=1
                            
            lineIter+=1
        
        print('Finished Reading OBJ')

    def objShow(self):
        
        '''
        # Show OBJ File
        '''
        npVertices = np.array(self.vertices)  
        npVerticesX = npVertices[:,0]
        npVerticesY = npVertices[:,1]
        npVerticesZ = npVertices[:,2]
        
        npVerticesX = [float(npVerticesX[i]) for i in range(self.numVerts)]
        npVerticesY = [float(npVerticesY[i]) for i in range(self.numVerts)]
        npVerticesZ = [float(npVerticesZ[i]) for i in range(self.numVerts)]
        
        npFaces = np.array(self.faces)
        npFacesSplit = []
            
        [npFacesSplit.append([int(npFaces[i][0].split('/')[0])-1,int(npFaces[i][1].split('/')[0])-1,int(npFaces[i][2].split('/')[0])-1]) for i in range(self.numFaces)]
               
        minX = min(npVerticesX)
        maxX = max(npVerticesX)
        minY = min(npVerticesY)
        maxY = max(npVerticesY)
        minZ = min(npVerticesZ)
        maxZ = max(npVerticesZ)
        
        # Can't get axis equal with plot 3D - so scale accordingly with a box        
        xS =  max([maxY,maxZ]) / maxX
        yS = 1 #Leave on axis fixed - should be arbitrary
        zS = max([maxX,maxY]) / maxZ    
        
        boxX = np.array([minX*xS,maxX*xS,minX*xS,maxX*xS,minX*xS,maxX*xS,minX*xS,maxX*xS])
        boxY = np.array([minY*yS,minY*yS,minY*yS,minY*yS,maxY*yS,maxY*yS,maxY*yS,maxY*yS])
        boxZ = np.array([minZ*zS,minZ*zS,maxZ*zS,maxZ*zS,minZ*zS,minZ*zS,maxZ*zS,maxZ*zS])
        
        print('Drawing OBJ..')               
        ax = plt.axes(projection="3d")                              
        ax.plot3D(boxX,boxZ,boxY,'wo')        
        ax.plot_trisurf(npVerticesX, npVerticesZ,npVerticesY,triangles = npFacesSplit)
        #ax.plot3D(npVerticesX, npVerticesZ, npVerticesY, 'ro')                       

        plt.xticks([])
        plt.yticks([])
        ax.zaxis.set_ticklabels([])        
        
        plt.show()
           

if __name__ == '__main__':
    print('OBJData \'main\' is running the default demo..')
    print('Run as a program, this will run through basic usage.')
    print('System inputs', sys.argv)
    
    objFileName = 'neutralMesh.obj'
    objObject = OBJData()
    objObject.objRead(objFileName)
    objObject.objShow()
    
    
    
    
    
    