---
title: ColorPicker.h and ColorSync 2.0
apple_id: DTS10001129
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/c/cs01.html
archived_at: '2026-07-18T02:29:24.118641Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Carbon](https://developer.apple.com/referencelibrary/Carbon/index.html)

|  |
| --- |
| Technical Q&A CS01ColorPicker.h and ColorSync 2.0 |

|  |
| --- |
| ---   Q: The old ColorPicker.h has a typo that prevents it from working with the ColorSync 2.0 CMApplication.h, if it is included prior to CMApplication.h. Is an updated version of ColorPicker.h available?  A: The latest version of the universal interfaces (version 2.0a3 from the ETO #16:MPW prerelease) works properly with the latest version of the ColorSync interfaces (from the 2.0f2 seed). This version of ColorSync does have a few minor changes. The most notable change is that some of the fields in the `CMProfileLocation` and `CMProfLoc` structures were renamed so that they don't conflict with Pascal keywords. For example, the 'type' field was changed to `'locType'`. |

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
