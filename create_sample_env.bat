@echo off
setlocal enabledelayedexpansion

REM Set the paths for the .env and env.sample files
set "envFile=.env"
set "sampleFile=.env.sample"

REM Check if the .env file exists
if not exist %envFile% (
    echo Error: The .env file does not exist.
    exit /b 1
)

REM Create or clear the env.sample file
type nul > %sampleFile%

REM Read the .env file line by line
for /f "tokens=1,* delims==" %%a in (%envFile%) do (
    REM Skip empty lines or lines starting with #
    if "%%a" neq "" if not "%%a"=="#" (
        REM Append the key to the env.sample file without the value
        echo %%a= >> %sampleFile%
    )
)

echo %sampleFile% file created.

endlocal
