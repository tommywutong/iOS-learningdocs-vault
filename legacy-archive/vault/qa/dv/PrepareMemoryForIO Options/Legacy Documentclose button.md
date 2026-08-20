---
title: PrepareMemoryForIO Options
apple_id: DTS10001185
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-09-22'
source_url: https://developer.apple.com/library/archive/qa/dv/dv44.html
archived_at: '2026-07-18T02:29:28.359534Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A DV44PrepareMemoryForIO Options |

|  |
| --- |
| ---   Q: I am calling `PrepareMemoryForIO`. What is the meaning of the `kIOShareMappingTables` bit of the options field of the `IOPreparationTable`? I've read the documentation in [Designing PCI Cards and Drivers for Power Macintosh Computers](https://developer.apple.com/documentation/hardware/DeviceManagers/pci_srvcs/pci_cards_drivers/index.html) and it didn't really help.  A: In all existing implementations this bit does nothing. This oversight is an artifact of the difference between the DriverServicesLib model and its implementation on traditional Mac OS. See DTS Q&A DV 43 [InterfaceLib and Native Drivers](../Coordinating%20Deferred%20Tasks%20and%20Secondary%20Interrupts/Legacy%20Documentclose%20button-2.md) for more information on that topic.  While we're on the subject of `PrepareMemoryForIO` options, you should note that a number of other options have no effect on current implementations. The full list is given below.   - `kIOShareMappingTables` - `kIOCoherentDataPath` - `kIOTransferIsLogical` - `kIOClientIsUserMode`   In addition, the `kIOLogicalRanges` option must always be set because current implementations do not support preparation based on physical address.  The following options are implemented as documented.   - `kIOMultipleRanges` - `kIOMinimalLogicalMapping` - `kIOIsInput` - `kIOIsOutput`   Finally, just in case you're wondering, the following options to `CheckpointIO` have no effect on current systems.   - `kNextIOIsInput` - `kNextIOIsOutput`   The remaining option, `kMoreIOTransfers`, has its documented effect. |

#### [Sep 22 2000]

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
