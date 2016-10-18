from bdeep.context import getJobArgs, getConfig

args = getJobArgs()
config = getConfig()
environment = config["environment"]

print "Hello, %s we're running in %s" % (args["name"], environment)

