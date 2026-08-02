---
title: Hidden Volumes in HFS
apple_id: DTS10001189
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-01'
source_url: https://developer.apple.com/library/archive/qa/fl/fl03.html
archived_at: '2026-07-18T02:29:28.614428Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



A primary category has yet to be selected for this document.

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > File Management](https://developer.apple.com/referencelibrary/Carbon/idxFileManagement-date.html)

|  |
| --- |
| Technical Q&A FL03Hidden Volumes in HFS |

|  |
| --- |
| ---   Q: Is there a preferred way to define "hidden" volumes in HFS (i.e., the way AOCE declares "Mail Enclosures", etc.)?  A: AOCE's Mail Enclosures volume is hidden because its root directory has the `kIsInvisible` Finder flag set. You can use the `SetIsInvisible` routine in the `MoreFiles` DTS sample code to make the root directory of a volume invisible, so the next time the volume is mounted, the Finder doesn't show that volume. There is no way to force the Finder to notice the change and make the volume invisible on the fly.  Note that the Finder did not support invisible volumes until System 7 Pro (System 7.1.1). Therefore, with System 7.1 and earlier versions, you can't make volumes invisible. The `SetIsInvisible` function can be found in the MoreFilesExtras.c file at the following path on the Developer CD:  Dev.CD Feb 95:Sample Code:MoreFiles 1.2.1:MoreFilesExtras.c |

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
