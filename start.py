import datetime
import os


def currentTime():
    time = str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    return time


def currentTimeF():
    time = str(datetime.datetime.now().strftime("%m%d%Y_%H%M%S"))
    return time


# Function to print and write to log
def printAndLog(msg):
    print(msg)
    writeToLog(logLocation, msg)


# Function to write to log
def writeToLog(file, msg):
    try:
        with open(file, 'a') as file:
            file.write(currentTime() + " --- " + msg + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")


# variables to create log file
workingDir = os.path.expanduser("~")
logFile = "VigilantNetstat_" + currentTimeF()
logLocation = workingDir, logFile

print(logFile)
