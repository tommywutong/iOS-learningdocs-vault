---
title: Asserting fast-back-to-back transfers in the PCI Power Mac
apple_id: DTS10001294
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw22.html
archived_at: '2026-07-18T02:29:36.290842Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A HW22Asserting fast-back-to-back transfers in the PCI Power Mac |

|  |
| --- |
| ---   Q: Does the PCI controller in the PCI Power Macs ever assert, or is it capable of ever asserting fast-back-to-back transfers? This data transfer mode is listed under Reserve Name Registry property names in the March 9, 1995 version of _Designing PCI Cards and Drivers for Power Macintosh Computers._ If this transfer mode is implemented, how can it be invoked by system software for testing purposes?  A: The answer to the first part of your question -- does the PCI controller in the PCI Power Macs ever assert, or is it capable of ever asserting fast-back-to-back transfers? -- is no. It can respond to fast-back-to-back transfers correctly, but it will never generate fast-back-to-back cycles.  As for the second part of your question, the property fast-back-to-back will appear in a PCI device's standard PCI properties if its PCI Configuration space Status register's fast-back-to-back-capable bit is asserted. If all devices on a PCI Bus have this property (i.e., are fast-back-to-back-capable), the system software will enable all devices fast-back-to-back-enable bits in their PCI Configuration space Command registers. That is all the property fast-back-to-back is used for.  Again, the PCI bridge chip on the PCI PowerMacs will not generate fast back to back cycles, but other masters in the system could, so your device should be able to respond to them correctly. In fact, it is a requirement from the PCI Compliance Checklist that you respond correctly to fast-back-to-back cycles. The PCI Compliance Checklist is available from the PCI SIG. |

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
