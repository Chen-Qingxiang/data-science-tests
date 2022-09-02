# 2022-08 ICRAR Data Science Exercise

## General instructions

1. Clone this repository into your own GitHub account.
1. All your work will be done in your repository.
1. Inspect the data and understand what is available.
1. When going through the exercise, create git commits, making a history of changes that can be inspected later.
1. The exercise should be completed in Python 3.8+.
1. Your cloned git repository should be structured and populated using standard Python practice for software, which other people might reuse.
1. At the end of the exercise, you will __have__ to push your code to your GitHUB repository and share it with the two people who contributed to the original repo. You can also push regularly before that if you want.


## Details

The two objectives of this exercise are:
1. Produce cleaned and consolidated data files suitable for quick loading by another process (which is not part of this exercise).
1. Produce a visualisation showing significant events/features in the data. 

### Objective 1

You need to clean and consolidate the CSV data files in the data directory and produce three output files, one for each month. 
The cadence of the output data files needs to be strictly hourly (i.e. 00:00:00, 01:00:00, 02:00:00, etc.) and complete, i.e. 24 rows for every day in the monthly file. When you encounter missing rows in the original data files, use the following rules:

1. If the top of the hour (00 minutes) entry is missing or empty, the data for 10 minutes to the hour should be used. 
1. If that is also unavailable, use the data for 10 minutes past the hour.
1. If neither of these values is available, record NaNs for all the columns. 

No matter what, the __observe_time__ column should always contain the respective top of the hour value.

The format of the output files is up to you. 
Choose whatever you think is appropriate for the data at hand to allow for quick loading times for additional steps you would expect in an ML pipeline.

### Objective 2

For the visualisation, think about a situation, where you have to explain and describe the data to somebody and verify that your cleaning actually worked as expected. 
What would you show and how would you show it? 
Given that we have actually not told you anything about what the data actually is, this really needs to concentrate on what you can derive from looking at the data, i.e. plotting it in various ways.

The python package you use to produce the visualisation is up to you.
