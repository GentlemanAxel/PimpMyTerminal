@echo off
title Terminal
mode 87, 30
chcp 65001 >nul
echo.
echo.
echo  [34m                                            ______                    _             __[0m
echo  [94m                                           /_  __/__  _________ ___  (_)___  ____ _/ /[0m
echo  [94m                                            / / / _ \/ ___/ __ `__ \/ / __ \/ __ `/ / [0m
echo  [96m                                           / / /  __/ /  / / / / / / / / / / /_/ / /  [0m
echo  [96m                                          /_/  \___/_/  /_/ /_/ /_/_/_/ /_/\__,_/_/   [0m
echo.                                                                                    
echo.                                        
echo.
echo.
echo.
for /f %%A in ('"prompt $H &echo on &for %%B in (1) do rem"') do set BS=%%A
:input
echo.
echo  [97m╔══[0m([92m%username%[0m@[95m%computername%[0m)-[[91m%cd%[0m]
set /p cmd=".%BS% [97m╚══>[0m "
echo.
%cmd%
goto input