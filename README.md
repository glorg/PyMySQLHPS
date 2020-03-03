# PyMySQLHPS

pymysqlhps - Python-written script for Htop-like MySQL processlist monitoring

## What this tool does

This monitoring tool can be useful if you are looking for some kind of SQL query that sometimes creates unwanted issues (for example, garbage in database or performance issues) and can't or don't want to simply dump all the queries into one large log file but what to browse processlist statuses in historical order

## How this tool works

The tool has two components: 
* daemon (pymysqlhps.py) part that should run in the background. It will connect to MySQL, take processlist snapshots in certain periods and save them into configured directory. On startup it writes snapshots to the directory set in settings.py file and also appends file named sqlprocesses.briefs.log containing statistics.
At the moment script can;t daemonize and rotate snapshots itself yet, so you have to start it in, for example, screen.
* viewer part (pyhpsviewer.py, that is in fact curses interface) for browsing processlist snapshots. One can start viewer with _./pyhpsviewer.py_ command and browse processlists. You can also point specific moment you want to see in the form of

./pyhpsviewer.py 2020-02-20-23-59

Last matching snapshot available will be opened. If you are not sure that snapshot was taken in particular time, shorten down mask passed as agrument. If no mask is given or mask doesn't match anything, last available processlist will be displayed.
You can use arrow keys to scroll processlist (left and right will open previous/next), use 'q' or 'esc' key to exit.

## Required python modules:
* pymysql
* hashlib
* curses
