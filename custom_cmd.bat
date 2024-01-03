@echo off
title PimpMyTerminal
mode 87, 30
chcp 65001 >nul
cd %homedrive%%homepath% >nul

echo.
echo.
echo.                                    ::::::::::::::::::::  :::   :::  ::::::::: :::   ::: 
echo.                                   :+:    :+:   :+:     :+:+: :+:+: :+:    :+::+:   :+:  
echo.                                  +:+    +:+   +:+    +:+ +:+:+ +:++:+    +:+ +:+ +:+    
echo.                                 +#++:++#+    +#+    +#+  +:+  +#++#++:++#+   +#++:      
echo.                                +#+          +#+    +#+       +#++#+          +#+        
echo.                               #+#          #+#    #+#       #+##+#          #+#         
echo.                              ###      ##############       ######          ###          
echo.                              
echo.
echo.
echo.
for /f %%A in ('"prompt $H &echo on &for %%B in (1) do rem"') do set BS=%%A
:input
echo.
set /p cmd=" BetaUser001 -> "
echo.
%cmd%
goto input