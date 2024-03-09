:: ==============================================================================
:: @author jbarry302
:: ==============================================================================
@echo off
setlocal enabledelayedexpansion


set SAMPLE_FILE=.env.sample
set ENV_FILE=.env
if exist %ENV_FILE% del %ENV_FILE%

echo (leave blank to manually configure in the .env file)
for /f "tokens=1,* delims==" %%a in ('type %SAMPLE_FILE%') do (
    set "hint="
    if /i "%%a"=="DEBUG" set "hint= (True or False)"

    set /p "input=Enter a value for %%a!hint!: "
    
    if defined input (
        echo %%a=!input!>> %ENV_FILE%
    ) else (
        echo %%a=>> %ENV_FILE%
    )
)

echo .env file has been created with user input.
