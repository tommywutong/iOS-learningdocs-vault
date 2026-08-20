---
title: How to use the OT modem script engine
apple_id: DTS10001462
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/nw/nw50.html
archived_at: '2026-07-18T02:29:46.974557Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/idxNetworking-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Networking](https://developer.apple.com/referencelibrary/HardwareDrivers/idxNetworking-date.html)

|  |
| --- |
| Technical Q&A NW50How to use the OT modem script engine |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: I am in the process of developing software that requires the ability to establish serial connection via a modem. Rather than have the user enter cryptic AT commands or write a CCL parser to configure the modem, I would like to leverage the CCL scripts used in ARA and Open Transport/PPP.  Having a single system-level modem access and control method would be extremely useful. Modem vendors have only one CCL engine to support and client developers have a single API to use rather than special casing each modem. New modems can be supported through modem scripts rather than new releases of client software. This greatly reduces support cost for both client developer and modem vendor. By using a common interface, developers of client software can also reduce conflicts.  Is there any documentation or SDKs available?  A: At this time, there is no official SDK or support for third party access to the Open Transport Modem/Script engine. However, it is possible (and quite easy) to use the Open Transport API to access this functionality.    |  | | --- | | __Note:__  USE THE FOLLOWING INFORMATION AT YOUR OWN RISK!! THIS IS NOT SUPPORTED BY DTS AND COULD (WILL PROBABLY) CHANGE IN THE FUTURE. |    The Open Transport Modem/Script engine consist of a number of things including a "OpenTpt Modem" library, the "Modems" control panel and a directory called "Modem Scripts". These files are installed as part of the Open Transport/PPP and ARA 3.0 distribution.  Once the "OpenTpt Modem" module is installed and configured, you can simply open an OT endpoint to the Modem/Script engine in the same manner as you would an OT Serial endpoint with the exception that you pass "Script" in the config field.   |  | | --- | | ``` Err = OTAsyncOpenEndpoint( OTCreateConfiguration("Script"), .....) ``` |   This endpoint will act like a serial endpoint, the `OT_CONNECT` will initialize the connection, disconnect etc. In fact, you should be able to pass in the phone number from the Connect in the addr field. Since there is no `OpenTransportModem.h` file available, you will need some of the following information:   |  | | --- | | ``` // The Configuration name for the Opentransport Modem/Script engine         #define kScriptName "Script" // To check if the  Modem/Script engine is installed you should interrogate // the proper Gestalt Selectors for Open Transport-based Modem libraries. #define gestaltOpenTptModem             'otmo' #define gestaltOpenTptModemPresent      0 #define gestaltOpenTptModemVersion      'otmv' #define kGestaltOpenTptModemVersion     0x01000080 // Note: possible values for the "stage" byte are: // development = 0x20, alpha = 0x40, beta = 0x60, final & release = 0x80 // These are the  Modem/Script Configurator error codes.  Other codes may be // returned from Open Transport and operating system routines. #define kModemNoError               0 #define kModemOutOfMemory           -14000 #define kModemPreferencesMissing    -14001 #define kModemScriptMissing         -14002 ``` |   Since you either have to set the modem type manually through the Modems Control panel, or hack the Modem Configuration pref file yourself (all warnings// apply) it might be helpful to know a few things about the Modem preference file.   |  | | --- | | ``` // The Modem Configuration pref resource file  constants.     kModemConfigFileCreator     = 'modm',     kModemConfigFileType        = 'mdpf',     kModemConfigVersion         = 0x00010000,     kModemConfigExportType      = 'mdex',     kModemScriptType            = 'mlts',   // Same as ARA 1.0/2.0     kModemScriptCreator         = 'slnk',   // Same as ARA 1.0/2.0 // Configuration resource constants.     kModemConfigTypeModem       = 'ccl ',   // Type for Modem config resource     kModemSelectedConfigID      = 1,        // ID of resource containing..     kModemSelectedConfigType    = 'ccfg',   // the ID of current selected CCL     kModemConfigNameType        = 'cnam',   // type of config name rez     kModemConfigTypeLocks       = 'lkmd',   // Types for lock rez     kModemConfigFirstID         = 128       // lowest id for configuration rez // Maximum script file name size.  Same as \ // "name" field of FSSpec kMaxScriptNameSize = 64 // File name to use only if the internationalized one can't be read // from the resource fork.     #define kDefaultModemPrefsFileName  "\pModem Preferences" // Dial tone modes     enum     {         kDialToneNormal = 0,         kDialToneIgnore = 1,         kDialToneManual = 2     }; //  Modem Configuration //  Resource format for Modem configuration info.     typedef struct     {         UInt32      version;         Boolean     useModemScript;         FSSpec      modemScript;         Boolean     modemSpeakerOn;         Boolean     modemPulseDial;         UInt32      modemDialToneMode;         SInt8       lowerLayerName[kMaxProviderNameSize];     } RAConfigModem; ``` | |

#### [Jul 11 1997]

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
