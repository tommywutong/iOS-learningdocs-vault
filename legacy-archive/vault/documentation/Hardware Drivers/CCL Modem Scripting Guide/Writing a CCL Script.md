---
title: CCL Modem Scripting Guide
apple_id: TP40005464
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2007-06-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Reference/CCLScriptingRef/ScriptBasics/ScriptBasics.html
archived_at: '2026-07-15T07:41:16.440792Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CCL Modem Scripting Guide](Introduction%20to%20CCL%20Modem%20Scripting%20Guide.md)


[Next](CCL%20Script%20Syntax.md)[Previous](Introduction%20to%20CCL%20Modem%20Scripting%20Guide.md)

# Writing a CCL Script

This chapter describes the basic tasks a CCL scriptmust perform. For detailed descriptions of the modem scripting commands, see [CCL Command Reference](CCL%20Command%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnbnknltc).

A modem script executes in one of two possible modes, each with a separate entry point. The modes are as follows:

**originate**
: used when a call is initiated.

**answer**
: used when call answering is enabled. OS X does not provide a user interface for enabling or using answer mode.

**hangup**
: used to terminate every connection, whether in originate or answer mode, and whether or not the connection was successful.

The following figure provides an overview of the tasks your script must perform in each mode. The remainder of this chapter describes these tasks.

| Originate mode  (to initiate a call)  `@ORIGINATE` entry point | _Answer mode_  (to answer a call)  `@ANSWER` entry point | _Hangup mode_  (to terminate a call)  `@HANGUP` entry point |
| --- | --- | --- |
| Configure serial port. | Configure serial port. | Turn off CTS hardware handshaking. |
| Turn off CTS hardware handshaking. | Turn off CTS hardware handshaking. | Issue hangup command. |
| Configure modem. | Configure modem. | If unsuccessful, put modem in command mode and issue hangup again. |
| Dial. | Enable auto-answering. | Recall factory defaults. |
| Wait for response. | Detect ring. | Turn off auto-answering. |
| If call fails, exit with error result code. | If call fails, exit with error result code. | Exit. |
| If call succeeds, display message. | If call succeeds, display message. |  |
| If modem error correction established, issue `USERHOOK 2` or `USERHOOK 4`. | If modem error correction established, issue `USERHOOK 2` or `USERHOOK 4`. |  |
| If modem data compression established, issue `USERHOOK 3`. | If modem data compression established, issue `USERHOOK 3`. |  |
| Configure serial port. | Configure serial port. |  |
| If appropriate, turn on CTS hardware handshaking. | If appropriate, turn on CTS hardware handshaking. |  |
| Issue `USERHOOK 1`. | Issue `USERHOOK 1`. |  |

When OS X initiates a call, it executes the script starting at the `@ORIGINATE` entry point. The script must perform the following tasks to initiate a call:

1. __Configure the communication channel.__

   Use the `SERRESET` command to reset the communication parameters of the serial port (or emulated equivalent communication channel). Set the speed of the connection to the maximum speed of the device. (You may change the serial port speed later in the script.) Set the number of bits to be used for stop, start, and parity.

   Use the `HSRESET` command to turn off the serial port's flow control options. (You will turn on the appropriate options later in the script.)
2. __Configure the device.__

   Following is a list of standard steps for configuring a modem-like communication device. Check the documentation that came with your device to determine whether it requires different steps.

   1. Recall the factory default configuration settings.
   2. If your device has a speed of 14,400 bps or higher, you need to configure the device for RTS/CTS handshaking. For modems, an appropriate cable must be used, as described in [Cable Specifications](Cable%20Specifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnrnknltc). Do not turn on hardware handshaking until the connection has been made.
   3. Configure the modem for DTR usage.
   4. Turn local echo off. When local echo is on, the modem sends commands it receives back to the computer.
   5. Set the modem to return detailed result codes including the speed of the connection and the results of error correction and data compression negotiation.
   6. If the modem can do error correction, set error correction according to `varString4`.

      If `varString4` is set to 0, turn error correction off.

      If `varString4` is set to 1, have the modem negotiate the best available error correction with the remote modem. If no error correction can be established, have the modems remain connected without error correction.

      If `varString4` is set to 2, have the modem try to establish MNP10 error correction with the remote modem. If MNP10 negotiation fails, have the modems remain connected without error correction.
   7. OS X is generally more efficient than a modem or similar device at compressing data. If you believe you have a special situation in which hardware data compression is preferable, have the script set up the device to negotiate data compression.
   8. Turn the speaker on or off according to the value of `varString2`.
3. __Dial the phone number.__

   1. Have the script check whether the dial string extends into `varString8` (then `varString9`) by using the `IFSTR` command to check for a blank string. If the entire dial string fits in `varString7`, have the script issue a single dial command. If the dial string is longer than `varString7`, have the script issue multiple dial commands referencing `varString7`, `varString8`, and if necessary, `varString9`.
   2. Set tone or pulse dialing in the dial command according to the value of `varString3`.
   3. If `varString6` is set to 1, have the device begin dialing without confirmation of dial tone detection. This is useful when the phone system provides a nonstandard dial tone that can't be recognized by a modem's tone detection circuitry.

      If `varString6` is set to 2, the user has already dialed the remote number. Have the script cause the modem to retrain with the remote system. This is useful when the dialing sequence is too complex or interactive for the CCL script to navigate.
   4. Display the dialed phone number in the Internet Connect status window and the activity log using the `NOTE` command. Use `varString1` in log messages rather than a concatenation of `varString7`, `varString8`, and `varString9`.
4. __Wait for the device to respond.__
5. __If the call fails, return an error result code indicating what happened.__

   For example, use error result code -6022 if the line is busy. (See [Result Codes](Result%20Codes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqobnknltc) for a complete list.)
6. __If the call is successful, indicate that a connection has been established.__

   Display a message such as "Communicating at 9600 bps" in the Internet Connect status window using the `NOTE` command. Also display messages indicating the results of error correction and data compression negotiation, if applicable.

   If you were successful in establishing error correction, issue `USERHOOK 4` (for MNP10 error correction) or `USERHOOK 2` (for all other error correction) to advise OS X that a reliable link was established.

   If you were successful in establishing data compression, issue `USERHOOK 3` to advise OS X to turn off its built-in data compression.
7. __Configure the communication channel based on the device speed and the connection rate.__

   If your device has a speed of 14,400 bps or higher (and, for modems, if you are using a RTS/CTS handshaking cable as described in [Cable Specifications](Cable%20Specifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnrnknltc)), use the `HSRESET` command to set flow control to `outputCTS` . Use the `COMMUNICATINGAT` command to tell OS X the connection speed so that it can set its timers appropriately.

   If your device has a speed of 9600 bps or slower, use the `SERRESET` command to reset the serial port speed to the speed of the connection.
8. __Exit the script so that OS X can use the connection.__

For more details on the commands and variables described in this section, see [CCL Command Reference](CCL%20Command%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnbnknltc).

To answer a call, OS X executes the script starting at the `@ANSWER` entry point. The script must perform the following tasks to answer a call:

1. _Configure the communication channel._

   Use the `SERRESET` command to reset the communication parameters of the serial port (or emulated equivalent communication channel). Set the speed of the connection to the maximum speed of the device. (You may change the serial port speed later in the script.) Set the number of bits to be used for stop, start, and parity.

   Use the `HSRESET` command to turn off the serial port's flow control options. (You will turn on the appropriate options later in the script.)
2. _Configure the device._

   It will require several commands to completely configure the device. To prevent calls being answered before the configuration is complete, disable auto-answering in the first command the script issues. (You will enable it in step 3.)

   For additional details about configuring the device, see step 2 of [Initiating a Call](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqmznknltg) earlier in this chapter.

   1. Recall the factory default configuration settings.
   2. If your device has a speed of 14,400 bps or higher, set up the device for RTS/CTS handshaking. For modems, use an appropriate cable, as described in [Cable Specifications](Cable%20Specifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnrnknltc).
   3. Configure the device for DTR usage.
   4. Turn local echo off.
   5. Set the device to return detailed result codes including the speed of the connection and the results of error correction and data compression negotiation.
   6. If the device can do error correction, set error correction according to `varString4`.
   7. OS X is generally more efficient than a modem at compressing data. If you believe you have a special situation in which hardware data compression is preferable, have the script set up the modem to negotiate data compression.
   8. Turn the speaker on or off according to the value of `varString2`.
3. _Enable auto-answering and wait for the result._

   On an incoming call, the device issues a `RING` result code.
4. _If the call fails, return an error result code indicating what happened._

   For example, use error result code -6021 if the device cannot detect a carrier signal on the phone line. (See [Result Codes](Result%20Codes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqobnknltc) for a complete list.)
5. _If the call is successful, indicate that a connection has been established._

   Display a message such as "Communicating at 9600 bps" in the Internet Connect status window using the `NOTE` command. Also display messages indicating the results of error correction and data compression negotiation, if applicable.

   If you were successful in establishing hardware error correction, issue `USERHOOK 4` (for MNP10 error correction) or `USERHOOK 2` (for all other error correction) to advise OS X that a reliable link was established.

   If you were successful in establishing data compression, issue `USERHOOK 3` to advise OS X to turn off its built-in data compression.
6. _Configure the communication channel based on the device speed and the connection rate._

   Issue the `USERHOOK 1` command. The `USERHOOK 1` command informs OS X that the serial port or equivalent is busy answering a call, which prevents OS X from giving it up to another application.

   If your device has a speed of 14,400 bps or higher (and, for modems, if you are using a RTS/CTS handshaking cable as described in [Cable Specifications](Cable%20Specifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnrnknltc)), use the `HSRESET` command to set flow control for`outputCTS`.

   Use the `COMMUNICATINGAT` command to tell OS X the connection speed so that it can set its timers appropriately.

   If your device has a speed of 9600 bps or slower, use the `SERRESET` command to reset the serial port speed to the speed of the connection.
7. _Exit the script so that OS X can use the connection._

For more details on the commands and variables described in this section, see [CCL Command Reference](CCL%20Command%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnbnknltc).

To terminate a call, OS X executes the script starting at the `@HANGUP` entry point.

The hangup part of the script is executed to terminate a connection whenever the `@ORIGINATE` or `@ANSWER` parts of the script have been executed, regardless of the result. The hangup part of the script is also executed when OS X terminates answer mode.

The script must perform the following tasks to terminate a call:

1. _If hardware handshaking is used in the_ `@ORIGINATE` _or_ `@ANSWER` _part of the script, turn off hardware handshaking._

   Use the `HSRESET` command to turn off hardware handshaking.
2. _If possible, cause the device to enter command mode._

   Before you issue a hangup command, you may need to get the attention of the device by, for example, issuing a short break, a long break, or the attention sequence "`+++`", or by toggling DTR. Consult your device documentation for the appropriate method.
3. _Issue a hangup command._
4. _Recall the factory default configuration settings._

   Since you recalled the default settings at the beginning of the script, this is not necessary if the only communications application you use is OS X’s built-in modem support; however, recalling the default settings at the end of your script is recommended in case the next communications application that you use does not take care of this itself.
5. _Turn off auto-answering._

   This prevents the device from answering the phone until call answering is enabled.
6. _Exit with an appropriate message._

   If successful, return a result code of `0`. If unsuccessful, return the appropriate error result code as listed in [Result Codes](Result%20Codes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqobnknltc)

For more details on the commands and variables described in this section, see [CCL Command Reference](CCL%20Command%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tinrufvbuqnbnknltc).

[Next](CCL%20Script%20Syntax.md)[Previous](Introduction%20to%20CCL%20Modem%20Scripting%20Guide.md)

