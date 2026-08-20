---
title: Print Job Cancelling
apple_id: DTS10001223
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd08.html
archived_at: '2026-07-18T02:29:32.474795Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD08Print Job Cancelling |

|  |  |  |
| --- | --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: I've been experimenting to see what happens when a print job is cancelled part of the way through, and if I cancel when `OpenConnection` and `StartSendPage` have both completed successfully, I get unexpected `CleanUpOpenConnection` and `CleanupStartSendPage` messages. If I cancel at another other point in the job (for example, during `RenderPage` via the Remove button in the DTP status window), `CleanUpStartSendPage` and `CleanUpOpenConnection` messages are passed through after `ImageDocument` exits. This behavior seems very odd, and it doesn't appear to be discussed anywhere in the documentation. Shouldn't `CleanUpOpenConnection` and `CleanupStartSendPage` be called only if their respective routines return an error?  A: The unexpected `CleanUpOpenConnection` and `CleanupStartSendPage` messages are coming from the default implementations of `ImageJob` and `ImagePage`. The `ImageJob` code tries to `Send_GXSetupImageData`, and if an error occurs, it sends `CleanUpOpenConnection`. `ImagePage` tries to `Send_GXRenderPage` and sends `CleanupStartSendPage` if an error occurs.  If `GXStartSendPage` and/or `GXOpenConnection` do not complete successfully, the respective clean-up calls are not sent. These clean-up calls are sent only if `openConnection` and/or `startSendPage` are completed, and something goes wrong after completion.  Although the documentation states otherwise, this behavior is correct for the existing code, as shown here:   |  | | --- | | ``` ImageJob ... Send_GXOpenConnection(_); if (anErr) <dispose of data> Send_GXSetupImageData(_); if (anErr) {   Send_GXCleanUpOpenConnection(_);   <dispose of data> } ... ImagePage ... Send_GXStartSendPage(_); if (anErr) <dispose of data> Send_GXRenderPage(_); if (anErr) {   Send_GXCleanupStartSendPage(_);   <dispose of data> } ... ``` | |

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
