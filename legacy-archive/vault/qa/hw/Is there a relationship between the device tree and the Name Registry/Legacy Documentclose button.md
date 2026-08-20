---
title: Is there a relationship between the device tree and the Name Registry?
apple_id: DTS10001313
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-02-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw41.html
archived_at: '2026-07-18T02:29:37.336708Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Apple Hardware](https://developer.apple.com/referencelibrary/HardwareDrivers/idxAppleHardware-date.html)

|  |
| --- |
| Technical Q&A HW41Is there a relationship between the device tree and the Name Registry? |

|  |
| --- |
| ---   Q: Is there a relationship between the device tree and the Name Registry?  A: The device tree is an Open Firmware entity that describes the topology of the motherboard and more. See IEEE 1275 Section 3. "Device Tree" for details.  During the boot sequence, the Mac OS interacts with Open Firmware to move part of the device tree into the Name Registry. However, the Name Registry is a Mac OS database and subject to change. At present, the device tree is a node in Name Registry. In short, they are related, with the Name Registry being a super set of the device tree. |

#### [Feb 15 1999]

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
