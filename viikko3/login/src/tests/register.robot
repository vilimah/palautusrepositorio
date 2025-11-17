*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  vilizu
    Set Password  vili123
    Set Password Confirmation  vili123
    Click Button  Register new user
    Registration Should Succeed With Message  Welcome newuser!

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  vili1234
    Set Password Confirmation  vili1234
    Click Button  Register new user
    Registration Should Fail With Message  Username should have at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  vilizu
    Set Password  12
    Set Password Confirmation  12
    Click Button  Register new user
    Registration Should Fail With Message  Password should have at least 8 characters

Register With Valid Username And Invalid Password
    Set Username  vilizu
    Set Password  vili1234
    Set Password Confirmation  vili123
    Click Button  Register new user
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Nonmatching Password And Password Confirmation
    Set Username  vilizu
    Set Password  vili1234
    Set Password Confirmation  vili123
    Click Button  Register new user
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  vilizu
    Set Password  vili1234
    Set Password Confirmation  vili1234
    Click Button  Register new user
    Registration Should Fail With Message  Username already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  vilizu  vili1234
    Go To Register Page

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Registration Should Succeed With Message
    [Arguments]  ${message}
    Main Page Should Be Open
    Page Should Contain  ${message}

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

