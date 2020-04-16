#Simple configuration file for pymysqlhps utility
interval=5 #seconds between processlist requerying
#Number of snapshot to rotate. Please set to reasonable depth
rotate=1000
#Whether snaphot creating module should print anything to console
verbose=False
#Whether snaphot creating module should print anything to log file
verboselog=True
#Logfile name. If verboselog is True, this file fil have both log of snapshot creating and viewing tools
logfile='/var/log/pymysqlhps/messages'
#Mysql access settings
mysqlpasswd=""
mysqluser="root"
mysqlhost="127.0.0.1"
#my.cnf file to read pasword from, it can be used for obtaining password if this variable is not empty
#password will be taen from first 'password=' line in this file. Overrides mysqlpasswd variable.
#To ise above mentioned mysql access settings, set mycnf to empty string ('')
mycnf="/root/.my.cnf"
#if "vertical" is True, print text formatted in the way mysql does with "\G"
vertical=True
#column list to select. This parameter is required if "vertical" is True
columns='ID,TIME,COMMAND,State,MAX_MEMORY_USED,info'
#query used to check processlist
#Warning. This query is written for Mariadb 10.4, please adjust it for other versions if required
monitorquery='select '+columns+' from INFORMATION_SCHEMA.PROCESSLIST ORDER BY TIME ASC;'
#monitorquery='select '+columns+' from INFORMATION_SCHEMA.PROCESSLIST WHERE Info IS NOT NULL AND Info NOT LIKE "%PROCESSLIST%" ORDER BY TIME ASC;'
snapdirectory="/var/log/sqlstats/"
#viewer will try to process files with following mask:
filemask=".*[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}.*.log"
