---
title: Apple Accelerator Card & Textures
apple_id: DTS10001859
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d61.html
archived_at: '2026-07-18T02:38:43.199029Z'
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
| Technical Q&A QD3D61Apple Accelerator Card & Textures |

|  |
| --- |
|  Q: I have an Apple Accelerator card in my PowerMac 9500. I'm seeing great acceleration with small models (without textures). However, I noticed with large models, performance actually gets worse! Yes, it is faster without the card! Can you explain this?  A: You will find the Apple card is good when you have very limited texture requirements, and only a few triangles in the scene (i.e., it is good at Gerbils), but it will quickly get bogged down when the triangle count goes up. This is because it doesn't start rendering until all the triangles are available - it can take up many megabytes of system memory to store them and you get no concurrency between the application and the rasterization.  Using a more traditional Z-buffered graphics architecture overcomes these limitations. That is not to say the Apple scanline method does not have some advantages.  There are several good high quality QD3D accelerator cards based on the defacto standard OpenGL chip (GLINT 500TX from 3Dlabs) in the PC market. They are generally more expensive than the Apple card, so they are probably not a "home" purchase. However, "you get what you pay for" is as true for 3D graphics as in other walks of life. |

#### [Jul 11 1997]

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
