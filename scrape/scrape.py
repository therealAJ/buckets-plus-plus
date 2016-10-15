# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 12:08:49 2016

@author: Alex
"""

import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html 
from bs4 import BeautifulSoup
from lxml.etree import tostring

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

url = 'http://www.masseyratings.com/nba/ratings'  
r = Render(url)  
result = r.frame.toHtml()

text_file = open('output.html', 'w')
text_file.write(result)


