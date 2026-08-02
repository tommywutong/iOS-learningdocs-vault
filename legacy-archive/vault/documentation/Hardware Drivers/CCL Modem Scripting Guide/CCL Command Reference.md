---
title: CCL Modem Scripting Guide
apple_id: TP40005464
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2007-06-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Reference/CCLScriptingRef/CCLCommands/CCLCommands.html
archived_at: '2026-07-15T07:41:16.324646Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CCL Modem Scripting Guide](Introduction%20to%20CCL%20Modem%20Scripting%20Guide.md)


[Next](Result%20Codes.md)[Previous](CCL%20Bundles%20and%20Property%20Lists.md)

# CCL Command Reference

This chapter describes the CCL commands interpreted by OS X. The commands are presented in alphabetical order. Each command section contains a description of the command; the syntax of the command, including any parameters; and an example, if appropriate.

To insert a comment or a blank line in the script, start the line with an exclamation point.

**_Syntax:_**
: |  |
```
! comment
```

**_Examples:_**
: |  |
```
! Turn echo off
!
```


The `@ANSWER` section label marks the script entry point when the script is executed in answer mode.

**_Syntax:_**
: |  |
```
@ANSWER
```


Available _only_ in OS X.

The `@CCLSCRIPT` section label marks the start of a CCL script. The label is optional and has no functional purpose..

**_Syntax:_**
: |  |
```
@CCLSCRIPT
```


The `@HANGUP` section label marks the script entry point when the script is executed in hangup mode.

**_Syntax:_**
: |  |
```
@HANGUP
```


The `@LABEL` command sets a numeric label in the script that can then be referenced from other script commands, such as `JUMP`, `JSR`, and `IFTRIES`. A script may include up to 128 labels, numbered 1 through 128. To make debugging easier, assign the labels in ascending sequence. They don't need to be consecutive.

**_Syntax:_**
: |  |
```
@LABEL labelnum
```

**_Parameter:_**
: **`labelnum`**
: A value from 1–128 that specifies the label number.

**_Example:_**
: |  |
```
@LABEL 30
```


The `@ORIGINATE` section label marks the script entry point when the script plays in originate mode (that is, when initiating a call).

**_Syntax_**
: |  |
```
@ORIGINATE
```


The `ASK` command causes a dialog box to be displayed to obtain information from the user. The dialog box contains a prompt message, an optional data entry field, a Cancel button, and an OK button. You may need the ASK command if your telephone system uses special telecommunications equipment. This command is typically used in originate mode only.

"String Formats" in Chapter 1 shows how to use the `ASK` string as part of another string. The ASK string is set if the user presses either the OK button or the Cancel button.

**_Syntax_**
: |  |
```
ASK maskflag "message" [jumpLabel]
```

**_Parameters_**
: **`maskflag`**
: **0**
: Echo the user's input/

**1**
: Mask the user's input with bullets (••••).

**2**
: Do not allow user input.

**`message`**
: The string to display in the dialog box as a prompt for the user.

**`jumpLabel`**
: If supplied, the label to jump to, where execution continues when the Cancel button is pressed; if not supplied, or if the OK button is pressed, then execution continues at the next CCL line.

**_Example_**
: |  |
```
ASK 1 "Enter your password to access the network."
ASK 2 "When the remote modem answers, click OK, otherwise click Cancel to stop Manual Dialing."
```


The `CHRDELAY` command allows you to specify a delay time between characters for all subsequent `WRITE` commands. This is useful for telecommunications equipment that requires data at a speed slower than the interface speed.

_Syntax_

```
CHRDELAY delay
```

**_Parameter_**
: **`delay`**
: The delay time, in tenths of a second.

**_Example_**
: |  |
```
CHRDELAY 8
```


For V.32bis devices that support RTS/CTS hardware flow control (including modems with an appropriate cable, as described in [Cable Specifications](Cable%20Specifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnrnknltc)), use the `COMMUNICATINGAT` command to indicate the speed of the modem connection if the modem speed is different from the serial port speed. This is necessary because OS X’s internal timers are based on the connection speed.

**_Syntax_**
: |  |
```
COMMUNICATINGAT baud
```

**_Parameter_**
: **`baud`**
: The modem speed, in bits per second.

**_Example_**
: |  |
```
COMMUNICATINGAT 4800
```


The `DECTRIES` command decreases the variable `tryCounter` by one. The CCL interpreter maintains `tryCounter`, which you may set to a value and increase or decrease by one. See also the commands `IFTRIES`, `INCTRIES`, and `SETTRIES`.

**_Syntax_**
: `DECTRIES`

The `DTRCLEAR` command clears (that is, deasserts) the Data Terminal Ready (DTR) signal on the RS-232 interface.

**_Syntax_**
: |  |
```
DTRCLEAR
```


The `DTRSET` command sets (that is, asserts) the Data Terminal Ready (DTR) signal on the RS-232 interface.

**_Syntax_**
: |  |
```
DTRSET
```


`EXIT` terminates execution of the script and returns a result code along with an optional string.

- If the script executes successfully, have it return a result code of `0`.
- If the script fails for any reason, it should return the appropriate error result code, as listed in [Result Codes](Result%20Codes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqobnknltc)

To give the user a nonstandard error message, use result code -6002 and use the string parameter to pass the nonstandard error message.

**_Syntax_**
: |  |
```
EXIT result ["string"]
```

**_Parameters_**
: **`result`**
: One of the CCL result codes listed in Appendix A, "Result Codes".

**`string`**
: The message displayed to the user when a connection attempt fails; if you include a string for one of the standard result codes, it overrides the message that OS X would normally display.

**_Examples_**
: |  |
```
EXIT -6022
EXIT -6002 "unable to communicate with PBX"
```


`FLUSH` empties all characters from the serial driver input buffer.

**_Syntax_**
: |  |
```
FLUSH
```


The `HSRESET` command sets the serial port's flow control options. If you are using a standard modem cable, you will turn off flow control and leave it off. If you are using a device that supports RTS/CTS handshaking, you need only the `outputCTS` parameter. Turn all options off at hangup.

**_Syntax_**
: |  |
```
HSRESET outputXON/XOFF outputCTS XON XOFF
        inputXON/XOFF inputDTR
```

**_Parameters_**
: **`outputXON/XOFF`**
: XON/XOFF handshaking for output. For OS X, it must be off.

**`outputCTS`**
: CTS hardware handshaking for output. For a modem, if you are using a cable that supports RTS/CTS handshaking, it should be on for originate and answer modes and off for hangup mode.

**`XON`**
: Specifies the XON character. (DO NOT USE with OS X.)

**`XOFF`**
: Specifies the XOFF character. (DO NOT USE for Apple Remote Access.)

**`inputXON/XOFF`**
: XON/XOFF handshaking for input. For Apple Remote Access, it must be off.

**`inputDTR`**
: DTR hardware handshaking for input. For Apple Remote Access, it should be off. For more information, see _Inside Macintosh,_ volume 4 (no longer in print) or _Inside Macintosh: Devices,_ available through the Apple Developer Catalog.

**_Example_**
: |  |
```
HSRESET 0 1 0 0 0 0
```


If the script is executing in answer mode, the `IFANSWER` command causes execution to continue at the specified label.

**_Syntax_**
: |  |
```
IFANSWER jumpLabel
```

**_Parameter_**
: **`jumpLabel`**
: The label to which execution should conditionally jump.

**_Example_**
: |  |
```
IFANSWER 30
```


If the script is executing in originate mode, the `IFORIGINATE` command causes execution to continue at the specified label.

**_Syntax_**
: |  |
```
IFORIGINATE jumpLabel
```

**_Parameter_**
: **`jumpLabel`**
: The label to which execution should conditionally jump.

**_Example_**
: `IFORIGINATE 7`

The `IFSTR` command compares two strings: one of the variable strings (described in [Variable Strings (varStrings)](CCL%20Script%20Syntax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqojnknltc)) and a literal string that you specify in the script. If the strings are equal, the script continues execution at the specified label.

**_Syntax_**
: |  |
```
IFSTR varStringIndex jumpLabel
      "compareString"
```

**_Parameters_**
: **`varStringIndex`**
: The number of the variable string to compare.

**`jumpLabel`**
: The label to which execution should conditionally jump.

**`compareString`**
: The string to which the variable string is compared.

In the following example, if the modem speaker flag (`varString2`) is on (`1`), execution jumps to label `55`. Otherwise, the next command is executed.

**_Example_**
: |  |
```
IFSTR 2 55 "1"
```


The `IFTRIES` command compares a parameter with the variable `tryCounter`. If the value of `tryCounter` is greater than or equal to the parameter, the script continues execution at the specified label. See also the commands`DECTRIES`, `INCTRIES`, and `SETTRIES`.

**_Syntax_**
: |  |
```
IFTRIES numTries jumpLabel
```

**_Parameters_**
: **`numTries`**
: The parameter to compare with the variable `tryCounter`.

**`jumpLabel`**
: The label to which execution should conditionally jump.

The following example checks to see if the value of `tryCounter` is greater than or equal to `3`. If so, execution jumps to label `62` and continues. If not, the next instruction is executed.

**_Example_**
: `IFTRIES 3 62`

The `INCTRIES` command increases the variable `tryCounter` by one. See also the commands `DECTRIES`, `IFTRIES`, and `SETTRIES`.

**_Syntax_**
: `INCTRIES`

The `JSR` command causes script execution to jump to the subroutine located at the specific label, saving the address of the line following the `JSR` command. When a `RETURN` command is encountered, execution resumes at the line following the `JSR` command. `JSR` commands can be nested up to 16 deep.

**_Syntax_**
: |  |
```
JSR jumpLabel
```

**_Parameter_**
: **`jumpLabel`**
: The label where execution should continue after the jump.

**_Example_**
: |  |
```
JSR 50
```


The `JUMP` command causes script execution to continue at the specified label.

**_Syntax_**
: |  |
```
JUMP jumpLabel
```

**_Parameter_**
: **`jumpLabel`**
: The label where execution should continue after the jump.

**_Example_**
: `JUMP 59`

The `LBREAK` command generates a long break (3.5 seconds) on the transmission line.

**_Syntax_**
: `LBREAK`

The CCL interpreter has a buffer that holds up to 32 strings loaded by the `MATCHSTR` command. The `MATCHCLR` command erases all strings in the buffer. Use the `MATCHCLR` command before loading each new group of strings. See also the `MATCHREAD` and `MATCHSTR` commands.

**_Syntax_**
: `MATCHCLR`

The CCL interpreter has a buffer that holds up to 32 strings loaded by the `MATCHSTR` command. The `MATCHREAD` command reads input from the serial driver and compares the input to the strings currently in the buffer. If a match is found within the specified `MATCHREAD` time, execution continues at the label associated with that match string (as defined by the `MATCHSTR` command that loaded the string). See also the `MATCHCLR` and `MATCHSTR` commands.

**_Syntax_**
: |  |
```
MATCHREAD time
```

**_Parameter_**
: **`time`**
: The time allowed for a match, in tenths of a second.

The following example searches for a match within 3 seconds.

**_Example_**
: |  |
```
MATCHREAD 30
```


The CCL interpreter has a buffer that holds up to 32 strings. The `MATCHSTR` command loads a string to the buffer, so that incoming strings can be matched against it by a `MATCHREAD` command. If an incoming string matches the stored string, script execution continues at the label specified in the `MATCHSTR` command. See also the commands `MATCHCLR` and `MATCHREAD`.

**_Syntax_**
: |  |
```
MATCHSTR matchNum matchLabel "matchStr"
```

**_Parameters_**
: **`matchNum`**
: A value from 1–32 specifying which string in the buffer to replace.

**`matchLabel`**
: The label where execution should continue when a `MATCHREAD` command detects a matching string.

**`matchStr`**
: A string (1–255 characters in length) to compare against.

The following example loads the string `"OK\13\10"` into the buffer as string 1. If a subsequent MATCHREAD reads a string that matches this one, then execution jumps to label 8.

**_Example_**
: |  |
```
MATCHSTR 1 8 "OK\13\10"
```


Available _only_ in OS X.

Enables or disables Data Carrier Detect (DCD).

**_Syntax_**
: |  |
```
MONITORLINE monitor
```

**_Parameters_**
: **`monitor`**
: **`0`**
: Disable DCD (soft carrier mode).

**`1`**
: Enable DCD (hard carrier mode).

The following example enables data carrier detect.

**_Example_**
: |  |
```
MONITORLINE 1
```


The `NOTE` command displays status and log information, passing the message string as a parameter. Optionally, you can set the message level to specify where the message should appear.

**_Syntax_**
: |  |
```
NOTE msgStr [msgLevel]
```

**_Parameters_**
: **`msgStr`**
: The message to display.

**`msgLevel`**
: The message level (the default level is 3).

**1**
: Send the message to the activity log only.

**2**
: Send the message to the Internet Connect status window only.

**3**
: Send the message to both the activity log and the Internet Connect status window.

The following examples show important places in which you should use the `NOTE` command. In the first example, the script logs outgoing calls by displaying the dialed phone number in the Internet Connect status window and the activity log. In the second example, the script displays the speed of the connection in the Internet Connect status window.

**_Examples_**
: |  |
```
NOTE "DIALING ^1" 3
NOTE "Communicating at 9600 bps." 2
```


`PAUSE` causes script execution to halt for a specified period of time.

**_Syntax_**
: |  |
```
PAUSE time
```

**_Parameter_**
: **`time`**
: The time to pause, in tenths of a second.

The following example causes script execution to pause for 2 seconds.

**_Example_**
: |  |
```
PAUSE 20
```


The `RETURN` command terminates a subroutine. Script execution continues with the line following the `JSR` command.

**_Syntax_**
: |  |
```
RETURN
```


The `SBREAK` command generates a short break (.5 seconds) on the transmission line.

**_Syntax_**
: `SBREAK`

The `SERRESET` command configures the serial port by passing values for baud rate, parity, data bits, and stop bits to the serial driver. Specifying a value other than the values listed below causes the default value to be used. The defaults for each parameter are listed below.

**_Syntax_**
: |  |
```
SERRESET baudRate, parity, dataBits,
         stopBits
```

**_Parameters_**
: **`baudRate`**
: `300`, `1200`, `2400` (the default), `4800`, `9600`, `14400`, `19200`, `28800`, `38400`, `57600`, and so on.

**`parity`**
: 1 for odd parity 2 for even parity 0 or 3 for no parity (the default)

**`dataBits`**
: 5, 6, 7, or 8 (the default)

**`stopBits`**
: 1 for 1 stop bit (the default) 2 for 2 stop bits 3 for 1.5 stop bits

**_Example_**
: |  |
```
SERRESET 9600, 0, 8, 1
```


The `SETSPEED` command sets the asynchronous serial interface speed to the specified speed. Use `SETSPEED` to set speeds other than those allowed in `SERRESET`.

**_Syntax_**
: |  |
```
SETSPEED interfacespeed
```

**_Parameter_**
: **`interfacespeed`**
: The serial interface speed.

**_Example_**
: |  |
```
SETSPEED 24000
```


`SETTRIES` initializes the tryCounter variable to the specified value. See also the commands `DECTRIES`, `IFTRIES`, and `INCTRIES`.

**_Syntax_**
: |  |
```
SETTRIES tries
```

**_Parameter_**
: **`tries`**
: The value to assign to the `tryCounter` variable.

**_Example_**
: |  |
```
SETTRIES 0
```


`USERHOOK` conveys information about the state of the modem to OS X.

**_Syntax_**
: |  |
```
USERHOOK opcode
```

**_Parameter_**
: **`opcode`**
: The user hook to execute.

**`1`**
: Indicates that the script is answering a call and that a ring is indicated by the modem. This prevents other applications from using the serial port until after the call has terminated.

**`2`**
: Reports that the modem is doing error correction (other than MNP10, which is indicated by opcode 4).

**`3`**
: Requests that OS X turn off its built-in data compression.

**`4`**
: Reports that the modem is doing MNP10 error correction.

**_Example_**
: |  |
```
USERHOOK 1
```


`WRITE` writes the specified string to the serial driver.

**_Syntax_**
: |  |
```
WRITE message
```

**_Parameter_**
: **`message`**
: The message written to the device.

The following example sends to the serial driver the modem command `ATDT` followed by variable string #1 and a carriage return. (For more information, see [Variable Strings (varStrings)](CCL%20Script%20Syntax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqojnknltc).)

**_Example_**
: |  |
```
WRITE "ATDT^1\13"
```

[Next](Result%20Codes.md)[Previous](CCL%20Bundles%20and%20Property%20Lists.md)

