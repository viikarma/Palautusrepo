*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input  kalle
    Input  kalle@123
    Run Application
    Output Should Contain  User created successfully
