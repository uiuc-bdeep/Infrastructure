"""
This module sets up the proper environment context for BDEEP python scripts.
"""

import os
import glob
import json
from pprint import pprint

config = {
        "environment": "TESTING",
        "inputRoot": ".",
        "outputRoot": ".",
        "args": {}
        }

# Set environment is exists
env = os.environ.get('BDEEP_ENV')
if env is not None:
    config["environment"] = env

# Set inputRoot if exists
inputRoot = os.environ.get('BDEEP_INPUT_ROOT')
if inputRoot is not None:
    config["inputRoot"] = inputRoot

# Set outputRoot if exists
outputRoot = os.environ.get('BDEEP_OUTPUT_ROOT')
if outputRoot is not None:
    config["outputRoot"] = outputRoot

# Bring in Config if exists
configPath = os.environ.get('BDEEP_CONFIG')
if configPath is None:
    configs = glob.glob("bdeep_config_*.json")
    if len(configs) > 1:
        assert False, "Too many configuration files matching 'bdeep_config_*.json'"
    if len(configs) == 1:
        configPath = configs[0]
if configPath is not None:
    with open(configPath, 'r') as f:
        config = json.load(f)

""" Client API """
def generateInputPath(pathStr):
    return os.path.join(config["inputRoot"], pathStr)

def generateOutputPath(pathStr):
    return os.path.join(config["outputRoot"], pathStr)

def getJobArgs():
    return config["args"]

def generateProjectPath(pathStr):
    return os.path.join(config["mainPath"], pathStr)

def getConfig():
    return config

def setConfig(cfg):
    global config
    config = cfg

def loadConfig(path):
    global config
    with open(path, 'r') as f:
        setConfig(json.load(f))
