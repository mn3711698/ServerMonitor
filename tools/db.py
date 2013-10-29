#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import Connection

con = Connection()
db = con.ServerMonitor

def documents():
    """
    return documents form mongodb one time
    """
    temperatures = db.temperature
    server = db.server
    location = db.location

    return temperatures, server, location
