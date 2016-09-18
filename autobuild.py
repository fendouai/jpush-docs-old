#!/usr/bin/env python
import logging
import commands
import os
import time


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/opt/push/jpush-docs/autobuild.log',
                    filemode='a+')

print (os.chdir("/opt/push/jpush-docs/jpush-docs/"))
add_result= (commands.getstatusoutput("git add ."))
commit_result=(commands.getstatusoutput('git commit -m "fix the pull to push"'))
push_result= (commands.getstatusoutput("git push origin renew"))
print push_result[0]

print ("git push origin renew,test")






