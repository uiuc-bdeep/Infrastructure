from bdeep.context import getJobArgs

args = getJobArgs()

print "Hello, %s" % args["name"]
