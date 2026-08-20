---
title: Can't Print Hairlines
apple_id: DTS10001243
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd28.html
archived_at: '2026-07-18T02:29:33.514393Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD28Can't Print Hairlines |

|  |  |  |
| --- | --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: How can I draw and print hairlines with QuickDraw GX? We use a PicComment in the normal print code, but this seems to make QuickDraw GX fail. (We get a -51 error, i.e., reference number invalid, when we call `GXGetJobError` after calling `GXFinishJob`, and we sometimes get this error without the `PicComment` code.)  We also tried calling `GXSetShapePen` in our spool procedure. When we set it to a fractional value, we get a wide line, but when we set it to a wide value, such as 8, it works properly. What do we need to do to print fractional widths?  I can print hairlines when I use:   |  | | --- | | ``` SetPt((Point*)*lineWidth,2,1); PicComment(182,sizeof(Point),lineWidth); ``` |   but they are one pixel wide not two-pixel-wide, half-width lines (I am passing 1/2 in).  A: Here are two ways to get QuickDraw GX to draw hairlines when printing:   1. Call `GXSetShapePen(myShape, 0)`; This sets your pen width to 0, which indicates that your pen should be set as thin as renderable on the output device. QuickDraw GX always draws hairlines at the resolution of the output device -- one pixel wide. 2. Call `GXSetStylePen(myStyle, 0)`; This also sets your pen width to 0.   When using the `GXSetShapePen` and `GXSetStylePen` calls, don't specify the pen width as an integer. Calling `GXSetStylePen(myStyle, 1)` sets the pen width to 1/65536. Calling `GXSetStylePen(myStyle, ff(1))` sets the pen width to 1.0.  QuickDraw GX uses a backing store file (it's an invisible file within the System folder) to send QuickDraw GX objects to disk when additional space is needed within the QuickDraw GX heap.  Almost all -51 errors from within QuickDraw GX or an application using QuickDraw GX are caused by double-disposing of a QuickDraw GX object (i.e., a shape, ink, style, or transform). The -51 error occurs because the double dispose causes QuickDraw GX to set the shape attributes, which tells QuickDraw GX that it has sent the QuickDraw GX object to disk. When it needs this object, it goes to the backing store and tries to get it, but it's not there. We have found a few cases where QuickDraw GX was double-disposing of objects, and these were fixed in QuickDraw GX version 1.1.  Before calling `GXDrawShape` (before calling `GXFinishPage`), call `GXValidateShape` on the shape(s) you are trying print. This ensures that a shape is valid before it is drawn or printed. This slows things down a little, but you will be able to determine if a shape is still available before you attempt to draw it (you might be disposing of a shape before you draw it). If you have an error handler installed, you usually receive the "shape_already_disposed" message, but you may not receive this message if something is wrong with the QuickDraw GX backing store.  It is also possible that the hairline drawing problems you are encountering are related to the translation options you are using. A translator takes your QuickDraw drawing commands and converts them to QuickDraw GX objects, based on options you provide. If you use the `gxDefaultOptionsTranslation` setting, a QuickDraw line turns into a 6-sided filled polygon. When your object is a polygon, changing the pen width has no effect.  To avoid this, call `GXInstallQDTranslator()` with either the `gxSimpleGeometryTranslation` or the `gxReplaceLineWidthTranslation` option. The `gxSimpleGeometryTranslation` option turns on both the simple-lines and simple-scaling translation options, and it translates QuickDraw lines into QuickDraw GX lines with flat endcaps. The QuickDraw GX line shape runs along the center of the original QuickDraw line, and it covers all the pixels of the QuickDraw line and more. The `gxReplaceLineWidthTranslation` option turns a QuickDraw line into a QuickDraw GX line with a width that is the average of the original pen's width and height. The `gxReplaceLineWidthTranslation` also affects the way the `SetLineWidth` PicComment is interpreted.  Once you set the translation option, your calls to `GXSetShapePen()` and/or `GXSetStylePen()` should behave as you expect them to, because they are acting on QuickDraw GX lines -- not polygons. When you have installed a translator, be sure to remove it with `GXRemoveQDTranslator()`. To learn more about the translation options, see:  Chapter 1 of _Inside Macintosh: QuickDraw GX Environment and Utilities_.  _Inside Macintosh: QuickDraw GX Printing_ _Inside Macintosh: QuickDraw GX Printing Extensions and Drivers_ _Inside Macintosh: QuickDraw GX Graphics_ |

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
