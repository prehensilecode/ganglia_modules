# temperature
Since ipmitool read requires root access, kludge it by 
running a root cron job which writes a single temperature
value to a world-readable log file.

The gmond module then reads this value.

# TODO
Probably want to use a metric name without whitespace.

