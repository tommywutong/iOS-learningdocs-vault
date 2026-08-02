---
title: PCI Interrupts
apple_id: DTS10001297
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw25.html
archived_at: '2026-07-18T02:29:36.441312Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A HW25PCI Interrupts |

|  |
| --- |
| ---   Q: The PCI specification (Section 6.2.4, Page 159) says that the `POST` code is responsible for allocating the interrupt vectors for all PCI cards. The `POST` software writes the vector to the PCI "Interrupt Line" register associated with every card that has a non-zero PCI "Interrupt Pin."  Is this what the Mac implementation of the POST standard does?  A: Open Firmware does not allocate interrupt vectors as in a typical x86 PC environment. Interrupts on PCI PowerMac CPUs are organized as 1 Interrupt per slot. At the motherboard connector, `INTA#`, `INTB#`, `INTC#`, and `INTD#` signals are tied together per slot and the resulting signal is called "`SlotXInt#`". Therefore, Open Firmware does not need to interrogate the Interrupt Line Register in Configuration Space.  The control and propagation of hardware interrupts are abstracted from the driver software. A interrupt source for a PCI card or device is represented by a node in a hierarchical tree, called Interrupt Source Tree (IST).  For a good description of Interrupts on PCI PowerMac CPUs, please refer to the Interrupt Management section in the Driver Services Library chapter in _Designing PCI Cards and Drivers for Power Macintosh Computers_, A8 draft or later. |

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
