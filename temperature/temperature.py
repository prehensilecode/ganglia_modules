#!/usr/bin/env python
import os
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(name)s - %(levelname)s\t Thread-%(thread)d - %(message)s")
logging.debug('starting up')

descriptors = []


def get_temp(component_temp):
    if component_temp == 'Inlet Temperature':
        inlet_temp = 0
        inlet_temp_file = "/var/log/inlet_temp"
        with open(inlet_temp_file, 'r') as f:
            inlet_temp = f.read()
    
        return int(inlet_temp)


def metric_init(params={}):
    global descriptors

    logging.debug('init: ' + str(params))
    
    inlettemp = {'name': 'Inlet Temperature',
            'call_back': get_temp,
            'time_max': 90,
            'value_type': 'uint',
            'units': 'C',
            'format': '%u',
            'description': 'Inlet temperature of host through IPMI',
            'groups': 'temperature'}

    descriptors = [inlettemp]
    return descriptors


def metric_cleanup():
    logging.shutdown()


if __name__ == '__main__':
    logging.debug('running interactively')

    metric_init()
    for d in descriptors:
        v = d['call_back'](d['name'])
        print('value for %s is %u' % (d['name'], v))

