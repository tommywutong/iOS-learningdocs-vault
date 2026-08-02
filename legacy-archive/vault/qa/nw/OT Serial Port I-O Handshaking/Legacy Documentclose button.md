---
title: OT Serial Port I/O Handshaking
apple_id: DTS10001456
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-11-27'
source_url: https://developer.apple.com/library/archive/qa/nw/nw44.html
archived_at: '2026-07-18T02:29:46.703183Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW44OT Serial Port I/O Handshaking |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ---   Q: How do I specify and control Open Transport Serial port I/O handshaking? The options seem a bit confusing.  A: By using the the `SRL_OPT_HANDSHAKE` Option provided by the Open Transport native interfaces you can customize serial port handshaking in variety of ways. For instance, you can request that input handshake be controlled by the CTS line, or by the `XON/OFF`  sequence. The handshaking behavior is specified by a 4-byte unsigned integer value that is passed in with the `SRL_OPT_HANDSHAKE` Option:   |  | | --- | | ``` +=====-========-========-========-========-========-========-========-========+ |  Bit|   7    |   6    |   5    |   4    |   3    |   2    |   1    |   0    | |Byte |        |        |        |        |        |        |        |        | |=====+========+========+=====================================================| |  0  |        |        |        |        |        |        |        |        | |-----+-----------------------------------------------------------------------| |  1  |        |        |        |        | DTR    | CTS    | XON/OFF| XON/OFF| |     |        |        |        |        | Output | Input  | Input  | Output | |-----+-----------------------------------------------------------------------| |  2  |                         XON character                                 | |-----+-----------------------------------------------------------------------| |  3  |                         XOff character                                | +=============================================================================+ ``` |   The high word (16 bits) of the integer is a bitmap with 1 or more of the following bits set:   |  | | --- | | ```         kOTSerialXOnOffInputHandshake   = 1         kOTSerialXOnOffOutputHandshake  = 2         kOTSerialCTSInputHandshake      = 4         kOTSerialDTROutputHandshake     = 8 ``` |   The 2nd lowest byte is the `XOn` character value; the lowest byte is the `XOff` character value.  If these values are 0, and `XOnOff` handshaking was requested, the default values of Control-S for `XOff` and Control-Q for `XOn` will be used.  There is an inline function (or #define for C users) `SerialHandshakeData(type, onChar, offChar)` defined in OpenTptSerial.h can be used to create this 4-byte value. The default value of this option is no handshaking.  For instance, if you wish to enable `XON/XOFF` input handshaking, but you wanted to specify that the `XON` char be a ^T instead of an ^Q. You would create an option structure in this manner.   |  | | --- | | ```     TOption     opt;     opt.len     = kOTFourByteOptionSize;     opt.level   = XTI_GENERIC;     opt.name    = SERIAL_OPT_HANDSHAKE;     opt.value   = OTSerialHandshakeData  ( kOTSerialXOnOffInputHandshake,                               ('T' & ~0x40),                 // normally kOTSerialDefaultOnChar kOTSerialDefaultOffChar); ``` |   You also have the ability to control the XOff state of the serial input port by using the the `I_SetSerialXOffState Ioctl` command. A value of 0 will unconditionally clear the `XOFF` state, while a value of 1 will unconditionally set it.   |  | | --- | | ``` OTIoctl(theSerialEndpoint, I_SetSerialXOffState, 1);    // Set XOFF state to ON ``` |   The `I_SetSerialXOn` Ioctl causes the serial port to send an `XON` character. A value of 0 will only cause it to be sent if we're in the `XOFF` state, while a value of 1 will unconditionally send the character.   |  | | --- | | ``` OTIoctl(theSerialEndpoint, I_SetSerialXOn, 1);          // Unconditionally send an XON ``` |   Conversely, the `I_SetSerialXOff Ioctl` causes the serial port to send an `XOFF` character. A value of 0 will only cause it to be sent if we're in the `XON` state, while a value of 1 will unconditionally send the character.   |  | | --- | | ``` OTIoctl(theSerialEndpoint, I_SetSerialXOff, 1);         // Unconditionally send an XOFF ``` | |

#### [Nov 27 1996]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
