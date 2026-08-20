---
title: Window Manager and EraseRect
apple_id: DTS10001785
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd26.html
archived_at: '2026-07-18T02:38:36.774560Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD26Window Manager and EraseRect |

|  |
| --- |
| ---   Q: I'm erasing my windows with a color other than white, by setting the window's background color and calling `EraseRect`. But in cases where the Window Manager gets there first (window ordering changes or a window's size gets larger) I still get flicker, because the Window Manager erases with the `wContent` color from the window's color table (white by default) and not the port's background color. Is there a friendly, clean way to avoid that flicker? (I notice that in System 7.5, background colors are implemented with `EraseRect`, just as I'm doing it. Are you simply assuming the flash will be minimal?)  A: One of the Window Manager's functions is to ensure that the content region of a window is opaque when it needs to be: that's why the Window Manager "pre-erases" the window when the content region grows, before your application gets a chance to. As you point out, if your application is then erasing large areas of the window to a different color, you'll get a noticeable flicker in those parts of the content region that needed to be opaque. This is an unfortunate side effect of a necessary maneuver by the Window Manager. Any system dialogs that set a background color and use `EraseRect` will suffer from the same flicker (although you won't spot it so often, since for the most part they're modal, nonresizable, and relatively small).  There are two solutions: If you create your windows from '`WIND`' resources, you can create '`wctb`' resources with the same ID and an appropriate `wContent` color and they'll automatically be used when the window is created. Alternatively, you can use the `SetWinColor` routine to apply a color table to a window after it has been created. |

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
