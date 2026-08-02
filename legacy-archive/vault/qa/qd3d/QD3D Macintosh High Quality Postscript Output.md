---
title: QD3D Macintosh High Quality Postscript Output
apple_id: DTS10001851
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/qd3d/qd3d53.html
archived_at: '2026-07-18T02:38:42.433851Z'
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
| Technical Q&A QD3D53QD3D Macintosh High Quality Postscript Output |

|  |
| --- |
|  Q: Does QuickDraw 3D support high quality PostScript output (that is, conversion of objects to PostScript for high quality antialiased edges)?  A: QD3D doesn't directly support conversion of objects to PostScript. To convert a QD3D object to PostScript you would first draw your image into a QD3D pixmap draw context (see "[3D Graphics Programming with QuickDraw 3D](https://developer.apple.com/documentation/quicktime/qtdevdocs/QD3D/qd3d_book.htm)" by Addison Wesley, Chapter 12). Once you've drawn the image into the pixmap draw context you could then use a standard Mac OS printing loop (see the "[Printing Loop That Cares](https://developer.apple.com/library/archive/technotes/tn/tn1092.html)" technical note on the Apple Developer World web site: developer.apple.com) to print the image either to a printer or PostScript file.  However, the Mac OS doesn't directly support (via Toolbox functions) anti-aliasing for text &and graphics, either. But there are certain tricks you can play with QuickDraw which will allow you to achieve anti-aliasing effects. The article "[Realistic Color for Real-World Applications](https://developer.apple.com/library/archive/dev/techsupport/develop/issue01toc.shtml)" in issue 1 of _develop_ journal describes one simple method.  In addition, many other third-party products have implemented anti-aliasing for the Mac OS. A simple search on the InterNet or any Macintosh software guide/magazine will reveal such products. |

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
