---
title: View Hints
apple_id: DTS10001845
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-04-08'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d47.html
archived_at: '2026-07-18T02:38:42.055001Z'
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
| Technical Q&A QD3D47View Hints |

|  |
| --- |
|  Q: What are view hints in the QuickDraw 3D MetaFile format (3DMF)?  A: The concept of view hints was included early on in the development of QuickDraw 3D. It became apparent that the settings for determining how a scene should be rendered are not always transportable from one application to another (for example, settings such as the camera location, lighting, camera type, etc.).  The idea of a view hint is that it sets up a series of hints that tell the reading application how the author of a MetaFile intended the geometries within the MetaFile to be rendered. The fact that these are hints implies that the reading application can ignore them.  Rather than writing out the lighting information to the MetaFile as absolute objects, Apple recommends creating a view in the normal manner, adding lighting, camera, renderer and other information in the normal manner, and then extracting the view hints from the view with `Q3ViewHints_New( theView )`. You pass in a view object, and this function returns a view hints object that includes the view configuration for the view you pass in. See Also:  - View hints have a bunch of handy access routines for getting and setting   renderers light groups and the like. See the File Objects chapter of _3D   Graphics Programming with QuickDraw 3D_. - The Tumbler and Podium sample code, that comes with the QuickDraw 3D SDK,   illustrates how to use view hints read from a metafile to configure a view.   Look in the file Tumbler_document.c for details. |

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
