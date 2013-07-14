# attribute-filler.py

This is a super simple Python script that will allow you to fill all of the attribute fields of a large shapefile you have imported into your geodatabase table. This will save you the tedium of having to fill in possibly hundreds of new rows with values that are the same for each.

Rename all of the variables at the beginning of the file to have the values you want in the table. The script finds all of the new rows that you just added by changing only the ones that have nothing in the `project_number` field.

Nicholas Hallahan
nick@theoutpost.io

Sun Jul 14 2013
