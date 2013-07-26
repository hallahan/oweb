# This script filters out the word "riparian" or "Riparian" from treatment_comment

TABLE_PATH = r"C:\oweb\git\MappingTemplates_Hallahan_07262013.gdb\OWRI\OWRI_lines"

import arcpy
import string

rows = arcpy.UpdateCursor(TABLE_PATH)
for row in rows:
	treatmentComment = row.getValue("treatment_comment")
	print(treatmentComment)
	idx = string.find(treatmentComment, 'riparian')
	if (idx == -1):
		idx = string.find(treatmentComment, 'Riparian')
	if (idx != -1):
		treatmentComment = treatmentComment[:idx] + treatmentComment[idx+9:]
		print(treatmentComment)
	print(idx)
	row.setValue("treatment_comment", treatmentComment)
	rows.updateRow(row)
print("Finished!")
		
		

