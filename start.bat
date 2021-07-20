echo RUNNING NPM INSTALL
call npm install
echo RUNNING PIP INSTALL TORNADO
call pip install tornado
echo STARTING SERBER
start cmd /k call startServer.bat
echo STARTING APP
call npm start