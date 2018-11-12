import os

#Place this script in the directory with your townmap.cslmap.gz
#This is usually C:\Program Files (x86)\Steam\steamapps\common\Cities_Skylines\CSLMapView

fileList = os.listdir() #Get all files in the directory

#User parameters ------------------------------------------------------------------------------------------------------
mapResolution=4096 #The resolution of the map image. Since the image should always be square, you only need one dimension
cityName='Santander-' #If there are non timestamped saves of the city, add the dash at the end to include only timestamped maps
folderName='SantanderMaps' #This is the folder that all the generated map images will be dumped to
numberOfTiles=5
#----------------------------------------------------------------------------------------------------------------------

def writeBatchFile(fileName, dirName, createDir=0): #This function writes the batch file to export the map
    imgName = fileName.replace('.cslmap.gz', '')+'.png' #Create the name of the image that will be exported from the .cslmap.gz by replacing the extension with .png
    f = open('mapExporter.bat', 'w') #Open the batch file for editing
    if createDir==1:
        f.write('mkdir '+dirName+'\n') #If specified, create the image dump directory

    f.write('start /W cslmapview.exe -input '+fileName+' -output '+imgName+' -imagewidth '+str(mapResolution)+' -area '+str(numberOfTiles)+' -silent\n') #Write the batch file command to export the map image from cslmapview.exe
    f.write('copy '+imgName+' '+dirName+'\n') #Copy this image into the image dump folder
    f.close()
    return 'mapExporter.bat' #Return the filename of the batch file. This is useful if you want to create the batch file in this function, because you can call the returned name below


dirCreated=0 #Assume the image dump directory has not been created
for fileName in fileList:
    if cityName in fileName and '.cslmap.gz' in fileName: #If the city name is in the file name
        if dirCreated==0:
            batFileName = writeBatchFile(fileName, folderName, 1) #Create the batch file and have it create a new image dump directory
            dirCreated=1
        else:
            batFileName = writeBatchFile(fileName, folderName, 0) #Create the batch file, but dont create a new directory

        os.system(batFileName) #Run the created batch file
