---
title: Problems Creating a Mask for a Picture
apple_id: DTS10001786
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd27.html
archived_at: '2026-07-18T02:38:36.840022Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/Carbon/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Graphics & Imaging](https://developer.apple.com/referencelibrary/Carbon/idxGraphicsImaging-date.html)

|  |
| --- |
| Technical Q&A QD27Problems Creating a Mask for a Picture |

|  |
| --- |
| ---   Q: I want to create a mask for a picture, such that the mask is 0 wherever the picture's pixels are pure white, and 1 everywhere else. My first try was to simply use `CopyBits` to copy the rectangle enclosing the PICT onto a same-sized rect in a 1-bit-deep offscreen world. This didn't work, however, as the yellows get transformed to 0, which is not what I want. I tried various transfer modes with `CopyBits` (from 0 to 100) to no avail. The `SeedCFill` and the `CalcCMask` routines don't seem to be what I want either, because it appears that their masks have to be keyed off a certain point or side(s). I can take the brute force approach and go through the pixels of the PICT one by one, checking to see if they're white and setting the mask accordingly, but this seems insane. Is there a good method for doing this?  A: The way to do this is to install a custom color search procedure, then call `CopyBits` to copy into the 1-bit GWorld and let the search proc determine the color to use. The search proc would simply look at the color asked for and return white if it's white or black if it's nonwhite.  See "Color Manager" in _Inside Macintosh: Advanced Color Imaging_  (forthcoming in print from Addison-Wesley). |

#### [Sep 15 1995]

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
