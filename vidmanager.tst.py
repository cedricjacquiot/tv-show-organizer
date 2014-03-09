#! /usr/bin/python

import unittest
import vidmanager


class TestSequenceFunctions(unittest.TestCase):

################# correct file type #################	
	def test_correctShowNameAvi(self):
 		self.nameTesting("toto.S03E01.loltv.avi", True)
 		
 	def test_correctShowNameMkv(self):
 		self.nameTesting("glop.flop.S11E02.loltv.mkv", True)
 		
 	def test_correctShowNamemp4(self):
 		self.nameTesting("mp4test.S01E50.loltv.mp4", True)
 		
 	def test_incorrectShowNameMissingSeason(self):
 		self.nameTesting("mp4test.E50.loltv.mp4", False)
 		
 	def test_incorrectShowNameMissingEpisode(self):
 		self.nameTesting("montest.S01.avi", False)
 		
 	def test_incorrectShowNameWrongExtension(self):
 		self.nameTesting("montest.tot", False)
 		
 	def test_incorrectShowNameNoExtension(self):
 		self.nameTesting("montest", False)
 		
 	def test_incorrectShowNameNoName(self):
 		self.nameTesting("S01E01.avi", False)
 		
################# Name extraction #################
 		
 	def test_showNameExtracted(self):
 		self.showNameFinding("monshow.S01E01.avi", "monshow")
 		
 	def test_showNameCompositeExtracted(self):
 		self.showNameFinding("Teen.Wolf.S02E01.HDTV.x264-2HD.mp4", "Teen Wolf")
 		
################# Season extraction #################
 
	def test_seasonNumberExtracted(self):
		unsortedFile = vidmanager.UnsortedFile("Teen.Wolf.S02E02.HDTV.x264-2HD.mp4", "toto")
		unsortedFile.extractSeasonNumber()
		self.assertEqual(unsortedFile.seasonNumber, 2)
		
################# Exist show finder #################

	def test_showFolderExists(self):
		showFinder = vidmanager.ShowFinder("Teen Wolf", 1)
		self.assertTrue(showFinder.existsShowFolder())
		self.assertTrue(showFinder.existsSeasonFolder())
		
	
	def test_showFolderNotExists(self):
		showFinder = vidmanager.ShowFinder("Teen blop", 1)
		self.assertFalse(showFinder.existsShowFolder())
		
		
	def test_showFolderNotExists(self):
		showFinder = vidmanager.ShowFinder("Teen Wolf", 25)
		self.assertFalse(showFinder.existsSeasonFolder())

################# Helper functions #################
 	def showNameFinding(self, filename, expectedName):
 		unsortedFile = vidmanager.UnsortedFile(filename, "toto")
 		unsortedFile.extractShowName()
 		self.assertEqual(unsortedFile.showName, expectedName)
 		
 	def nameTesting(self, filename, isOk):
 		unsortedFile = vidmanager.UnsortedFile(filename, "toto")
 		self.assertEqual(unsortedFile.isTvShowEpisode(), isOk)
 		
 		
suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)