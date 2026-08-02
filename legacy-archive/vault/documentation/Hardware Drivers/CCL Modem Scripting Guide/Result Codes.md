---
title: CCL Modem Scripting Guide
apple_id: TP40005464
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2007-06-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Reference/CCLScriptingRef/ReturnValues/ReturnValues.html
archived_at: '2026-07-15T07:41:16.418776Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CCL Modem Scripting Guide](Introduction%20to%20CCL%20Modem%20Scripting%20Guide.md)


[Next](Cable%20Specifications.md)[Previous](CCL%20Command%20Reference.md)

# Result Codes

This appendix lists the result codes returned by the Communication Command Language (CCL). Each result code is shown with a description of the error and the message, if any, that is displayed to the user.

If the script executes successfully, have it exit with result code `0`. If the script is unsuccessful for any reason, have it exit with one of the error result codes listed in this appendix. Note that result code `-6002` allows you to pass a custom message to the user.

| Result code | Description | Message displayed |
| --- | --- | --- |
| `-6002` | Generic CCL error. | (Supplied by the string parameter in the `EXIT` command.) |
| `-6003` | Subroutine overflow. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6004` | The target label is undefined. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6005` | Bad parameter error. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6006` | Duplicate label error. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6007` | Close error. | (No message is displayed.) |
| `-6008` | The script was canceled. | (No message is displayed.) |
| `-6009` | The script contains too many lines. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6010` | The script contains too many characters. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6011` | The CCL has not been initialized. | (No message is displayed.) |
| `-6012` | Cancel in progress. | (No message is displayed.) |
| `-6013` | Another script is in progress. | (No message is displayed.) |
| `-6014` | Exit with no error. | (No message is displayed.) |
| `-6015` | A label is out of range. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6016` | Bad command. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6017` | End of script reached; expected `Exit`. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6018` | The match string index is out of bounds. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6019` | Modem error; the modem is not responding. | Modem not responding. Reset modem, check connections, or check to see that the proper port and modem type were specified in the Remote Access Setup control panel. |
| `-6020` | No dial tone. | The modem cannot acquire a dial tone. |
| `-6021` | No carrier. | The modems could not connect. Try again. |
| `-6022` | The line is busy. | The phone number you are calling is busy. |
| `-6023` | No answer. | The phone number you are calling does not answer. |
| `-6024` | No `@ORIGINATE` command in the modem script. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6025` | No `@ANSWER` command in the modem script. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |
| `-6026` | No `@HANGUP` command in the modem script. | The file for the modem you selected does not work properly. It may be damaged; try replacing the file in the Extensions folder. |

[Next](Cable%20Specifications.md)[Previous](CCL%20Command%20Reference.md)

