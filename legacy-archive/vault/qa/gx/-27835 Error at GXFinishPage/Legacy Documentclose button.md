---
title: -27835 Error at GXFinishPage
apple_id: DTS10001211
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/gx/gx06.html
archived_at: '2026-07-18T02:29:31.050835Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GX06-27835 Error at GXFinishPage |

|  |
| --- |
| ---   Q: My application returns the following error code -27835 at `GXFinishPage`. This only happens with Metrowerks' C/C++ 68K 1.2.1 compiler. I do not get the error with Metrowerks' PPC native compiler or with Symantec's C++ 7.0.3. With these compilers, I can print normally and can create PDD files. What would cause this?  A: It's unlikely that the compiler is the cause of the problem. The -27835 error code means "invalid viewport reference," which implies that QuickDraw GX is losing its viewport while printing. These are some possible causes for this problem:   - Your application is disposing of the viewport. - You're running out of memory, which causes QuickDraw GX to accidentally dispose of the `viewPort` when it is trying to clean up the GX heap. - Something is corrupting the QuickDraw GX heap. |

#### [Aug 01 1995]

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
