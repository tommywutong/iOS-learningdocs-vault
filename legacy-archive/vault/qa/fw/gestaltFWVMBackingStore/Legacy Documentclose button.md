---
title: gestaltFWVMBackingStore
apple_id: DTS10001204
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-10-05'
source_url: https://developer.apple.com/library/archive/qa/fw/fw04.html
archived_at: '2026-07-18T02:29:30.632117Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A FW04gestaltFWVMBackingStore |

|  |
| --- |
| ---   Q: I noticed that with the latest version of the FireWire 2.2 SDK that there is a new `Gestalt` attribute bit defined, `gestaltFWVMBackingStore`. Does this mean that FireWire 2.2 supports FireWire hard disks as a VM backing store?  A: Unfortunately, no, it does not. FireWire 2.2 is not able to be on the page fault path, so it cannot control a FireWire disk which contains the VM backing store. This bit was incorrectly set in FireWire 2.2.  However, now that the cat’s out of the bag, it is obviously an important future direction for FireWire hard disks to be a fully functional part of the system. Becoming able to be on the page fault path and control the VM backing store is an important first step towards this.  The solution is to ignore this bit completely. It has been deprecated and will never be defined to be anything meaningful. In future versions of FireWire.h, `gestaltFWVMBackingStore` will be renamed `gestaltFWBogus` to make sure that your compiler forces you to not check this bit (at least not without first flagging it as an error).  Look for a new bit being defined, `gestaltFWVMBacking`, which will be correctly set once FireWire is able to be on the page fault path. Currently `gestaltFWVMBacking` will return `0` on all versions of FireWire, including version 2.2.  However, once FireWire is able to be on the page fault path, it does not guarantee that the FireWire disk driver can be. It is possible for a FireWire disk driver to be written in such a way as to __not__ be able to be on the VM page fault path (however, that seems unlikely). It will not be known what drivers are capable of supporting the VM backing store until FireWire itself is made capable of being on the VM page fault path. |

#### [Oct 05 1999]

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
