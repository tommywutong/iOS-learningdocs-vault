---
title: Default Number of Surface Planes
apple_id: DTS10001854
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d56.html
archived_at: '2026-07-18T02:38:42.644609Z'
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
| Technical Q&A QD3D56Default Number of Surface Planes |

|  |  |
| --- | --- |
|  Q: When rendering a QuickDraw 3D 1.5 file containing objects such as cylinders and ellipsoids, the default number of surface planes is much higher than in QD3D version 1.0.6. While this looks nice, it requires more memory. Is there a way in my application to limit the "resolution" (i.e., the number of surface planes) used by QD3D 1.5?  A: You can use a subdivision style to get control over the number of faces generated. For example, you can create a subdivision style object as follows:   |  | | --- | | ``` theSubdivisionStyleData.method = kQ3SubdivisionMethodScreenSpace; theSubdivisionStyleData.c1 = (float)20; theSubdivisionStyleData.c2 = (float)20; mSubdivisionStyle = Q3SubdivisionStyle_New(&theSubdivisionStyleData); ``` |   You can then submit the subdivision style in your rendering loop before you submit your geometry. |

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
