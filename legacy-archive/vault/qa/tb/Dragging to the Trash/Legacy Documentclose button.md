---
title: Dragging to the Trash
apple_id: DTS10002217
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-11-27'
source_url: https://developer.apple.com/library/archive/qa/tb/tb31.html
archived_at: '2026-07-18T02:38:56.727095Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB31Dragging to the Trash |

|  |
| --- |
| Q How do I support dragging to the trash and avoid having the Finder create a clipping inside the trash? I tried several options but they all failed.   A There is no good way to prevent both a clipping file and the failed-drag zoom feedback. The problem is that Finder treats the trash like a folder for this purpose. In this context, the drag succeeds or fails according to the user's supposed intent with respect to a folder.   However, in our opinion, this is good, since it is consistent with the Trash metaphor. When the user drags an icon from a Finder window into the trash, she expects the trash to get fat so she can later change her mind, open the Trash and drag the icon out. Creating a clipping file in the trash merely extends the metaphor. The only problem this might cause is that the user ought to be able to reverse her decision and drag the clipping back into the application. If your application doesn't already support this action, you may have some work ahead.  We realize other apps manage to avoid making the Trash fat. This is, in our opinion, a Bad Thing. A hack. Wrong. Nevertheless, if you still feel you need to avoid making the trash fat, it might be possible to do so. It would probably involve creating a file via flavorTypePromiseHFS, then deleting it before Finder had a chance to make the Trash fat. Unfortunately, since this involves "fooling" Finder, it isn't likely to work for future versions of Finder even if it does work today. [Nov 27 1996] |

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
