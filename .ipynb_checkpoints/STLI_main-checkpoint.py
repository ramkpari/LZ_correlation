#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.0),
    on Thu 09 May 2019 05:21:14 PM CEST
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice
import os  # handy system and path functions
import sys  # to get file system encoding
import matplotlib.image as mpimg
from psychopy.hardware import keyboard
from random import sample
from psychopy.hardware import keyboard
import csv,shutil
import pandas as pd
import datetime
import cv2 #you may need: pip install opencv-python
from scipy.misc import imread
from datetime import datetime
#from multiprocessing import Pool


#Neccersary bits to setup parallel port
from ctypes import windll
pport=windll.inpoutx64
pport_address=0xD010
 
#Function to send EEG triggers to parallel port

def sendParallelTrigger(pport_address,triggerCode):
  try:
      pport.Out32(pport_address,triggerCode)  #set the pins to the correspondent input (triggerCode)
      print (pport.Inp32(pport_address))
      core.wait(0.05)
      pport.Out32(pport_address,0)   #reset all the pins to 0
  except:
      print ("Error")
      
#Window Parameters
winsize=(800,600) # window size
winunits='pix' #window units (e.g pix, cm)
FullScreen_opt= True  #FullScreen option (set it to "True" or "False")
wincol=(0,0,0) #window color

#Message Parameters
msgpos=(0,0) # messages position
msgheight=30 #messages height



def runTrials():
 
 '''
 This script assumes there are is a folder called 'images' with all images and a folder 'shuffled' 
 but having the same file names 
 
 Script must be run from th folder where the script is located!
 '''
 
 trial_duration=4 #how long is one trial in sec
 reps=54 #how often each condition'shuffle pair is shown. It's always the same order.
  
 ##############################################
 ##############################################

 conditions=[]  
 for i in [2,4,6]:#this is frame_rates in Hz
  for j in [False,True]:
   conditions.append([i,j])
 nReps=len(conditions)*reps #how many trials like this; must be multiple of 6 as each of the 3 frame rates is followed by a shuffled version


# Ensure that relative paths start from the same directory as this script
 #_thisDir = os.path.dirname(os.path.abspath(__file__))
 _thisDir = 'C:/Users/Sackler6/Documents/Nick/'
 os.chdir(_thisDir)

 # Store info about the experiment session
 psychopyVersion = '3.1.0'
 expName = 'oneImage'  # from the Builder filename that created this script
 expInfo = {'participant': '', 'session': '06'}
 dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
 if dlg.OK == False:
     core.quit()  # user pressed cancel
 expInfo['date'] = data.getDateStr()  # add a simple timestamp
 expInfo['expName'] = expName
 expInfo['psychopyVersion'] = psychopyVersion
 

 # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
 filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
 
 # An ExperimentHandler isn't essential but helps with data saving
 thisExp = data.ExperimentHandler(name=expName, version='',
     extraInfo=expInfo, runtimeInfo=None,
     originPath='untitled.py',
     savePickle=True, saveWideText=True,
     dataFileName=filename)

 endExpNow = False  # flag for 'escape' or other condition => quit the exp


#Welcome Message
 instr='''
In this experiment we are interested in the speed at which you can process visual information.\n
We will present you with a stream of either real or scambled images.\n
Your task is to maintain fixation on a red  square, while paying attention to the periphery of your vision. \n
During the stream of images we will present a red square in a random corner of one of the images\n
At the end of each trial you will be asked which corner the image was presented in.\n

*** Please place your chin on the chinrest, relax till the count of 5 the press any key***\n

***The experiment will begin as soon as you press any key***\n
'''

#Create the main Window 
 win = visual.Window([1000,1000],monitor="testMonitor",  units="height", fullscr=FullScreen_opt)

#Print the instruction message

 instructions = visual.TextStim(win, 
                                text=instr,
                                units='pix', 
                                color='white',
                                font='Arial', 
                                height=22, 
                                pos=(0,0))
 instructions.autoDraw = True  # Automatically draw every frame
 win.flip()
 event.waitKeys() #wait for any key to be pressed to continue the experiment
 instructions.autoDraw = False  # Turn off instructions
 win.flip()
 core.wait(1.0)

 ##############################################
 ##############################################

  
 #create a constant little square box as a fixation point
 fixation = visual.GratingStim(win=win, size=0.01, pos=[0,0], sf=0, color='red')

 #create rating for square location: it must be in one corner
 rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.5, pos=[0.0, -0.4], low=1,textSize=0.4, high=4,tickMarks=range(1,5), labels=['Top left','Top right','Bottom right','Bottom left'], scale='In which corner was the red square?')

 # Create some handy timers
 globalClock = core.Clock()  # to track the time since experiment started
 routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

 # set up handler to look after randomisation of conditions etc
 trials_3 = data.TrialHandler(nReps=nReps, method='random', 
     extraInfo=expInfo, originPath=-1,
     trialList=[None],
     seed=None, name='trials_3')
 thisExp.addLoop(trials_3)  # add the loop to the experiment
 thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
 # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
 if thisTrial_3 != None:
     for paramName in thisTrial_3:
         exec('{} = thisTrial_3[paramName]'.format(paramName))

 t_rial=0

 for thisTrial_3 in trials_3:
   
     frame_rate,shuffle_trial=conditions[t_rial%6]

     n_images=trial_duration*frame_rate
     duration_of_each_image=float(frame_rate)**-1 
  
     currentLoop = trials_3
     # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
     if thisTrial_3 != None:
         for paramName in thisTrial_3:
             exec('{} = thisTrial_3[paramName]'.format(paramName))

     # ------Prepare to start Routine "trial"-------

     #Red square to be detected: pick random frame, random corner  

     locs=[[-0.2,0.2],[0.2,0.2],[0.2,-0.2],[-0.2,-0.2]]
     chosen_index_for_location=choice(range(4),1)[0]
     chosen_loc=locs[chosen_index_for_location]
     chosen_image=choice(range(n_images),1)
     
     red_square = visual.GratingStim(win=win, size=0.01, pos=chosen_loc, sf=0, color='red')


     path_to_images='C:/Users/Sackler6/Documents/Nick/images/' 
     path_to_shuffled_images='/'.join(path_to_images.split('/')[:-2])+'/shuffled/'


     if shuffle_trial: #load image paths used for previous block

      path_to_exp_data=os.path.dirname(filename)

      img_paths=np.load(path_to_exp_data+'/images.npy')     

      im_50=[]

      for img_path in img_paths: #save corresponding shuffled image paths
 
       im_50.append(path_to_shuffled_images+'/%s' %((img_path.split('/'))[-1]))

     else:

      #we want to show random images in sequence, always other images; this is achieved by sampling from that massive mini-imagenet, a folder with many low-res images
      
      f=os.listdir(path_to_images)
      f_50=sample(f,n_images)

      im_50=[path_to_images+'/'+i for i in f_50]

     images=[]
     image_names=[]
     image_paths=[]

     # Initialize components for Routine "trial"
     trialClock = core.Clock()

     for i in range(n_images):

         img=im_50[i]
         image_paths.append(img)
         images.append(visual.ImageStim(
         win=win,
         name='image'+str(i), 
         image=img, mask=None,
         ori=0, pos=(0, 0), size=(0.5, 0.5),
         color=[1,1,1], colorSpace='rgb', opacity=1,
         flipHoriz=False, flipVert=False,
         texRes=128, interpolate=True, depth=1.0))
         win.flip()
         image_names.append('image'+str(i))

     np.save('C:/Users/Sackler6/Documents/Nick/data/images.npy',image_paths)
 
     t_rial+=1

     t = 0
     trialClock.reset()  # clock
     frameN = -1

     continueRoutine = True
     #routineTimer.add(n_images*duration_of_each_image)
     # update component parameters for each repeat
     # keep track of which components have finished
     trialComponents = [x for x in images]
     trialComponents.append(rating)
     for thisComponent in trialComponents:
         thisComponent.tStart = None
         thisComponent.tStop = None
         thisComponent.tStartRefresh = None
         thisComponent.tStopRefresh = None
         if hasattr(thisComponent, 'status'):
             thisComponent.status = NOT_STARTED

     rating.reset()
     

      ######################################################################################################
      ######################################################################################################
      #Send a an EEG marker here based on framerate i.e. 2,4,6
     if shuffle_trial:
                        
       triggerCode=frame_rate + 10
     else:
       triggerCode=frame_rate
       
     sendParallelTrigger(pport_address,triggerCode) 

     
     # -------Start Routine "trial"-------
     while continueRoutine:# and routineTimer.getTime() > 0:
         # get current time
         t = trialClock.getTime()
         frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
         # update/draw components on each frame
         fixation.setAutoDraw(True) 
         fixation.setDepth(0.0)

         k=0 #image counter
         k_max=len(images)


         for image in images:
          # *image* updates
          images_start=t
          
           
          
          
          
          if t >= duration_of_each_image*k and image.status == NOT_STARTED:
              # keep track of start time/frame for later
                      
              image.tStart = t  # not accounting for scr refresh
 


              image.frameNStart = frameN  # exact frame index
              win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
              image.setAutoDraw(True)
          
              if k==chosen_image:
               red_square.setAutoDraw(True) 
               red_square.setDepth(0.0)          
              
          frameRemains = duration_of_each_image*k + duration_of_each_image - win.monitorFramePeriod * 0.75  # most of one frame period left
          if image.status == STARTED and t >= frameRemains:
                    
              # keep track of stop time/frame for later
              image.tStop = t  # not accounting for scr refresh
              image.frameNStop = frameN  # exact frame index
              win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
              image.setAutoDraw(False)

              if k==chosen_image:
               red_square.setAutoDraw(False)            

          k+=1     
       
         if t>trial_duration and rating.status == NOT_STARTED:
             # keep track of start time/frame for later
             rating.tStart = t  # not accounting for scr refresh

             
            ######################################################################################################
            ######################################################################################################
            #Send a an EEG marker here based on framerate + 100
             if shuffle_trial:
              triggerCode=frame_rate+10 +100
             else:
              triggerCode=frame_rate +100

             sendParallelTrigger(pport_address,triggerCode)

             rating.frameNStart = frameN  # exact frame index
             win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
             rating.setAutoDraw(True)
             continueRoutine &= rating.noResponse

         # check for quit (typically the Esc key)
         if endExpNow or keyboard.Keyboard().getKeys(keyList=["escape"]):
             core.quit()
             visual.Window.close()
         
         # check if all components have finished
         if not continueRoutine:  # a component has requested a forced-end of Routine
             break
         continueRoutine = False  # will revert to True if at least one component still running
         for thisComponent in trialComponents:
             if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                 continueRoutine = True
                 break  # at least one component has not yet finished
         
         # refresh the screen
         if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
             win.flip()

         if len(event.getKeys())>0:
             break


     # -------Ending Routine "trial"-------
     for thisComponent in trialComponents:
         if hasattr(thisComponent, "setAutoDraw"):
             thisComponent.setAutoDraw(False)

     trials_3.addData('square_correct',(rating.getRating()-1)==chosen_index_for_location)
     trials_3.addData('frame_rate',frame_rate)
     trials_3.addData('shuffle_trial',shuffle_trial)
     trials_3.addData('trial_duration',trial_duration)
     trials_3.addData('images_start',images_start)
     trials_3.addData('images_start_CPU',str(datetime.now()))                
     trials_3.addData('rating.tStart',rating.tStart)
     trials_3.addData('rating.tStart_CPU',str(datetime.now()))
     thisExp.nextEntry() 

 os.remove('C:/Users/Sackler6/Documents/Nick/data/images.npy')
 # Flip one final time so any remaining win.callOnFlip() 
 # and win.timeOnFlip() tasks get executed before quitting
 win.flip()
 thisExp.saveAsWideText(filename+'.csv')
# logging.flush()

 # make sure everything is closed down
 thisExp.abort()  # or data files will save again on exit
 win.close()
 core.quit()


#############################
#############################
'''
after you shuffled all images,
by running shuffle_all(),
COMMENT OUT INDICATED SECTION
'''
#############################
#############################

#COMMENT THIS OUT FROM HERE

#path_to_images='C:/Users/Sackler6/Documents/images/' #SET THIS TO YOUR PATH
#
#nCPU=multiprocessing.cpu_count()
#path_to_shuffled_images='/'.join(path_to_images.split('/')[:-2])+'/shuffled/'
#if path_to_images[-1]!='/':
# print('path must end with /')
#
#if not os.path.exists(path_to_shuffled_images):
#   os.makedirs(path_to_shuffled_images)
#
#f=os.listdir(path_to_images)
#full_paths=[path_to_images+x for x in f]

#UNTIL HERE

#############################
#############################


#def shuffle_all():
#
# startTime = datetime.now()
# with Pool(processes=nCPU) as pool:
#     result = pool.map(shuffle_save, range(len(full_paths)))
# print(datetime.now()-startTime)
#
#def shuffle_save(img_idx):
# img_path=full_paths[img_idx] 
# try:
#  shuff_img=shuffle_image(img_path)   
#  print('shuffled image %s' %img_path)
# except:
#  print("didn't work %s" %img_path)
#  return  
# mpimg.imsave(path_to_shuffled_images+'%s' %(img_path.split('/')[-1]),shuff_img) 
#
#
#def shuffle_image(image_path):
#  '''
#  That's a helper function for the shuffle control.
#
#  input: path of image
#  output: array of image with shuffled pixels
#
#  For the control condition, there are the npy files saved in Data folder to keep track with images were used.
#  You can load them, shuffle them, save in folder and use for control run (not implemented, but shuffle function is here).
#
#  '''
#  
#  rgbImg_orig=mpimg.imread(image_path)
#  rgbImg=rgbImg_orig.copy()
#  if len(rgbImg.shape)<3: #check if image is greyscale, if so, convert to RGB
#   rgbImg = cv2.cvtColor(rgbImg,cv2.COLOR_GRAY2RGB)
#  rndImg2= np.reshape(rgbImg, (rgbImg.shape[0] * rgbImg.shape[1], rgbImg.shape[2]))
#  np.random.shuffle(rndImg2)
#  img = np.reshape(rndImg2, rgbImg.shape)
#  return img








