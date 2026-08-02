---
title: PCI Card's Assigned-Address Properties
apple_id: DTS10001292
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw20.html
archived_at: '2026-07-18T02:29:36.162389Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A HW20PCI Card's Assigned-Address Properties |

|  |
| --- |
| ---   Q: I'm in the process of developing a PCI device driver. How do I get from local addresses on the card to addresses that the Mac understands belong to my card. My card has 2 memory areas I need to deal with. Do I add the local starting address to the assigned address that's assigned during start up?  A: Your PCI card's memory space(s) has assigned-address property(ies) in the Name Registry.  The configuration your card requests - in this case, two memory spaces - is defined by the card's configuration space. At boot time, the Mac's Open Firmware (also called boot firmware) scans all PCI devices and constructs a Device Tree containing information about configured PCI devices. (Your card's memory space will be reassigned into available PCI address space at this time.) The Device Tree is the structure from which the Mac OS extracts the original information to create the device portion of the Name Registry. You'll need to obtain the assigned addresses for your card's memory spaces from the Name Registry.  Refer to the latest PCI DDK (Driver Developer Kit), and _Designing PCI Cards and Drivers for Power Macintosh Computers._Also, for code examples on how to access and iterate the Name Registry, refer to the `DisplayNameRegistry` sample on the DDK. |

#### [Jul 15 1995]

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
