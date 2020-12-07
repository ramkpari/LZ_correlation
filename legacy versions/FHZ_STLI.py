#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Edited outside the builder. 

This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on November 23, 2020, at 18:27
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'new_STLI'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
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
    originPath='C:\\Users\\Ram\\OneDrive - University of Sussex\\Desktop\\LZ correlation\\LZ_correlation\\new_STLI.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "rsvp"
rsvpClock = core.Clock()
Cross = visual.ShapeStim(
    win=win, name='Cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Presentation_image_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
Fixation_cross = visual.ShapeStim(
    win=win, name='Fixation_cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Topleft = visual.ImageStim(
    win=win,
    name='Topleft', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Topright = visual.ImageStim(
    win=win,
    name='Topright', 
    image='sin', mask=None,
    ori=0, pos=(0.25 , 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Bottomleft = visual.ImageStim(
    win=win,
    name='Bottomleft', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Bottomright = visual.ImageStim(
    win=win,
    name='Bottomright', 
    image='sin', mask=None,
    ori=0, pos=(0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Break"
BreakClock = core.Clock()
text_break = visual.TextStim(win=win, name='text_break',
    text='Time for a break \n\nPress either of the keys "v" , "b" or "n" to continue when ready',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "rsvp"
rsvpClock = core.Clock()
Cross = visual.ShapeStim(
    win=win, name='Cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Presentation_image_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
Fixation_cross = visual.ShapeStim(
    win=win, name='Fixation_cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Topleft = visual.ImageStim(
    win=win,
    name='Topleft', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Topright = visual.ImageStim(
    win=win,
    name='Topright', 
    image='sin', mask=None,
    ori=0, pos=(0.25 , 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Bottomleft = visual.ImageStim(
    win=win,
    name='Bottomleft', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Bottomright = visual.ImageStim(
    win=win,
    name='Bottomright', 
    image='sin', mask=None,
    ori=0, pos=(0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Break"
BreakClock = core.Clock()
text_break = visual.TextStim(win=win, name='text_break',
    text='Time for a break \n\nPress either of the keys "v" , "b" or "n" to continue when ready',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "rsvp"
rsvpClock = core.Clock()
Cross = visual.ShapeStim(
    win=win, name='Cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Presentation_image_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
Fixation_cross = visual.ShapeStim(
    win=win, name='Fixation_cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Topleft = visual.ImageStim(
    win=win,
    name='Topleft', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Topright = visual.ImageStim(
    win=win,
    name='Topright', 
    image='sin', mask=None,
    ori=0, pos=(0.25 , 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Bottomleft = visual.ImageStim(
    win=win,
    name='Bottomleft', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Bottomright = visual.ImageStim(
    win=win,
    name='Bottomright', 
    image='sin', mask=None,
    ori=0, pos=(0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Break"
BreakClock = core.Clock()
text_break = visual.TextStim(win=win, name='text_break',
    text='Time for a break \n\nPress either of the keys "v" , "b" or "n" to continue when ready',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "rsvp"
rsvpClock = core.Clock()
Cross = visual.ShapeStim(
    win=win, name='Cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Presentation_image_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
Fixation_cross = visual.ShapeStim(
    win=win, name='Fixation_cross', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Topleft = visual.ImageStim(
    win=win,
    name='Topleft', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Topright = visual.ImageStim(
    win=win,
    name='Topright', 
    image='sin', mask=None,
    ori=0, pos=(0.25 , 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Bottomleft = visual.ImageStim(
    win=win,
    name='Bottomleft', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Bottomright = visual.ImageStim(
    win=win,
    name='Bottomright', 
    image='sin', mask=None,
    ori=0, pos=(0.25, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='End\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
WelcomeComponents = [text]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
block_one = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stim_present_data_block_1.csv'),
    seed=None, name='block_one')
thisExp.addLoop(block_one)  # add the loop to the experiment
thisBlock_one = block_one.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_one.rgb)
if thisBlock_one != None:
    for paramName in thisBlock_one:
        exec('{} = thisBlock_one[paramName]'.format(paramName))

for thisBlock_one in block_one:
    currentLoop = block_one
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_one.rgb)
    if thisBlock_one != None:
        for paramName in thisBlock_one:
            exec('{} = thisBlock_one[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rsvp"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Presentation_image_1.setImage(imageone)
    Presentation_image_2.setImage(imagetwo)
    Presentation_image_3.setImage(imagethree)
    Presentation_image_4.setImage(imagefour)
    # keep track of which components have finished
    rsvpComponents = [Cross, Presentation_image_1, Presentation_image_2, Presentation_image_3, Presentation_image_4]
    for thisComponent in rsvpComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rsvpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rsvp"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rsvpClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rsvpClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Cross* updates
        if Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cross.frameNStart = frameN  # exact frame index
            Cross.tStart = t  # local t and not account for scr refresh
            Cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
            Cross.setAutoDraw(True)
        if Cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Cross.tStop = t  # not accounting for scr refresh
                Cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cross, 'tStopRefresh')  # time at next scr refresh
                Cross.setAutoDraw(False)
        
        # *Presentation_image_1* updates
        if Presentation_image_1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_1.frameNStart = frameN  # exact frame index
            Presentation_image_1.tStart = t  # local t and not account for scr refresh
            Presentation_image_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_1, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_1.setAutoDraw(True)
        if Presentation_image_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_1.tStop = t  # not accounting for scr refresh
                Presentation_image_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_1, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_1.setAutoDraw(False)
        
        # *Presentation_image_2* updates
        if Presentation_image_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_2.frameNStart = frameN  # exact frame index
            Presentation_image_2.tStart = t  # local t and not account for scr refresh
            Presentation_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_2, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_2.setAutoDraw(True)
        if Presentation_image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_2.tStop = t  # not accounting for scr refresh
                Presentation_image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_2, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_2.setAutoDraw(False)
        
        # *Presentation_image_3* updates
        if Presentation_image_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_3.frameNStart = frameN  # exact frame index
            Presentation_image_3.tStart = t  # local t and not account for scr refresh
            Presentation_image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_3, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_3.setAutoDraw(True)
        if Presentation_image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_3.tStop = t  # not accounting for scr refresh
                Presentation_image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_3, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_3.setAutoDraw(False)
        
        # *Presentation_image_4* updates
        if Presentation_image_4.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_4.frameNStart = frameN  # exact frame index
            Presentation_image_4.tStart = t  # local t and not account for scr refresh
            Presentation_image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_4, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_4.setAutoDraw(True)
        if Presentation_image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_4.tStop = t  # not accounting for scr refresh
                Presentation_image_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_4, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rsvpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rsvp"-------
    for thisComponent in rsvpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_one.addData('Cross.started', Cross.tStartRefresh)
    block_one.addData('Cross.stopped', Cross.tStopRefresh)
    block_one.addData('Presentation_image_1.started', Presentation_image_1.tStartRefresh)
    block_one.addData('Presentation_image_1.stopped', Presentation_image_1.tStopRefresh)
    block_one.addData('Presentation_image_2.started', Presentation_image_2.tStartRefresh)
    block_one.addData('Presentation_image_2.stopped', Presentation_image_2.tStopRefresh)
    block_one.addData('Presentation_image_3.started', Presentation_image_3.tStartRefresh)
    block_one.addData('Presentation_image_3.stopped', Presentation_image_3.tStopRefresh)
    block_one.addData('Presentation_image_4.started', Presentation_image_4.tStartRefresh)
    block_one.addData('Presentation_image_4.stopped', Presentation_image_4.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    Topleft.setImage(imageTL)
    Topright.setImage(imageTR)
    Bottomleft.setImage(imageBL)
    Bottomright.setImage(imageBR)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [Fixation_cross, Topleft, Topright, Bottomleft, Bottomright, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_cross* updates
        if Fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_cross.frameNStart = frameN  # exact frame index
            Fixation_cross.tStart = t  # local t and not account for scr refresh
            Fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_cross, 'tStartRefresh')  # time at next scr refresh
            Fixation_cross.setAutoDraw(True)
        if Fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_cross.tStop = t  # not accounting for scr refresh
                Fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_cross, 'tStopRefresh')  # time at next scr refresh
                Fixation_cross.setAutoDraw(False)
        
        # *Topleft* updates
        if Topleft.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Topleft.frameNStart = frameN  # exact frame index
            Topleft.tStart = t  # local t and not account for scr refresh
            Topleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Topleft, 'tStartRefresh')  # time at next scr refresh
            Topleft.setAutoDraw(True)
        if Topleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Topleft.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Topleft.tStop = t  # not accounting for scr refresh
                Topleft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Topleft, 'tStopRefresh')  # time at next scr refresh
                Topleft.setAutoDraw(False)
        
        # *Topright* updates
        if Topright.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Topright.frameNStart = frameN  # exact frame index
            Topright.tStart = t  # local t and not account for scr refresh
            Topright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Topright, 'tStartRefresh')  # time at next scr refresh
            Topright.setAutoDraw(True)
        if Topright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Topright.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Topright.tStop = t  # not accounting for scr refresh
                Topright.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Topright, 'tStopRefresh')  # time at next scr refresh
                Topright.setAutoDraw(False)
        
        # *Bottomleft* updates
        if Bottomleft.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Bottomleft.frameNStart = frameN  # exact frame index
            Bottomleft.tStart = t  # local t and not account for scr refresh
            Bottomleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bottomleft, 'tStartRefresh')  # time at next scr refresh
            Bottomleft.setAutoDraw(True)
        if Bottomleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bottomleft.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Bottomleft.tStop = t  # not accounting for scr refresh
                Bottomleft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Bottomleft, 'tStopRefresh')  # time at next scr refresh
                Bottomleft.setAutoDraw(False)
        
        # *Bottomright* updates
        if Bottomright.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Bottomright.frameNStart = frameN  # exact frame index
            Bottomright.tStart = t  # local t and not account for scr refresh
            Bottomright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bottomright, 'tStartRefresh')  # time at next scr refresh
            Bottomright.setAutoDraw(True)
        if Bottomright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bottomright.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Bottomright.tStop = t  # not accounting for scr refresh
                Bottomright.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Bottomright, 'tStopRefresh')  # time at next scr refresh
                Bottomright.setAutoDraw(False)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['a', 'z', 'k', 'm'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # was this correct?
                if (key_resp.keys == str(correct_answer)) or (key_resp.keys == correct_answer):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_one.addData('Fixation_cross.started', Fixation_cross.tStartRefresh)
    block_one.addData('Fixation_cross.stopped', Fixation_cross.tStopRefresh)
    block_one.addData('Topleft.started', Topleft.tStartRefresh)
    block_one.addData('Topleft.stopped', Topleft.tStopRefresh)
    block_one.addData('Topright.started', Topright.tStartRefresh)
    block_one.addData('Topright.stopped', Topright.tStopRefresh)
    block_one.addData('Bottomleft.started', Bottomleft.tStartRefresh)
    block_one.addData('Bottomleft.stopped', Bottomleft.tStopRefresh)
    block_one.addData('Bottomright.started', Bottomright.tStartRefresh)
    block_one.addData('Bottomright.stopped', Bottomright.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(correct_answer).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block_one (TrialHandler)
    block_one.addData('key_resp.keys',key_resp.keys)
    block_one.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        block_one.addData('key_resp.rt', key_resp.rt)
    block_one.addData('key_resp.started', key_resp.tStart)
    block_one.addData('key_resp.stopped', key_resp.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_one'


# ------Prepare to start Routine "Break"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
BreakComponents = [text_break, key_resp_2]
for thisComponent in BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Break"-------
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_break* updates
    if text_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_break.frameNStart = frameN  # exact frame index
        text_break.tStart = t  # local t and not account for scr refresh
        text_break.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_break, 'tStartRefresh')  # time at next scr refresh
        text_break.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['v', 'n', 'b'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_break.started', text_break.tStartRefresh)
thisExp.addData('text_break.stopped', text_break.tStopRefresh)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block_two = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stim_present_data_block_2.csv'),
    seed=None, name='block_two')
thisExp.addLoop(block_two)  # add the loop to the experiment
thisBlock_two = block_two.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_two.rgb)
if thisBlock_two != None:
    for paramName in thisBlock_two:
        exec('{} = thisBlock_two[paramName]'.format(paramName))

for thisBlock_two in block_two:
    currentLoop = block_two
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_two.rgb)
    if thisBlock_two != None:
        for paramName in thisBlock_two:
            exec('{} = thisBlock_two[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rsvp"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Presentation_image_1.setImage(imageone)
    Presentation_image_2.setImage(imagetwo)
    Presentation_image_3.setImage(imagethree)
    Presentation_image_4.setImage(imagefour)
    # keep track of which components have finished
    rsvpComponents = [Cross, Presentation_image_1, Presentation_image_2, Presentation_image_3, Presentation_image_4]
    for thisComponent in rsvpComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rsvpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rsvp"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rsvpClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rsvpClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Cross* updates
        if Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cross.frameNStart = frameN  # exact frame index
            Cross.tStart = t  # local t and not account for scr refresh
            Cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
            Cross.setAutoDraw(True)
        if Cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Cross.tStop = t  # not accounting for scr refresh
                Cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cross, 'tStopRefresh')  # time at next scr refresh
                Cross.setAutoDraw(False)
        
        # *Presentation_image_1* updates
        if Presentation_image_1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_1.frameNStart = frameN  # exact frame index
            Presentation_image_1.tStart = t  # local t and not account for scr refresh
            Presentation_image_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_1, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_1.setAutoDraw(True)
        if Presentation_image_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_1.tStop = t  # not accounting for scr refresh
                Presentation_image_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_1, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_1.setAutoDraw(False)
        
        # *Presentation_image_2* updates
        if Presentation_image_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_2.frameNStart = frameN  # exact frame index
            Presentation_image_2.tStart = t  # local t and not account for scr refresh
            Presentation_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_2, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_2.setAutoDraw(True)
        if Presentation_image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_2.tStop = t  # not accounting for scr refresh
                Presentation_image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_2, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_2.setAutoDraw(False)
        
        # *Presentation_image_3* updates
        if Presentation_image_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_3.frameNStart = frameN  # exact frame index
            Presentation_image_3.tStart = t  # local t and not account for scr refresh
            Presentation_image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_3, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_3.setAutoDraw(True)
        if Presentation_image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_3.tStop = t  # not accounting for scr refresh
                Presentation_image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_3, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_3.setAutoDraw(False)
        
        # *Presentation_image_4* updates
        if Presentation_image_4.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_4.frameNStart = frameN  # exact frame index
            Presentation_image_4.tStart = t  # local t and not account for scr refresh
            Presentation_image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_4, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_4.setAutoDraw(True)
        if Presentation_image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_4.tStop = t  # not accounting for scr refresh
                Presentation_image_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_4, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rsvpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rsvp"-------
    for thisComponent in rsvpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_two.addData('Cross.started', Cross.tStartRefresh)
    block_two.addData('Cross.stopped', Cross.tStopRefresh)
    block_two.addData('Presentation_image_1.started', Presentation_image_1.tStartRefresh)
    block_two.addData('Presentation_image_1.stopped', Presentation_image_1.tStopRefresh)
    block_two.addData('Presentation_image_2.started', Presentation_image_2.tStartRefresh)
    block_two.addData('Presentation_image_2.stopped', Presentation_image_2.tStopRefresh)
    block_two.addData('Presentation_image_3.started', Presentation_image_3.tStartRefresh)
    block_two.addData('Presentation_image_3.stopped', Presentation_image_3.tStopRefresh)
    block_two.addData('Presentation_image_4.started', Presentation_image_4.tStartRefresh)
    block_two.addData('Presentation_image_4.stopped', Presentation_image_4.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    Topleft.setImage(imageTL)
    Topright.setImage(imageTR)
    Bottomleft.setImage(imageBL)
    Bottomright.setImage(imageBR)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [Fixation_cross, Topleft, Topright, Bottomleft, Bottomright, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_cross* updates
        if Fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_cross.frameNStart = frameN  # exact frame index
            Fixation_cross.tStart = t  # local t and not account for scr refresh
            Fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_cross, 'tStartRefresh')  # time at next scr refresh
            Fixation_cross.setAutoDraw(True)
        if Fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_cross.tStop = t  # not accounting for scr refresh
                Fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_cross, 'tStopRefresh')  # time at next scr refresh
                Fixation_cross.setAutoDraw(False)
        
        # *Topleft* updates
        if Topleft.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Topleft.frameNStart = frameN  # exact frame index
            Topleft.tStart = t  # local t and not account for scr refresh
            Topleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Topleft, 'tStartRefresh')  # time at next scr refresh
            Topleft.setAutoDraw(True)
        if Topleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Topleft.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Topleft.tStop = t  # not accounting for scr refresh
                Topleft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Topleft, 'tStopRefresh')  # time at next scr refresh
                Topleft.setAutoDraw(False)
        
        # *Topright* updates
        if Topright.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Topright.frameNStart = frameN  # exact frame index
            Topright.tStart = t  # local t and not account for scr refresh
            Topright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Topright, 'tStartRefresh')  # time at next scr refresh
            Topright.setAutoDraw(True)
        if Topright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Topright.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Topright.tStop = t  # not accounting for scr refresh
                Topright.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Topright, 'tStopRefresh')  # time at next scr refresh
                Topright.setAutoDraw(False)
        
        # *Bottomleft* updates
        if Bottomleft.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Bottomleft.frameNStart = frameN  # exact frame index
            Bottomleft.tStart = t  # local t and not account for scr refresh
            Bottomleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bottomleft, 'tStartRefresh')  # time at next scr refresh
            Bottomleft.setAutoDraw(True)
        if Bottomleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bottomleft.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Bottomleft.tStop = t  # not accounting for scr refresh
                Bottomleft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Bottomleft, 'tStopRefresh')  # time at next scr refresh
                Bottomleft.setAutoDraw(False)
        
        # *Bottomright* updates
        if Bottomright.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Bottomright.frameNStart = frameN  # exact frame index
            Bottomright.tStart = t  # local t and not account for scr refresh
            Bottomright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bottomright, 'tStartRefresh')  # time at next scr refresh
            Bottomright.setAutoDraw(True)
        if Bottomright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bottomright.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Bottomright.tStop = t  # not accounting for scr refresh
                Bottomright.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Bottomright, 'tStopRefresh')  # time at next scr refresh
                Bottomright.setAutoDraw(False)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['a', 'z', 'k', 'm'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # was this correct?
                if (key_resp.keys == str(correct_answer)) or (key_resp.keys == correct_answer):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_two.addData('Fixation_cross.started', Fixation_cross.tStartRefresh)
    block_two.addData('Fixation_cross.stopped', Fixation_cross.tStopRefresh)
    block_two.addData('Topleft.started', Topleft.tStartRefresh)
    block_two.addData('Topleft.stopped', Topleft.tStopRefresh)
    block_two.addData('Topright.started', Topright.tStartRefresh)
    block_two.addData('Topright.stopped', Topright.tStopRefresh)
    block_two.addData('Bottomleft.started', Bottomleft.tStartRefresh)
    block_two.addData('Bottomleft.stopped', Bottomleft.tStopRefresh)
    block_two.addData('Bottomright.started', Bottomright.tStartRefresh)
    block_two.addData('Bottomright.stopped', Bottomright.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(correct_answer).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block_two (TrialHandler)
    block_two.addData('key_resp.keys',key_resp.keys)
    block_two.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        block_two.addData('key_resp.rt', key_resp.rt)
    block_two.addData('key_resp.started', key_resp.tStart)
    block_two.addData('key_resp.stopped', key_resp.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_two'


# ------Prepare to start Routine "Break"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
BreakComponents = [text_break, key_resp_2]
for thisComponent in BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Break"-------
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_break* updates
    if text_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_break.frameNStart = frameN  # exact frame index
        text_break.tStart = t  # local t and not account for scr refresh
        text_break.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_break, 'tStartRefresh')  # time at next scr refresh
        text_break.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['v', 'n', 'b'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_break.started', text_break.tStartRefresh)
thisExp.addData('text_break.stopped', text_break.tStopRefresh)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block_three = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stim_present_data_block_3.csv'),
    seed=None, name='block_three')
thisExp.addLoop(block_three)  # add the loop to the experiment
thisBlock_three = block_three.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_three.rgb)
if thisBlock_three != None:
    for paramName in thisBlock_three:
        exec('{} = thisBlock_three[paramName]'.format(paramName))

for thisBlock_three in block_three:
    currentLoop = block_three
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_three.rgb)
    if thisBlock_three != None:
        for paramName in thisBlock_three:
            exec('{} = thisBlock_three[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rsvp"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Presentation_image_1.setImage(imageone)
    Presentation_image_2.setImage(imagetwo)
    Presentation_image_3.setImage(imagethree)
    Presentation_image_4.setImage(imagefour)
    # keep track of which components have finished
    rsvpComponents = [Cross, Presentation_image_1, Presentation_image_2, Presentation_image_3, Presentation_image_4]
    for thisComponent in rsvpComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rsvpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rsvp"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rsvpClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rsvpClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Cross* updates
        if Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cross.frameNStart = frameN  # exact frame index
            Cross.tStart = t  # local t and not account for scr refresh
            Cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
            Cross.setAutoDraw(True)
        if Cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Cross.tStop = t  # not accounting for scr refresh
                Cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cross, 'tStopRefresh')  # time at next scr refresh
                Cross.setAutoDraw(False)
        
        # *Presentation_image_1* updates
        if Presentation_image_1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_1.frameNStart = frameN  # exact frame index
            Presentation_image_1.tStart = t  # local t and not account for scr refresh
            Presentation_image_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_1, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_1.setAutoDraw(True)
        if Presentation_image_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_1.tStop = t  # not accounting for scr refresh
                Presentation_image_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_1, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_1.setAutoDraw(False)
        
        # *Presentation_image_2* updates
        if Presentation_image_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_2.frameNStart = frameN  # exact frame index
            Presentation_image_2.tStart = t  # local t and not account for scr refresh
            Presentation_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_2, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_2.setAutoDraw(True)
        if Presentation_image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_2.tStop = t  # not accounting for scr refresh
                Presentation_image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_2, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_2.setAutoDraw(False)
        
        # *Presentation_image_3* updates
        if Presentation_image_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_3.frameNStart = frameN  # exact frame index
            Presentation_image_3.tStart = t  # local t and not account for scr refresh
            Presentation_image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_3, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_3.setAutoDraw(True)
        if Presentation_image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_3.tStop = t  # not accounting for scr refresh
                Presentation_image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_3, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_3.setAutoDraw(False)
        
        # *Presentation_image_4* updates
        if Presentation_image_4.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_4.frameNStart = frameN  # exact frame index
            Presentation_image_4.tStart = t  # local t and not account for scr refresh
            Presentation_image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_4, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_4.setAutoDraw(True)
        if Presentation_image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_4.tStop = t  # not accounting for scr refresh
                Presentation_image_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_4, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rsvpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rsvp"-------
    for thisComponent in rsvpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_three.addData('Cross.started', Cross.tStartRefresh)
    block_three.addData('Cross.stopped', Cross.tStopRefresh)
    block_three.addData('Presentation_image_1.started', Presentation_image_1.tStartRefresh)
    block_three.addData('Presentation_image_1.stopped', Presentation_image_1.tStopRefresh)
    block_three.addData('Presentation_image_2.started', Presentation_image_2.tStartRefresh)
    block_three.addData('Presentation_image_2.stopped', Presentation_image_2.tStopRefresh)
    block_three.addData('Presentation_image_3.started', Presentation_image_3.tStartRefresh)
    block_three.addData('Presentation_image_3.stopped', Presentation_image_3.tStopRefresh)
    block_three.addData('Presentation_image_4.started', Presentation_image_4.tStartRefresh)
    block_three.addData('Presentation_image_4.stopped', Presentation_image_4.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    Topleft.setImage(imageTL)
    Topright.setImage(imageTR)
    Bottomleft.setImage(imageBL)
    Bottomright.setImage(imageBR)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [Fixation_cross, Topleft, Topright, Bottomleft, Bottomright, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_cross* updates
        if Fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_cross.frameNStart = frameN  # exact frame index
            Fixation_cross.tStart = t  # local t and not account for scr refresh
            Fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_cross, 'tStartRefresh')  # time at next scr refresh
            Fixation_cross.setAutoDraw(True)
        if Fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_cross.tStop = t  # not accounting for scr refresh
                Fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_cross, 'tStopRefresh')  # time at next scr refresh
                Fixation_cross.setAutoDraw(False)
        
        # *Topleft* updates
        if Topleft.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Topleft.frameNStart = frameN  # exact frame index
            Topleft.tStart = t  # local t and not account for scr refresh
            Topleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Topleft, 'tStartRefresh')  # time at next scr refresh
            Topleft.setAutoDraw(True)
        if Topleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Topleft.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Topleft.tStop = t  # not accounting for scr refresh
                Topleft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Topleft, 'tStopRefresh')  # time at next scr refresh
                Topleft.setAutoDraw(False)
        
        # *Topright* updates
        if Topright.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Topright.frameNStart = frameN  # exact frame index
            Topright.tStart = t  # local t and not account for scr refresh
            Topright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Topright, 'tStartRefresh')  # time at next scr refresh
            Topright.setAutoDraw(True)
        if Topright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Topright.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Topright.tStop = t  # not accounting for scr refresh
                Topright.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Topright, 'tStopRefresh')  # time at next scr refresh
                Topright.setAutoDraw(False)
        
        # *Bottomleft* updates
        if Bottomleft.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Bottomleft.frameNStart = frameN  # exact frame index
            Bottomleft.tStart = t  # local t and not account for scr refresh
            Bottomleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bottomleft, 'tStartRefresh')  # time at next scr refresh
            Bottomleft.setAutoDraw(True)
        if Bottomleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bottomleft.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Bottomleft.tStop = t  # not accounting for scr refresh
                Bottomleft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Bottomleft, 'tStopRefresh')  # time at next scr refresh
                Bottomleft.setAutoDraw(False)
        
        # *Bottomright* updates
        if Bottomright.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Bottomright.frameNStart = frameN  # exact frame index
            Bottomright.tStart = t  # local t and not account for scr refresh
            Bottomright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bottomright, 'tStartRefresh')  # time at next scr refresh
            Bottomright.setAutoDraw(True)
        if Bottomright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bottomright.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Bottomright.tStop = t  # not accounting for scr refresh
                Bottomright.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Bottomright, 'tStopRefresh')  # time at next scr refresh
                Bottomright.setAutoDraw(False)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['a', 'z', 'k', 'm'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # was this correct?
                if (key_resp.keys == str(correct_answer)) or (key_resp.keys == correct_answer):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_three.addData('Fixation_cross.started', Fixation_cross.tStartRefresh)
    block_three.addData('Fixation_cross.stopped', Fixation_cross.tStopRefresh)
    block_three.addData('Topleft.started', Topleft.tStartRefresh)
    block_three.addData('Topleft.stopped', Topleft.tStopRefresh)
    block_three.addData('Topright.started', Topright.tStartRefresh)
    block_three.addData('Topright.stopped', Topright.tStopRefresh)
    block_three.addData('Bottomleft.started', Bottomleft.tStartRefresh)
    block_three.addData('Bottomleft.stopped', Bottomleft.tStopRefresh)
    block_three.addData('Bottomright.started', Bottomright.tStartRefresh)
    block_three.addData('Bottomright.stopped', Bottomright.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(correct_answer).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block_three (TrialHandler)
    block_three.addData('key_resp.keys',key_resp.keys)
    block_three.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        block_three.addData('key_resp.rt', key_resp.rt)
    block_three.addData('key_resp.started', key_resp.tStart)
    block_three.addData('key_resp.stopped', key_resp.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_three'


# ------Prepare to start Routine "Break"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
BreakComponents = [text_break, key_resp_2]
for thisComponent in BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Break"-------
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_break* updates
    if text_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_break.frameNStart = frameN  # exact frame index
        text_break.tStart = t  # local t and not account for scr refresh
        text_break.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_break, 'tStartRefresh')  # time at next scr refresh
        text_break.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['v', 'n', 'b'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_break.started', text_break.tStartRefresh)
thisExp.addData('text_break.stopped', text_break.tStopRefresh)
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block_four = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stim_present_data_block_4.csv'),
    seed=None, name='block_four')
thisExp.addLoop(block_four)  # add the loop to the experiment
thisBlock_four = block_four.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_four.rgb)
if thisBlock_four != None:
    for paramName in thisBlock_four:
        exec('{} = thisBlock_four[paramName]'.format(paramName))

for thisBlock_four in block_four:
    currentLoop = block_four
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_four.rgb)
    if thisBlock_four != None:
        for paramName in thisBlock_four:
            exec('{} = thisBlock_four[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rsvp"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    Presentation_image_1.setImage(imageone)
    Presentation_image_2.setImage(imagetwo)
    Presentation_image_3.setImage(imagethree)
    Presentation_image_4.setImage(imagefour)
    # keep track of which components have finished
    rsvpComponents = [Cross, Presentation_image_1, Presentation_image_2, Presentation_image_3, Presentation_image_4]
    for thisComponent in rsvpComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rsvpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rsvp"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rsvpClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rsvpClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Cross* updates
        if Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cross.frameNStart = frameN  # exact frame index
            Cross.tStart = t  # local t and not account for scr refresh
            Cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
            Cross.setAutoDraw(True)
        if Cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Cross.tStop = t  # not accounting for scr refresh
                Cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cross, 'tStopRefresh')  # time at next scr refresh
                Cross.setAutoDraw(False)
        
        # *Presentation_image_1* updates
        if Presentation_image_1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_1.frameNStart = frameN  # exact frame index
            Presentation_image_1.tStart = t  # local t and not account for scr refresh
            Presentation_image_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_1, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_1.setAutoDraw(True)
        if Presentation_image_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_1.tStop = t  # not accounting for scr refresh
                Presentation_image_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_1, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_1.setAutoDraw(False)
        
        # *Presentation_image_2* updates
        if Presentation_image_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_2.frameNStart = frameN  # exact frame index
            Presentation_image_2.tStart = t  # local t and not account for scr refresh
            Presentation_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_2, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_2.setAutoDraw(True)
        if Presentation_image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_2.tStop = t  # not accounting for scr refresh
                Presentation_image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_2, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_2.setAutoDraw(False)
        
        # *Presentation_image_3* updates
        if Presentation_image_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_3.frameNStart = frameN  # exact frame index
            Presentation_image_3.tStart = t  # local t and not account for scr refresh
            Presentation_image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_3, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_3.setAutoDraw(True)
        if Presentation_image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_3.tStop = t  # not accounting for scr refresh
                Presentation_image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_3, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_3.setAutoDraw(False)
        
        # *Presentation_image_4* updates
        if Presentation_image_4.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
            # keep track of start time/frame for later
            Presentation_image_4.frameNStart = frameN  # exact frame index
            Presentation_image_4.tStart = t  # local t and not account for scr refresh
            Presentation_image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Presentation_image_4, 'tStartRefresh')  # time at next scr refresh
            Presentation_image_4.setAutoDraw(True)
        if Presentation_image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Presentation_image_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Presentation_image_4.tStop = t  # not accounting for scr refresh
                Presentation_image_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Presentation_image_4, 'tStopRefresh')  # time at next scr refresh
                Presentation_image_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rsvpComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rsvp"-------
    for thisComponent in rsvpComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_four.addData('Cross.started', Cross.tStartRefresh)
    block_four.addData('Cross.stopped', Cross.tStopRefresh)
    block_four.addData('Presentation_image_1.started', Presentation_image_1.tStartRefresh)
    block_four.addData('Presentation_image_1.stopped', Presentation_image_1.tStopRefresh)
    block_four.addData('Presentation_image_2.started', Presentation_image_2.tStartRefresh)
    block_four.addData('Presentation_image_2.stopped', Presentation_image_2.tStopRefresh)
    block_four.addData('Presentation_image_3.started', Presentation_image_3.tStartRefresh)
    block_four.addData('Presentation_image_3.stopped', Presentation_image_3.tStopRefresh)
    block_four.addData('Presentation_image_4.started', Presentation_image_4.tStartRefresh)
    block_four.addData('Presentation_image_4.stopped', Presentation_image_4.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    Topleft.setImage(imageTL)
    Topright.setImage(imageTR)
    Bottomleft.setImage(imageBL)
    Bottomright.setImage(imageBR)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [Fixation_cross, Topleft, Topright, Bottomleft, Bottomright, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_cross* updates
        if Fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_cross.frameNStart = frameN  # exact frame index
            Fixation_cross.tStart = t  # local t and not account for scr refresh
            Fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_cross, 'tStartRefresh')  # time at next scr refresh
            Fixation_cross.setAutoDraw(True)
        if Fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_cross.tStop = t  # not accounting for scr refresh
                Fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation_cross, 'tStopRefresh')  # time at next scr refresh
                Fixation_cross.setAutoDraw(False)
        
        # *Topleft* updates
        if Topleft.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Topleft.frameNStart = frameN  # exact frame index
            Topleft.tStart = t  # local t and not account for scr refresh
            Topleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Topleft, 'tStartRefresh')  # time at next scr refresh
            Topleft.setAutoDraw(True)
        if Topleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Topleft.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Topleft.tStop = t  # not accounting for scr refresh
                Topleft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Topleft, 'tStopRefresh')  # time at next scr refresh
                Topleft.setAutoDraw(False)
        
        # *Topright* updates
        if Topright.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Topright.frameNStart = frameN  # exact frame index
            Topright.tStart = t  # local t and not account for scr refresh
            Topright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Topright, 'tStartRefresh')  # time at next scr refresh
            Topright.setAutoDraw(True)
        if Topright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Topright.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Topright.tStop = t  # not accounting for scr refresh
                Topright.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Topright, 'tStopRefresh')  # time at next scr refresh
                Topright.setAutoDraw(False)
        
        # *Bottomleft* updates
        if Bottomleft.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Bottomleft.frameNStart = frameN  # exact frame index
            Bottomleft.tStart = t  # local t and not account for scr refresh
            Bottomleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bottomleft, 'tStartRefresh')  # time at next scr refresh
            Bottomleft.setAutoDraw(True)
        if Bottomleft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bottomleft.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Bottomleft.tStop = t  # not accounting for scr refresh
                Bottomleft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Bottomleft, 'tStopRefresh')  # time at next scr refresh
                Bottomleft.setAutoDraw(False)
        
        # *Bottomright* updates
        if Bottomright.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Bottomright.frameNStart = frameN  # exact frame index
            Bottomright.tStart = t  # local t and not account for scr refresh
            Bottomright.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bottomright, 'tStartRefresh')  # time at next scr refresh
            Bottomright.setAutoDraw(True)
        if Bottomright.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Bottomright.tStartRefresh + 4.0-frameTolerance:
                # keep track of stop time/frame for later
                Bottomright.tStop = t  # not accounting for scr refresh
                Bottomright.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Bottomright, 'tStopRefresh')  # time at next scr refresh
                Bottomright.setAutoDraw(False)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['a', 'z', 'k', 'm'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # was this correct?
                if (key_resp.keys == str(correct_answer)) or (key_resp.keys == correct_answer):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
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
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_four.addData('Fixation_cross.started', Fixation_cross.tStartRefresh)
    block_four.addData('Fixation_cross.stopped', Fixation_cross.tStopRefresh)
    block_four.addData('Topleft.started', Topleft.tStartRefresh)
    block_four.addData('Topleft.stopped', Topleft.tStopRefresh)
    block_four.addData('Topright.started', Topright.tStartRefresh)
    block_four.addData('Topright.stopped', Topright.tStopRefresh)
    block_four.addData('Bottomleft.started', Bottomleft.tStartRefresh)
    block_four.addData('Bottomleft.stopped', Bottomleft.tStopRefresh)
    block_four.addData('Bottomright.started', Bottomright.tStartRefresh)
    block_four.addData('Bottomright.stopped', Bottomright.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(correct_answer).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for block_four (TrialHandler)
    block_four.addData('key_resp.keys',key_resp.keys)
    block_four.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        block_four.addData('key_resp.rt', key_resp.rt)
    block_four.addData('key_resp.started', key_resp.tStart)
    block_four.addData('key_resp.stopped', key_resp.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'block_four'


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text_2]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
