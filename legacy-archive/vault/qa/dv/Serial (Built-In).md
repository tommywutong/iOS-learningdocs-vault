---
title: Serial (Built-In)
apple_id: DTS10001171
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-05-27'
source_url: https://developer.apple.com/library/archive/qa/dv/dv30.html
archived_at: '2026-07-18T02:29:26.975976Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Serial](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSerial-date.html)

|  |
| --- |
| Technical Q&A DV30Serial (Built-In) |

|  |
| --- |
| ---   Q: What is the "Serial (Built-In)" file, and what does it do?  A: PCI Macs have two different types of serial drivers. These are known as "Serial (Built-in)" and SerialDMA. These drivers provide similar basic functionality, but they differ in their implementation:  "Serial (Built-in)" is a set of ASLM shared libraries that provide a basic serial driver (e.g., .AOut) and a hardware abstraction layers capable of supporting more than just asynchronous serial (e.g., GeoPort).  "Serial (Built-in)" comes in two flavors. An early version is built into the ROMs on PCI PowerMacs and there is also an ASLM shared library in the Extensions folder.  The other serial driver is SerialDMA. This also comes in two flavors. Prior to System 7.5.3, SerialDMA shipped as a separate system extension. For 7.5.3 and later, SerialDMA is built into the system software. You can read more about the SerialDMA driver in [Technote 1018 "Understanding the SerialDMA Driver"](https://developer.apple.com/library/archive/technotes/tn/tn1018.html). In general, SerialDMA is more reliable than "Serial (Built-in)" and is the serial driver that will continue to be provided in the future.  The original system software for PCI PowerMacs contained only the "Serial (Built-in)" driver, both in the ROM and an updated version in the Extensions folder. Later a patch (the Printing Fix) shipped SerialDMA as a system extension. This extension loaded after "Serial (Built-in)", overriding the basic serial driver functionality of the "Serial (Built-in)" driver, leaving only the extra functionality (eg GeoPort) remaining.  With System 7.5.3, SerialDMA was rolled into the system. Unfortunately this caused "Serial (Built-in)" to load after SerialDMA, and override it instead of the other way around! So a new version of "Serial (Built-in)" was built. This version does not provide the basic serial driver -- it only provides the extra functionality that is still needed by things like the QuickTake camera software.  The weird thing is that, if you remove the "Serial (Built-in)" file from the Extensions folder, the Mac loads the older ROM version of the driver instead. This version still has the basic serial driver functionality, so under 7.5.3 removing the "Serial (Built-in)" extension actually causes SerialDMA to be disabled. |

#### [May 27 1997]

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
