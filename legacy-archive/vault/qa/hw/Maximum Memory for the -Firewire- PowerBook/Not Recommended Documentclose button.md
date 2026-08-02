---
title: Maximum Memory for the "Firewire" PowerBook
apple_id: DTS10001355
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-03-13'
source_url: https://developer.apple.com/library/archive/qa/hw/hw83.html
archived_at: '2026-07-18T02:29:39.732353Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/index.html) > [Apple Hardware](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/idxAppleHardware-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Apple Hardware](https://developer.apple.com/referencelibrary/HardwareDrivers/idxAppleHardware-date.html)

|  |
| --- |
| Technical Q&A HW83Maximum Memory for the "Firewire" PowerBook |

|  |
| --- |
| ---   Q: There appears to be some discrepancies between the maximum memory configurations published for the new "FireWire" Powerbook.  The PowerBook Developer Note says that the maximum memory is 1GB, but the updated TIL articles 14870 and 58582 say that it's 512MB. Which is correct?  A: Actually, all of the documents are correct, provided you read the complete PowerBook Developer Note concerning SDRAM.  The Developer Note states that "An SO-DIMM using currently available parts can contain either 32, 64, 128, 256, or 512 MB of memory. The computer can support up to 1 GB total RAM using the highest-density devices available, but SO-DIMMs made with such devices may draw too much current in sleep mode to allow battery sleep swapping. See RAM SO-DIMM Electrical Limits." Click [here](https://developer.apple.com/documentation/hardware/Developer_Notes/Macintosh_CPUs-G3/PowerBook/PowerBook-92.html) for the PowerBook Developer Note on RAM Expansion Slots. Note that the developer note differentiates between "currently available parts", current draw, and "Electrical Limits."  Following the documentation URL thread to the "Electrical Limits" section, the developer note suggests that if 512MB SO-DIMMs existed and they could meet the current requirements specified, the new Powerbooks would support the full 1GB configuration. This means there are no OS or addressing restrictions to support 1GB of memory.  Click [here](https://developer.apple.com/documentation/hardware/Developer_Notes/Macintosh_CPUs-G3/PowerBook/PowerBook-99.html) for the PowerBook Developer Note on RAM SO-DIMM Electrical Limits.  The TIL articles, therefore, have decided to tackle the current practical memory limits while the Developer Note has attempted to address the theoretical limits for developers. Since the focus of the developer note is toward development, there may be new DRAM technologies able to meet the powerbook's SO-DIMM requirements. |

#### [Mar 13 2000]

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
