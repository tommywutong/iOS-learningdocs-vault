---
title: Error -151 and NewGWorld
apple_id: DTS10001777
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd18.html
archived_at: '2026-07-18T02:38:36.277540Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD18Error -151 and NewGWorld |

|  |
| --- |
| ---   Q: I received an error code of -151 from `NewGWorld` when creating a very large off-screen bitmap. Does this mean not enough memory? If so, can I count on it not to change in future versions of the system? It's not listed as one of the possible errors in _Inside Macintosh Volume VI_.  A: The error -151 is `cTempMemErr`, "failed to allocate memory for temporary structures," or in other words, there wasn't enough temporary memory available for `NewGWorld`. `NewGWorld` returns this error after it receives a `memFullErr` from `TempNewHandle`. This was inadvertently left out of _Inside Macintosh Volume VI_ but does appear in the MPW interface files. You can count on this error code in future versions of system software.  See _Inside Macintosh: Memory_ or the Memory Management chapter of _Inside Macintosh Volume VI_ for more information about temporary memory. |

#### [Sep 15 1995]

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
