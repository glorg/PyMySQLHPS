#!/usr/bin/env python3
# This module contains common procedures used for both viewer and process state dumping parts
# License GNU Public License GPL-2.0 http://opensource.org/licenses/gpl-2.0
# Created by Eugene K., 2019-2020

def logline(verbose,verboselog,logfile,message,eol):
#verbose,verboselog,logfile,oel: boolean
#verbose: print to console
#verboselog: prit to file
#eol: whether to put newline after message
    errtext=''
    if verboselog:
        try:
            logfile=open(logfile,"a")
            if eol:
                print("%s" % message,file=logfile)
            else:
                print("%s" % message, end = '',file=logfile)
            logfile.close()
        except Exception as e:
#incorrect logging should not affect application.
            errtext=format(e)
    if verbose:
        try:
            if eol:
                print("%s" % message)
            else:
                print("%s" % message, end = '')
        except Exception as e:
#incorrect logging should not affect application.
            errtext=format(e)
    return(errtext)
