#! /usr/bin/python

import os.path
import shutil
import re
import string
import time
import os.path
import os

home = "/home/cedric/"
showroot = home + "video/series/"
newshows = showroot + "torrents/"
badshows = []

class UnsortedFile:
	def __init__(self, filename, filepath):
		self.filename = filename
		self.filepath = filepath
		self.showName = ""

	def isTvShowEpisode(self):
		numberobj = re.search("^.+\.[Ss][0-9]{1,2}[Ee][0-9]{1,2}.*\.(avi|mkv|mp4)$", self.filename)
		print self.filename
		if numberobj:
			print "true"
			return True;
		print "false"
		return False;
	
	def extractShowName(self):
	 	splitobj = re.split("\.[Ss][0-9]{1,2}[Ee][0-9]{1,2}", self.filename)
 		self.showName = string.replace(splitobj[0], ".", " ")
 		return self.showName
 		
 	def extractSeasonNumber(self):
 		numberobj = re.search("[Ss][0-9]{1,2}", self.filename)
 		self.seasonNumber = string.replace(numberobj.group(0), "S", "")
 		self.seasonNumber = string.atoi(string.replace(self.seasonNumber, "s", ""))
 		return self.seasonNumber
 		
 	def fileFullPath(self):
 		return self.filepath + "/" + self.filename
 		
class ShowFinder:
 	def __init__(self, showname, season):
 		self.showname = showname
 		self.season = season
 		
 	def showpath(self):
 		return showroot + self.showname + "/"
 		
 	def seasonpath(self):
 		return self.showpath() + "Saison " + str(self.season) + "/"
 	
 	def existsShowFolder(self):
 		return os.path.isdir(self.showpath());
 		
 	def existsSeasonFolder(self):
 		return os.path.isdir(self.seasonpath())
 		
 	def createShowFolder(self):
 		os.mkdir(self.showpath())
 		
 	def createSeasonFolder(self):
 		os.mkdir(self.seasonpath())
 		
 	def createNecessaryFolders(self):
 		if not(self.existsShowFolder()):
 			self.createShowFolder()
 			print "creating folder:", self.showname
 		if not(self.existsSeasonFolder()):
 			print "creating season folder:", self.season
 			self.createSeasonFolder()
 			
class NewEpisodesFinder:
	def __init__(self, showLocation):
		self.showLocation = showLocation
		
	def listNewEpisodes(self):
		unsortedEpisodes = []
		for root, dirs, files in os.walk(self.showLocation):
			for file in files:
				unsortedEpisode = UnsortedFile(file, root)
				if unsortedEpisode.isTvShowEpisode():
					unsortedEpisodes.append(unsortedEpisode)
		return unsortedEpisodes

	def sortNewEpisodes(self):
		unsortedEpisodes = self.listNewEpisodes()
		for ep in unsortedEpisodes:
			showfinder = ShowFinder(ep.extractShowName(), ep.extractSeasonNumber())
			showfinder.createNecessaryFolders()
			print ep.fileFullPath(), "=>", showfinder.seasonpath()
			shutil.move(ep.fileFullPath(), showfinder.seasonpath())

NewEpisodesFinder(newshows).sortNewEpisodes()
