---
title: Differences between iMac models
apple_id: DTS10001304
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-01-25'
source_url: https://developer.apple.com/library/archive/qa/hw/hw32.html
archived_at: '2026-07-18T02:29:36.704598Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Apple Hardware](https://developer.apple.com/referencelibrary/HardwareDrivers/idxAppleHardware-date.html)

|  |
| --- |
| Technical Q&A HW32Differences between iMac models |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: What are the differences between the iMac rev A, B & iMac 266 models?  A: There are a number of changes among the three revisions the iMac that are relevant to Mac developers. The first iMac (rev A) was built with a different logic board than the Rev B and iMac 266 models.  As far as actual part numbers are concerned, the iMac 266 is not classified as a revision C; it is actually a revision A product and has been assigned new part numbers (one for each color). Part numbers  | Part Number | Model | Color | | --- | --- | --- | | M6709LL/A | iMac Rev A | Bondi Blue | | M6709LL/B | iMac Rev B | Bondi Blue | | M7389LL/A | iMac 266 | Strawberry | | M7392LL/A | iMac 266 | Lime | | M7391LL/A | iMac 266 | Tangerine | | M7390LL/A | iMac 266 | Grape | | M7345LL/A | iMac 266 | Blueberry |  Mezzanine Connector Earlier iMac models (revision A & B) included an internal connector that some sources referred to as the _Mezzanine connector._ This connector was intended for Apple's initial internal development and manufacturing purposes, and was never at any time supported for third-party development. Thus, it has been removed from the logic board. Floppy support The iMac revision A & B had provisions for an internal floppy disk connector that was intended for initial internal development and manufacturing purposes. This connector and associated ROM code was never supported for third-party development and thus was also removed from the logic board.  Floppy drives are, however, supported as USB peripherals and available from a number of third parties. Note: The currently version of USB software does not support booting from a floppy device. IrDA The iMac 266 has removed the IrDA port. However, IrDA is still very important for portables, but their usage and user requirements are different from desktop Macs. In addition, due to the success of USB, Apple has decided to focus on USB as the primary method of connecting peripherals to desktop computers. Graphics Acceleration Hardware The iMac rev A was shipped with the ATI RAGE IIc graphics controller and 2 MB of video memory. The rev B & iMac 266 have been updated with the higher performance ATI RAGE PRO TURBO accelerated 2D/3D graphics controller and 6MB (2 MB Built-in + 4 MB DIMM) of video memory. RAM There are no changes to iMac memory expandability between models. USB Revision A iMacs were shipped with USB 1.0, while revision B iMacs shipped with USB 1.0.1. "iMac Update 1.0" can be used to update rev A iMacs to USB 1.0.1. The 266 Mhz iMacs feature USB 1.1.  USB 1.1 fixes several significant bugs in the notification of new devices, as well as improves the robustness of hot-plugging. The USB 1.1 kit installs Zip and SuperDisk drivers, Game Sprockets (which includes drivers for about a dozen controllers/joysticks). USB 1.1 also includes the HP and Epson printer drivers in CD Extras folder.  Both Revision A and B iMacs can be upgraded to USB 1.1 with "iMac Update v1.1". Note that in order to use this update on a Rev A. iMac, Mac OS System Software 8.5 must be present. System Software Below is a table of system software shipped with each revision of iMac.   | iMac Model | Mac OS | USB | | --- | --- | --- | | Rev - A | 8.1 | 1.0 | | Rev - B | 8.5 | 1.0.1 | | iMac 266 | 8.5.1 | 1.1 |  Specifications The latest spec sheet for the iMac can be found at the [iMac specification page](http://www.apple.com/imac/techspecs.html). |

#### [Jan 25 1999]

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
