---
title: Gestalt Selectors for Macintosh Networking
apple_id: DTS10001453
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-01-31'
source_url: https://developer.apple.com/library/archive/qa/nw/nw41.html
archived_at: '2026-07-18T02:29:46.518778Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW41Gestalt Selectors for Macintosh Networking |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: What are the different Gestalt selectors for Macintosh networking?  A: Here is the breakdown: MacTCPThe `Gestalt` selector for MacTCP is '`mtcp`'.  - MacTCP versions 1.0 through 1.0.3 did not register this selector. - MacTCP version 1.1 returns a value of 1. - MacTCP version 1.1.1 returns a value of 2. - MacTCP version 2.0 returns a value of 3.   A value of 0 is returned if the driver is not opened. AppleTalk The `Gestalt` selectors for AppleTalk are '`atkv`' and '`atlk`'.  The '`atlk`' `Gestalt` selector was introduced in AppleTalk version 54 to provide basic version information. Calling `Gestalt` with the '`atlk`' selector provides the major revision version in the low-order byte of the function result. For example, passing the '`atlk`' selector in a `Gestalt` call or through MacsBuG with a result of `0x0000003C` means that AppleTalk version 60 is present. (Please note that the '`atlk`' selector is not available when AppleTalk is turned off in the Chooser.)  The '`atkv`' Gestalt selector was introduced as an alternative in AppleTalk version 56 to provide more complete version information via the '`vers`' resource. For example, passing the '`atkv`' selector to AppleTalk version 60 through a `Gestalt` call or MacsBuG yields the following `LONGINT` result: `0x3C108000`. Open Transport The Gestalt selectors for Open Transport are '`otan`' and '`otvr`'. You can test whether Open Transport and its various parts are available by using the Gestalt function with the '`otan`' selector. The bits currently used are defined by constants, defined in OpenTransport.h and shown below.   |  | | --- | | ``` enum {         gestaltOpenTpt                   = 'otan',         gestaltOpenTptPresent           = 0x00000001,         gestaltOpenTptLoaded            = 0x00000002,         gestaltOpenTptAppleTalkPresent  = 0x00000004,         gestaltOpenTptAppleTalkLoaded   = 0x00000008,         gestaltOpenTptTCPPresent        = 0x00000010,         gestaltOpenTptTCPLoaded         = 0x00000020,         gestaltOpenTptNetwarePresent    = 0x00000040,         gestaltOpenTptNetwareLoaded     = 0x00000080 }; ``` |   If `Gestalt` returns no error and responds with a non-zero value, Open Transport is available. To find out whether OT, AppleTalk, TCP, or NetWare are present, you can examine the response parameter bits as shown above. For example, passing the '`otan`' selector in a `Gestalt` call or through MacsBuG with a result of `0x0000001F` means that the Open Transport is present and loaded, AppleTalk driver is also present and loaded, and MacTCP is present but NOT loaded.  The '`otvr`' selector is used to determine the Open Transport Version in `NumVersion` format. For example, passing the '`otvr`' selector through a `Gestalt` call or MacsBuG to OT version 1.1.1b9 yields the following `LONGINT` result: `0x01116009`. (Note that OT versions 1.0 through 1.0.8 did not register this selector.) For more information on Apple's Version Numbering Scheme and `NumVersion` format, please see [Technote OV12:Version Territory.](https://developer.apple.com/library/archive/technotes/ov/ov_12.html) Open Transport / PPP The `Gestalt` selectors for Open Transport / PPP are '`otra`' and '`otrv`'. You can test whether Open Transport / PPP and its various parts are available by using the `Gestalt` function with the '`otra`' selector. The bits currently used are defined by constants, defined in OpenTptPPP.h check [OT/PPP SDK](https://developer.apple.com/library/archive/sdk/index.html) and shown below.   |  | | --- | | ``` enum {         gestaltOpenTptRemoteAccess      = 'otra',         gestaltOpenTptRemoteAccessPresent       = 0x00000000,         gestaltOpenTptRemoteAccessLoaded        = 0x00000001,         gestaltOpenTptRemoteAccessClientOnly    = 0x00000002,         gestaltOpenTptRemoteAccessPServer       = 0x00000003,         gestaltOpenTptRemoteAccessMPServer      = 0x00000004,         gestaltOpenTptPPPPresent                = 0x00000005,         gestaltOpenTptARAPPresent               = 0x00000006  }; ``` |     |  | | --- | | __Note:__  If you are writing an control strip or startup item that uses OpenTransport / PPP you should be aware that it takes a few event cycles for the remote access software to complete loading. Your software should check the `gestaltOpenTptRemoteAccessPresent` bit of the 'otra' gestalt to see if remote access software is present, then periodically check the `gestaltOpenTptRemoteAccessLoaded` to determine if loading is completed. |    More information on accessing using the Open Transport / PPP API is available in the [Open Transport documentation.](https://developer.apple.com/documentation/mac/NetworkingOT/NetworkingWOT-2.html) Open Transport / Modem The `Gestalt` selectors for Open Transport/Modem are '`otmo`' and '`otmv`'. You can test whether Open Transport/ Modem and its various parts are available by using the Gestalt function with the '`otmo`' selector.   |  | | --- | | ``` enum {         gestaltOpenTptModem         = 'otmo',         gestaltOpenTptModemPresent      = 0x00000000  }; ``` | |

#### [Jan 31 1997]

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
