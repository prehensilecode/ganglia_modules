#!/bin/bash
### log file needs to be world-readable since gmond runs as nobody
umask 0022
IPMITOOL=/mnt/HA/sysadmin/bin/ipmitool
INLETTEMPLOG=/var/log/inlet_temp

if [ $(echo ${HOSTNAME} | grep "^ac") ]
then
    ${IPMITOOL} -c sdr get "FCB Ambient1" | cut -f2 -d, > $INLETTEMPLOG
elif [ ${HOSTNAME} = "proteusa01" ]
then
    ${IPMITOOL} -c sdr get "Ambient Temp" | cut -f2 -d, > $INLETTEMPLOG
else
    ${IPMITOOL} -c sdr get "Inlet Temp" | cut -f2 -d, > $INLETTEMPLOG
fi

