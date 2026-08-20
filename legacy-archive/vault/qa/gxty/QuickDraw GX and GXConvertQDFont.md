---
title: QuickDraw GX and GXConvertQDFont
apple_id: DTS10001261
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxty/gxty02.html
archived_at: '2026-07-18T02:29:34.519669Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXTY02QuickDraw GX and GXConvertQDFont |

|  |
| --- |
| ---   Q: I have a few questions concerning the processing provided by `GXConvertQDFont`:   1. According to the documentation, the basic style settings (plain, bold, and italic) should not cause font-conversion problems, but other, more complex styles may not convert as easily or accurately. Is this font-dependent? 2. I tried changing the styles of two fonts, Times and Parisian. Times accepted the new style setting during conversion, but Parisian did not. My application should be able to take any system-installed font and update the layout shape with the selected font, as well as update the basic style (plain, bold, italic, bold/italic). When the style did not convert, the `GXConvertQDFont` routine returned the style I gave it as the "extra style bits." How is the use of this routine different from converting a QD pict of the text with the font and style to a QDGX layout shape? 3. I'm currently using `GXConvertQDFont`, but I previously used the QD to QDGX conversion hack using `GXConvertPICTToShape`. At first, the description of `GXConvertQDFont` in its documentation sounded like a better approach than what I was using, but now I am not sure. What advice can you give me on this issue? I need to set the font and style on a layout shape based on a QD representation given to me.   A: `GXConvertQDFont()` sets the style using as much information about the QD font and `styleBits` as it can without creating a `textFace`. `StyleBits` returned by `GXConvertQDFont()` can be ignored, or your application can convert them to a textFace (i.e., algorithmic stylings). In other words, `GXConvertQDFont` finds the best font it can, but it is up to your application to do the rest.  In your examples, Times worked correctly, since there are fonts for bold, italic, and bold-italic. If Parisian is available in only one style, and you asked for bold, `GXConvertQDFont` would return the bold `styleBit` set. However, if you do the conversion with `GXConvertPICTToShape`, the resulting shape is the best possible representation of the QD text. With `GXConvertPICTToShape`, the text shape may include `textFaces`. |

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
