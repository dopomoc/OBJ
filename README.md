# OBJ
<p>
Simple OBJ Class

OBJData Class - v1.0

Utility class for OBJ Files
Written by Darren Cosker 2020

For info on the OBJ format, see:
    https://en.wikipedia.org/wiki/Wavefront_.obj_file

NB - not guarantee to cover all features! 
Simple OBJ display function included.

Example Usage:</p>
<code>
    objFileName = 'neutralMesh.obj'
    
    objObject = OBJData()
    
    objObject.objRead(objFileName)
    
    objObject.objShow()    
    
</code>
