---
title: Distorted Panoramas
apple_id: DTS10002060
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-01'
source_url: https://developer.apple.com/library/archive/qa/qtvr/qtvr16.html
archived_at: '2026-07-18T02:38:51.169111Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Virtual Reality](https://developer.apple.com/referencelibrary/QuickTime/idxVirtualReality-date.html)

|  |
| --- |
| Technical Q&A QTVR16Distorted Panoramas |

|  |
| --- |
| Q My final nodes are distorted -- what do I do?   A Here are a few possibilities: 1. fovy is set incorrectly:  Stitch your image with the verbose switch included and some clearance on the fovy. For example, stitch ... `-verbose -fovy 97 10....`  When you do this, the stitch command will calculate the correlation at all angles from 87 to 107. Then, when it is done it will say `view angle = <angle> @ <hOffset> <vOffset>`. If there seems to be no maximum (or, more correctly, the maximum is either the first or last number), try the stitch again and move your whole scale down (or up depending on which number was the max) to `-fovy 80 15.`  In general, correlation should be above 0.85 for both numbers.  2. There is height and/or width distortion.  Try taking the outHeight and outWidth commands out of the stitch script and rerun. Load the resulting file into Adobe PhotoShop or some other graphics package and look at its size in pixels. Then, rerun all of your scripts setting outWidth to the width found in pixels and set outHeight to the number closest to the height in pixels that is divisible by 24 (assuming that you are dicing 1x24).  3. vPanRange in msnm is set incorrectly.  This should be a little less than half of your fovy. For example, if fovy was set to 96, vPanrange should be 45. This is a switch in msnm - vPanRange 45 -45. Alternatively, the proper vPanAngle should come out of the stitch command with the verbose switch on. It will be labeled as cylAngle. If your cylAngle is 90, vPanRange is 45 -45. [Sep 01 1995] |

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
