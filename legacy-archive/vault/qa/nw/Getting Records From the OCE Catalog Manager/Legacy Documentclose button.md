---
title: Getting Records From the OCE Catalog Manager
apple_id: DTS10001428
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/nw/nw16.html
archived_at: '2026-07-18T02:29:44.744849Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW16Getting Records From the OCE Catalog Manager |

|  |
| --- |
| ---   Q: When we use the `DirFindRecordGet` function, we get the message `kOCEInvalidCommand (-1501)`. Is there another way to get all records from a given catalog?  A: The catalog you are attempting to get record information about does not support the `DirFindRecordGet` function (few out there actually do). To check whether or not a particular catalog supports this function, you need to first call `DirGetDirectoryInfo()` and check the features flags that are returned. Check the `kSupportsFindRecordBit` (see _[Inside Macintosh: AOCE Application Interface](https://developer.apple.com/documentation/mac/aoceapi/Contents.html),_ p. 8-31) to see if this call is supported. If it is not supported, you'll have to use `DirEnumerateGet` instead to get all the records from a catalog. You also might want to look at the "DTS Catalog Peek" sample code on the Mac OS SDK. |

#### [Sep 01 1995]

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
