"""
Stimulation presentation order csv file for use with the LZ correlation experiment with Psychopy.

Outputs CSV files with a randomized structure for stimulus presentation.

Uses rank in a loaded list for randomization. Randomization conditions used 
-> No repeat in simultaneous trial

Keys used for the forced choice task are A,Z,K,M.  A for Top-Left , Z for Bottom Left , K for Top right , M for Bottom Right.


Condition field contains a comination of frequency of stimulation and tyoe of stimulus encoded into one. eg: 11 for Natural at 1 hz

""" 

# Initiallization 

import os
import glob
#from PIL import Image
#import imageio
import random
import numpy as np
import copy
from pathlib import Path

# Storage array for stimulus paths
stim_present_data = np.zeros((180,22),dtype = 'U240')

# Edited to produce only one file. 
#stim_choice_data = np.zeros((180,5),dtype = 'U240')

# Randomization function with checker and redo function.

def randfchoice(a,b):
    """ Function for randomization within the choice task function. Pulls an appropriate stimuli image not in the stimulus section of current trial """
    
    # Store control variable from loop for accessing the respective row in list
    
    access_index = a
    
    # Pull stimulus type from the list. 1 - Natural 2 - Scrambled 3- Noise
    stimulus_type = b
    
    # Main control loop
    
    func_break_limit = 0 
    
    while func_break_limit == 0:
        if stimulus_type == 1:
            # Randomised assign from shuffled list of natural images.
            temp = random.choice(stim_list_natural)

            # Verify if randomisation works , if not repick 

            if temp == stim_present_data[access_index,0] or temp == stim_present_data[access_index,1] or temp == stim_present_data[access_index,2] or temp == stim_present_data[access_index,3] or temp == stim_present_data[access_index,4] or temp == stim_present_data[access_index,5] or temp == stim_present_data[access_index,6] or temp == stim_present_data[access_index,7] or temp == stim_present_data[access_index,8] or temp == stim_present_data[access_index,9] or temp == stim_present_data[access_index,10] or temp == stim_present_data[access_index,11] or temp == stim_present_data[access_index,12] or temp == stim_present_data[access_index,13] or temp == stim_present_data[access_index,14] or temp == stim_present_data[access_index,15]:
                continue

            else: 

                break

        elif stimulus_type == 2:
            # Randomised assign from shuffled list of scrambled images.
            temp = random.choice(stim_list_scrambled)

            # Verify if randomisation works , if not repick 

            if temp == stim_present_data[access_index,0] or temp == stim_present_data[access_index,1] or temp == stim_present_data[access_index,2] or temp == stim_present_data[access_index,3] or temp == stim_present_data[access_index,4] or temp == stim_present_data[access_index,5] or temp == stim_present_data[access_index,6] or temp == stim_present_data[access_index,7] or temp == stim_present_data[access_index,8] or temp == stim_present_data[access_index,9] or temp == stim_present_data[access_index,10] or temp == stim_present_data[access_index,11] or temp == stim_present_data[access_index,12] or temp == stim_present_data[access_index,13] or temp == stim_present_data[access_index,14] or temp == stim_present_data[access_index,15]:
                continue

            else: 

                break


        elif stimulus_type == 3:
            # Randomised assign from shuffled list of scrambled images.
            temp = random.choice(stim_list_noise)

            # Verify if randomisation works , if not repick 

            if temp == stim_present_data[access_index,0] or temp == stim_present_data[access_index,1] or temp == stim_present_data[access_index,2] or temp == stim_present_data[access_index,3] or temp == stim_present_data[access_index,4] or temp == stim_present_data[access_index,5] or temp == stim_present_data[access_index,6] or temp == stim_present_data[access_index,7] or temp == stim_present_data[access_index,8] or temp == stim_present_data[access_index,9] or temp == stim_present_data[access_index,10] or temp == stim_present_data[access_index,11] or temp == stim_present_data[access_index,12] or temp == stim_present_data[access_index,13] or temp == stim_present_data[access_index,14] or temp == stim_present_data[access_index,15]:
                continue

            else: 

                break
        
    return temp

def randstim(a,s,d):
    """ Function for randomisation of stimuli """
    
    # Store the frequency of presentation 
    
    freque = d
    
    # Store control variable from loop for accessing the respective row in list for the previous trial. Minus one to access index since we're looking at the previous row. 
    
    access_index = a - 1
    
    # Pull stimulus type from the list. 1 - Natural 2 - Scrambled 3- Noise
    stimulus_type = s
    
    # Main control variable for loop 
    
    break_limit = 0
    
    while break_limit == 0:
        if stimulus_type == 1:
            #natural
            
            
            # Randomised assign from shuffled list of natural images.
            temp = stim_list_natural_copy.pop(0)
            
            # Verify if pick is not repeated from last trial, if not repick. Within trial aspect is managed using shuffle from list and popping

            if temp == stim_present_data[access_index,0] or temp == stim_present_data[access_index,1] or temp == stim_present_data[access_index,2] or temp == stim_present_data[access_index,3] or temp == stim_present_data[access_index,4] or temp == stim_present_data[access_index,5] or temp == stim_present_data[access_index,6] or temp == stim_present_data[access_index,7] or temp == stim_present_data[access_index,8] or temp == stim_present_data[access_index,9] or temp == stim_present_data[access_index,10] or temp == stim_present_data[access_index,11] or temp == stim_present_data[access_index,12] or temp == stim_present_data[access_index,13] or temp == stim_present_data[access_index,14] or temp == stim_present_data[access_index,15]:
                continue

            else: 

                break
                
        
        
        elif stimulus_type == 2:
            #scrambled
            
             # Randomised assign from shuffled list of scrambled images.
            temp = stim_list_scrambled_copy.pop(0)
            
            # Verify if pick is not repeated from last trial, if not repick. Within trial aspect is managed using shuffle from list and popping

            if temp == stim_present_data[access_index,0] or temp == stim_present_data[access_index,1] or temp == stim_present_data[access_index,2] or temp == stim_present_data[access_index,3] or temp == stim_present_data[access_index,4] or temp == stim_present_data[access_index,5] or temp == stim_present_data[access_index,6] or temp == stim_present_data[access_index,7] or temp == stim_present_data[access_index,8] or temp == stim_present_data[access_index,9] or temp == stim_present_data[access_index,10] or temp == stim_present_data[access_index,11] or temp == stim_present_data[access_index,12] or temp == stim_present_data[access_index,13] or temp == stim_present_data[access_index,14] or temp == stim_present_data[access_index,15]:
                continue

            else: 

                break
                
            
        
        elif stimulus_type == 3:
            #noise
            
            # Randomised assign from shuffled list of scrambled images.
            temp = stim_list_noise_copy.pop(0)
            
            
            # Verify if pick is not repeated from last trial, if not repick. Within trial aspect is managed using shuffle from list and popping

            if temp == stim_present_data[access_index,0] or temp == stim_present_data[access_index,1] or temp == stim_present_data[access_index,2] or temp == stim_present_data[access_index,3] or temp == stim_present_data[access_index,4] or temp == stim_present_data[access_index,5] or temp == stim_present_data[access_index,6] or temp == stim_present_data[access_index,7] or temp == stim_present_data[access_index,8] or temp == stim_present_data[access_index,9] or temp == stim_present_data[access_index,10] or temp == stim_present_data[access_index,11] or temp == stim_present_data[access_index,12] or temp == stim_present_data[access_index,13] or temp == stim_present_data[access_index,14] or temp == stim_present_data[access_index,15]:
                continue

            else: 

                break
                
    
    # Return the pick
    return temp


# Run this section before execution to ensure limits and lists are properly set and loaded respectively

# Loading file with specified criteria using Glob. Path included in criteria. Three paths used due to three sets of stimuli to be used. Make sure the filepath does not have any spaces in them for final.

stim_list_natural = [f for f in glob.glob(r'LZ_natural/*.jpg')]
stim_list_scrambled = [f for f in glob.glob(r'LZ_scrambled/*.jpg')]
stim_list_noise = [f for f in glob.glob(r'LZ_noise/*.jpg')]


# Shuffling the lists for randomised order. Initial shuffle. 
random.shuffle(stim_list_natural)
random.shuffle(stim_list_scrambled)
random.shuffle(stim_list_natural)

loop_len_natural = range(len(stim_list_natural))
loop_len_scrambled = range(len(stim_list_scrambled))
loop_len_noise = range(len(stim_list_noise))

# Number of blocks 
block_count = 3 

# Global limits for each condition variable for the entire experiment. Both type of stimuli and presentation frequency of stimuli. (3x4 experimental design). Limits set to ensure equal distribution across blocks. 

# 4 hz version removed , So currently uses a 3x3 experimental design

limit_natural = 180
limit_scrambled = 180
limit_noise = 180
limit_onehz = 180
limit_twohz = 180
limit_threehz = 180
limit_fourhz = 0

# Limit for number of trials in which an image from presentaion stream is displayed (p - present) or not displayed (np - not present). Actual limits assigned during runtime inside the main loop
limit_answer_type = 30

# Number of trials per block. Also statically set within the loop
trial_len = 180

#Recursive loops to create the file structure

# Block structure control. 

for i in range(block_count):
    
    # Dynamically allocate limits for each stimulus type based on number of blocks 
    block_limit_natural = limit_natural / block_count
    block_limit_scrambled = limit_scrambled / block_count
    block_limit_noise = limit_noise / block_count
    block_limit_onehz = limit_onehz / block_count
    block_limit_twohz = limit_twohz / block_count
    block_limit_threehz = limit_threehz / block_count
    block_limit_fourhz = limit_fourhz / block_count
    
    # Allocating limits for each choice type. (p vs np)
    block_limit_natural_p = block_limit_natural / 2
    block_limit_natural_np = block_limit_natural / 2
    block_limit_scrambled_p = block_limit_scrambled / 2
    block_limit_scrambled_np =  block_limit_scrambled / 2
    block_limit_noise_p = block_limit_noise / 2
    block_limit_noise_np = block_limit_noise / 2
    
    
    # Reset randomised set each time to for stimulus selction through list popping. Pulled is shuffles everytime for a block.
    stim_list_natural_copy = copy.deepcopy(stim_list_natural)
    stim_list_scrambled_copy = copy.deepcopy(stim_list_scrambled)
    stim_list_noise_copy = copy.deepcopy(stim_list_noise)
    
    random.shuffle(stim_list_natural_copy)
    random.shuffle(stim_list_scrambled_copy)
    random.shuffle(stim_list_noise_copy)
    
    
    
    # Control varible for each trial in a single block.
    x = 0
    
    while x < 180:
        # Main loop to decide to type of stimulus. 1- Natural , 2- Scrambled and 3- Noise. Laddered structure baseed on choice
        stim_type_choice = random.choice([1,2,3])
        
        # Manual reset.
        frequency_choice = 0

        if stim_type_choice == 1 and block_limit_natural != 0: 
            # Natural images block
            
            #Verify if images still left in block. Else refill the block
            
            if len(stim_list_natural_copy) <= 32:
                stim_list_natural_copy = copy.deepcopy(stim_list_natural)
                random.shuffle(stim_list_natural_copy)
                

            block_limit_natural = block_limit_natural - 1
            
            

            # Emergency break condition
            break_limit = 0 

            while break_limit == 0: 
                
                # Frequnecy of stimuli presentation choice .
                frequency_choice = random.choice([1,2,3])
                
                if frequency_choice == 1: 
                    # Check if limit is reached
                    if block_limit_onehz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 1
                        block_limit_onehz = block_limit_onehz - 1
                        break

                elif frequency_choice == 2:
                    # Check if limit is reached
                    if block_limit_twohz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 2
                        block_limit_twohz = block_limit_twohz - 1
                        break

                elif frequency_choice == 3:
                    # Check if limit is reached
                    if block_limit_threehz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 3
                        block_limit_threehz = block_limit_threehz - 1
                        break
                elif frequency_choice == 4:
                    # Check if limit is reached
                    if block_limit_fourhz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 4
                        block_limit_fourhz = block_limit_fourhz - 1
                        break

            # Stimulus Presentation section
            
            # Image selection for RSVP stream
            stim_present_data[x,0] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,1] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,2] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,3] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,20] = stim_type_choice
            
            if frequency_choice == 2 or frequency_choice == 3 or frequency_choice == 4:
            
                stim_present_data[x,4] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,5] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,6] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,7] = randstim(x,stim_type_choice,frequency_choice)
                
                
            if frequency_choice == 3 or frequency_choice == 4:
                stim_present_data[x,8] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,9] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,10] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,11] = randstim(x,stim_type_choice,frequency_choice)
                
                
            if frequency_choice == 4:
                stim_present_data[x,12] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,13] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,14] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,15] = randstim(x,stim_type_choice,frequency_choice)
                
            
            
            
            
            

          
            # Choice section
 
            #   P vs NP trials. Aka image present or not present in stim presentation stream. 

            
            
            # Randomly pick one image from the presentation section if p trial or one not in presentation section if np trial. Alter based on frequency and number of images presented. 
            
            choice_break_limit = 0
            
            while choice_break_limit == 0:
                choice_present = random.choice([0,1])
                                
                if choice_present == 1:
                    if block_limit_natural_p == 0:
                        continue
                        
                    else:
                        
                        correct_answer_key = 'a'
                        stim_present_data[x,18] = choice_present
                        stim_present_data[x,19] = correct_answer_key
                        

                        if frequency_choice == 1:

                            correct_answer = random.randrange(0,3)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]

                        elif frequency_choice == 2:

                            correct_answer = random.randrange(0,7)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]

                        elif frequency_choice == 3:

                            correct_answer = random.randrange(0,11)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]

                        elif frequency_choice == 4:

                            correct_answer = random.randrange(0,15)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]
                            
                        block_limit_natural_p = block_limit_natural_p - 1
                        
                        break
                
                elif choice_present == 0:
                    if block_limit_natural_np == 0:
                        continue
                        
                    else:
                        
                        correct_answer_key = 'l'
                        stim_present_data[x,18] = choice_present
                        stim_present_data[x,19] = correct_answer_key
                        
                        stim_present_data[x,17] = randfchoice(x,stim_type_choice)
                        
                        block_limit_natural_np = block_limit_natural_np - 1
                        
                        break
                    
            
    

        elif stim_type_choice == 2 and block_limit_scrambled != 0: 
        # Scrambled images block 
        
        
        #Verify if images still left in block. Else refill the block
            
            if len(stim_list_scrambled_copy) <= 32:
                stim_list_scrambled_copy = copy.deepcopy(stim_list_scrambled)
                random.shuffle(stim_list_scrambled_copy)

            block_limit_scrambled = block_limit_scrambled - 1
            
            
              
            

            # Emergency break condition
            break_limit = 0 

            while break_limit == 0: 
                # Frequnecy of stimuli presentation choice . 
                frequency_choice = random.choice([1,2,3])
                if frequency_choice == 1: 
                    # Check if limit is reached
                    if block_limit_onehz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 1
                        block_limit_onehz = block_limit_onehz - 1
                        break

                elif frequency_choice == 2:
                    # Check if limit is reached
                    if block_limit_twohz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 2
                        block_limit_twohz = block_limit_twohz - 1
                        break

                elif frequency_choice == 3:
                    # Check if limit is reached
                    if block_limit_threehz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 3
                        block_limit_threehz = block_limit_threehz - 1
                        break
                elif frequency_choice == 4:
                    # Check if limit is reached
                    if block_limit_fourhz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 4
                        block_limit_fourhz = block_limit_fourhz - 1
                        break


            # Stimulus Presentation section

            # Image selection for RSVP stream
            stim_present_data[x,0] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,1] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,2] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,3] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,20] = stim_type_choice

            if frequency_choice == 2 or frequency_choice == 3 or frequency_choice == 4:
            
                stim_present_data[x,4] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,5] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,6] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,7] = randstim(x,stim_type_choice,frequency_choice)
                
                
            if frequency_choice == 3 or frequency_choice == 4:
                stim_present_data[x,8] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,9] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,10] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,11] = randstim(x,stim_type_choice,frequency_choice)
                
                
            if frequency_choice == 4:
                stim_present_data[x,12] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,13] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,14] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,15] = randstim(x,stim_type_choice,frequency_choice)
                
            
          

            # Choice section
            
            #   P vs NP trials. Aka image present or not present in stim presentation stream. 

            
            
            # Randomly pick one image from the presentation section if p trial or one not in presentation section if np trial. Alter based on frequency and number of images presented. 
            
            choice_break_limit = 0
            
            while choice_break_limit == 0:
                choice_present = random.choice([0,1])
                                
                if choice_present == 1:
                    if block_limit_scrambled_p == 0:
                        continue
                        
                    else:
                        
                        correct_answer_key = 'a'
                        stim_present_data[x,18] = choice_present
                        stim_present_data[x,19] = correct_answer_key
                        

                        if frequency_choice == 1:

                            correct_answer = random.randrange(0,3)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]

                        elif frequency_choice == 2:

                            correct_answer = random.randrange(0,7)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]

                        elif frequency_choice == 3:

                            correct_answer = random.randrange(0,11)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]

                        elif frequency_choice == 4:

                            correct_answer = random.randrange(0,15)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]
                            
                        block_limit_scrambled_p = block_limit_scrambled_p - 1
                            
                        break
                
                elif choice_present == 0:
                    if block_limit_scrambled_np == 0:
                        continue
                        
                    else:
                        
                        correct_answer_key = 'l'
                        stim_present_data[x,18] = choice_present
                        stim_present_data[x,19] = correct_answer_key
                        
                        stim_present_data[x,17] = randfchoice(x,stim_type_choice)
                        
                        block_limit_scrambled_np = block_limit_scrambled_np - 1
                        
                        break
                    

            


        elif stim_type_choice == 3 and block_limit_noise != 0:
        # Visual Noise images block
        
        #Verify if images still left in block. Else refill the block
            
            if len(stim_list_noise_copy) <= 32:
                stim_list_noise_copy = copy.deepcopy(stim_list_noise)
                random.shuffle(stim_list_noise_copy)

            block_limit_noise = block_limit_noise - 1 
            
            

            # Emergency break condition
            break_limit = 0 

            while break_limit == 0: 
                # Frequnecy of stimuli presentation choice . 
                frequency_choice = random.choice([1,2,3])
                if frequency_choice == 1: 
                    # Check if limit is reached
                    if block_limit_onehz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 1
                        block_limit_onehz = block_limit_onehz - 1
                        break

                elif frequency_choice == 2:
                    # Check if limit is reached
                    if block_limit_twohz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 2
                        block_limit_twohz = block_limit_twohz - 1
                        break

                elif frequency_choice == 3:
                    # Check if limit is reached
                    if block_limit_threehz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 3
                        block_limit_threehz = block_limit_threehz - 1
                        break
                elif frequency_choice == 4:
                    # Check if limit is reached
                    if block_limit_fourhz == 0: 
                        continue
                    else:
                        stim_present_data[x,16] = 4
                        block_limit_fourhz = block_limit_fourhz - 1
                        break


            # Stimulus Presentation section

            # Image selection for RSVP stream
            stim_present_data[x,0] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,1] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,2] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,3] = randstim(x,stim_type_choice,frequency_choice)
            stim_present_data[x,20] = stim_type_choice

            
            if frequency_choice == 2 or frequency_choice == 3 or frequency_choice == 4:
            
                stim_present_data[x,4] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,5] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,6] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,7] = randstim(x,stim_type_choice,frequency_choice)
                
                
            if frequency_choice == 3 or frequency_choice == 4:
                stim_present_data[x,8] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,9] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,10] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,11] = randstim(x,stim_type_choice,frequency_choice)
                
                
            if frequency_choice == 4:
                stim_present_data[x,12] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,13] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,14] = randstim(x,stim_type_choice,frequency_choice)
                stim_present_data[x,15] = randstim(x,stim_type_choice,frequency_choice)
            

            # Choice section
            
            #   P vs NP trials. Aka image present or not present in stim presentation stream. 

            
            
            # Randomly pick one image from the presentation section if p trial or one not in presentation section if np trial. Alter based on frequency and number of images presented. 
            
            choice_break_limit = 0
            
            while choice_break_limit == 0:
                choice_present = random.choice([0,1])
                                
                if choice_present == 1:
                    if block_limit_noise_p == 0:
                        continue
                        
                    else:
                        
                        correct_answer_key = 'a'
                        stim_present_data[x,18] = choice_present
                        stim_present_data[x,19] = correct_answer_key
                        

                        if frequency_choice == 1:

                            correct_answer = random.randrange(0,3)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]

                        elif frequency_choice == 2:

                            correct_answer = random.randrange(0,7)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]

                        elif frequency_choice == 3:

                            correct_answer = random.randrange(0,11)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]

                        elif frequency_choice == 4:

                            correct_answer = random.randrange(0,15)
                            stim_present_data[x,17] = stim_present_data[x,correct_answer]
                            
                        block_limit_noise_p = block_limit_noise_p - 1
                            
                        break
                
                elif choice_present == 0:
                    if block_limit_noise_np == 0:
                        continue
                        
                    else:
                        
                        correct_answer_key = 'l'
                        stim_present_data[x,18] = choice_present
                        stim_present_data[x,19] = correct_answer_key
                        
                        stim_present_data[x,17] = randfchoice(x,stim_type_choice)
                        
                        block_limit_noise_np = block_limit_noise_np - 1
                        
                        break

            
        else:
            continue

           
        # Setting frequency condition for parllel port out to EEG recording
        # Using a combination of stimulus type and frequency of presentation into one
        
        condition_code = '%i%i' %(stim_type_choice,frequency_choice)
        stim_present_data[x,21] = condition_code
        
        # Loop incrementor 
        x = x + 1
    
    # Checking to make sure the trial struture works
    print('one block done')
    # Saving generated stimulus files. Filesnames set according to blocknumber
    presentation_filename = 'stim_present_data_block_%s.csv' % (i+1)
    #choice_filename = 'stim_choice_data_block_%s.csv' % (i+1)
    
    
    
    
    np.savetxt(presentation_filename, stim_present_data, header = "imageone,imagetwo,imagethree,imagefour,imagefive,imagesix,imageseven,imageeight,imagenine,imageten,imageeleven,imagetwelve,imagethirteen,imagefourteen,imagefifteen,imagesixteen,frequency,choice_image,choice_type,correct_answer,stimulus_type,condition_code" ,fmt='%s', delimiter =',', comments='') 
    #np.savetxt(choice_filename, stim_choice_data, header = "imageTL,imageBL,imageTR,imageBR,correct_answer" ,fmt='%5s', delimiter =', ', comments='') 
    
    
    # Reseting the array to avoid clashes in future blocks. 
    stim_present_data.fill('')
    
    