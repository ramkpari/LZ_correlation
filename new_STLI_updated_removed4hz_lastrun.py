#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on December 02, 2020, at 16:15
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.2.5')


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
psychopyVersion = '2020.2.5'
expName = 'new_STLI_updated_removed4hz'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Ram\\OneDrive - University of Sussex\\Desktop\\LZ correlation\\LZ_correlation\\new_STLI_updated_removed4hz_lastrun.py',
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
    text='Welcome to the experiment\n\nPress the Space key to start the experiment\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Welcome_enter = keyboard.Keyboard()

# Initialize components for Routine "Cross_and_control"
Cross_and_controlClock = core.Clock()
Crossm = visual.ShapeStim(
    win=win, name='Crossm', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "rsvp_f1"
rsvp_f1Clock = core.Clock()
Presentation_image_f1_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f1_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f1_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f1_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "rsvp_f2"
rsvp_f2Clock = core.Clock()
Presentation_image_f2_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f2_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f2_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f2_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_f2_5 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Presentation_image_f2_6 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_6', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Presentation_image_f2_7 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_7', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Presentation_image_f2_8 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_8', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)

# Initialize components for Routine "rsvp_f3"
rsvp_f3Clock = core.Clock()
Presentation_image_f3_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f3_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f3_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f3_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_f3_5 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Presentation_image_f3_6 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_6', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Presentation_image_f3_7 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_7', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Presentation_image_f3_8 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_8', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
Presentation_image_f3_9 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_9', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Presentation_image_f3_10 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_10', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
Presentation_image_f3_11 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_11', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
Presentation_image_f3_12 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_12', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "choice"
choiceClock = core.Clock()
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

# Initialize components for Routine "Cross_and_control"
Cross_and_controlClock = core.Clock()
Crossm = visual.ShapeStim(
    win=win, name='Crossm', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "rsvp_f1"
rsvp_f1Clock = core.Clock()
Presentation_image_f1_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f1_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f1_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f1_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "rsvp_f2"
rsvp_f2Clock = core.Clock()
Presentation_image_f2_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f2_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f2_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f2_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_f2_5 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Presentation_image_f2_6 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_6', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Presentation_image_f2_7 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_7', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Presentation_image_f2_8 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_8', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)

# Initialize components for Routine "rsvp_f3"
rsvp_f3Clock = core.Clock()
Presentation_image_f3_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f3_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f3_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f3_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_f3_5 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Presentation_image_f3_6 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_6', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Presentation_image_f3_7 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_7', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Presentation_image_f3_8 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_8', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
Presentation_image_f3_9 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_9', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Presentation_image_f3_10 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_10', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
Presentation_image_f3_11 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_11', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
Presentation_image_f3_12 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_12', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "choice"
choiceClock = core.Clock()
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

# Initialize components for Routine "Cross_and_control"
Cross_and_controlClock = core.Clock()
Crossm = visual.ShapeStim(
    win=win, name='Crossm', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "rsvp_f1"
rsvp_f1Clock = core.Clock()
Presentation_image_f1_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f1_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f1_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f1_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "rsvp_f2"
rsvp_f2Clock = core.Clock()
Presentation_image_f2_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f2_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f2_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f2_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_f2_5 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Presentation_image_f2_6 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_6', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Presentation_image_f2_7 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_7', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Presentation_image_f2_8 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_8', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)

# Initialize components for Routine "rsvp_f3"
rsvp_f3Clock = core.Clock()
Presentation_image_f3_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f3_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f3_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f3_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_f3_5 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Presentation_image_f3_6 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_6', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Presentation_image_f3_7 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_7', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Presentation_image_f3_8 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_8', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
Presentation_image_f3_9 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_9', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Presentation_image_f3_10 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_10', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
Presentation_image_f3_11 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_11', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
Presentation_image_f3_12 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_12', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "choice"
choiceClock = core.Clock()
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

# Initialize components for Routine "Cross_and_control"
Cross_and_controlClock = core.Clock()
Crossm = visual.ShapeStim(
    win=win, name='Crossm', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "rsvp_f1"
rsvp_f1Clock = core.Clock()
Presentation_image_f1_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f1_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f1_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f1_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f1_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "rsvp_f2"
rsvp_f2Clock = core.Clock()
Presentation_image_f2_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f2_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f2_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f2_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_f2_5 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Presentation_image_f2_6 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_6', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Presentation_image_f2_7 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_7', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Presentation_image_f2_8 = visual.ImageStim(
    win=win,
    name='Presentation_image_f2_8', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)

# Initialize components for Routine "rsvp_f3"
rsvp_f3Clock = core.Clock()
Presentation_image_f3_1 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Presentation_image_f3_2 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Presentation_image_f3_3 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Presentation_image_f3_4 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Presentation_image_f3_5 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Presentation_image_f3_6 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_6', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
Presentation_image_f3_7 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_7', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Presentation_image_f3_8 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_8', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
Presentation_image_f3_9 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_9', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Presentation_image_f3_10 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_10', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
Presentation_image_f3_11 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_11', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
Presentation_image_f3_12 = visual.ImageStim(
    win=win,
    name='Presentation_image_f3_12', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "choice"
choiceClock = core.Clock()
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
# update component parameters for each repeat
Welcome_enter.keys = []
Welcome_enter.rt = []
_Welcome_enter_allKeys = []
# keep track of which components have finished
WelcomeComponents = [text, Welcome_enter]
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
while continueRoutine:
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
    
    # *Welcome_enter* updates
    waitOnFlip = False
    if Welcome_enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_enter.frameNStart = frameN  # exact frame index
        Welcome_enter.tStart = t  # local t and not account for scr refresh
        Welcome_enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_enter, 'tStartRefresh')  # time at next scr refresh
        Welcome_enter.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Welcome_enter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Welcome_enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Welcome_enter.status == STARTED and not waitOnFlip:
        theseKeys = Welcome_enter.getKeys(keyList=['space'], waitRelease=False)
        _Welcome_enter_allKeys.extend(theseKeys)
        if len(_Welcome_enter_allKeys):
            Welcome_enter.keys = _Welcome_enter_allKeys[-1].name  # just the last key pressed
            Welcome_enter.rt = _Welcome_enter_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
    
    # ------Prepare to start Routine "Cross_and_control"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    dofone = 0 
    doftwo = 0
    dofthree = 0 
    
    if frequency == 1:
        dofone = 1
        doftwo = 0
        dofthree = 0
        
        
    elif frequency == 2:
        dofone = 0
        doftwo = 1
        dofthree = 0
        
        
    elif frequency == 3:
        dofone = 0
        doftwo = 0
        dofthree = 1
        
       
       
    # keep track of which components have finished
    Cross_and_controlComponents = [Crossm]
    for thisComponent in Cross_and_controlComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Cross_and_controlClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Cross_and_control"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Cross_and_controlClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Cross_and_controlClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Crossm* updates
        if Crossm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Crossm.frameNStart = frameN  # exact frame index
            Crossm.tStart = t  # local t and not account for scr refresh
            Crossm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Crossm, 'tStartRefresh')  # time at next scr refresh
            Crossm.setAutoDraw(True)
        if Crossm.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Crossm.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Crossm.tStop = t  # not accounting for scr refresh
                Crossm.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Crossm, 'tStopRefresh')  # time at next scr refresh
                Crossm.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cross_and_controlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cross_and_control"-------
    for thisComponent in Cross_and_controlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_one.addData('Crossm.started', Crossm.tStartRefresh)
    block_one.addData('Crossm.stopped', Crossm.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    fone_control_b1 = data.TrialHandler(nReps=dofone, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fone_control_b1')
    thisExp.addLoop(fone_control_b1)  # add the loop to the experiment
    thisFone_control_b1 = fone_control_b1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFone_control_b1.rgb)
    if thisFone_control_b1 != None:
        for paramName in thisFone_control_b1:
            exec('{} = thisFone_control_b1[paramName]'.format(paramName))
    
    for thisFone_control_b1 in fone_control_b1:
        currentLoop = fone_control_b1
        # abbreviate parameter names if possible (e.g. rgb = thisFone_control_b1.rgb)
        if thisFone_control_b1 != None:
            for paramName in thisFone_control_b1:
                exec('{} = thisFone_control_b1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f1"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Presentation_image_f1_1.setImage(imageone)
        Presentation_image_f1_2.setImage(imagetwo)
        Presentation_image_f1_3.setImage(imagethree)
        Presentation_image_f1_4.setImage(imagefour)
        # keep track of which components have finished
        rsvp_f1Components = [Presentation_image_f1_1, Presentation_image_f1_2, Presentation_image_f1_3, Presentation_image_f1_4]
        for thisComponent in rsvp_f1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f1_1* updates
            if Presentation_image_f1_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_1.frameNStart = frameN  # exact frame index
                Presentation_image_f1_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_1.setAutoDraw(True)
            if Presentation_image_f1_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_1.setAutoDraw(False)
            
            # *Presentation_image_f1_2* updates
            if Presentation_image_f1_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_2.frameNStart = frameN  # exact frame index
                Presentation_image_f1_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_2.setAutoDraw(True)
            if Presentation_image_f1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_2.setAutoDraw(False)
            
            # *Presentation_image_f1_3* updates
            if Presentation_image_f1_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_3.frameNStart = frameN  # exact frame index
                Presentation_image_f1_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_3.setAutoDraw(True)
            if Presentation_image_f1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_3.setAutoDraw(False)
            
            # *Presentation_image_f1_4* updates
            if Presentation_image_f1_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_4.frameNStart = frameN  # exact frame index
                Presentation_image_f1_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_4.setAutoDraw(True)
            if Presentation_image_f1_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f1"-------
        for thisComponent in rsvp_f1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fone_control_b1.addData('Presentation_image_f1_1.started', Presentation_image_f1_1.tStartRefresh)
        fone_control_b1.addData('Presentation_image_f1_1.stopped', Presentation_image_f1_1.tStopRefresh)
        fone_control_b1.addData('Presentation_image_f1_2.started', Presentation_image_f1_2.tStartRefresh)
        fone_control_b1.addData('Presentation_image_f1_2.stopped', Presentation_image_f1_2.tStopRefresh)
        fone_control_b1.addData('Presentation_image_f1_3.started', Presentation_image_f1_3.tStartRefresh)
        fone_control_b1.addData('Presentation_image_f1_3.stopped', Presentation_image_f1_3.tStopRefresh)
        fone_control_b1.addData('Presentation_image_f1_4.started', Presentation_image_f1_4.tStartRefresh)
        fone_control_b1.addData('Presentation_image_f1_4.stopped', Presentation_image_f1_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed dofone repeats of 'fone_control_b1'
    
    
    # set up handler to look after randomisation of conditions etc
    ftwo_control_b1 = data.TrialHandler(nReps=doftwo, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ftwo_control_b1')
    thisExp.addLoop(ftwo_control_b1)  # add the loop to the experiment
    thisFtwo_control_b1 = ftwo_control_b1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFtwo_control_b1.rgb)
    if thisFtwo_control_b1 != None:
        for paramName in thisFtwo_control_b1:
            exec('{} = thisFtwo_control_b1[paramName]'.format(paramName))
    
    for thisFtwo_control_b1 in ftwo_control_b1:
        currentLoop = ftwo_control_b1
        # abbreviate parameter names if possible (e.g. rgb = thisFtwo_control_b1.rgb)
        if thisFtwo_control_b1 != None:
            for paramName in thisFtwo_control_b1:
                exec('{} = thisFtwo_control_b1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f2"-------
        continueRoutine = True
        routineTimer.add(3.950000)
        # update component parameters for each repeat
        Presentation_image_f2_1.setImage(imageone)
        Presentation_image_f2_2.setImage(imagetwo)
        Presentation_image_f2_3.setImage(imagethree)
        Presentation_image_f2_4.setImage(imagefour)
        Presentation_image_f2_5.setImage(imagefive)
        Presentation_image_f2_6.setImage(imagesix)
        Presentation_image_f2_7.setImage(imageseven)
        Presentation_image_f2_8.setImage(imageeight)
        # keep track of which components have finished
        rsvp_f2Components = [Presentation_image_f2_1, Presentation_image_f2_2, Presentation_image_f2_3, Presentation_image_f2_4, Presentation_image_f2_5, Presentation_image_f2_6, Presentation_image_f2_7, Presentation_image_f2_8]
        for thisComponent in rsvp_f2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f2_1* updates
            if Presentation_image_f2_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_1.frameNStart = frameN  # exact frame index
                Presentation_image_f2_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_1.setAutoDraw(True)
            if Presentation_image_f2_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_1.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_1.setAutoDraw(False)
            
            # *Presentation_image_f2_2* updates
            if Presentation_image_f2_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_2.frameNStart = frameN  # exact frame index
                Presentation_image_f2_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_2.setAutoDraw(True)
            if Presentation_image_f2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_2.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_2.setAutoDraw(False)
            
            # *Presentation_image_f2_3* updates
            if Presentation_image_f2_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_3.frameNStart = frameN  # exact frame index
                Presentation_image_f2_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_3.setAutoDraw(True)
            if Presentation_image_f2_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_3.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_3.setAutoDraw(False)
            
            # *Presentation_image_f2_4* updates
            if Presentation_image_f2_4.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_4.frameNStart = frameN  # exact frame index
                Presentation_image_f2_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_4.setAutoDraw(True)
            if Presentation_image_f2_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_4.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_4.setAutoDraw(False)
            
            # *Presentation_image_f2_5* updates
            if Presentation_image_f2_5.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_5.frameNStart = frameN  # exact frame index
                Presentation_image_f2_5.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_5, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_5.setAutoDraw(True)
            if Presentation_image_f2_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_5.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_5.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_5, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_5.setAutoDraw(False)
            
            # *Presentation_image_f2_6* updates
            if Presentation_image_f2_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_6.frameNStart = frameN  # exact frame index
                Presentation_image_f2_6.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_6, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_6.setAutoDraw(True)
            if Presentation_image_f2_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_6.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_6.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_6, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_6.setAutoDraw(False)
            
            # *Presentation_image_f2_7* updates
            if Presentation_image_f2_7.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_7.frameNStart = frameN  # exact frame index
                Presentation_image_f2_7.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_7, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_7.setAutoDraw(True)
            if Presentation_image_f2_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_7.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_7.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_7, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_7.setAutoDraw(False)
            
            # *Presentation_image_f2_8* updates
            if Presentation_image_f2_8.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_8.frameNStart = frameN  # exact frame index
                Presentation_image_f2_8.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_8, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_8.setAutoDraw(True)
            if Presentation_image_f2_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_8.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_8.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_8, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f2"-------
        for thisComponent in rsvp_f2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ftwo_control_b1.addData('Presentation_image_f2_1.started', Presentation_image_f2_1.tStartRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_1.stopped', Presentation_image_f2_1.tStopRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_2.started', Presentation_image_f2_2.tStartRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_2.stopped', Presentation_image_f2_2.tStopRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_3.started', Presentation_image_f2_3.tStartRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_3.stopped', Presentation_image_f2_3.tStopRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_4.started', Presentation_image_f2_4.tStartRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_4.stopped', Presentation_image_f2_4.tStopRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_5.started', Presentation_image_f2_5.tStartRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_5.stopped', Presentation_image_f2_5.tStopRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_6.started', Presentation_image_f2_6.tStartRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_6.stopped', Presentation_image_f2_6.tStopRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_7.started', Presentation_image_f2_7.tStartRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_7.stopped', Presentation_image_f2_7.tStopRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_8.started', Presentation_image_f2_8.tStartRefresh)
        ftwo_control_b1.addData('Presentation_image_f2_8.stopped', Presentation_image_f2_8.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doftwo repeats of 'ftwo_control_b1'
    
    
    # set up handler to look after randomisation of conditions etc
    fthree_control_b1 = data.TrialHandler(nReps=dofthree, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fthree_control_b1')
    thisExp.addLoop(fthree_control_b1)  # add the loop to the experiment
    thisFthree_control_b1 = fthree_control_b1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFthree_control_b1.rgb)
    if thisFthree_control_b1 != None:
        for paramName in thisFthree_control_b1:
            exec('{} = thisFthree_control_b1[paramName]'.format(paramName))
    
    for thisFthree_control_b1 in fthree_control_b1:
        currentLoop = fthree_control_b1
        # abbreviate parameter names if possible (e.g. rgb = thisFthree_control_b1.rgb)
        if thisFthree_control_b1 != None:
            for paramName in thisFthree_control_b1:
                exec('{} = thisFthree_control_b1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f3"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Presentation_image_f3_1.setImage(imageone)
        Presentation_image_f3_2.setImage(imagetwo)
        Presentation_image_f3_3.setImage(imagethree)
        Presentation_image_f3_4.setImage(imagefour)
        Presentation_image_f3_5.setImage(imagefive)
        Presentation_image_f3_6.setImage(imagesix)
        Presentation_image_f3_7.setImage(imageseven)
        Presentation_image_f3_8.setImage(imageeight)
        Presentation_image_f3_9.setImage(imagenine)
        Presentation_image_f3_10.setImage(imageten)
        Presentation_image_f3_11.setImage(imageeleven)
        Presentation_image_f3_12.setImage(imagetwelve)
        # keep track of which components have finished
        rsvp_f3Components = [Presentation_image_f3_1, Presentation_image_f3_2, Presentation_image_f3_3, Presentation_image_f3_4, Presentation_image_f3_5, Presentation_image_f3_6, Presentation_image_f3_7, Presentation_image_f3_8, Presentation_image_f3_9, Presentation_image_f3_10, Presentation_image_f3_11, Presentation_image_f3_12]
        for thisComponent in rsvp_f3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f3_1* updates
            if Presentation_image_f3_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_1.frameNStart = frameN  # exact frame index
                Presentation_image_f3_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_1.setAutoDraw(True)
            if Presentation_image_f3_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_1.tStartRefresh + 0.30-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_1.setAutoDraw(False)
            
            # *Presentation_image_f3_2* updates
            if Presentation_image_f3_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_2.frameNStart = frameN  # exact frame index
                Presentation_image_f3_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_2.setAutoDraw(True)
            if Presentation_image_f3_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_2.setAutoDraw(False)
            
            # *Presentation_image_f3_3* updates
            if Presentation_image_f3_3.status == NOT_STARTED and tThisFlip >= 0.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_3.frameNStart = frameN  # exact frame index
                Presentation_image_f3_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_3.setAutoDraw(True)
            if Presentation_image_f3_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_3.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_3.setAutoDraw(False)
            
            # *Presentation_image_f3_4* updates
            if Presentation_image_f3_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_4.frameNStart = frameN  # exact frame index
                Presentation_image_f3_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_4.setAutoDraw(True)
            if Presentation_image_f3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_4.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_4.setAutoDraw(False)
            
            # *Presentation_image_f3_5* updates
            if Presentation_image_f3_5.status == NOT_STARTED and tThisFlip >= 1.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_5.frameNStart = frameN  # exact frame index
                Presentation_image_f3_5.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_5, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_5.setAutoDraw(True)
            if Presentation_image_f3_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_5.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_5.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_5, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_5.setAutoDraw(False)
            
            # *Presentation_image_f3_6* updates
            if Presentation_image_f3_6.status == NOT_STARTED and tThisFlip >= 1.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_6.frameNStart = frameN  # exact frame index
                Presentation_image_f3_6.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_6, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_6.setAutoDraw(True)
            if Presentation_image_f3_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_6.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_6.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_6, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_6.setAutoDraw(False)
            
            # *Presentation_image_f3_7* updates
            if Presentation_image_f3_7.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_7.frameNStart = frameN  # exact frame index
                Presentation_image_f3_7.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_7, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_7.setAutoDraw(True)
            if Presentation_image_f3_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_7.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_7.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_7, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_7.setAutoDraw(False)
            
            # *Presentation_image_f3_8* updates
            if Presentation_image_f3_8.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_8.frameNStart = frameN  # exact frame index
                Presentation_image_f3_8.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_8, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_8.setAutoDraw(True)
            if Presentation_image_f3_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_8.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_8.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_8, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_8.setAutoDraw(False)
            
            # *Presentation_image_f3_9* updates
            if Presentation_image_f3_9.status == NOT_STARTED and tThisFlip >= 2.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_9.frameNStart = frameN  # exact frame index
                Presentation_image_f3_9.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_9, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_9.setAutoDraw(True)
            if Presentation_image_f3_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_9.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_9.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_9, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_9.setAutoDraw(False)
            
            # *Presentation_image_f3_10* updates
            if Presentation_image_f3_10.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_10.frameNStart = frameN  # exact frame index
                Presentation_image_f3_10.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_10, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_10.setAutoDraw(True)
            if Presentation_image_f3_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_10.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_10.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_10, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_10.setAutoDraw(False)
            
            # *Presentation_image_f3_11* updates
            if Presentation_image_f3_11.status == NOT_STARTED and tThisFlip >= 3.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_11.frameNStart = frameN  # exact frame index
                Presentation_image_f3_11.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_11, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_11.setAutoDraw(True)
            if Presentation_image_f3_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_11.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_11.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_11, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_11.setAutoDraw(False)
            
            # *Presentation_image_f3_12* updates
            if Presentation_image_f3_12.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_12.frameNStart = frameN  # exact frame index
                Presentation_image_f3_12.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_12, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_12.setAutoDraw(True)
            if Presentation_image_f3_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_12.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_12.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_12, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_12.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f3"-------
        for thisComponent in rsvp_f3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fthree_control_b1.addData('Presentation_image_f3_1.started', Presentation_image_f3_1.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_1.stopped', Presentation_image_f3_1.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_2.started', Presentation_image_f3_2.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_2.stopped', Presentation_image_f3_2.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_3.started', Presentation_image_f3_3.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_3.stopped', Presentation_image_f3_3.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_4.started', Presentation_image_f3_4.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_4.stopped', Presentation_image_f3_4.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_5.started', Presentation_image_f3_5.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_5.stopped', Presentation_image_f3_5.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_6.started', Presentation_image_f3_6.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_6.stopped', Presentation_image_f3_6.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_7.started', Presentation_image_f3_7.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_7.stopped', Presentation_image_f3_7.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_8.started', Presentation_image_f3_8.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_8.stopped', Presentation_image_f3_8.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_9.started', Presentation_image_f3_9.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_9.stopped', Presentation_image_f3_9.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_10.started', Presentation_image_f3_10.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_10.stopped', Presentation_image_f3_10.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_11.started', Presentation_image_f3_11.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_11.stopped', Presentation_image_f3_11.tStopRefresh)
        fthree_control_b1.addData('Presentation_image_f3_12.started', Presentation_image_f3_12.tStartRefresh)
        fthree_control_b1.addData('Presentation_image_f3_12.stopped', Presentation_image_f3_12.tStopRefresh)
        thisExp.nextEntry()
        
    # completed dofthree repeats of 'fthree_control_b1'
    
    
    # ------Prepare to start Routine "choice"-------
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
    choiceComponents = [Fixation_cross, Topleft, Topright, Bottomleft, Bottomright, key_resp]
    for thisComponent in choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice"-------
    while continueRoutine:
        # get current time
        t = choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choiceClock)
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
        for thisComponent in choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice"-------
    for thisComponent in choiceComponents:
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
    # the Routine "choice" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "Cross_and_control"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    dofone = 0 
    doftwo = 0
    dofthree = 0 
    
    if frequency == 1:
        dofone = 1
        doftwo = 0
        dofthree = 0
        
        
    elif frequency == 2:
        dofone = 0
        doftwo = 1
        dofthree = 0
        
        
    elif frequency == 3:
        dofone = 0
        doftwo = 0
        dofthree = 1
        
       
       
    # keep track of which components have finished
    Cross_and_controlComponents = [Crossm]
    for thisComponent in Cross_and_controlComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Cross_and_controlClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Cross_and_control"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Cross_and_controlClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Cross_and_controlClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Crossm* updates
        if Crossm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Crossm.frameNStart = frameN  # exact frame index
            Crossm.tStart = t  # local t and not account for scr refresh
            Crossm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Crossm, 'tStartRefresh')  # time at next scr refresh
            Crossm.setAutoDraw(True)
        if Crossm.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Crossm.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Crossm.tStop = t  # not accounting for scr refresh
                Crossm.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Crossm, 'tStopRefresh')  # time at next scr refresh
                Crossm.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cross_and_controlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cross_and_control"-------
    for thisComponent in Cross_and_controlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_two.addData('Crossm.started', Crossm.tStartRefresh)
    block_two.addData('Crossm.stopped', Crossm.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    fone_control_b2 = data.TrialHandler(nReps=dofone, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fone_control_b2')
    thisExp.addLoop(fone_control_b2)  # add the loop to the experiment
    thisFone_control_b2 = fone_control_b2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFone_control_b2.rgb)
    if thisFone_control_b2 != None:
        for paramName in thisFone_control_b2:
            exec('{} = thisFone_control_b2[paramName]'.format(paramName))
    
    for thisFone_control_b2 in fone_control_b2:
        currentLoop = fone_control_b2
        # abbreviate parameter names if possible (e.g. rgb = thisFone_control_b2.rgb)
        if thisFone_control_b2 != None:
            for paramName in thisFone_control_b2:
                exec('{} = thisFone_control_b2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f1"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Presentation_image_f1_1.setImage(imageone)
        Presentation_image_f1_2.setImage(imagetwo)
        Presentation_image_f1_3.setImage(imagethree)
        Presentation_image_f1_4.setImage(imagefour)
        # keep track of which components have finished
        rsvp_f1Components = [Presentation_image_f1_1, Presentation_image_f1_2, Presentation_image_f1_3, Presentation_image_f1_4]
        for thisComponent in rsvp_f1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f1_1* updates
            if Presentation_image_f1_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_1.frameNStart = frameN  # exact frame index
                Presentation_image_f1_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_1.setAutoDraw(True)
            if Presentation_image_f1_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_1.setAutoDraw(False)
            
            # *Presentation_image_f1_2* updates
            if Presentation_image_f1_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_2.frameNStart = frameN  # exact frame index
                Presentation_image_f1_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_2.setAutoDraw(True)
            if Presentation_image_f1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_2.setAutoDraw(False)
            
            # *Presentation_image_f1_3* updates
            if Presentation_image_f1_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_3.frameNStart = frameN  # exact frame index
                Presentation_image_f1_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_3.setAutoDraw(True)
            if Presentation_image_f1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_3.setAutoDraw(False)
            
            # *Presentation_image_f1_4* updates
            if Presentation_image_f1_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_4.frameNStart = frameN  # exact frame index
                Presentation_image_f1_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_4.setAutoDraw(True)
            if Presentation_image_f1_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f1"-------
        for thisComponent in rsvp_f1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fone_control_b2.addData('Presentation_image_f1_1.started', Presentation_image_f1_1.tStartRefresh)
        fone_control_b2.addData('Presentation_image_f1_1.stopped', Presentation_image_f1_1.tStopRefresh)
        fone_control_b2.addData('Presentation_image_f1_2.started', Presentation_image_f1_2.tStartRefresh)
        fone_control_b2.addData('Presentation_image_f1_2.stopped', Presentation_image_f1_2.tStopRefresh)
        fone_control_b2.addData('Presentation_image_f1_3.started', Presentation_image_f1_3.tStartRefresh)
        fone_control_b2.addData('Presentation_image_f1_3.stopped', Presentation_image_f1_3.tStopRefresh)
        fone_control_b2.addData('Presentation_image_f1_4.started', Presentation_image_f1_4.tStartRefresh)
        fone_control_b2.addData('Presentation_image_f1_4.stopped', Presentation_image_f1_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed dofone repeats of 'fone_control_b2'
    
    
    # set up handler to look after randomisation of conditions etc
    ftwo_control_b2 = data.TrialHandler(nReps=doftwo, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ftwo_control_b2')
    thisExp.addLoop(ftwo_control_b2)  # add the loop to the experiment
    thisFtwo_control_b2 = ftwo_control_b2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFtwo_control_b2.rgb)
    if thisFtwo_control_b2 != None:
        for paramName in thisFtwo_control_b2:
            exec('{} = thisFtwo_control_b2[paramName]'.format(paramName))
    
    for thisFtwo_control_b2 in ftwo_control_b2:
        currentLoop = ftwo_control_b2
        # abbreviate parameter names if possible (e.g. rgb = thisFtwo_control_b2.rgb)
        if thisFtwo_control_b2 != None:
            for paramName in thisFtwo_control_b2:
                exec('{} = thisFtwo_control_b2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f2"-------
        continueRoutine = True
        routineTimer.add(3.950000)
        # update component parameters for each repeat
        Presentation_image_f2_1.setImage(imageone)
        Presentation_image_f2_2.setImage(imagetwo)
        Presentation_image_f2_3.setImage(imagethree)
        Presentation_image_f2_4.setImage(imagefour)
        Presentation_image_f2_5.setImage(imagefive)
        Presentation_image_f2_6.setImage(imagesix)
        Presentation_image_f2_7.setImage(imageseven)
        Presentation_image_f2_8.setImage(imageeight)
        # keep track of which components have finished
        rsvp_f2Components = [Presentation_image_f2_1, Presentation_image_f2_2, Presentation_image_f2_3, Presentation_image_f2_4, Presentation_image_f2_5, Presentation_image_f2_6, Presentation_image_f2_7, Presentation_image_f2_8]
        for thisComponent in rsvp_f2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f2_1* updates
            if Presentation_image_f2_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_1.frameNStart = frameN  # exact frame index
                Presentation_image_f2_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_1.setAutoDraw(True)
            if Presentation_image_f2_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_1.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_1.setAutoDraw(False)
            
            # *Presentation_image_f2_2* updates
            if Presentation_image_f2_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_2.frameNStart = frameN  # exact frame index
                Presentation_image_f2_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_2.setAutoDraw(True)
            if Presentation_image_f2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_2.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_2.setAutoDraw(False)
            
            # *Presentation_image_f2_3* updates
            if Presentation_image_f2_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_3.frameNStart = frameN  # exact frame index
                Presentation_image_f2_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_3.setAutoDraw(True)
            if Presentation_image_f2_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_3.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_3.setAutoDraw(False)
            
            # *Presentation_image_f2_4* updates
            if Presentation_image_f2_4.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_4.frameNStart = frameN  # exact frame index
                Presentation_image_f2_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_4.setAutoDraw(True)
            if Presentation_image_f2_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_4.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_4.setAutoDraw(False)
            
            # *Presentation_image_f2_5* updates
            if Presentation_image_f2_5.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_5.frameNStart = frameN  # exact frame index
                Presentation_image_f2_5.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_5, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_5.setAutoDraw(True)
            if Presentation_image_f2_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_5.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_5.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_5, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_5.setAutoDraw(False)
            
            # *Presentation_image_f2_6* updates
            if Presentation_image_f2_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_6.frameNStart = frameN  # exact frame index
                Presentation_image_f2_6.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_6, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_6.setAutoDraw(True)
            if Presentation_image_f2_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_6.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_6.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_6, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_6.setAutoDraw(False)
            
            # *Presentation_image_f2_7* updates
            if Presentation_image_f2_7.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_7.frameNStart = frameN  # exact frame index
                Presentation_image_f2_7.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_7, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_7.setAutoDraw(True)
            if Presentation_image_f2_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_7.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_7.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_7, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_7.setAutoDraw(False)
            
            # *Presentation_image_f2_8* updates
            if Presentation_image_f2_8.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_8.frameNStart = frameN  # exact frame index
                Presentation_image_f2_8.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_8, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_8.setAutoDraw(True)
            if Presentation_image_f2_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_8.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_8.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_8, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f2"-------
        for thisComponent in rsvp_f2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ftwo_control_b2.addData('Presentation_image_f2_1.started', Presentation_image_f2_1.tStartRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_1.stopped', Presentation_image_f2_1.tStopRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_2.started', Presentation_image_f2_2.tStartRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_2.stopped', Presentation_image_f2_2.tStopRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_3.started', Presentation_image_f2_3.tStartRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_3.stopped', Presentation_image_f2_3.tStopRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_4.started', Presentation_image_f2_4.tStartRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_4.stopped', Presentation_image_f2_4.tStopRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_5.started', Presentation_image_f2_5.tStartRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_5.stopped', Presentation_image_f2_5.tStopRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_6.started', Presentation_image_f2_6.tStartRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_6.stopped', Presentation_image_f2_6.tStopRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_7.started', Presentation_image_f2_7.tStartRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_7.stopped', Presentation_image_f2_7.tStopRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_8.started', Presentation_image_f2_8.tStartRefresh)
        ftwo_control_b2.addData('Presentation_image_f2_8.stopped', Presentation_image_f2_8.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doftwo repeats of 'ftwo_control_b2'
    
    
    # set up handler to look after randomisation of conditions etc
    fthree_control_b2 = data.TrialHandler(nReps=dofthree, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fthree_control_b2')
    thisExp.addLoop(fthree_control_b2)  # add the loop to the experiment
    thisFthree_control_b2 = fthree_control_b2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFthree_control_b2.rgb)
    if thisFthree_control_b2 != None:
        for paramName in thisFthree_control_b2:
            exec('{} = thisFthree_control_b2[paramName]'.format(paramName))
    
    for thisFthree_control_b2 in fthree_control_b2:
        currentLoop = fthree_control_b2
        # abbreviate parameter names if possible (e.g. rgb = thisFthree_control_b2.rgb)
        if thisFthree_control_b2 != None:
            for paramName in thisFthree_control_b2:
                exec('{} = thisFthree_control_b2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f3"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Presentation_image_f3_1.setImage(imageone)
        Presentation_image_f3_2.setImage(imagetwo)
        Presentation_image_f3_3.setImage(imagethree)
        Presentation_image_f3_4.setImage(imagefour)
        Presentation_image_f3_5.setImage(imagefive)
        Presentation_image_f3_6.setImage(imagesix)
        Presentation_image_f3_7.setImage(imageseven)
        Presentation_image_f3_8.setImage(imageeight)
        Presentation_image_f3_9.setImage(imagenine)
        Presentation_image_f3_10.setImage(imageten)
        Presentation_image_f3_11.setImage(imageeleven)
        Presentation_image_f3_12.setImage(imagetwelve)
        # keep track of which components have finished
        rsvp_f3Components = [Presentation_image_f3_1, Presentation_image_f3_2, Presentation_image_f3_3, Presentation_image_f3_4, Presentation_image_f3_5, Presentation_image_f3_6, Presentation_image_f3_7, Presentation_image_f3_8, Presentation_image_f3_9, Presentation_image_f3_10, Presentation_image_f3_11, Presentation_image_f3_12]
        for thisComponent in rsvp_f3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f3_1* updates
            if Presentation_image_f3_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_1.frameNStart = frameN  # exact frame index
                Presentation_image_f3_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_1.setAutoDraw(True)
            if Presentation_image_f3_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_1.tStartRefresh + 0.30-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_1.setAutoDraw(False)
            
            # *Presentation_image_f3_2* updates
            if Presentation_image_f3_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_2.frameNStart = frameN  # exact frame index
                Presentation_image_f3_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_2.setAutoDraw(True)
            if Presentation_image_f3_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_2.setAutoDraw(False)
            
            # *Presentation_image_f3_3* updates
            if Presentation_image_f3_3.status == NOT_STARTED and tThisFlip >= 0.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_3.frameNStart = frameN  # exact frame index
                Presentation_image_f3_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_3.setAutoDraw(True)
            if Presentation_image_f3_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_3.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_3.setAutoDraw(False)
            
            # *Presentation_image_f3_4* updates
            if Presentation_image_f3_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_4.frameNStart = frameN  # exact frame index
                Presentation_image_f3_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_4.setAutoDraw(True)
            if Presentation_image_f3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_4.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_4.setAutoDraw(False)
            
            # *Presentation_image_f3_5* updates
            if Presentation_image_f3_5.status == NOT_STARTED and tThisFlip >= 1.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_5.frameNStart = frameN  # exact frame index
                Presentation_image_f3_5.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_5, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_5.setAutoDraw(True)
            if Presentation_image_f3_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_5.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_5.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_5, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_5.setAutoDraw(False)
            
            # *Presentation_image_f3_6* updates
            if Presentation_image_f3_6.status == NOT_STARTED and tThisFlip >= 1.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_6.frameNStart = frameN  # exact frame index
                Presentation_image_f3_6.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_6, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_6.setAutoDraw(True)
            if Presentation_image_f3_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_6.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_6.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_6, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_6.setAutoDraw(False)
            
            # *Presentation_image_f3_7* updates
            if Presentation_image_f3_7.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_7.frameNStart = frameN  # exact frame index
                Presentation_image_f3_7.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_7, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_7.setAutoDraw(True)
            if Presentation_image_f3_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_7.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_7.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_7, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_7.setAutoDraw(False)
            
            # *Presentation_image_f3_8* updates
            if Presentation_image_f3_8.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_8.frameNStart = frameN  # exact frame index
                Presentation_image_f3_8.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_8, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_8.setAutoDraw(True)
            if Presentation_image_f3_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_8.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_8.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_8, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_8.setAutoDraw(False)
            
            # *Presentation_image_f3_9* updates
            if Presentation_image_f3_9.status == NOT_STARTED and tThisFlip >= 2.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_9.frameNStart = frameN  # exact frame index
                Presentation_image_f3_9.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_9, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_9.setAutoDraw(True)
            if Presentation_image_f3_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_9.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_9.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_9, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_9.setAutoDraw(False)
            
            # *Presentation_image_f3_10* updates
            if Presentation_image_f3_10.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_10.frameNStart = frameN  # exact frame index
                Presentation_image_f3_10.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_10, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_10.setAutoDraw(True)
            if Presentation_image_f3_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_10.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_10.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_10, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_10.setAutoDraw(False)
            
            # *Presentation_image_f3_11* updates
            if Presentation_image_f3_11.status == NOT_STARTED and tThisFlip >= 3.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_11.frameNStart = frameN  # exact frame index
                Presentation_image_f3_11.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_11, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_11.setAutoDraw(True)
            if Presentation_image_f3_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_11.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_11.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_11, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_11.setAutoDraw(False)
            
            # *Presentation_image_f3_12* updates
            if Presentation_image_f3_12.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_12.frameNStart = frameN  # exact frame index
                Presentation_image_f3_12.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_12, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_12.setAutoDraw(True)
            if Presentation_image_f3_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_12.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_12.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_12, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_12.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f3"-------
        for thisComponent in rsvp_f3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fthree_control_b2.addData('Presentation_image_f3_1.started', Presentation_image_f3_1.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_1.stopped', Presentation_image_f3_1.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_2.started', Presentation_image_f3_2.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_2.stopped', Presentation_image_f3_2.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_3.started', Presentation_image_f3_3.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_3.stopped', Presentation_image_f3_3.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_4.started', Presentation_image_f3_4.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_4.stopped', Presentation_image_f3_4.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_5.started', Presentation_image_f3_5.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_5.stopped', Presentation_image_f3_5.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_6.started', Presentation_image_f3_6.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_6.stopped', Presentation_image_f3_6.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_7.started', Presentation_image_f3_7.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_7.stopped', Presentation_image_f3_7.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_8.started', Presentation_image_f3_8.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_8.stopped', Presentation_image_f3_8.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_9.started', Presentation_image_f3_9.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_9.stopped', Presentation_image_f3_9.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_10.started', Presentation_image_f3_10.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_10.stopped', Presentation_image_f3_10.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_11.started', Presentation_image_f3_11.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_11.stopped', Presentation_image_f3_11.tStopRefresh)
        fthree_control_b2.addData('Presentation_image_f3_12.started', Presentation_image_f3_12.tStartRefresh)
        fthree_control_b2.addData('Presentation_image_f3_12.stopped', Presentation_image_f3_12.tStopRefresh)
        thisExp.nextEntry()
        
    # completed dofthree repeats of 'fthree_control_b2'
    
    
    # ------Prepare to start Routine "choice"-------
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
    choiceComponents = [Fixation_cross, Topleft, Topright, Bottomleft, Bottomright, key_resp]
    for thisComponent in choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice"-------
    while continueRoutine:
        # get current time
        t = choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choiceClock)
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
        for thisComponent in choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice"-------
    for thisComponent in choiceComponents:
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
    # the Routine "choice" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "Cross_and_control"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    dofone = 0 
    doftwo = 0
    dofthree = 0 
    
    if frequency == 1:
        dofone = 1
        doftwo = 0
        dofthree = 0
        
        
    elif frequency == 2:
        dofone = 0
        doftwo = 1
        dofthree = 0
        
        
    elif frequency == 3:
        dofone = 0
        doftwo = 0
        dofthree = 1
        
       
       
    # keep track of which components have finished
    Cross_and_controlComponents = [Crossm]
    for thisComponent in Cross_and_controlComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Cross_and_controlClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Cross_and_control"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Cross_and_controlClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Cross_and_controlClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Crossm* updates
        if Crossm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Crossm.frameNStart = frameN  # exact frame index
            Crossm.tStart = t  # local t and not account for scr refresh
            Crossm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Crossm, 'tStartRefresh')  # time at next scr refresh
            Crossm.setAutoDraw(True)
        if Crossm.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Crossm.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Crossm.tStop = t  # not accounting for scr refresh
                Crossm.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Crossm, 'tStopRefresh')  # time at next scr refresh
                Crossm.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cross_and_controlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cross_and_control"-------
    for thisComponent in Cross_and_controlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_three.addData('Crossm.started', Crossm.tStartRefresh)
    block_three.addData('Crossm.stopped', Crossm.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    fone_control_b3 = data.TrialHandler(nReps=dofone, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fone_control_b3')
    thisExp.addLoop(fone_control_b3)  # add the loop to the experiment
    thisFone_control_b3 = fone_control_b3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFone_control_b3.rgb)
    if thisFone_control_b3 != None:
        for paramName in thisFone_control_b3:
            exec('{} = thisFone_control_b3[paramName]'.format(paramName))
    
    for thisFone_control_b3 in fone_control_b3:
        currentLoop = fone_control_b3
        # abbreviate parameter names if possible (e.g. rgb = thisFone_control_b3.rgb)
        if thisFone_control_b3 != None:
            for paramName in thisFone_control_b3:
                exec('{} = thisFone_control_b3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f1"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Presentation_image_f1_1.setImage(imageone)
        Presentation_image_f1_2.setImage(imagetwo)
        Presentation_image_f1_3.setImage(imagethree)
        Presentation_image_f1_4.setImage(imagefour)
        # keep track of which components have finished
        rsvp_f1Components = [Presentation_image_f1_1, Presentation_image_f1_2, Presentation_image_f1_3, Presentation_image_f1_4]
        for thisComponent in rsvp_f1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f1_1* updates
            if Presentation_image_f1_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_1.frameNStart = frameN  # exact frame index
                Presentation_image_f1_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_1.setAutoDraw(True)
            if Presentation_image_f1_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_1.setAutoDraw(False)
            
            # *Presentation_image_f1_2* updates
            if Presentation_image_f1_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_2.frameNStart = frameN  # exact frame index
                Presentation_image_f1_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_2.setAutoDraw(True)
            if Presentation_image_f1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_2.setAutoDraw(False)
            
            # *Presentation_image_f1_3* updates
            if Presentation_image_f1_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_3.frameNStart = frameN  # exact frame index
                Presentation_image_f1_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_3.setAutoDraw(True)
            if Presentation_image_f1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_3.setAutoDraw(False)
            
            # *Presentation_image_f1_4* updates
            if Presentation_image_f1_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_4.frameNStart = frameN  # exact frame index
                Presentation_image_f1_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_4.setAutoDraw(True)
            if Presentation_image_f1_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f1"-------
        for thisComponent in rsvp_f1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fone_control_b3.addData('Presentation_image_f1_1.started', Presentation_image_f1_1.tStartRefresh)
        fone_control_b3.addData('Presentation_image_f1_1.stopped', Presentation_image_f1_1.tStopRefresh)
        fone_control_b3.addData('Presentation_image_f1_2.started', Presentation_image_f1_2.tStartRefresh)
        fone_control_b3.addData('Presentation_image_f1_2.stopped', Presentation_image_f1_2.tStopRefresh)
        fone_control_b3.addData('Presentation_image_f1_3.started', Presentation_image_f1_3.tStartRefresh)
        fone_control_b3.addData('Presentation_image_f1_3.stopped', Presentation_image_f1_3.tStopRefresh)
        fone_control_b3.addData('Presentation_image_f1_4.started', Presentation_image_f1_4.tStartRefresh)
        fone_control_b3.addData('Presentation_image_f1_4.stopped', Presentation_image_f1_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed dofone repeats of 'fone_control_b3'
    
    
    # set up handler to look after randomisation of conditions etc
    ftwo_control_b3 = data.TrialHandler(nReps=doftwo, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ftwo_control_b3')
    thisExp.addLoop(ftwo_control_b3)  # add the loop to the experiment
    thisFtwo_control_b3 = ftwo_control_b3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFtwo_control_b3.rgb)
    if thisFtwo_control_b3 != None:
        for paramName in thisFtwo_control_b3:
            exec('{} = thisFtwo_control_b3[paramName]'.format(paramName))
    
    for thisFtwo_control_b3 in ftwo_control_b3:
        currentLoop = ftwo_control_b3
        # abbreviate parameter names if possible (e.g. rgb = thisFtwo_control_b3.rgb)
        if thisFtwo_control_b3 != None:
            for paramName in thisFtwo_control_b3:
                exec('{} = thisFtwo_control_b3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f2"-------
        continueRoutine = True
        routineTimer.add(3.950000)
        # update component parameters for each repeat
        Presentation_image_f2_1.setImage(imageone)
        Presentation_image_f2_2.setImage(imagetwo)
        Presentation_image_f2_3.setImage(imagethree)
        Presentation_image_f2_4.setImage(imagefour)
        Presentation_image_f2_5.setImage(imagefive)
        Presentation_image_f2_6.setImage(imagesix)
        Presentation_image_f2_7.setImage(imageseven)
        Presentation_image_f2_8.setImage(imageeight)
        # keep track of which components have finished
        rsvp_f2Components = [Presentation_image_f2_1, Presentation_image_f2_2, Presentation_image_f2_3, Presentation_image_f2_4, Presentation_image_f2_5, Presentation_image_f2_6, Presentation_image_f2_7, Presentation_image_f2_8]
        for thisComponent in rsvp_f2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f2_1* updates
            if Presentation_image_f2_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_1.frameNStart = frameN  # exact frame index
                Presentation_image_f2_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_1.setAutoDraw(True)
            if Presentation_image_f2_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_1.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_1.setAutoDraw(False)
            
            # *Presentation_image_f2_2* updates
            if Presentation_image_f2_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_2.frameNStart = frameN  # exact frame index
                Presentation_image_f2_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_2.setAutoDraw(True)
            if Presentation_image_f2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_2.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_2.setAutoDraw(False)
            
            # *Presentation_image_f2_3* updates
            if Presentation_image_f2_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_3.frameNStart = frameN  # exact frame index
                Presentation_image_f2_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_3.setAutoDraw(True)
            if Presentation_image_f2_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_3.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_3.setAutoDraw(False)
            
            # *Presentation_image_f2_4* updates
            if Presentation_image_f2_4.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_4.frameNStart = frameN  # exact frame index
                Presentation_image_f2_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_4.setAutoDraw(True)
            if Presentation_image_f2_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_4.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_4.setAutoDraw(False)
            
            # *Presentation_image_f2_5* updates
            if Presentation_image_f2_5.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_5.frameNStart = frameN  # exact frame index
                Presentation_image_f2_5.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_5, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_5.setAutoDraw(True)
            if Presentation_image_f2_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_5.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_5.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_5, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_5.setAutoDraw(False)
            
            # *Presentation_image_f2_6* updates
            if Presentation_image_f2_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_6.frameNStart = frameN  # exact frame index
                Presentation_image_f2_6.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_6, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_6.setAutoDraw(True)
            if Presentation_image_f2_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_6.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_6.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_6, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_6.setAutoDraw(False)
            
            # *Presentation_image_f2_7* updates
            if Presentation_image_f2_7.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_7.frameNStart = frameN  # exact frame index
                Presentation_image_f2_7.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_7, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_7.setAutoDraw(True)
            if Presentation_image_f2_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_7.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_7.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_7, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_7.setAutoDraw(False)
            
            # *Presentation_image_f2_8* updates
            if Presentation_image_f2_8.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_8.frameNStart = frameN  # exact frame index
                Presentation_image_f2_8.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_8, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_8.setAutoDraw(True)
            if Presentation_image_f2_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_8.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_8.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_8, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f2"-------
        for thisComponent in rsvp_f2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ftwo_control_b3.addData('Presentation_image_f2_1.started', Presentation_image_f2_1.tStartRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_1.stopped', Presentation_image_f2_1.tStopRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_2.started', Presentation_image_f2_2.tStartRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_2.stopped', Presentation_image_f2_2.tStopRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_3.started', Presentation_image_f2_3.tStartRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_3.stopped', Presentation_image_f2_3.tStopRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_4.started', Presentation_image_f2_4.tStartRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_4.stopped', Presentation_image_f2_4.tStopRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_5.started', Presentation_image_f2_5.tStartRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_5.stopped', Presentation_image_f2_5.tStopRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_6.started', Presentation_image_f2_6.tStartRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_6.stopped', Presentation_image_f2_6.tStopRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_7.started', Presentation_image_f2_7.tStartRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_7.stopped', Presentation_image_f2_7.tStopRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_8.started', Presentation_image_f2_8.tStartRefresh)
        ftwo_control_b3.addData('Presentation_image_f2_8.stopped', Presentation_image_f2_8.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doftwo repeats of 'ftwo_control_b3'
    
    
    # set up handler to look after randomisation of conditions etc
    fthree_control_b3 = data.TrialHandler(nReps=dofthree, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fthree_control_b3')
    thisExp.addLoop(fthree_control_b3)  # add the loop to the experiment
    thisFthree_control_b3 = fthree_control_b3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFthree_control_b3.rgb)
    if thisFthree_control_b3 != None:
        for paramName in thisFthree_control_b3:
            exec('{} = thisFthree_control_b3[paramName]'.format(paramName))
    
    for thisFthree_control_b3 in fthree_control_b3:
        currentLoop = fthree_control_b3
        # abbreviate parameter names if possible (e.g. rgb = thisFthree_control_b3.rgb)
        if thisFthree_control_b3 != None:
            for paramName in thisFthree_control_b3:
                exec('{} = thisFthree_control_b3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f3"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Presentation_image_f3_1.setImage(imageone)
        Presentation_image_f3_2.setImage(imagetwo)
        Presentation_image_f3_3.setImage(imagethree)
        Presentation_image_f3_4.setImage(imagefour)
        Presentation_image_f3_5.setImage(imagefive)
        Presentation_image_f3_6.setImage(imagesix)
        Presentation_image_f3_7.setImage(imageseven)
        Presentation_image_f3_8.setImage(imageeight)
        Presentation_image_f3_9.setImage(imagenine)
        Presentation_image_f3_10.setImage(imageten)
        Presentation_image_f3_11.setImage(imageeleven)
        Presentation_image_f3_12.setImage(imagetwelve)
        # keep track of which components have finished
        rsvp_f3Components = [Presentation_image_f3_1, Presentation_image_f3_2, Presentation_image_f3_3, Presentation_image_f3_4, Presentation_image_f3_5, Presentation_image_f3_6, Presentation_image_f3_7, Presentation_image_f3_8, Presentation_image_f3_9, Presentation_image_f3_10, Presentation_image_f3_11, Presentation_image_f3_12]
        for thisComponent in rsvp_f3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f3_1* updates
            if Presentation_image_f3_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_1.frameNStart = frameN  # exact frame index
                Presentation_image_f3_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_1.setAutoDraw(True)
            if Presentation_image_f3_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_1.tStartRefresh + 0.30-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_1.setAutoDraw(False)
            
            # *Presentation_image_f3_2* updates
            if Presentation_image_f3_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_2.frameNStart = frameN  # exact frame index
                Presentation_image_f3_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_2.setAutoDraw(True)
            if Presentation_image_f3_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_2.setAutoDraw(False)
            
            # *Presentation_image_f3_3* updates
            if Presentation_image_f3_3.status == NOT_STARTED and tThisFlip >= 0.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_3.frameNStart = frameN  # exact frame index
                Presentation_image_f3_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_3.setAutoDraw(True)
            if Presentation_image_f3_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_3.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_3.setAutoDraw(False)
            
            # *Presentation_image_f3_4* updates
            if Presentation_image_f3_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_4.frameNStart = frameN  # exact frame index
                Presentation_image_f3_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_4.setAutoDraw(True)
            if Presentation_image_f3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_4.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_4.setAutoDraw(False)
            
            # *Presentation_image_f3_5* updates
            if Presentation_image_f3_5.status == NOT_STARTED and tThisFlip >= 1.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_5.frameNStart = frameN  # exact frame index
                Presentation_image_f3_5.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_5, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_5.setAutoDraw(True)
            if Presentation_image_f3_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_5.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_5.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_5, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_5.setAutoDraw(False)
            
            # *Presentation_image_f3_6* updates
            if Presentation_image_f3_6.status == NOT_STARTED and tThisFlip >= 1.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_6.frameNStart = frameN  # exact frame index
                Presentation_image_f3_6.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_6, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_6.setAutoDraw(True)
            if Presentation_image_f3_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_6.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_6.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_6, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_6.setAutoDraw(False)
            
            # *Presentation_image_f3_7* updates
            if Presentation_image_f3_7.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_7.frameNStart = frameN  # exact frame index
                Presentation_image_f3_7.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_7, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_7.setAutoDraw(True)
            if Presentation_image_f3_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_7.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_7.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_7, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_7.setAutoDraw(False)
            
            # *Presentation_image_f3_8* updates
            if Presentation_image_f3_8.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_8.frameNStart = frameN  # exact frame index
                Presentation_image_f3_8.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_8, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_8.setAutoDraw(True)
            if Presentation_image_f3_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_8.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_8.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_8, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_8.setAutoDraw(False)
            
            # *Presentation_image_f3_9* updates
            if Presentation_image_f3_9.status == NOT_STARTED and tThisFlip >= 2.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_9.frameNStart = frameN  # exact frame index
                Presentation_image_f3_9.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_9, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_9.setAutoDraw(True)
            if Presentation_image_f3_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_9.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_9.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_9, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_9.setAutoDraw(False)
            
            # *Presentation_image_f3_10* updates
            if Presentation_image_f3_10.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_10.frameNStart = frameN  # exact frame index
                Presentation_image_f3_10.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_10, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_10.setAutoDraw(True)
            if Presentation_image_f3_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_10.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_10.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_10, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_10.setAutoDraw(False)
            
            # *Presentation_image_f3_11* updates
            if Presentation_image_f3_11.status == NOT_STARTED and tThisFlip >= 3.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_11.frameNStart = frameN  # exact frame index
                Presentation_image_f3_11.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_11, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_11.setAutoDraw(True)
            if Presentation_image_f3_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_11.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_11.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_11, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_11.setAutoDraw(False)
            
            # *Presentation_image_f3_12* updates
            if Presentation_image_f3_12.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_12.frameNStart = frameN  # exact frame index
                Presentation_image_f3_12.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_12, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_12.setAutoDraw(True)
            if Presentation_image_f3_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_12.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_12.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_12, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_12.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f3"-------
        for thisComponent in rsvp_f3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fthree_control_b3.addData('Presentation_image_f3_1.started', Presentation_image_f3_1.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_1.stopped', Presentation_image_f3_1.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_2.started', Presentation_image_f3_2.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_2.stopped', Presentation_image_f3_2.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_3.started', Presentation_image_f3_3.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_3.stopped', Presentation_image_f3_3.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_4.started', Presentation_image_f3_4.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_4.stopped', Presentation_image_f3_4.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_5.started', Presentation_image_f3_5.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_5.stopped', Presentation_image_f3_5.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_6.started', Presentation_image_f3_6.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_6.stopped', Presentation_image_f3_6.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_7.started', Presentation_image_f3_7.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_7.stopped', Presentation_image_f3_7.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_8.started', Presentation_image_f3_8.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_8.stopped', Presentation_image_f3_8.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_9.started', Presentation_image_f3_9.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_9.stopped', Presentation_image_f3_9.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_10.started', Presentation_image_f3_10.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_10.stopped', Presentation_image_f3_10.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_11.started', Presentation_image_f3_11.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_11.stopped', Presentation_image_f3_11.tStopRefresh)
        fthree_control_b3.addData('Presentation_image_f3_12.started', Presentation_image_f3_12.tStartRefresh)
        fthree_control_b3.addData('Presentation_image_f3_12.stopped', Presentation_image_f3_12.tStopRefresh)
        thisExp.nextEntry()
        
    # completed dofthree repeats of 'fthree_control_b3'
    
    
    # ------Prepare to start Routine "choice"-------
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
    choiceComponents = [Fixation_cross, Topleft, Topright, Bottomleft, Bottomright, key_resp]
    for thisComponent in choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice"-------
    while continueRoutine:
        # get current time
        t = choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choiceClock)
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
        for thisComponent in choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice"-------
    for thisComponent in choiceComponents:
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
    # the Routine "choice" was not non-slip safe, so reset the non-slip timer
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
    
    # ------Prepare to start Routine "Cross_and_control"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    dofone = 0 
    doftwo = 0
    dofthree = 0 
    
    if frequency == 1:
        dofone = 1
        doftwo = 0
        dofthree = 0
        
        
    elif frequency == 2:
        dofone = 0
        doftwo = 1
        dofthree = 0
        
        
    elif frequency == 3:
        dofone = 0
        doftwo = 0
        dofthree = 1
        
       
       
    # keep track of which components have finished
    Cross_and_controlComponents = [Crossm]
    for thisComponent in Cross_and_controlComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Cross_and_controlClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Cross_and_control"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Cross_and_controlClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Cross_and_controlClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Crossm* updates
        if Crossm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Crossm.frameNStart = frameN  # exact frame index
            Crossm.tStart = t  # local t and not account for scr refresh
            Crossm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Crossm, 'tStartRefresh')  # time at next scr refresh
            Crossm.setAutoDraw(True)
        if Crossm.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Crossm.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Crossm.tStop = t  # not accounting for scr refresh
                Crossm.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Crossm, 'tStopRefresh')  # time at next scr refresh
                Crossm.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Cross_and_controlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Cross_and_control"-------
    for thisComponent in Cross_and_controlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block_four.addData('Crossm.started', Crossm.tStartRefresh)
    block_four.addData('Crossm.stopped', Crossm.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    fone_control_b4 = data.TrialHandler(nReps=dofone, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fone_control_b4')
    thisExp.addLoop(fone_control_b4)  # add the loop to the experiment
    thisFone_control_b4 = fone_control_b4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFone_control_b4.rgb)
    if thisFone_control_b4 != None:
        for paramName in thisFone_control_b4:
            exec('{} = thisFone_control_b4[paramName]'.format(paramName))
    
    for thisFone_control_b4 in fone_control_b4:
        currentLoop = fone_control_b4
        # abbreviate parameter names if possible (e.g. rgb = thisFone_control_b4.rgb)
        if thisFone_control_b4 != None:
            for paramName in thisFone_control_b4:
                exec('{} = thisFone_control_b4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f1"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Presentation_image_f1_1.setImage(imageone)
        Presentation_image_f1_2.setImage(imagetwo)
        Presentation_image_f1_3.setImage(imagethree)
        Presentation_image_f1_4.setImage(imagefour)
        # keep track of which components have finished
        rsvp_f1Components = [Presentation_image_f1_1, Presentation_image_f1_2, Presentation_image_f1_3, Presentation_image_f1_4]
        for thisComponent in rsvp_f1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f1_1* updates
            if Presentation_image_f1_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_1.frameNStart = frameN  # exact frame index
                Presentation_image_f1_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_1.setAutoDraw(True)
            if Presentation_image_f1_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_1.setAutoDraw(False)
            
            # *Presentation_image_f1_2* updates
            if Presentation_image_f1_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_2.frameNStart = frameN  # exact frame index
                Presentation_image_f1_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_2.setAutoDraw(True)
            if Presentation_image_f1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_2.setAutoDraw(False)
            
            # *Presentation_image_f1_3* updates
            if Presentation_image_f1_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_3.frameNStart = frameN  # exact frame index
                Presentation_image_f1_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_3.setAutoDraw(True)
            if Presentation_image_f1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_3.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_3.setAutoDraw(False)
            
            # *Presentation_image_f1_4* updates
            if Presentation_image_f1_4.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f1_4.frameNStart = frameN  # exact frame index
                Presentation_image_f1_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f1_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f1_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f1_4.setAutoDraw(True)
            if Presentation_image_f1_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f1_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f1_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f1_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f1_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f1_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f1"-------
        for thisComponent in rsvp_f1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fone_control_b4.addData('Presentation_image_f1_1.started', Presentation_image_f1_1.tStartRefresh)
        fone_control_b4.addData('Presentation_image_f1_1.stopped', Presentation_image_f1_1.tStopRefresh)
        fone_control_b4.addData('Presentation_image_f1_2.started', Presentation_image_f1_2.tStartRefresh)
        fone_control_b4.addData('Presentation_image_f1_2.stopped', Presentation_image_f1_2.tStopRefresh)
        fone_control_b4.addData('Presentation_image_f1_3.started', Presentation_image_f1_3.tStartRefresh)
        fone_control_b4.addData('Presentation_image_f1_3.stopped', Presentation_image_f1_3.tStopRefresh)
        fone_control_b4.addData('Presentation_image_f1_4.started', Presentation_image_f1_4.tStartRefresh)
        fone_control_b4.addData('Presentation_image_f1_4.stopped', Presentation_image_f1_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed dofone repeats of 'fone_control_b4'
    
    
    # set up handler to look after randomisation of conditions etc
    ftwo_control_b4 = data.TrialHandler(nReps=doftwo, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ftwo_control_b4')
    thisExp.addLoop(ftwo_control_b4)  # add the loop to the experiment
    thisFtwo_control_b4 = ftwo_control_b4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFtwo_control_b4.rgb)
    if thisFtwo_control_b4 != None:
        for paramName in thisFtwo_control_b4:
            exec('{} = thisFtwo_control_b4[paramName]'.format(paramName))
    
    for thisFtwo_control_b4 in ftwo_control_b4:
        currentLoop = ftwo_control_b4
        # abbreviate parameter names if possible (e.g. rgb = thisFtwo_control_b4.rgb)
        if thisFtwo_control_b4 != None:
            for paramName in thisFtwo_control_b4:
                exec('{} = thisFtwo_control_b4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f2"-------
        continueRoutine = True
        routineTimer.add(3.950000)
        # update component parameters for each repeat
        Presentation_image_f2_1.setImage(imageone)
        Presentation_image_f2_2.setImage(imagetwo)
        Presentation_image_f2_3.setImage(imagethree)
        Presentation_image_f2_4.setImage(imagefour)
        Presentation_image_f2_5.setImage(imagefive)
        Presentation_image_f2_6.setImage(imagesix)
        Presentation_image_f2_7.setImage(imageseven)
        Presentation_image_f2_8.setImage(imageeight)
        # keep track of which components have finished
        rsvp_f2Components = [Presentation_image_f2_1, Presentation_image_f2_2, Presentation_image_f2_3, Presentation_image_f2_4, Presentation_image_f2_5, Presentation_image_f2_6, Presentation_image_f2_7, Presentation_image_f2_8]
        for thisComponent in rsvp_f2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f2_1* updates
            if Presentation_image_f2_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_1.frameNStart = frameN  # exact frame index
                Presentation_image_f2_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_1.setAutoDraw(True)
            if Presentation_image_f2_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_1.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_1.setAutoDraw(False)
            
            # *Presentation_image_f2_2* updates
            if Presentation_image_f2_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_2.frameNStart = frameN  # exact frame index
                Presentation_image_f2_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_2.setAutoDraw(True)
            if Presentation_image_f2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_2.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_2.setAutoDraw(False)
            
            # *Presentation_image_f2_3* updates
            if Presentation_image_f2_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_3.frameNStart = frameN  # exact frame index
                Presentation_image_f2_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_3.setAutoDraw(True)
            if Presentation_image_f2_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_3.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_3.setAutoDraw(False)
            
            # *Presentation_image_f2_4* updates
            if Presentation_image_f2_4.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_4.frameNStart = frameN  # exact frame index
                Presentation_image_f2_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_4.setAutoDraw(True)
            if Presentation_image_f2_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_4.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_4.setAutoDraw(False)
            
            # *Presentation_image_f2_5* updates
            if Presentation_image_f2_5.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_5.frameNStart = frameN  # exact frame index
                Presentation_image_f2_5.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_5, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_5.setAutoDraw(True)
            if Presentation_image_f2_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_5.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_5.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_5, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_5.setAutoDraw(False)
            
            # *Presentation_image_f2_6* updates
            if Presentation_image_f2_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_6.frameNStart = frameN  # exact frame index
                Presentation_image_f2_6.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_6, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_6.setAutoDraw(True)
            if Presentation_image_f2_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_6.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_6.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_6, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_6.setAutoDraw(False)
            
            # *Presentation_image_f2_7* updates
            if Presentation_image_f2_7.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_7.frameNStart = frameN  # exact frame index
                Presentation_image_f2_7.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_7, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_7.setAutoDraw(True)
            if Presentation_image_f2_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_7.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_7.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_7, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_7.setAutoDraw(False)
            
            # *Presentation_image_f2_8* updates
            if Presentation_image_f2_8.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f2_8.frameNStart = frameN  # exact frame index
                Presentation_image_f2_8.tStart = t  # local t and not account for scr refresh
                Presentation_image_f2_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f2_8, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f2_8.setAutoDraw(True)
            if Presentation_image_f2_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f2_8.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f2_8.tStop = t  # not accounting for scr refresh
                    Presentation_image_f2_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f2_8, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f2_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f2"-------
        for thisComponent in rsvp_f2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ftwo_control_b4.addData('Presentation_image_f2_1.started', Presentation_image_f2_1.tStartRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_1.stopped', Presentation_image_f2_1.tStopRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_2.started', Presentation_image_f2_2.tStartRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_2.stopped', Presentation_image_f2_2.tStopRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_3.started', Presentation_image_f2_3.tStartRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_3.stopped', Presentation_image_f2_3.tStopRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_4.started', Presentation_image_f2_4.tStartRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_4.stopped', Presentation_image_f2_4.tStopRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_5.started', Presentation_image_f2_5.tStartRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_5.stopped', Presentation_image_f2_5.tStopRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_6.started', Presentation_image_f2_6.tStartRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_6.stopped', Presentation_image_f2_6.tStopRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_7.started', Presentation_image_f2_7.tStartRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_7.stopped', Presentation_image_f2_7.tStopRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_8.started', Presentation_image_f2_8.tStartRefresh)
        ftwo_control_b4.addData('Presentation_image_f2_8.stopped', Presentation_image_f2_8.tStopRefresh)
        thisExp.nextEntry()
        
    # completed doftwo repeats of 'ftwo_control_b4'
    
    
    # set up handler to look after randomisation of conditions etc
    fthree_control_b4 = data.TrialHandler(nReps=dofthree, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='fthree_control_b4')
    thisExp.addLoop(fthree_control_b4)  # add the loop to the experiment
    thisFthree_control_b4 = fthree_control_b4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFthree_control_b4.rgb)
    if thisFthree_control_b4 != None:
        for paramName in thisFthree_control_b4:
            exec('{} = thisFthree_control_b4[paramName]'.format(paramName))
    
    for thisFthree_control_b4 in fthree_control_b4:
        currentLoop = fthree_control_b4
        # abbreviate parameter names if possible (e.g. rgb = thisFthree_control_b4.rgb)
        if thisFthree_control_b4 != None:
            for paramName in thisFthree_control_b4:
                exec('{} = thisFthree_control_b4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "rsvp_f3"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        Presentation_image_f3_1.setImage(imageone)
        Presentation_image_f3_2.setImage(imagetwo)
        Presentation_image_f3_3.setImage(imagethree)
        Presentation_image_f3_4.setImage(imagefour)
        Presentation_image_f3_5.setImage(imagefive)
        Presentation_image_f3_6.setImage(imagesix)
        Presentation_image_f3_7.setImage(imageseven)
        Presentation_image_f3_8.setImage(imageeight)
        Presentation_image_f3_9.setImage(imagenine)
        Presentation_image_f3_10.setImage(imageten)
        Presentation_image_f3_11.setImage(imageeleven)
        Presentation_image_f3_12.setImage(imagetwelve)
        # keep track of which components have finished
        rsvp_f3Components = [Presentation_image_f3_1, Presentation_image_f3_2, Presentation_image_f3_3, Presentation_image_f3_4, Presentation_image_f3_5, Presentation_image_f3_6, Presentation_image_f3_7, Presentation_image_f3_8, Presentation_image_f3_9, Presentation_image_f3_10, Presentation_image_f3_11, Presentation_image_f3_12]
        for thisComponent in rsvp_f3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        rsvp_f3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "rsvp_f3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = rsvp_f3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=rsvp_f3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Presentation_image_f3_1* updates
            if Presentation_image_f3_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_1.frameNStart = frameN  # exact frame index
                Presentation_image_f3_1.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_1, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_1.setAutoDraw(True)
            if Presentation_image_f3_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_1.tStartRefresh + 0.30-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_1.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_1, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_1.setAutoDraw(False)
            
            # *Presentation_image_f3_2* updates
            if Presentation_image_f3_2.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_2.frameNStart = frameN  # exact frame index
                Presentation_image_f3_2.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_2, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_2.setAutoDraw(True)
            if Presentation_image_f3_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_2.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_2, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_2.setAutoDraw(False)
            
            # *Presentation_image_f3_3* updates
            if Presentation_image_f3_3.status == NOT_STARTED and tThisFlip >= 0.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_3.frameNStart = frameN  # exact frame index
                Presentation_image_f3_3.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_3, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_3.setAutoDraw(True)
            if Presentation_image_f3_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_3.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_3.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_3, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_3.setAutoDraw(False)
            
            # *Presentation_image_f3_4* updates
            if Presentation_image_f3_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_4.frameNStart = frameN  # exact frame index
                Presentation_image_f3_4.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_4, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_4.setAutoDraw(True)
            if Presentation_image_f3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_4.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_4.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_4, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_4.setAutoDraw(False)
            
            # *Presentation_image_f3_5* updates
            if Presentation_image_f3_5.status == NOT_STARTED and tThisFlip >= 1.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_5.frameNStart = frameN  # exact frame index
                Presentation_image_f3_5.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_5, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_5.setAutoDraw(True)
            if Presentation_image_f3_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_5.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_5.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_5, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_5.setAutoDraw(False)
            
            # *Presentation_image_f3_6* updates
            if Presentation_image_f3_6.status == NOT_STARTED and tThisFlip >= 1.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_6.frameNStart = frameN  # exact frame index
                Presentation_image_f3_6.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_6, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_6.setAutoDraw(True)
            if Presentation_image_f3_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_6.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_6.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_6, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_6.setAutoDraw(False)
            
            # *Presentation_image_f3_7* updates
            if Presentation_image_f3_7.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_7.frameNStart = frameN  # exact frame index
                Presentation_image_f3_7.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_7, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_7.setAutoDraw(True)
            if Presentation_image_f3_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_7.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_7.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_7, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_7.setAutoDraw(False)
            
            # *Presentation_image_f3_8* updates
            if Presentation_image_f3_8.status == NOT_STARTED and tThisFlip >= 2.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_8.frameNStart = frameN  # exact frame index
                Presentation_image_f3_8.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_8, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_8.setAutoDraw(True)
            if Presentation_image_f3_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_8.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_8.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_8, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_8.setAutoDraw(False)
            
            # *Presentation_image_f3_9* updates
            if Presentation_image_f3_9.status == NOT_STARTED and tThisFlip >= 2.70-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_9.frameNStart = frameN  # exact frame index
                Presentation_image_f3_9.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_9, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_9.setAutoDraw(True)
            if Presentation_image_f3_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_9.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_9.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_9, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_9.setAutoDraw(False)
            
            # *Presentation_image_f3_10* updates
            if Presentation_image_f3_10.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_10.frameNStart = frameN  # exact frame index
                Presentation_image_f3_10.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_10, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_10.setAutoDraw(True)
            if Presentation_image_f3_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_10.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_10.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_10, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_10.setAutoDraw(False)
            
            # *Presentation_image_f3_11* updates
            if Presentation_image_f3_11.status == NOT_STARTED and tThisFlip >= 3.35-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_11.frameNStart = frameN  # exact frame index
                Presentation_image_f3_11.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_11, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_11.setAutoDraw(True)
            if Presentation_image_f3_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_11.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_11.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_11, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_11.setAutoDraw(False)
            
            # *Presentation_image_f3_12* updates
            if Presentation_image_f3_12.status == NOT_STARTED and tThisFlip >= 3.7-frameTolerance:
                # keep track of start time/frame for later
                Presentation_image_f3_12.frameNStart = frameN  # exact frame index
                Presentation_image_f3_12.tStart = t  # local t and not account for scr refresh
                Presentation_image_f3_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Presentation_image_f3_12, 'tStartRefresh')  # time at next scr refresh
                Presentation_image_f3_12.setAutoDraw(True)
            if Presentation_image_f3_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Presentation_image_f3_12.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    Presentation_image_f3_12.tStop = t  # not accounting for scr refresh
                    Presentation_image_f3_12.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Presentation_image_f3_12, 'tStopRefresh')  # time at next scr refresh
                    Presentation_image_f3_12.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in rsvp_f3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "rsvp_f3"-------
        for thisComponent in rsvp_f3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fthree_control_b4.addData('Presentation_image_f3_1.started', Presentation_image_f3_1.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_1.stopped', Presentation_image_f3_1.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_2.started', Presentation_image_f3_2.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_2.stopped', Presentation_image_f3_2.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_3.started', Presentation_image_f3_3.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_3.stopped', Presentation_image_f3_3.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_4.started', Presentation_image_f3_4.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_4.stopped', Presentation_image_f3_4.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_5.started', Presentation_image_f3_5.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_5.stopped', Presentation_image_f3_5.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_6.started', Presentation_image_f3_6.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_6.stopped', Presentation_image_f3_6.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_7.started', Presentation_image_f3_7.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_7.stopped', Presentation_image_f3_7.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_8.started', Presentation_image_f3_8.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_8.stopped', Presentation_image_f3_8.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_9.started', Presentation_image_f3_9.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_9.stopped', Presentation_image_f3_9.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_10.started', Presentation_image_f3_10.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_10.stopped', Presentation_image_f3_10.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_11.started', Presentation_image_f3_11.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_11.stopped', Presentation_image_f3_11.tStopRefresh)
        fthree_control_b4.addData('Presentation_image_f3_12.started', Presentation_image_f3_12.tStartRefresh)
        fthree_control_b4.addData('Presentation_image_f3_12.stopped', Presentation_image_f3_12.tStopRefresh)
        thisExp.nextEntry()
        
    # completed dofthree repeats of 'fthree_control_b4'
    
    
    # ------Prepare to start Routine "choice"-------
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
    choiceComponents = [Fixation_cross, Topleft, Topright, Bottomleft, Bottomright, key_resp]
    for thisComponent in choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "choice"-------
    while continueRoutine:
        # get current time
        t = choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choiceClock)
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
        for thisComponent in choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice"-------
    for thisComponent in choiceComponents:
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
    # the Routine "choice" was not non-slip safe, so reset the non-slip timer
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
