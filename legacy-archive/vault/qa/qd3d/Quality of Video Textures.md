---
title: Quality of Video Textures
apple_id: DTS10001842
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-04-08'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d44.html
archived_at: '2026-07-18T02:38:41.555810Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A QD3D44Quality of Video Textures |

|  |
| --- |
|  Q: We created an application similar to the TextureEyes demo distributed by Apple: it maps a moving image texture onto a spinning cube. The display quality of TextureEyes, however, is much better than ours.  We're using large high-quality textures (480x320), but the image mapped onto the cube is quite chunky even when we are using the Apple QuickDraw 3D Acceleration card, and the animation seems to be slower and jerkier. What's TextureEyes' secret?  A: No secrets! TextureEyes is a straightforward implementation of the texturing of QD3D geometries.  The problem is that your texture is actually of too high quality. QuickDraw 3D uses a tri-linear MIP map algorithm to obtain the best possible quality texture mapping.  To create a MIP map from an image requires creating sub-images sized for every inverse power of two; i.e. 1/4, 1/16, 1/32 etc. The process of creating a MIP map for every texture takes time, and larger textures will require longer. TextureEyes uses a 128X128 source for its movie and video textures. See Also:  - For more information on MIP maps, see _Computer Graphics, Principles and   Practice_, Second Edition in C, by Foley, VanDam, Feiner, & Hughes,   1996, Addison Wesley. |

#### [Apr 08 1996]

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
