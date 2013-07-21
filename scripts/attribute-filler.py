TABLE_PATH        = r"E:\oweb\git\nh-database.gdb\OWRI\OWRI_polygons"
GIS_SOURCE        = "owri_poly"
PROJECT_NBR       = "20120444"
RI_PROJECT_ID     = "15467"
ACTIVITY_TYPE     = "Riparian"
TREATMENT_COMMENT = "Riparian treated for non-native or noxious plant species; Riparian trees planted: hardwood; Riparian shrubs or herbaceous vegetation planted/reseeded"
MAPPER            = "OSU-NH"
MAPPER_CONFIDENCE = "High"
GIS_TYPE          = "GIS Polygon Centroid"
ANALYSIS_SCALE    = "6th Field HUC"
ORIGIN_DATE       = "7/20/2013"

import arcpy
rows = arcpy.UpdateCursor(TABLE_PATH)
for row in rows:
	val = row.getValue("project_nbr")
	if (val == None):
		originalComment = row.getValue("treatment_comment")
		if (originalComment != "" and originalComment != None):
			comment = originalComment + "; " + TREATMENT_COMMENT + "; Source data from shapefile"
		else:
			comment = TREATMENT_COMMENT + "; Source data from shapefile"
		row.setValue("gis_source", GIS_SOURCE)
		row.setValue("project_nbr", PROJECT_NBR)
		row.setValue("ri_project_id", RI_PROJECT_ID)
		row.setValue("activity_type", ACTIVITY_TYPE)
		row.setValue("treatment_comment", comment)
		row.setValue("mapper", MAPPER)
		row.setValue("mapper_confidence", MAPPER_CONFIDENCE)
		row.setValue("gis_type", GIS_TYPE)
		row.setValue("analysis_scale", ANALYSIS_SCALE)
		row.setValue("origin_date", ORIGIN_DATE)
		rows.updateRow(row)
print("Finished!")
		
		

