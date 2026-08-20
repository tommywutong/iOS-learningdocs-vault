---
title: Problems with Stitching
apple_id: DTS10002045
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qtvr/qtvr01.html
archived_at: '2026-07-18T02:38:50.223513Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Virtual Reality](https://developer.apple.com/referencelibrary/QuickTime/idxVirtualReality-date.html)

|  |
| --- |
| Technical Q&A QTVR01Problems with Stitching |

|  |
| --- |
| Q I can see the stitch command in the QuickTime VR template, but when I insert my information, highlight the command, and press return, all that happens is that it gives me the definition of the stitch command. What am I doing wrong?   A In MPW, when you type "command - <enter>", you get a list of all the variables that you can place after the command. Highlight all of the information you want to add to the command, and press Return. If anything is incorrect, you get a list of variables that you can place after the command. In other words, it's telling you that you entered something incorrectly and that you should choose the correct version from the commands it's displaying.   Q Whenever I try to stitch photos together with the QuickTime VR Tools, I get the following error message:  ```     File CorrelateTools.c; Line 1397 ## Assertion failed: rr             ### MPW Shell - stitch aborted. ```   This error occurs when the PICT files to be stitched are not found, or when they cannot be read. I tried running the example from the documentation, and got the same error message. The paths are all set correctly according to the protocol outlined in the Development Tool Suite binder. The following is the text of the worksheet I am using:   ```     set panInFolder "Beau Soleil:Photos:192 x 128"     set panOutFolder "Beau Soleil:Photos:Stitched PICTs"     set panFOV 50     set panRotate 0     set panX 100     set panY 0     set panDX 40     set panDY 20     export panRotate panFOV panX panY panDX panDY panOutFolder      Stitch192NoWrap 21-31 Sydney.192.Pan      File CorrelateTools.c; Line 1397 ## Assertion failed: rr      ### MPW Shell - stitch aborted. ```  A The error you are getting is definitely a File Not Found error. Try double-checking the accuracy of the spelling. For example, is the folder you call "192 x 128" actually "192x128" (with or without spaces around the "x")? It might help to rename all the folders involved so there are no spaces in the names.   Q Why does Stitch crash with "xMin>=cRect.left&&xMax<=cRect.right"?   A You need to set both -cyldim parameters to be 10 percent greater in both directions than what the verbose Stitch tells you the cylinder resolution actually is. For example, if Stitch returns "cyl res: 900 2000", include "-cyldim 990 2200" in the stitch command, and omit outWidth and outHeight. These take a lot of memory, and if Stitch runs out of memory, it crashes. Outwidth and outHeight can also cause distortions, so it is preferable to resize your images in another application, such as PhotoShop.   [Jun 01 1995] |

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
