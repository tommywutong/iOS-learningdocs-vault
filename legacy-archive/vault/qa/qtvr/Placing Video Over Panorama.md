---
title: Placing Video Over Panorama
apple_id: DTS10002058
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-01'
source_url: https://developer.apple.com/library/archive/qa/qtvr/qtvr14.html
archived_at: '2026-07-18T02:38:51.062374Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Virtual Reality](https://developer.apple.com/referencelibrary/QuickTime/idxVirtualReality-date.html)

|  |
| --- |
| Technical Q&A QTVR14Placing Video Over Panorama |

|  |
| --- |
| Q How do I place blue screen video over a panorama?   A For starters, you need to know the exact view over which you want to place video. Note that if you are only warping in one dimension, things may be a bit tricky. To get a very close match, take the following steps:  1. Push each individual frame of the motion sequence through the Stitcher (assuming that the motion fits within a single photograph) with -wrap turned off, and the same -vfov set as for the panorama. The resulting images will be warped into the same space as your complete panorama.  2. Either turn your single frame image into a partial panoramic movie or replace the appropriate part in your background panorama with the single frame.  3. p2mv and msnm it and use VR to dewarp it with warpMode 1 with the precise hpan, vpan and zoom data set. You may want to p2mv with the "raw " compressor in order to maximize your image quality.  4. Capture the image from the screen.  5. If you do this for every image (this can be automated with scripting), you should get a completely matched motion sequence which you can turn into a QuickTime movie with standard tools. This is where you should do your compression (not at Step 3).  This should mostly take machine time, not your time. Step 1 can be scripted in MPW. Step 2 can be scripted in AppleScript using PhotoFlash, or in DeBabelizer. Step 3 can be scripted in MPW. Step 4 can be scripted in HyperCard or Director. Step 5 uses ConvertToMovie. Once you develop these scripting tools the first time, each sequence should be pretty quick to fire up. [Sep 01 1995] |

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
