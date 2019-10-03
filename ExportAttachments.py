import arcpy				#imports arcpy toolset
from arcpy import da			#imports data access from arcpy
import os				#imports operating system toolset, allows python to access files and folders

inTable = arcpy.GetParameterAsText(0)	#inTable is a variable with the first column (zero) in the table.
fileLocation = arcpy.GetParameterAsText(1) #creates variable with the second column (one) in the table. 

with da.SearchCursor(inTable, ['DATA', 'ATT_NAME', 'ATTACHMENTID']) as cursor: 
    for item in cursor:
        attachment = item[0]
        filenum = "ATT" + str(item[2]) + "_"
        filename = "GlobalID" + filenum + str(item[1])
        open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
        del item
        del filenum
        del filename
        del attachment
