---
title: Setting the preferred CMM programatically?
apple_id: DTS10001635
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-10-24'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1086.html
archived_at: '2026-07-18T02:38:11.941507Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > ColorSync](https://developer.apple.com/referencelibrary/GraphicsImaging/idxColorSync-date.html)

|  |
| --- |
| Technical Q&A QA1086Setting the preferred CMM programatically? |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: I would like to be able to check the current state of the ColorSync preferred CMM, save it, set it to a different CMM, perform some color matching functions, then restore the old state. Is this possible? In other words, is there a `CMSetPreferredCMM` function to go along with `CMGetPreferredCMM`?  A: There is no public API to set the preferred CMM because giving developers the ability to bypass/change the user preference (set in the ColorSync control panel) defeats the purpose of the user setting. Just as there are developers who want to set the preferred CMM, there are also users who want to set the CMM. ColorSync decided to favor the user's right to choose over the developer's.  That being said, if a developer uses the `NCWConcatColorWorld` function (see [<http://developer.apple.com/technotes/tn/tn1160.html>](https://developer.apple.com/library/archive/technotes/tn/tn1160.html) ) it is possible to use the `NCMConcatProfileSet` structure to specify the CMM (and quality and rendering intent) to be used to make the `CMWorldRef`. With this API it is possible for the developer's choice to override the user's choice. The only catch is the chosen CMM must support the `kNCMMConcatInit` component selector on Mac OS 9 or the `NCMMConcatInit` `CFBundle` symbol on Mac OS X.  Here's some additional details regarding the `flags` and `flagsMask` fields of the `NCMConcatProfileSet` structure. In the past, if an application wanted to control the quality and rendering intent for a match it would need to modify the various flag bits of the profiles before creating the `ColorWorld`. Now this can be done more easily with the `NCMConcatProfileSpec` structure.  For example, if you would like to force best quality mode, specify the `flags` and `flagsMask` as follows:     |  | | --- | | ```     flags = cmBestMode << 16;     flagsMask = cmQualityMask; ``` |     If you would like to force normal quality mode, specify the `flags` and `flagsMask` as follows:     |  | | --- | | ```     flags = cmNormalMode << 16;     flagsMask = cmQualityMask; ``` |     If you would like to force draft quality mode, specify the `flags` and `flagsMask` as follows:     |  | | --- | | ```     flags = cmDraftMode << 16;     flagsMask = cmQualityMask; ``` |     If you don't need to perform gamut checking (`CWCheckPixMap`, `CWCheckBitmap`, etc.) you can more quickly build the `ColorWorld` by specifying:     |  | | --- | | ```     flags = cmGamutCheckingMask;     flagsMask = cmGamutCheckingMask; ``` |     Setting the gamut checking flag will reduce the time and memory needed to build the `ColorWorld`.   ---  [Oct 24 2001] |

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
