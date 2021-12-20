This is the first draft of the HyPep PMS Module.

To run module, through command line navigate to directory and run User_export.py.
**if you are not familiar with the command line, here are a few things to keep in mind:
to get to User_export.py, find it in your file explorer, copy the path from the toolbar (windows) and paste in the command line after typing cd:
example: cd documents\sample_files\User_export.py

Path can be inputted by dragging from file explorer to command prompt.

Mass query.csv is a csv with a list of masses from experimental data for matching.
 A sample is provided, mass_query.csv, formatting must be the same.

Enter error margin:
Typical value is 5, this does not pertain to PTM allowance, specifically is to account for 
instrumentation errors

Database Sequence.csv is a list of de novo database peptides. See example saved as Sequence2.csv

Output mass match .csv is a blank csv that you would like all matches to be saved to. Example is df_seq3.csv

Output ptm match .csv is a blank csv where all possible PTMs will be stored. If you are not interested in
 PTM analysis, still direct to blank csv and nothing will be recorded. Example is ptm_report_df.csv

Analysis type:
	Type "complex" if you would like to account for PTMs
	Type "simple" if you don't want to factor for PTMs

	*if you are looking for a specific PTM that is not on our list, you can set the error margin 
	to the value of PTM of interest and run the simple analysis.