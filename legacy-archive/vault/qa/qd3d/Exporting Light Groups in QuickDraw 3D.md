---
title: Exporting Light Groups in QuickDraw 3D
apple_id: DTS10001820
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d22.html
archived_at: '2026-07-18T02:38:40.374779Z'
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
| Technical Q&A QD3D22Exporting Light Groups in QuickDraw 3D |

|  |
| --- |
|  Q: I am writing a 3DMF export procedure, and I'm having trouble exporting a single-directional light source. The resulting file ends prematurely in the directional light's parameter list.  A: Apple developed the concept of view hints early on in the development of QuickDraw 3D, when it became apparent the particular settings for determining how a scene should be rendered in one application were not always transportable to another. In particular, settings such as the camera location, lighting, camera type, and so on can be very different in two different apps. For example, a modeling application might set everything up so the object looks good, but when the object is exported to another application and becomes part of a larger scene, it may not make sense to have the camera and light information included along with the geometry being drawn. This is why we developed view hints.  The concept of a view hint is that it sets up a series of hints that tell the reading application how the author of the metafile intended the geometries within the metafile to be rendered. Since these are hints, the reading application can ignore them.  Rather than writing out the lighting information to the metafile as absolute objects, you should create a view in the normal manner, and then add lighting, camera, renderer, and other information, also in the normal manner. Then, extract the view hints from the view with `3ViewHints_New( theView )` by passing in a view object. `3ViewHints_New( theView )` returns a view-hints object that includes the view configuration for the view you pass in.  View hints have many handy access routines for getting and setting renderers, light groups, and the like. See the "__File Objects "chapter of _Inside Macintosh: QuickDraw 3D_ (now called _3D Graphics Programming with QuickDraw 3D_)__. An electronic copy of this book was included on the last Reference Library CD in the New System Extensions folder, and as part of the beta seed kit.  Tumbler, which is also part of the beta kit, illustrates how to use view hints read from a metafile to configure a view. For details, see the __Tumbler_Document.c file__. |

#### [Jul 01 1995]

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
