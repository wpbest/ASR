# ASR
Automactic Speech Recognition 

# Install PyEnv Download from GitHub
https://github.com/pyenv-win/pyenv-win

Open PowerShell
Create a new folder .pyenv in your user folder with the name .pyenv. You can do this using the Explorer or the following PowerShell command:

```PowerShell
mkdir $HOME/.pyenv
```

Copy the pyenv-win folder and the .version file from the GitHub folder into the newly created .pyenv folder in your user folder.

Set the environment variables PYENV and PYENV_HOME that point to the installation folder:

```PowerShell
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
```

Add the bin folder to the PATH variable. Such that pyenv can be found when using the command line.

```PowerShell
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
```

Close the current PowerShell.

If you havent enabled script execution yet, start a new PowerShell with admin privileges by right-clicking on the PowerShell icon in the start menu and choose Run as administrator.

Enter the following command into the PowerShell to enable the execution of scripts:

```PowerShell
Set-ExecutionPolicy unrestricted
```

And press A to choose Yes to ALL. Afterward, you can close this PowerShell window and open a new one without admin privileges.

Now, you can run pyenv by entering:

```PowerShell
pyenv
```

If you encounter a security warning from where you have to choose if you want to run pyenv you can disable this warning by “unblocking” the pyenv script with the following command:

```PowerShell
Unblock-File $HOME/.pyenv/pyenv-win/bin/pyenv.ps1
```
# List all Version of Python installed
```PowerShell
pyenv install -l
```

# Installl a particular version of Python
```PowerShell
pyenv install 3.14.0
```

# Activate a particular version of Python
```PowerShell
pyenv shell 3.14.0
```

# Set the default version of Python
```PowerShell
pyenv global 3.14.0
```
3.11.9

# Check if PIP working
```PowerShell
get-command pip
```

# Create a Python Virual Environment
```PowerShell
python -m venv .venv
```

# Activate the Python Virtal Environment
```PowerShell
.\.venv\Scripts\Activate.ps1
```

code .

Open Command Pallet
Ctrl Shit P

settings json

"python.terminal.activateEnvironment": true

restart vscode

Select Run and Debug to create a launch.json file

pip install SpeechRecognition pyaudio pyttsx3 requests

# Install Ollama
https://ollama.com/download

Go to settings and expose Ollama to the network by enabling it.

# How to Run
Hover over debug/run button on the left button pane and select show automatic python configuration. It will show a list and then select ASR.