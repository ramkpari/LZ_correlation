# LZ Correlation Experiment
Contains all the code,analysis and processing files for LZ correlation experiment.
 
 
 ## Instructions for use:
 
 1. Run the stim_randomizer script to generate a random set of stimuli across five blocks for each participant.
 2. Ensure monitor calibration settings and EEG triggers addresses are accurate in the experiment code or within the Psychopy builder. Make sure to also check if the **EEG Triggers** are enabled in the the respective routines.
 3. Run the experiment script using the .py file or through the psychopy builder. 
 
 
#### Depreciated Frame time based versions
Note , All frame time specified versions have been depreciated and archived. If running any of the versions with predefined frame times, make sure you use the version associated with the refresh of the monitor you plan on using it with. 


## Condition codes used within the experiment 
EEG triggers are programmed in the experiment to fire at the start of the presentation phase of the stimuli and is based on the type of stimuli and the frequency at which it's being displayed. Example ' 11 ' for Natural images being presented at 1 Hz. First digit indicates stimuli type and second digit indicates the frequency.  **"67"** is used as the trigger to indicate the onset of breaks.