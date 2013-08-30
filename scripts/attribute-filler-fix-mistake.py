TABLE_PATH        = r"C:\oweb\git\MappingTemplates_Hallahan_08262013.gdb\OWRI\OWRI_polygons"
GIS_SOURCE        = "owri_poly"
PROJECT_NBR       = "20120231"
RI_PROJECT_ID     = "15269"
ACTIVITY_TYPE     = "Upland"
TREATMENT_COMMENT = "treated for non-native or noxious plant species"
MAPPER            = "OSU-NH"
MAPPER_CONFIDENCE = "High"
GIS_TYPE          = "GIS Polygon Centroid"
ANALYSIS_SCALE    = "6th Field HUC"
ORIGIN_DATE       = "8/30/2013"

import arcpy
rows = arcpy.UpdateCursor(TABLE_PATH)
for row in rows:
	val = row.getValue("ri_project_id")
	if (val == '15269' or val == 15269):
		originalComment = row.getValue("treatment_comment")
		comment = TREATMENT_COMMENT
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
		
		

