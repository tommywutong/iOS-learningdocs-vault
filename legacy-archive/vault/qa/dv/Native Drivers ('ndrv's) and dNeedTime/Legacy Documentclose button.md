---
title: Native Drivers ('ndrv's) and dNeedTime
apple_id: DTS10001176
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-04-26'
source_url: https://developer.apple.com/library/archive/qa/dv/dv35.html
archived_at: '2026-07-18T02:29:27.730318Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A DV35Native Drivers ('ndrv's) and dNeedTime |

|  |
| --- |
| ---   Q: I'm writing a native driver and I've noticed that, if I set `dNeedTime` in the `dCtlFlags` fields of my `DCtlEntry`, I never receive `accRun` events and the system crashes when my driver unloads. What's going on?  A: The designers of the native driver model felt that native driver should not access the Device Control Entry (DCE) and would never need system task time. Therefore, they reused a number of fields in the DCE for other purposes. The reused fields include:   - `dCtlCurTicks` - `dCtlStorage` - `dCtlOwner` - `dCtlWindow`   For native drivers, these fields are now __reserved__. Your software must not rely on their value nor modify them, either explicitly or implicitly. Setting `dNeedTime` causes the system to modify the value of `dCtlCurTicks`, which causes the system crash when it accesses `dCtlCurTicks` as it unloads your driver.  If you need system task time in your native driver, you should use the support provided by your driver's I/O family. For example, FireWire drivers can use `FWSendSoftwareInterrupt`, while drivers that use Open Transport can use `OTScheduleSystemTask`. If your driver has no I/O family, or its I/O family does not provide support for getting system task time, your only recourse is to use one of the techniques outlined in Technote 1033, ["Interrupts in Need of (a Good) Time"](https://developer.apple.com/library/archive/technotes/tn/tn1033.html). For native drivers, the best approach described by that technote is probably Approach #3.  External software can tell whether a driver is native by looking at bit 3 of the `dCtlFlags`, as described in DTS Q&A DV 27 [Device Driver Flags](Legacy%20Documentclose%20button-2.md).  The issue that native drivers can't get system task time is being tracked as bug ID 2323538. |

#### [Apr 26 1999]

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
