#!/usr/bin/env python3

# License GNU Public License GPL-2.0 http://opensource.org/licenses/gpl-2.0
# Created by Eugene K., 2019-2020
import pymysql
import datetime
import os
import time
import hashlib
from settings import *
from commons import *

while True:
#read passowrd from .my.cnf
    if len(mycnf.strip()) > 0 :
        mycnffile = open(mycnf, 'r')
        lines = mycnffile.readlines()
        for l in lines:
            if 'password' in l:
                mysqlpasswd=l.split('=')[1].replace('"', '').rstrip("\n\r")
        mycnffile.close()
#ensure configured log directory exists
    if not os.path.exists(snapdirectory):
        os.makedirs(snapdirectory)
#if "vertical" is set, parse columns
    column=columns.split(',')
    header_lenmax=len(max(column, key=len))
    try:
#establish mysql connection, it will NOT be closed while script is running
        connection = pymysql.connect(host=mysqlhost, user=mysqluser, password=mysqlpasswd)
#open brief statistics file containint timestamp, number or running queries and time to fetch processlist
        stfile=snapdirectory+"sqlprocesses.briefs.log"
        stf=open(stfile,"a")
#get my PID ant print header
        me=os.getpid()
        print(logline(verbose,verboselog,logfile,"Started monitor with PID %i"%me,True))
        print("#monitor PID:%i"%me,file=stf)
        print("#Date-time\t\ttime to fetch, uS\tnumber of rows\tlongest running query time, S",file=stf)
    #try:
        while True:
#get time...
            hrtstamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            logline(verbose,verboselog,logfile,"Snapshot at %s... " % hrtstamp,False)
            filesuffix=hashlib.md5(hrtstamp.encode('utf-8')).hexdigest()[0:10]
            fname=snapdirectory+"sqlprocesses-"+hrtstamp+"."+filesuffix+".log"
            t1=datetime.datetime.now()
#execute SQL query
            cursor=connection.cursor()
            cursor.execute(monitorquery)
            connection.commit()
#measire elapsed time
            t2=datetime.datetime.now()
            td=t2-t1
            nr=cursor.rowcount
            if nr > 0:
#open STAMP files, print results...
                fsf=open(fname,"a")
                for row in cursor.fetchall():
                    if not vertical:
                        for i in range(0,len(row)-1):
                            print("%s\t" % row[i], end = '',file=fsf)
                        print("\t\t%s" % row[len(row)-1],file=fsf)
                    else:
                        for i in range(0,len(row)):
                            print( "%s : %s" % ('{0: >{l}}'.format(column[i],l=header_lenmax),row[i]),file=fsf)
                        print('*******************************************************************',file=fsf)
                    maxtime=row[1]
                fsf.close()
                print("%s\t%s\t\t\t%i\t\t%s" % (hrtstamp,str(round(1000000*td.total_seconds())),nr,maxtime),file=stf)
                stf.flush()
            logline(verbose,verboselog,logfile,"done.",True)
            time.sleep(interval)
    except pymysql.Error as e:
        logline(verbose,verboselog,logfile,"%s" % format(e),True)
        logline(verbose,verboselog,logfile,"...could not query sql processes, will sleep for %d seconds..." % interval,True)
        time.sleep(interval)
    except Exception as e:
        logline(verbose,verboselog,logfile,"%s" % format(e),True)
        logline(verbose,verboselog,logfile,"unknown error or user interrupt received...",True)
        connection.close()
        stf.close()
    #    exit
