# Created by github.com/dyeadal

# Variable to store execution time
$execTime = Get-Date

Write-Host "Created by github.com/dyeadal"
Write-Host ""
Write-Host "Netstat Scanner"
Write-Host ""

$formattedTime = $execTime.ToString("MMddyyyy_HHmmss")

# Log file location, uncomment preferred location and comment out others
$logFile = "C:\Users\$env:USERNAME\Desktop\netstat_$formattedTime.txt"
#logFile = "C:\Scanner Logs\netstat_$formattedTime.txt"
#logFile = "C:C:\Users\$env:USERNAME\Documents\Scanner Logs\netstat_$formattedTime.txt"

#-----------------------------------------------------------------
# Functions
#-----------------------------------------------------------------
# Function to append text to our newly created log file
function LogMessage {
	
	# Function takes a single parameter, a string to append to our log file
	param (
		[string]$msg
	)
	
	# Retrieve timestamp of log entry
	$timestamp = Get-Date -Format "MM/dd/yyyy HH:mm:ss"
	
	#Add time and log entry to log file
	Add-Content -Path $logFile -Value "$timestamp --- $msg"
}

# Function to echo message and log it using LogMessage function 
function WriteHostLog {
	param (
		[string]$msg
	)
	
	Write-Host $msg
	LogMessage -msg $msg
}

#-----------------------------------------------------------------

### TODO: Create log folder to host uploaded netstat capture file, ???formated output of netstat as a csv???, and log file

# Create log text file, and log execution time of first line
Write-Host "Creating log file, $logFile"
New-Item -Path $logFile -ItemType File -Force
WriteHostLog -msg "Program executed, $execTime. Log file created."

# Check if Ollama EXE shortcut exists
WriteHostLog -msg "Verifying Ollama is installed"

$ollamaCheck = "C:\Users\env:$USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ollama.exe"
if ($ollamaCheck) {
    WriteHostLog -msg "Ollama is installed."
} else {
    WriteHostLog -msg "Ollama is NOT installed."
}

### TODO: Upload output of netstat command saved as a file (user will have to capture netstat output)

### TODO: Format output file to an easier use format

### TODO: Some interface to interact with which IoCs to investigate (Foreign IPs, ports)

### TODO: Launch default browser and search IoCs against OSINT sources
	###IP address OSINT search = VirusTotal, AlientVault OTX, GreyNoise, FortiGuard Labs, Censys
	
### TODO: Use Ollama to inform user what TCP or UDP port is typically used for and what to be wary of
	### TODO: Look up what dataset is best for TCP UDP port identification
 
Pause
