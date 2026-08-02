---
title: Using Legacy Ethernet Driver Processes on a PowerMac G3
apple_id: DTS10001469
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-02-08'
source_url: https://developer.apple.com/library/archive/qa/nw/nw57.html
archived_at: '2026-07-18T02:29:47.359946Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A NW57Using Legacy Ethernet Driver Processes on a PowerMac G3 |

|  |
| --- |
| ---    ---   __Q:__ I have a legacy application which uses the outdated Ethernet Driver APIs as described in the ENET.h interface file. The application has worked on all Power Macintosh models except for the Power Macintosh G3 systems using Mac OS 8.1. Is there any way for this application to work on a Power Macintosh G3 system?  A: There is a known issue with the older Power Macintosh G3 systems: the processes which used the legacy Ethernet APIs no longer work on these systems. These processes could not open the built-in Ethernet driver. This problem was addressed with the Power Macintosh G3 systems released beginning January 1999.  __Ethernet Shim History__  With the release of the first PCI-based Power Macintosh systems, an Ethernet shim was built into the System to support processes which used the Ethernet Driver API. On a PCI Power Macintosh, the Ethernet driver is native PowerPC code and is based on the Data Link Provider Interface (DLPI) for communications with client processes. The Ethernet Shim translates the Ethernet Driver API calls into DLPI equivalents and passes them on to the built-in driver. For incoming packets, the DLPI driver passes appropriate packets to the Ethernet shim, which in turns calls the Ethernet protocol handler, or looks for a queued `ENETRead` parameter block call to pass the packet.  The Ethernet shim was designed to support only the built-in Ethernet device, and not PCI Ethernet cards which are plugged into the various slots. The use of this shim required a specific coding change for some processes. In order to use the shim, the process could not use the `OpenDriver` call. Instead, the process was required to use the Slot Manager call `SGetTypeSRsrc` to identify the built-in Ethernet service, then use the `OpenSlot` call to open the Ethernet device in slot 0 to obtain the device `refNum`. The device `refNum` is used in all subsequent calls to the legacy .ENET API. Refer to [Inside Macintosh:Networking, Chapter 11 Listing 11-1](https://developer.apple.com/documentation/mac/Networking/Networking-262.html#HEADING262-6) for an example of this method. This code change applies to legacy Ethernet processes only.  __How the Ethernet Shim Works__  The Ethernet shim works by registering a device `sRsrc` with the Slot Manager for the built-in Ethernet hardware. When the `SGetTypeSRsrc` call is made to identify Ethernet services present, the device `sRsrc` for the built-in port, is returned. By using the `OpenSlot` call, the shim unit table driver was loaded and the driver `refNum` returned to the caller. The driver shim processed the standard `Open`, `Control`, `Status`, and `Close` calls to the Ethernet driver by translating each call into their DLPI (Data Link Provider Interface) message equivalent, and passing them to the DLPI driver for the built-in Ethernet hardware. The shim driver installed a packet handler with the DLPI driver so that it would be notified of incoming packets destined for the Ethernet shim clients.  The shim driver process worked well until the release of the Power Macintosh G3 system. With the Power Macintosh G3 systems released in 1997 - 1998, a change to the ROM broke the mechanism by which the Ethernet shim was able to register built-in Ethernet services with the Slot Manager. As a result, the calls to `SGetNextSRsrc` and `OpenSlot` fail.  __Workaround__  A workaround was implemented for Mac OS 8.5 such that, during startup, the System identified the original Power Macintosh G3 systems and installed the .ENET device driver into the unit table. A problem with this solution was that most legacy processes had already made the change to using the `OpenSlot` call; they no longer used the `OpenDriver` call. Many of these legacy processes included backup code to try to open the .ENET0 driver using the `OpenDriver` call, if the call to open a slot-based Ethernet driver failed. To accommodate these processes, Mac OS 8.5 also installs a copy of the ethernet shim driver with the .ENET0 name. If the legacy software still fails, then a possible alternative is to modify the code to make the `OpenDriver` call on the .ENET driver, if the `OpenSlot` call fails.  To summarize, it is a known issue that processes which use the legacy Ethernet API will fail when run on a Power Macintosh G3 system released in 1997 or 1998 running either Mac OS 8.0 or 8.1. This problem may be solved by using Mac OS 8.5 on these affected systems. |

#### [Feb 08 1999]

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
