---
title: Determining if a PCI Bus Exists
apple_id: DTS10001271
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-09-01'
source_url: https://developer.apple.com/library/archive/qa/hw/hw01.html
archived_at: '2026-07-18T02:29:35.200244Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A HW01Determining if a PCI Bus Exists |

|  |  |
| --- | --- |
| ---   Q: How do I determine if the Power Macintosh has PCI expansion slots?  A The only way to do this is to use the Name Registry. Use the `RegistryEntrySearch` routine to search for entries whose "device_type" value is "pci." If an entry is found (`RegistryEntrySearch` returns `noErr` and done is false), there is at least one PCI bus. The Name Registry is documented in Chapter 8 of "Designing PCI Cards and Drivers for Power Macintosh Computers".  To allow your program to run on machines that don't have the Name Registry, you should weak link to "NameRegistryLib." You can then determine whether the Name Registry is available by testing the address of a symbol in the library against `kUnresolvedCFragSymbolAddress`. This technique is documented in [Inside Macintosh: PowerPC System Software](https://developer.apple.com/documentation/mac/PPCSoftware/PPCSoftware-2.html), p1-25.  The following snippet demonstrates both techniques:   |  | | --- | | ``` static Boolean HasPCISlots(void)     // Returns true if the machine has any PCI slots.   Guards against the     //  absence of NameRegistryLib, so you can run this function on any PPC     //  computer. {     Boolean result;     RegEntryIter myIterator;     OSStatus err;     Boolean done;     RegEntryID foundEntry;     // Assume the worst.     result = false;     // Check that the link to NameRegistryLib was successful.     if (RegistryEntryIterateCreate != kUnresolvedCFragSymbolAddress) {         // Create an iterator         if (RegistryEntryIterateCreate(&myIterator) == noErr) {             // Search for a node of type "pci".             (void) RegistryEntryIDInit(&foundEntry);             err = RegistryEntrySearch(&myIterator, kRegIterContinue,                                         &foundEntry, &done,                                         "device_type",                                         "pci", sizeof("pci"));             // See whether we found one.             if (err == noErr && !done) {                 result = true;                 (void) RegistryEntryIDDispose(&foundEntry);             }             (void) RegistryEntryIterateDispose(&myIterator);         }     }     return (result); } ``` | |

#### [Nov 27 1996]

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
