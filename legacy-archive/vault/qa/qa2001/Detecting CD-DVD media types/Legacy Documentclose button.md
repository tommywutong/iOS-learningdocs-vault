---
title: Detecting CD/DVD media types
apple_id: DTS10001557
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-02-21'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1001.html
archived_at: '2026-07-18T02:38:01.122828Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A QA1001Detecting CD/DVD media types |

|  |
| --- |
| ---   How can I detect what types of media a CD/DVD drive supports?  You can make a Status call to the driver with `csCode` = `kdgGetCDDeviceInfo` to retrieve information about a CD/DVD drive, including supported media types. If successful, `csParam[0:2]` contain a `CDDeviceCharacteristics` structure. The `CDDeviceCharacteristics` structure has been extended to include flags for supported media.  The extended `CDDeviceCharacteristics` structure is described fully in the file DriverGestalt.h in [Universal Interfaces 3.4](https://developer.apple.com/sdk/index.html).   ---  [Feb 21 2001] |

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
