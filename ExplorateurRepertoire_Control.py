# -*- coding: utf-8 -*-
#! /usr/bin/python3

# ----------------------------------------------------
# Script''Explorateur de Repertoire'
# ----------------------------------------------------

# Par ''Alban MARTEL''
# Courriel : albanmartel(POINT)developpeur(AT)gmail(POINT)com
# License : GNU GPL
# Ce script permet d'explorer les répertoires


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListView, QWidget
from UIExplorateurRepertoire import Ui_Forms
import os
from os import path

class SystemFileAndDirectoryExplorer(object):
    def __init__(self):
        self.highestLevelDirectory = None
        self.findHighesstLevelDirectory()

    def findHighesstLevelDirectory(self):
        findH = os.getcwd()
        parentDirectory = path.dirname(findH)
        while parentDirectory != path.dirname(parentDirectory):
            parentDirectory = path.dirname(parentDirectory)
        self.highestLevelDirectory = parentDirectory
            
    def getHighestLevelDirectory(self):
        return self.highestLevelDirectory


class Control(Ui_Forms , SystemFileAndDirectoryExplorer, QWidget):
    """Class pour controler la vue"""
    def __init__(self):
        Ui_Forms.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)

        self.explorerFD = SystemFileAndDirectoryExplorer()

        self.listFolders = []
        self.index = 0
        self.path = []
        self.listFiles = []
        self.initPath()

        """ Call methods with buttons """
        self.pushButton_3.clicked.connect(self.submitOk)
        self.pushButton_4.clicked.connect(self.submitPrevious)
        self.pushButton_5.clicked.connect(self.submitParent)
        self.pushButton_6.clicked.connect(self.submitNext)
        self.lineEdit.returnPressed.connect(self.submitEnter)
        self.listWidget.itemClicked.connect(self.submitClickedItem)
        
        #self.lineEdit.dropEvent(self.submitDropEvent)
   
        self.showMaximized()
        

    def initPath(self):
        initPath = self.explorerFD.getHighestLevelDirectory()
        self.readFoldersAndFiles(initPath)
        self.displayListView(initPath)
        bouton = QtWidgets.QPushButton()
        bouton.setText("Valider")


    def readFoldersAndFiles(self, path):
        """
        Read Folders and File od a precise path
        Réinitialiser à zéro self.listFolders et self.ListFiles = []
        """

        self.path.append(path)
        
        self.listFolders = None
        self.listFiles = None
        self.listFolders = []
        self.listFiles = []
        
        listFoldersAndFiles = os.listdir(path)        
        for element in listFoldersAndFiles:            
            if os.path.isdir(path + "/" + element):
                self.listFolders.append(element)
            else:
                self.listFiles.append(element)
                
    def updateFoldersAndFiles(self, path):
        if self.path[len(self.path) -1] != path :
            self.readFoldersAndFiles(path)
            self.displayListView(path)
            self.path.append(path)
            self.index = self.index + 1
            

    def displayListView(self, path):

        self.lineEdit.setText(path)
        self.updateFoldersAndFiles(path)

        self.listWidget.clear()


        listFolders = sorted(self.listFolders)
        listFiles = sorted(self.listFiles)

    
        for element in listFolders:                
            itm = QtWidgets.QListWidgetItem(element);
            icon = QtGui.QIcon.fromTheme("folder_alban" ,QtGui.QIcon("icones/folder.svg"))
            itm.setIcon(icon)
            self.listWidget.addItem(itm)
            

        for element in listFiles:                


            itm = QtWidgets.QListWidgetItem(element);
            icon = QtGui.QIcon.fromTheme("document_alban" ,QtGui.QIcon("icones/document.svg"))
            itm.setIcon(icon)
            self.listWidget.addItem(itm)

        

        
    def submitPath(self, path):
        if os.path.isdir(path):
            self.updateFoldersAndFiles(path)
        else:
            path = os.path.dirname(path)
            self.lineEdit.setText(path)
            if path == '' :
                self.lineEdit.setText(self.path[len(self.path) -1])
                path = self.path[len(self.path) -1]
            self.submitPath(path)   


    def submitOk(self):
        path = self.lineEdit.text()
        self.submitPath(path)


    def submitParent(self):
        path = os.path.dirname(self.lineEdit.text())
        self.submitPath(path)

        
    def submitPrevious(self):
        if self.index -1 > -1:
            self.index = self.index - 1
        self.submitPath(self.path[self.index])
        

    def submitNext(self):        
        if self.index + 1 < len(self.path):
            self.index = self.index + 1
        self.submitPath(self.path[self.index])


    def submitEnter(self):
        self.submitOk()

    #Not implement
    def submitDropEvent(self):
        print(self.lineEdit.text())

    def submitClickedItem(self, item):
        path =  "/" + item.text()
        if self.lineEdit.text() != self.explorerFD.getHighestLevelDirectory():
            path = self.lineEdit.text() + "/" + item.text()
        print(path)
        self.lineEdit.setText(path)
        self.submitOk()

    def keyPressEvent(self, e):    
            
        if e.key() == Qt.Key_Left:
            self.submitPrevious()
        
        if e.key() == Qt.Key_Right:
            self.submitNext()

        #Not implement
        if e.key() == Qt.Key_Return:
            print("Return")

        #Not implement
        if e.key() == Qt.Key_Enter:
            print("Enter")







        

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    control = Control()
    sys.exit(app.exec_())
 
