---
title: MemError
apple_id: DTS10001410
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-09-12'
source_url: https://developer.apple.com/library/archive/qa/me/me06.html
archived_at: '2026-07-18T02:29:43.835676Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Audio > Hardware & Drivers](https://developer.apple.com/referencelibrary/MusicAudio/idxHardwareDrivers-date.html)
- [Games > Porting](https://developer.apple.com/referencelibrary/Games/idxPorting-date.html)
- [Hardware & Drivers > ATA](https://developer.apple.com/referencelibrary/HardwareDrivers/idxATA-date.html)
- [Hardware & Drivers > Audio](https://developer.apple.com/referencelibrary/HardwareDrivers/idxMusicAudio-date.html)
- [Hardware & Drivers > Ethernet](https://developer.apple.com/referencelibrary/HardwareDrivers/idxEthernet-date.html)
- [Hardware & Drivers > FireWire](https://developer.apple.com/referencelibrary/HardwareDrivers/idxFireWire-date.html)
- [Hardware & Drivers > Human Interface Device & Force Feedback](https://developer.apple.com/referencelibrary/HardwareDrivers/idxHumanInterfaceDeviceForceFeedback-date.html)
- [Hardware & Drivers > Networking](https://developer.apple.com/referencelibrary/HardwareDrivers/idxNetworking-date.html)
- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)
- [Hardware & Drivers > Printing](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPrinting-date.html)
- [Hardware & Drivers > Scanners](https://developer.apple.com/referencelibrary/HardwareDrivers/idxScanners-date.html)
- [Hardware & Drivers > SCSI](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSCSI-date.html)
- [Hardware & Drivers > Serial](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSerial-date.html)
- [Hardware & Drivers > Still Cameras](https://developer.apple.com/referencelibrary/HardwareDrivers/idxStillCameras-date.html)
- [Hardware & Drivers > Storage](https://developer.apple.com/referencelibrary/HardwareDrivers/idxMassStorageDevices-date.html)
- [Hardware & Drivers > USB](https://developer.apple.com/referencelibrary/HardwareDrivers/idxUSB-date.html)
- [Networking > Hardware & Drivers](https://developer.apple.com/referencelibrary/Networking/idxHardwareDrivers-date.html)
- [Printing > Hardware & Drivers](https://developer.apple.com/referencelibrary/Printing/idxHardwareDrivers-date.html)

|  |
| --- |
| Technical Q&A ME06MemError |

|  |
| --- |
|  Q: When I am debugging my application `MemError` always returns `noErr`. What's wrong with `MemError`?  A: Nothing, if you are debugging your application with a high level debugger. High level debuggers often call Memory Manager routines while stepping through your code. When a Memory Manager routine is called, it sets `MemError` and in this case, the debugger's memory request was successful (it returned `noErr`) and cleared your application's `MemError` result.  The solution to this problem is often just to not step over Memory Manager calls and the call to `MemError`. If you put a break point just after the `MemError` call, you usually get the correct error - the one your application would see if it wasn't running in the debugger.  The other option is to use a low level debugger such as MacsBug to debug your memory allocation problems.  As a general rule your application should check the value of the handle or pointer returned by `NewHandle`, `NewPtr`, etc: and if it is nil, you should call `MemError` for an error number. Just calling `MemError` without checking the value of the handle/pointer is not a good idea. [Sep 12 1997] |

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
