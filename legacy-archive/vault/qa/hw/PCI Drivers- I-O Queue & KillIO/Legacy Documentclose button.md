---
title: 'PCI Drivers: I/O Queue & KillIO'
apple_id: DTS10001289
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw17.html
archived_at: '2026-07-18T02:29:35.992247Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A HW17PCI Drivers: I/O Queue & KillIO |

|  |
| --- |
| ---   Q: Does the PCI Device Manager handle calls to drivers and the `KillIO` command the same way as the current Device Manager (all calls to drivers are treated as asynchronous calls)? If so, does this mean that the driver has control?  A: The PCI Device Manager handles `KillIO` the same way that the current Device Manager does. This means that you are issued one `killIO` (since they are delivered immediately), with the PB pointing to the block that needs to be killed. The Device Manager then walks the queue and removes and terminates all pending entries (it calls `IOCommandCompleted` with abort status).  This is only an issue if you maintain an internal queue (take entries off the device queue yourself). If you do this, you can either put the entries back or call `IOCommandCompleted` yourself. |

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
