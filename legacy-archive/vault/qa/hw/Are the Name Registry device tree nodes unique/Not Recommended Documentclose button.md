---
title: Are the Name Registry device tree nodes unique?
apple_id: DTS10001336
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-10-11'
source_url: https://developer.apple.com/library/archive/qa/hw/hw64.html
archived_at: '2026-07-18T02:29:38.681960Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/index.html) > [Open Firmware](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/idxOpenFirmware-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Open Firmware](https://developer.apple.com/referencelibrary/HardwareDrivers/idxOpenFirmware-date.html)

|  |
| --- |
| Technical Q&A HW64Are the Name Registry device tree nodes unique? |

|  |
| --- |
| ---   Q: Are the Name Registry device tree nodes unique?  A: No, the unit addresses from the Open Firmware device tree were not copied to the Name Registry. This means that there may be more than one node with the same name. For instance using a B&W G3, the PCI bridge node as viewed with the "Display Name Registry" utility has a name called "/pci". When viewed using the Open Firmware user interface the same node is displayed as `/pci@80000000`. The name "pci" is generic per the Recommended Practices for IEEE 1275. When searching the Name Registry for a string, remember to first determine how many PCI nodes there are in the device tree. Your search algorithm can then search each node until the individual searches are complete. |

#### [Oct 11 1999]

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
