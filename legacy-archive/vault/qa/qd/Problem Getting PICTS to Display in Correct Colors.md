---
title: Problem Getting PICTS to Display in Correct Colors
apple_id: DTS10001783
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd24.html
archived_at: '2026-07-18T02:38:36.645038Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/Carbon/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Graphics & Imaging](https://developer.apple.com/referencelibrary/Carbon/idxGraphicsImaging-date.html)

|  |
| --- |
| Technical Q&A QD24Problem Getting PICTS to Display in Correct Colors |

|  |
| --- |
|  Q: I'm having problems getting PICTs to display with the colors I want. I'm converting GIF files to PICTs by drawing the GIF into an offscreen `GWorld`. I'm using the Palette Manager to set up the colors, but there's no way to associate a palette with an offscreen `PixMap`. After I'm done drawing the GIF to a `PixMap`, I open the picture with the offscreen `PixMap` as the current port and use `CopyBits` to copy the `PixMap` onto itself, creating the picture. The problem is that if I use `srcCopy`, the colors are incorrect in the PICT when opened with TeachText (and other applications). But if I use `ditherCopy` the colors are saved correctly. I can use `srcCopy` if I do a `CopyBits` to/from a "color" window with the window's palette changed to my color palette. Is there a way to assign a palette to use for `OpenPicture` and still use `CopyBits` from an offscreen bitmap with `srcCopy`?  A: You can associate a palette with a `GWorld`, but it won't solve your problem: since a `GWorld` never becomes "active," the associated device's colors are never changed to match the palette. The solution is to use a custom color table with the `GWorld`. And you can easily use Palette Manager routines to convert your palette to a color table.  Use the `Palette2CTab` routine to perform the conversion. `Palette2CTab` takes a `PaletteHandle` and a `CTabHandle` and copies all the colors from the palette into the color table, resizing the color table as necessary. If the palette handle is nil, no change takes place.  Now you have a color table that you can associate with your `GWorld`. You can pass it to `NewGWorld` when you create your `GWorld` initially; the fourth parameter is a handle to a color table. You need to explicitly set the depth in this call for best results. (If you pass `nil` for the depth, the color table parameter will be ignored and the depth of the `GWorld` will be set to match the deepest device that intersects the `GWorld`'s boundary rectangle.) The other possibility is to associate the color table with an existing GWorld using `UpdateGWorld`.   --- |

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
