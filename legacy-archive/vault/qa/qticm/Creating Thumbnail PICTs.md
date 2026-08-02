---
title: Creating Thumbnail PICTs
apple_id: DTS10001927
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qticm/qticm08.html
archived_at: '2026-07-18T02:38:45.849077Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Compression & Decompression](https://developer.apple.com/referencelibrary/QuickTime/idxCompressionDecompression-date.html)

|  |
| --- |
| Technical Q&A QTICM08Creating Thumbnail PICTs |

|  |
| --- |
| Q How can I display the thumbnail of the PICT instead of some generic icon when I create QuickTime PICT files? This would really help with distinguishing files when someone wanted to create a movie and had a lot of these PICTs around.   A Follow this procedure: 1. Get the thumbnail. You can use either the MakeThumbnailFromPicture or MakeThumbnailFromPictureFile routines as listed in the ImageCompression interface file. It will pass back the PicHandle for the thumbnail. To install into the Finder, you need icon resources (ICN#, ics#, icl8, ics8, icl4, ics4).  2. Make the thumbnail into a 'icsx' format to store it as a resource. (Please see MakeIcon on the Developer CD. It is not modified for pichandles so you may have to add a DrawPicture. Basically, you need to create a GWorld and create the appropriate 16- or 32-bit image.)  3. Add icons to resource. You can use the basic Resource Manager's WriteResource and AddResource calls to add the resource.  4. Set Finder bits: Stuff icon resources into the file itself with resource ID kCustomIconResource, and set the hasCustomIcon bit.   ``` { myCInfoPBRec.ioFlFndrInfo.fdFlags := BOR(myCInfoPBRec.ioFlFndrInfo.fdFlags, $0400) }. ```  [May 01 1995] |

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
