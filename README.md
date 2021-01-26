# LZ Correlation Experiment
Contains all the code,analysis and processing files for LZ correlation experiment.

The main experiment file is new_STLI_updated.psyexp and currently has 5 blocks with a break in between (4 in total). At the start of each presentaion phase , a respective EEG trigger is sent based on the stimulus type and stimulus presentation frequency and also durind the break. In total the experiment has 540 trials , equally split across 3 different types of stimulus and stimulus presentation frequency. Note that while the number is equally split across each type and frequency , the number of trials might not be equal across a certain combination of bot stimulus type and frequnecy. 

## Requirments for the Experiment    
Experiment requires Psychopy , with atlast version v2020.2.5 and Python with a minimum version of 3.6.2
 
 
 ## Instructions for use:
 
 1. Run the stim_randomizer script to generate a random set of stimuli across five blocks for each participant.
 2. Ensure monitor calibration settings and EEG triggers addresses are accurate in the experiment code or within the Psychopy builder. Make sure to also check if the **EEG Triggers** are enabled in the the respective routines.
 3. Run the experiment script using the .py file or through the psychopy builder. 
 
 
#### Depreciated Frame time based versions
Note , All frame time specified versions have been depreciated and archived. If running any of the versions with predefined frame times, make sure you use the version associated with the refresh of the monitor you plan on using it with. 


## Condition codes used within the experiment 
EEG triggers are programmed in the experiment to fire at the start of the presentation phase of the stimuli and is based on the type of stimuli and the frequency at which it's being displayed. Example ' 11 ' for Natural images being presented at 1 Hz. First digit indicates stimuli type and second digit indicates the frequency.  **"67"** is used as the trigger to indicate the onset of breaks.


Experiment uses images from the OASIS dataset and was downloaded from https://db.tt/yYTZYCga .


References 

1. Kurdi B, Lozano S, Banaji MR. Introducing the Open Affective Standardized Image Set (OASIS). Behav Res Methods. 2017 Apr;49(2):457-470. doi: 10.3758/s13428-016-0715-3. PMID: 26907748. 
