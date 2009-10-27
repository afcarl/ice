#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

import os, sys

path = [ ".", "..", "../..", "../../..", "../../../.." ]
head = os.path.dirname(sys.argv[0])
if len(head) > 0:
    path = [os.path.join(head, p) for p in path]
path = [os.path.abspath(p) for p in path if os.path.exists(os.path.join(p, "scripts", "TestUtil.py")) ]
if len(path) == 0:
    raise "can't find toplevel directory!"
sys.path.append(os.path.join(path[0]))
from scripts import *

testdir = os.getcwd()
router = TestUtil.getGlacier2Router()

args = ' --Glacier2.RoutingTable.MaxSize=10' + \
       ' --Glacier2.Client.Endpoints="default -p 12347"' + \
       ' --Ice.Admin.Endpoints="tcp -h 127.0.0.1 -p 12348"' + \
       ' --Ice.Admin.InstanceName=Glacier2' + \
       ' --Glacier2.CryptPasswords="' + os.path.join(testdir, "passwords")  + '"'

print "starting router...",
starterProc = TestUtil.startServer(router, args, count=2)
print "ok"

TestUtil.clientServerTest()

starterProc.waitTestSuccess()

