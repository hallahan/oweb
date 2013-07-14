try:
    import arcpy

    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")

    # Path to the data (you can also set a workspace instead), change this to point to your data
    InputPath="C:/ProjectsPython/"

    # run the aspect tool
    OutRaster=arcpy.sa.Aspect(InputPath+"OregonDEM.img")

    # save to a TIFF file (try and GRID by removing the extention but it may not work)
    OutRaster.save(InputPath+"Aspect.img")

    print("Finished without an error")
    
except:
    print("An error occurred")
    print arcpy.GetMessages() 