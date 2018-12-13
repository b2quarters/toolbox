import arcpy  
arcpy.env.workspace = r'E:\Ethiopia'  # example folder (with shapefiles) as workspace  
fclasses = arcpy.ListFeatureClasses()  
  
for fclass in fclasses:  
    fctype = arcpy.Describe(fclass).shapeType  
    print "{0} is a {1} feature class".format(fclass, fctype) 
    
import arcpy, os  
arcpy.env.workspace = r'E:\Ethiopia'  
fclasses = arcpy.ListFeatureClasses()  
  
out_ws_all = r'E:\Ethiopia\python'  
out_ws_pol = r'E:\Ethiopia\python'  
  
for fclass in fclasses:  
    fctype = arcpy.Describe(fclass).shapeType  
    newname = fclass  
    if newname[-4:].upper() == ".SHP":  
        newname = newname[:-4] # trim the .shp extension from the name  
    out_fc = os.path.join(out_ws_all, fclass)  
    arcpy.CopyFeatures_management(fclass, out_fc)  
    if fctype == 'Polygon':  
        out_fc = os.path.join(out_ws_pol, fclass)  
        arcpy.CopyFeatures_management(fclass, out_fc) 
        
import arcpy  
arcpy.env.workspace = r'E:\Ethiopia'  # example folder (with shapefiles) as workspace  
fclasses = arcpy.ListFeatureClasses()  
  
for fclass in fclasses:  
    fctype = arcpy.Describe(fclass).shapeType  
    print (fclass) 
    
print (fctype)
import arcpy  
arcpy.env.workspace = r'E:\Ethiopia'  # example folder (with shapefiles) as workspace  
fclasses = arcpy.ListFeatureClasses()  
  
for fclass in fclasses:  
    fctype = arcpy.Describe(fclass).shapeType  
    print (fctype) 
    if fctype == 'Polygon':
        arcpy.CopyFeatures_management(fclass, copyfc)
        
import arcpy  
arcpy.env.workspace = r'E:\Ethiopia'  # example folder (with shapefiles) as workspace  
fclasses = arcpy.ListFeatureClasses()  
  
for fclass in fclasses:  
    fctype = arcpy.Describe(fclass).shapeType  
    print (fctype) 
    if fctype == 'Polygon':
        copyfc = os.path.join('E:\Ethiopia\python', fclass)
        arcpy.CopyFeatures_management(fclass, copyfc)
        
import arcpy  
arcpy.env.workspace = r'E:\Ethiopia'  # example folder (with shapefiles) as workspace  
fclasses = arcpy.ListFeatureClasses()  
  
for fclass in fclasses:  
    fctype = arcpy.Describe(fclass).shapeType  
    print (fctype) 
    if fctype == 'Polygon':
        copyfc = os.path.join('E:\Ethiopia\python', fclass)
        arcpy.CopyFeatures_management(fclass, copyfc)
        
import arcpy
from arcpy import env
env.workspace = "E:\school\Exercise09"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    print raster
    
import arcpy
from arcpy import env
env.workspace = "E:\school\exercise09"
raster = "tm.img"
desc = arcpy.Describe(raster)
print "Raster base name is: " + desc.basename
print "Raster data type is: " + desc.dataType
print "Raster file extension is: " + desc.extension

import arcpy
from arcpy import env
env.workspace = "E:\school\exercise09"
raster = "tm.img"
desc = arcpy.Describe(raster)
print "Raster base name is: " + desc.basename
print "Raster data type is: " + desc.dataType
print "Raster file extension is: " + desc.extension
print "Raster spatial reference is: " + desc.spatialReference.name
print "Raster format is: " + desc.format
print "Raster compression type is: " + desc.compressionType
print "Raster number of bands is: " + str(desc.bandCount)

import arcpy
from arcpy import env
env.workspace = "E:\school\exercise09"
raster = "tm.img"
desc = arcpy.Describe(raster)
print "Raster base name is: " + desc.basename
print "Raster data type is: " + desc.dataType
print "Raster file extension is: " + desc.extension
print "Raster spatial reference is: " + desc.spatialReference.name
print "Raster format is: " + desc.format
print "Raster compression type is: " + desc.compressionType
print "Raster number of bands is: " + str(desc.bandCount)

import arcpy
from arcpy import env
env.workspace = "E:\school\exercise09"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
print "Raster base name is: " + desc.basename
print "Raster data type is: " + desc.dataType
print "Raster file extension is: " + desc.extension
print "Raster spatial reference is: " + desc.spatialReference.name
print "Raster format is: " + desc.format
print "Raster compression type is: " + desc.compressionType
print "Raster number of bands is: " + str(desc.bandCount)

import arcpy
from arcpy import env
env.workspace = "E:\school\exercise09"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName

print "the raster resolution is " + str(x) + " by " +str(y) + " " + units + "."

 
