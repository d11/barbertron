#!/usr/bin/env python
import subprocess
from pyechonest import config,track
from secrets import echoNestSecrets

config.ECHO_NEST_API_KEY = echoNestSecrets['API_KEY']

def generateControlFile(inputFile, barbershopID):
  controlFilename = "control-"+ barbershopID + ".txt"
  
  uploadedTrack = track.track_from_filename(inputFile)
  key_offset = uploadedTrack.key - 6
  #audioKeyConfidence = uploadedTrack.key_confidence
  #audioBarCount = uploadedTrack.bars.count()
  
  # generate chord progression
  with open(controlFilename, "w+") as controlFile:

    # test, go up in whole tones
    for t in xrange(1,4):
      controlFile.write("%f %i %i\n" % (t*2.0, key_offset + 54 + 3 * t, 117 ))
      controlFile.write("%f %i %i\n" % (t*2.0, key_offset + 59 + 3 * t, 117 ))
      controlFile.write("%f %i %i\n" % (t*2.0, key_offset + 64 + 3 * t, 117 ))
  
  return controlFilename


def doBarberShopping(inputFile, outputFile, barbershopID):
  controlFilename = generateControlFile(inputFile, barbershopID)
  subprocess.call(["./barberism", "./patch.pd", inputFile, controlFilename, outputFile])

