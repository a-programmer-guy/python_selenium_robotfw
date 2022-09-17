*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    Chrome
${url}    https://saucedemo.com


*** Test Cases ***
LoginTest
    Open Browser    ${url}    ${browser}
    Input Text    id:user-name    standard_user
    Input Password    id:password    secret_sauce
    Click Element    id:login-button
    Close Browser


*** Keywords ***