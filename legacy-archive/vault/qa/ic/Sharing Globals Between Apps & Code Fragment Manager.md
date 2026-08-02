---
title: Sharing Globals Between Apps & Code Fragment Manager
apple_id: DTS10001374
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/ic/ic03.html
archived_at: '2026-07-18T02:29:40.462428Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Interapplication Communication](https://developer.apple.com/referencelibrary/Carbon/idxInterapplicationCommunication-date.html)

|  |
| --- |
| Technical Q&A IC03Sharing Globals Between Apps & Code Fragment Manager |

|  |
| --- |
| ---   Q: I have a shared library (PowerPC native CFM) that is used by several applications. The library includes a few global variables that are used in all of the applications (they declare them as "extern"s). My problem is that each application seems to have its own copy of the globals, but when I check the address of the same global in several applications, they are different. Aren't globals supposed to be sharable between applications?  A: The Code Fragment Manager allows shared libraries to allocate and use global variables in two different ways: Global instantiation or Per-context instantiation. At link time, you determine whether your library will support either global or per-context instantiation. The default PPCLink option is to support per-context instantiation, which is probably why you are seeing different addresses for the same global across applications.  These are the differences between the two types of instantiation:   1. Global instantiation: CFM allocates a single copy of the library's staticmdata, regardless of how many clients use the data. 2. Per-context instantiation: CFM allocates one copy of the static data for each separate process that uses that data.   If you want the CFM to allocate only a single copy of your library's static data, and if you are using PPCLink 1.2a1 from ETO 16, your link line must include the option (-share global), which sets the sharing mode for the static data to global instantiation. If you are using version 1.0 of the PPCLink tool, you must specify the global instantiation option (-s 4) on your `MakePef` command line. For `MakePef`, the default option is per-context (-s 1).  To learn more about how the Code Fragment Manager deals with global data by reading pages 1-50 through 1-52 of _Inside Macintosh:PowerPC System Software._ "Building for PowerPC" on ETO 16 has additional information on building a shared library. |

#### [May 01 1995]

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
