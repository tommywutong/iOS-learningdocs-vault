---
title: Fixing the crash in the Picture Sharing code example
apple_id: DTS10001747
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2003-01-21'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1224.html
archived_at: '2026-07-18T02:38:19.739205Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Cocoa](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCocoa-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Cocoa](https://developer.apple.com/referencelibrary/Cocoa/index.html)

|  |
| --- |
| Technical Q&A QA1224Fixing the crash in the Picture Sharing code example |

|  |
| --- |
| ---   Q: Why does the Picture Sharing code example crash?  A: The Rendezvous example installed with the Mac OS X Developer Tools (July 2002 or later) at /Developer/Examples/Foundation/PictureSharing has a bug in it that causes it to crash under some conditions. To fix this bug, the following line needs to be removed from PicSharingController.m, line 169:  [incomingConnection release];  The incomingConnection is handed to the program already autoreleased, so there is no need to release it, and in fact doing so is an error that causes the program to crash. This bug in the code example should be fixed in an upcoming release of the Mac OS X Developer Tools.   ---  [Jan 21 2003] |

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
