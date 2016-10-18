import logging
from bdeep.context import getJobArgs, getConfig

log = logging.getLogger("BDEEP")

args = getJobArgs()
config = getConfig()
environment = config["environment"]

log.debug("Hello, %s. We're running in %s", args["name"], environment)

