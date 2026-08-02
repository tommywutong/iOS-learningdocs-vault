---
title: Using Hardware Acceleration
apple_id: DTS10001858
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d60.html
archived_at: '2026-07-18T02:38:43.008760Z'
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
| Technical Q&A QD3D60Using Hardware Acceleration |

|  |
| --- |
|  Q: How do I set up QuickDraw 3D hardware acceleration? Is there any specific API calls I have to make? Or does hardware acceleration just work automatically if you have a hardware accelerator board installed?  A: The QD3D interactive renderer automatically uses hardware acceleration if a card is present (and selects the best hardware if there are multiple cards). The wireframe renderer does not.  You can tell a renderer to use hardware acceleration with the `Q3InteractiveRenderer_SetPreferences()` and `Q3View_SetRenderer` functions.  Check out the BoxPaint sample code from the QD3D SDK which uses the above functions to set the renderer. |

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
