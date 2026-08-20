---
title: Device Driver Flags
apple_id: DTS10001168
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-03-14'
source_url: https://developer.apple.com/library/archive/qa/dv/dv27.html
archived_at: '2026-07-18T02:29:26.705549Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [Native Drivers ('ndrv's) and dNeedTime](Legacy%20Documentclose%20button.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A DV27Device Driver Flags |

|  |
| --- |
| ---   Q: I'm debugging my PCI native driver and notice that the `dCtlFlags` field of my Device Control Entry (DCE) has some undocumented bits set. What do these flags mean?  A: The current bits in the `dCtlFlags` field of the DCE are:   - bit 0 -- `VMImmune` -- This bit indicates that your device driver is VM   safe. See [Technote NW 13](https://developer.apple.com/library/archive/technotes/nw/nw_13.html) for details. - bit 1 -- reserved - bit 2 -- `kmDriverGestaltEnableMask` (in "DriverGestalt.h") is set if the   driver supports the Driver Gestalt mechanism. See "Designing PCI Cards and   Drivers for Power Macintosh Computers" for a description of Driver Gestalt. - bit 3 -- Native Driver -- Set if the driver is a native driver (`ndrv`).   The system will set this bit when it loads your native driver. - bit 4 -- Concurrent -- Set if the native driver supports concurrent   operation. When loading a native driver, the system sets this bit based on the   `kDriverIsConcurrent` field of the `driverOSRuntimeInfo.driverRuntime` field of your   DriverDescription. See "Designing PCI Cards and Drivers for Power Macintosh   Computers" for a description of concurrent drivers. - bit 5 -- `dOpenedMask` (in "Devices.h") is set if the driver is open. - bit 6 -- `dRAMBasedMask` (in "Devices.h") is set if the `dCtlDriver` field   is a `DRVRHeaderHandle` rather than `aDRVRHeaderPtr` . - bit 7 -- `drvrActiveMask` (in "Devices.h") is set if the driver is   currently processing a request. - bit 8 -- `dReadEnableMask` (in "Devices.h") is set if the driver handles   _Read requests. - bit 9 -- `dWritEnableMask` (in "Devices.h") is set if the driver handles   _Write requests. - bit 10 -- `dCtlEnableMask` (in "Devices.h") is set if the driver handles   _Control requests. - bit 11 -- `dStatEnableMask` (in "Devices.h") is set if the driver handles   _Status requests. - bit 12 -- `dNeedGoodByeMask` (in "Devices.h") is set if the driver needs a   "goodbye" _Control call before the application heap is reinitialized. - bit 13 -- `dNeedTimeMask` (in "Devices.h") is set if the driver wants   periodic SystemTask time through the "accRun" _Control call. - bit 14 -- `dNeedLockMask` (in "Devices.h") is set if the driver requires   that its DCE and code be locked at all times when the driver is open. - bit 15 -- reserved   See ["_Inside Macintosh_:Devices"](https://developer.apple.com/documentation/mac/Devices/Devices-2.html) for more information about bits 5 through to 14. |

#### [Mar 10 1997]

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
