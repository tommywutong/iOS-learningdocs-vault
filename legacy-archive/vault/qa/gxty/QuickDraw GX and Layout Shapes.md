---
title: QuickDraw GX and Layout Shapes
apple_id: DTS10001263
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxty/gxty04.html
archived_at: '2026-07-18T02:29:34.622039Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXTY04QuickDraw GX and Layout Shapes |

|  |  |  |
| --- | --- | --- |
| ---   Q: I'm using a layout shape to represent an area for editable text that will have a fixed position, style, font, size, and width. This layout shape has some default text that the user is prompted to change (text content only; no other attributes).  Each time text is added (the new text replaces the previous text string), the UI code asks whether the size of the new string goes beyond the defined width. I do this by comparing the width of the local bounds with the width given within the layout-shape geometry found within the layout-options structure. In all cases, the justification setting is 0, but the flush setting varies (left/0, center/0.5, right/1.0).  When the user enters text into this shape, the bounds (as defined by my logic above) may or may not be found. That is, sometimes the bounds defined by the shape and the local bounds reach a point where the local bounds are wider than that indicated by the shape. However, in other cases, the local bounds diverge toward the width, but it never reaches or surpasses it. In this situation, the text is updated and begins to compress itself within the defined width. Sometimes, it appears that the compression or the meeting of the bounds depends on the font and/or the text used, but at other times, this does not seem to apply.  Here is my algorithm:   1. save the current string 2. get the defined width of the layout shape (Note: If the layout options structure width is 0, a width found on a tag attached to the shape is used.) 3. update the shape with the new string 4. get the local bounds of the shape with the new string 5. compare the width of the new bounds with the defined width if bounds width > defined width 6. then // in this case the new string is too long for the definition 7. reset the text string to the previous string 8. otherwise 9. return   How can I allow text to be entered till the width is reached, but not compressed? Can I do this based on the above detail? If there is something wrong with this approach, can you suggest another approach I could use?  A: The problem you describe was fixed in QuickDraw GX 1.1.1 by adding a new API call. The prototype for this call is:   |  | | --- | | ```  Fixed GXGetLayoutJustificationGap (gxShape layout); ``` |   This function returns information that was always generated during layout's justification processing, but was never made publicly visible before. It represents the signed difference between the specified width for the layout and the measured (unjustified) width.  By setting a width in the layout options, but leaving the justification factor at zero, you can keep adding text until the results of the `GXGetLayoutJustificationGap` call changes sign from positive to negative. At that point, the text starts to compress, so you should prohibit new text entry. It is a very fast call (since its result is cached as part of the layout process anyway), so calling it on every typed character shouldn't slow things down at all.  Some examples may help clarify the usage of this call: Suppose you create a layout with the width field of the gxLayoutOptions set to 500 points and the justification factor set to fract1 (i.e., full justification). If the unjustified width of the layout is only 450 points, this function returns +50 points. Similarly, if the unjustified width is 525 points, this function returns -25 points. A positive value means the line will be typographically stretched in order to fill the specified width, while a negative value means the line will be typographically condensed.  Note that the justification factor in the `gxLayoutOptions` doesn't have to be fract1 for this function to return useful results. For instance, by setting a width value but leaving the justification factor set to zero, layout will not justify the line unless the line's unjustified width exceeds the specified width. In this case, layout will typographically shrink the line. A client program wishing to determine when the end of a line is reached (for linebreaking purposes) can call this function after every character is added (as the user types, for example), and as soon as the value becomes negative, the client knows that the margin has been reached.    |  | | --- | | __Important:__  If you have based your QuickDraw GX printer driver on the sample LaserWriter IIsc driver from the QuickDraw GX v1.0.1 SDK or the Mac OS SDK, please see the updated sample and Read Me contained within the seed for details of important changes to this driver for QuickDraw GX v1.1.1. | |

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
