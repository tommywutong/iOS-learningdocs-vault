---
title: Accessing the ARA/PPP password
apple_id: DTS10001468
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/nw/nw56.html
archived_at: '2026-07-18T02:29:47.301590Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A NW56Accessing the ARA/PPP password |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---    ---   Q: My code needs to set the password used by ARA/PPP, but I can't find any documentation on how the password works. How do I create a password resource?  A: The Open Transport ARA/PPP password for a given configuration is stored in the `'pass'` resource of the "Remote Access Connections" file, which resides in the "Remote Access" preference folder. As of ARA version 2.0, the size of the `'pass'` resource has been extended to 256 bytes.  The actual password data is encoded using the Data Encryption Standard (DES) algorithm in Electronic Code Book (ECB) Mode. The key schedule for the encryption is derived from the first 56 bits (7 bytes) of the ARA/PPP configurations user name.  Currently there is no Open Transport API for encoding the ARA password. However, since the password is encoded using ECB mode of DES, it is possible to use the `PassWordMunger` function of the older Apple Remote Access API to encode a modern ARA/PPP password.  To properly encode the password, you must first zero pad the password data in a 256-byte buffer. Then, encode the cleartext password 8 bytes at a time using the user name string as a key, appending the result to the `'pass'` resource until all 256 bytes are processed. When you have completed this, zero out the first byte of the `'pass'` resource.  This process is illustrated in the following code snippet, taken from the MoreNetworkSetup module of the DTS MoreIsBetter library.   |  | | --- | | ``` static OSStatus EncodeRemotePasswordARA(                                 ConstStr255Param userName,                                 ConstStr255Param password,                                 Str255 encodedPassword)     // Encodes a password using the ARA API. {     OSStatus err;     TRemoteAccessPasswordMunger pb;     UInt8 chunkOfPassword[9];     ByteCount offset;       // Zero the encoded password buffer and copy the     // password (sans length byte) into it.      OTMemzero(encodedPassword, sizeof(Str255));     BlockMoveData(&password[1], encodedPassword, password[0]);      // Now walk through the password in chunks, copying     // a chunk into the chunkOfPassword buffer, encrypting     // that buffer with the ARA API, and then copying the     // buffer back out to the encrypted password.      // Note that the for loop increments offset by 8 each time.       for (offset = 0; offset < 256 ; offset += 8) {          // Copy a chunk of the password into chunkOfPassword.          BlockMoveData(encodedPassword + offset, &chunkOfPassword[1], 8);         chunkOfPassword[0] = 8;           // Setup the parameter block for a remote access API call.           pb.csCode       = RAM_EXTENDED_CALL;         pb.resultStrPtr = nil;         pb.extendedType = (char*) REMOTEACCESSNAME;         pb.extendedCode = CmdRemoteAccess_PassWordMunger;         pb.userNamePtr  = (UInt8 *) userName;         pb.passWordPtr  = chunkOfPassword;         pb.reserved     = 0;           err = PBRemoteAccess((TPRemoteAccessParamBlock) &pb, false);         if (err == noErr) {             err = pb.ioResult;         }         if (err == noErr) {               // Copy the encrypted chunk of password back out into             // encodedPassword.              BlockMoveData(&chunkOfPassword[1], encodedPassword + offset, 8);         } else {             break;         }     }       // Tidy up encoded password.  Move the encrypted data up     // one byte and insert a zero length byte.  Don't ask me     // why this is required, I didn't invent this scheme (-:       BlockMoveData(encodedPassword, encodedPassword + 1, sizeof(Str255) - 1);     encodedPassword[0] = 0;      return err; } ``` |   Once you have processed the encoded the password, you can set the actual `'pass'` resource in a number of ways:   1. The preferred method is to use the Network Setup    API, which is part of Open Transport 2.0 included    with MacOS 8.5. The Network Setup SDK really is the    proper long-term solution to accessing the configuration    database. A good example of how to use this API can be    found in the DTS sample code    [More    NetworkSetup](ftp://ftp.apple.com/developer/Sample_Code/Networking/MoreNetworkSetup.sit). 2. As an alternative, you can send an AppleEvent to    _Network Setup Scripting_ to set the password for a    given configuration. This is described below.    __Note:__ Version 1.0 of _Network Setup    Scripting_ does not encode the password properly; use    version 1.0.2 or newer.  |  | | --- | | ``` --setpassword("Configuration", "password")    on setpassword(configName, thePassword)     tell application "Network Setup Scripting"         open database         begin transaction          set password of Remote Access configuration configName to thePassword          end transaction          close database     end tell end setpassword   ``` |     3. As a last resort, your code could open and write into    the "Remote Access Connections" file directly. This    method is risky and I highly recommend against it. Since    ARA could open it at any time, you run the risk of    corrupting the file's resource map. There is also no    promise that the preference file data formats will not    change in the future.   At some point in the future, we hope that the Network Setup API will provide an interface for encoding the password. Until that happens, the above example should be sufficient.   |  |  | | --- | --- | | Further Reference: | [Inside Macintosh: Open Transport](https://developer.apple.com/documentation/macos8/NetworkCommSvcs/OpenTransport/opentransport.html)  [Sample Code: MoreNetworkSetup](ftp://ftp.apple.com/developer/Sample_Code/Networking/MoreNetworkSetup.sit) | |

#### [May 17 1999]

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
