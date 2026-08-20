---
title: CCL Modem Scripting Guide
apple_id: TP40005464
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2007-06-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Reference/CCLScriptingRef/CCLScriptSyntax/CCLScriptSyntax.html
archived_at: '2026-07-15T07:41:16.354963Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CCL Modem Scripting Guide](Introduction%20to%20CCL%20Modem%20Scripting%20Guide.md)


[Next](CCL%20Bundles%20and%20Property%20Lists.md)[Previous](Writing%20a%20CCL%20Script.md)

# CCL Script Syntax

A modem script is a set of instructions that tells a computer how to interact with a modem so that calls can be initiated and received. To establish a connection, a script typically configures and then connects the modem. To terminate a connection, the script disconnects the modem by hanging up and then restores the modem settings that were in effect before the call.

Each type of modem used with OS X requires a modem script. Many scripts are provided with OS X. (See [Available Modem Scripts](Introduction%20to%20CCL%20Modem%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqmjnknltc) in the Introduction of this document for more information.)

If no script is provided for your modem, you must write one using Communication Command Language (CCL), a programming language that configures and controls your modem. This section describes the basic elements and structure of a CCL file.

Each line of CCL code consists of one instruction that is made up of a command and its parameters, if any. Modem commands are used as parameters of CCL commands. For example, the command `write "ATDT^1\13"` includes the following:

- a CCL command, `write`
- a modem command, `ATDT`
- a modem command parameter, `^1\13`

This command tells the CCL interpreter to send to the modem the modem command `ATDT` followed by variable string #1, and a carriage return (ASCII code 13).

The CCL interpreter reads scripts from left to right and from top to bottom. It reads straight through, from beginning to end, unless you tell it otherwise (for example, by using the `JUMP` command).

For a complete list of commands and their usage, see [CCL Command Reference](CCL%20Command%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnbnknltc).

You can insert explanatory comments into your script. To enter a comment, start the line with an exclamation point (`!`).

You may also want to use a blank comment line to make your script more readable; to do so, type an exclamation point with no text and press Return.

The CCL interpreter is not case sensitive. Therefore, `@LABEL 1`, `@Label 1`, `@label 1`, and `@laBel 1` are all valid (and equivalent) instructions.

Labels are used to mark locations in the script. Other script commands, such as `JUMP`, transfer control to locations in the script marked by the `@LABEL` command. For instance, `JUMP 13` tells the CCL interpreter to jump to label 13 and start executing the commands after the `@LABEL 13` command. A script may use up to 128 labels, numbered 1–128.

To delimit a string in CCL code, you can use single quotation marks (`'`) or double quotation marks (`"`). If you do not start the string with a single or double quotation mark, any of the following characters determines the end of the string: space, return, tab, comma, or semicolon.

CCL strings may include references to variable strings. See [Variable Strings (varStrings)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqojnknltc) later in this chapter for details.

CCL strings may include nonprinting characters such as null, tab, and return. To support these nonprinting characters, the CCL interpreter recognizes two special characters: the backslash (`\`) and the caret (`^`).

The backslash is a quote character. You can use the backslash to include a nonprinting character by specifying the decimal representation of the ASCII character (decimal numbers 00 to 99 are valid) or to explicitly include the backslash or caret character in a string.

The caret is a variable delimiter character. You can use it to insert a variable string or an ASK string into another string. (For details, see [Variable Strings (varStrings)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqojnknltc) later in this chapter.)

Here are some examples of how the backslash and caret are used:

| String | Result |
| --- | --- |
| `\13` | inserts a carriage return (0x0D) into the string |
| `\00` | inserts the null character (0x00) into the string |
| `\\` | inserts the backslash (\) character (0x5C) into the string |
| `\^` | inserts the caret (^) character (0x5E) into the string |
| `^1` | inserts variable string 1 into the string |
| `^*` | inserts the ASK string into the string |

Here are some string examples:

| String contents | Printed Output |
| --- | --- |
| `'this is a test'` | `this is a test` |
| `thisisatest` | `thisisatest` |
| `"this is a test"` | `this is a test` |
| `this is a test` | `this` |
| `"this \34\73\83\34 a test"` | `this "IS" a test` |
| `"ATDT^1"` | `ATDT555-1212`(if variable string 1 is 555-1212) |

CCL strings may include references to variable strings, which are strings passed to the script as parameters. Most of these values are provided by OS X based on user-specified parameters.

OS X uses the following variable strings:

| Variable String | Contents | Values |
| --- | --- | --- |
| `varString1` | The complete dial string (the telephone number to dial, with the necessary prefixes and suffixes). |  |
| `varString2` | The modem speaker flag: | - `0`—Speaker off. - `1`—Speaker on. |
| `varString3` | The tone/pulse dialing selector: | - `T`—Tone dialing. - `P`—Pulse dialing. |
| `varString4` | The modem error correction flag: | - `0`—Script should not try to use modem error correction. - `1`—Script should try to use modem error correction. - `2`—Script should try to establish MNP10 error correction. |
| `varString5` | Reserved for future use. |  |
| `varString6` | The dialing mode flag: | - `0`—Normal dialing. - `1`—Blind dialing (that is, have the modem begin dialing without confirmation of dial tone detection). - `2`—Manual dialing (that is, have the script assume that the user has already picked up the phone and dialed the remote number). |
| `varString7`–`varString9` | Variable strings 7–9 break a long dial string into shorter strings for use with modems that can accept only a limited command string size. They are automatically generated by OS X. | The variables `varString7`, `varString8`, and `varString9` contain the contents of `varString1` divided into shorter pieces. Each of these strings is limited to 40 characters in length. Additional characters that will not fit into `varString7` spill over automatically into `varString8`, and so on.  If one or more of these three variables are unused, the empty variables contain a blank string (ASCII `20` hex). See [About mlts Resource Storage](CCL%20Bundles%20and%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnznknltc) for legacy information about these strings. |
| `varString27`–`varString30` | Defined in the information property list in your CCL script bundle. See [CCL Bundles and Property Lists](CCL%20Bundles%20and%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnznknlte) for information. |  |

All eight variable strings are passed to the script when it is running in originate mode. The modem speaker flag (`varString2`) and the error correction flag (`varString4`) are passed to the script when it is running in answer mode.

The CCL interpreter has a buffer that can hold up to 32 strings loaded by the `MATCHSTR` command. The `MATCHCLR` command erases the contents of the buffer. The `MATCHREAD` command reads input from the modem or other communication device and compares the input to the strings currently in the buffer. If a match is found in the specified time, execution continues at the label associated with that match string.

A recommended strategy for sending commands to the modem is as follows:

- Use `MATCHCLR` to clear all match strings.
- Use `MATCHSTR` to load match strings with appropriate responses.
- Use `WRITE` to send commands to the modem.
- Use `MATCHREAD` to check for defined modem responses. If an appropriate response is received, branch as defined by the corresponding `MATCHSTR` command.
- Use `SETTRIES`, `INCTRIES`, and `IFTRIES` to loop a few times.
- If an appropriate response is not received, branch to exit or to alternate code as defined by the `MATCHREAD` command.

Scripts may be a maximum of 32000 bytes. This is large enough for relatively complex dial scripts. However, if your script is too large, you may be able to make it small enough by minimizing the number and length of comments.

[Next](CCL%20Bundles%20and%20Property%20Lists.md)[Previous](Writing%20a%20CCL%20Script.md)

