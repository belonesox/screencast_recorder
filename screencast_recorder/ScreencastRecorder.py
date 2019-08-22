#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Time 4 Files

  Copy all files from given directory,
  trying extract creation time,
  and append this time info to
"""
from __future__ import print_function
import sys
import os
import optparse
import time
import shutil
import Xlib
import Xlib.display
#import MiscUtils as ut


class ScreenCastMe(object):
    """
    Main class for all commands
    """
    version__ = "01.01"

    def __init__(self):
        """Set up and parse command line options"""
        usage = "Usage: %prog [options] <source directory>"
        self.resolution = Xlib.display.Display().screen().root.get_geometry()
        #
        #self.parser = optparse.OptionParser(usage)
        #
        #self.parser.add_option('-d', '--directory',
        #                       dest='build_directory',
        #                       action='store_true',
        #                       default=False,
        #                       metavar="",
        #                       help="Build Time Directory for files")
        #
        #
        #self.options, self.args = self.parser.parse_args()
        self.homedir = os.getcwd()
        self.screendir = os.path.join(os.getcwd(), 'screencasts')
        if not os.path.exists(self.screendir):
            os.mkdir(self.screendir)

    def process(self):
        """
        Main entry point.
        Process command line options, call appropriate logic.
        """
        print(' '.join(['"' + arg + '"' for arg in sys.argv]))

        #if len(sys.argv) < 2:
        #    print "Please, specify source directory"
        #    sys.exit(0)

        while True:
            newfilename = time.strftime("%Y-%m-%d-%H-%M-%S.flv", time.localtime())
            screenpath = os.path.join(self.screendir, newfilename) 
    
            scmd = ('nice -n 19 '
                   ' ffmpeg -y -f x11grab -r 8 '
                   '-s ' + str(self.resolution.width) + 'x' + str(self.resolution.height) +
                   ' -i :0.0 -f alsa -i pulse -ab 256K -ar 44100 '
                   '-vcodec libx264 -preset ultrafast -qmin 2 -qmax 4  -vsync 1 '
                   ' -f flv '
                   + screenpath)
        
            print(scmd)
            os.system(scmd)


def main():
    """
     Start procedure
    """
    processor = ScreenCastMe()
    processor.process()

if __name__ == '__main__':
    main()
