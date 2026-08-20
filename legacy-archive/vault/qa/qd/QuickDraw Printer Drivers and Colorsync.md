---
title: QuickDraw Printer Drivers and Colorsync
apple_id: DTS10001763
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd04.html
archived_at: '2026-07-18T02:38:35.365675Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Printing](https://developer.apple.com/referencelibrary/Printing/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A QD04QuickDraw Printer Drivers and Colorsync |

|  |
| --- |
| ---   Q: I'm using ColorSync 1.0.5 with a custom CMM developed by another company, and I'm incorporating this into a color QuickDraw printer driver I'm developing. A representative of the company that developed the custom CMM told me that my printer drivers would be more efficient if I manually matched colors inside my `Stdxxx` bottlenecks, instead of calling `DrawMatchedPicture`. More specifically, he said that I should call `DrawPicture` instead of `DrawMatchedPicture`, and that I should get the RGB colors for the object inside each of my bottlenecks, then call `CWMatchColors` and put the RGB colors back in. He also said that, in the case of my stdbits bottleneck, I should call `CWMatchPixmap`.  I was surprised by these suggestions, in that objects drawn with an arithmetic transfer mode won't use the correct matched color. When I questioned his advice, he said that `DrawMatchedPicture` works fine for object-based material, and it calls `CMMatchColors` in the CMM. If, however, the source picture contains a pixmap, ColorSync converts it little-by-little into `RGBColors` and calls `CMMatchColors` on those bits before converting them back into a pixmap and putting them into the destination. Clearly, ColorSync should call `CMMatchPixmap` in this case. He also said that he implemented `CMMatchPixmap`, yet it never gets called during a `DrawMatchedPicture` playback. It is called when he calls `CWMatchPixMap` from the low-level interface.  If this is true, it would explain his findings, since converting the pixmap to `RGBColors` and back again takes time and memory. Also, any caching performed by the CMM would probably be less efficient. I would like your opinion on this issue. Is there a performance problem with `DrawMatchedPicture` that can be overcome by using the suggested procedure? If his information is accurate, is this fixed in ColorSync 2.0 ?  A: Surprising as it may be, it's more efficient for printer drivers to manually match colors inside `Stdxxx` bottlenecks, instead of calling `DrawMatchedPicture`. This is because ColorSync 1.0 `DrawMatchedPicture` does not use bottlenecks as you expected. It does install a bottleneck routine for `PicComments` (so that it can watch the embedded profiles go by), but it doesn't do the actual matching in bottleneck routines. Instead, it installs a `ColorSearchProc` in the current `GDevice`. Inside the `ColorSearchProc`, each color is matched one at a time.  While this implementation has some advantages, it's also painfully slow on `PixMaps`, because, even if the `PixMap` only contains 16 colors, each pixel is matched. This has been changed in CS 2.0. To boost performance, `PixMaps` (which are, after all, quite common), are now matched in the bottleneck instead of in `ColorSearchProc`. |

#### [May 01 1995]

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
