import logging
from bdeep.context import getJobArgs

log = logging.getLogger('BDEEP')

args = getJobArgs()

log.debug("Hello, %s" % args["name"])
