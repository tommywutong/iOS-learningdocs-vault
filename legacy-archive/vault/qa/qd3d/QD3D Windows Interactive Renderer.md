---
title: QD3D Windows Interactive Renderer
apple_id: DTS10001878
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d80.html
archived_at: '2026-07-18T02:38:44.494452Z'
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
| Technical Q&A QD3D80QD3D Windows Interactive Renderer |

|  |  |
| --- | --- |
| ---   Q: In the following code fragment, the `Q3Renderer_NewFromType` function works if the wireframe renderer is specified, but fails if the interactive render is specified. A subsequent call to `Q3Error_Get` returns 0. Why is this? I'm using Visual C++ 4.2 under Windows NT4.0.   |  | | --- | | ``` #if 0 	myRenderer =  Q3Renderer_NewFromType(kQ3RendererTypeWireFrame); #else 	myRenderer =  Q3Renderer_NewFromType(kQ3RendererTypeInteractive); #endif       ^^ this call is failing ``` |   A: Make sure you have the file `QD3D_IR2.q3x` in the same folder as the QD3D DLL. `QD3D_IR2.q3x` is the interactive renderer. [Jul 11 1997] |

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
