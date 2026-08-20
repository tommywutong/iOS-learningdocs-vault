---
title: Using GXNewPaperType
apple_id: DTS10001258
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-01-09'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd43.html
archived_at: '2026-07-18T02:29:34.373899Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD43Using GXNewPaperType |

|  |  |  |
| --- | --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: How can I create a new GX papertype on the fly within my QuickDraw GX application? I use `GXNewPaperType`, but for some reason the new papertype doesn't show up in the page set-up dialog.  A: This is actually related to a known bug in QuickDraw GX. If an application uses `GXNewPaperType` to create an application-defined paper type, GX doesn't find it in the page set-up dialog as it should. This is because GX is setting up the paper type flags incorrectly. But there is a workaround....  You need to create a job and custom `paperType` and flatten it to a file within the extensions folder. `GXNewPaperType` will create a valid `paperType`, but it does not set up the creator and the `paperType` flags correctly. Therefore, after calling `GXNewPaperType` to set up the new custom `paperType`, you'll need to set the `paperTypeFlags` and the creator. The following code fragments will do the trick.  The globals used to set up the creator and `paperType` flags:   |  | | --- | | ``` OSErr           collectionErr = noErr; Str255          paperTypeName; gxRectangle     paperDims; gxRectangle     pageDims; Collection      paperTypeCollection; gxFlagsInfo     paperTypeFlags; gxCreatorInfo   paperTypeCreator;   // //  We use this information to check to make sure that our //  new paperType was set up as we thought after calling GXNewPaperType // GXGetPaperTypeName( theNewPaperType, paperTypeName ); GXGetPaperTypeDimensions( theNewPaperType, &pageDims, &paperDims);  // //  We need to set our new paperType's flags and creator to allow //  GX to recognize it. // paperTypeCollection = GXGetPaperTypeCollection( theNewPaperType );  paperTypeFlags.flags = gxOldAndNewPaperTypeFlag;  collectionErr = AddCollectionItem( paperTypeCollection, gxFlagsTag,                                    gxPrintingTagID, sizeof(gxFlagsInfo),                                    &paperTypeFlags );  paperTypeCreator.creator = gxUserPaperType;  collectionErr = AddCollectionItem( paperTypeCollection, gxCreatorTag,                                    gxPrintingTagID, sizeof(gxCreatorInfo),                                    &paperTypeCreator ); ``` |   At this point, when a print dialog is displayed, the `paperType` list is recreated each time. This behavior ensures that any newly created `paperType` will be found from within a running app which is creating `paperTypes`.  After you have created the custom `paperType` and valid job, you'll need to call `GXFlattenJob` and `GXFlattenPaperType` and save this info into a file within the extension folder. Then it should show up in your page setup paper type list. |

#### [Jan 09 1997]

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
