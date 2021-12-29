This is the first draft of the HyPep PMS Module.

To run module, through command line navigate to directory and run User_export.py.
**if you are not familiar with the command line, here are a few things to keep in mind:
to get to User_export.py, find it in your file explorer, copy the path from the toolbar (Windows) and paste in the command line after typing cd:
example: cd documents\sample_files\User_export.py

Path can be inputted by dragging from file explorer to command prompt.

Mass query.csv is a csv with a list of masses from experimental data for matching.
 A sample is provided, mass_query.csv, formatting must be the same.

Enter error margin:
This does not pertain to PTM allowance, specifically is to account for 
instrumentation errors. This value is in ppm.

Database Sequence.csv is a list of de novo database peptides. See example saved as Sequence2.csv

Output simple mass match .csv is a blank csv that you would like all simple analysis matches to be saved to. Example is simple_out.csv.

Output complex mass match .csv is a blank csv that you would like all complex analysis matches to be saved to. Example is complex_out.csv.

*Even if you only intend to use one of these analyses, you must input a path for each prompt. Feel free to just use the path of the original package .csv

Output ptm match .csv is a blank csv where all possible PTMs will be stored. If you are not interested in
 PTM analysis, still direct to blank csv and nothing will be recorded. Example is ptm_report_df.csv

Analysis type:
	Type "complex" if you would like to account for PTMs
	Type "simple" if you don't want to factor for PTMs

*Results will overwrite in the .csv each time the program is ran.
