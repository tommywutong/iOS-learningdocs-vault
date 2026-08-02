---
title: Setting Data For Q3ViewerUseData
apple_id: DTS10001861
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d63.html
archived_at: '2026-07-18T02:38:43.353313Z'
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
| Technical Q&A QD3D63Setting Data For Q3ViewerUseData |

|  |
| --- |
| ---   Q: I've defined a pane where I want to display 3D objects with the 3DViewer. There is no problem if I load the 3D data from a file and use '`Q3ViewerUseFile`'. But I couldn't figure out how I have to set the data for the '`Q3ViewerUseData`' routine. From where do I get the "size"?  A: According to chapter 2 "3D Viewer" pg. 2-10 of [3D Graphics Programming with QuickDraw 3D](https://developer.apple.com/documentation/quicktime/qtdevdocs/QD3D/qd3d_book.htm): "You use the `Q3ViewerUseData` function to specify a 3D model whose data is already in memory (either on the Clipboard or elsewhere in RAM). `Q3ViewerUseData` takes a reference to an existing viewer object, a pointer to the metafile data in RAM, and the number of bytes occupied by that data."  Basically, the data you pass to `Q3ViewerUseData` must be in 3dmf object format. For example, if the user had copied a 3dmf file from the scrap.  In this case, you would get the size of the data from the Scrap Manager. Take a look at the Tumbler & Podium sample in the QD3D SDK for an example. [Jul 11 1997] |

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
