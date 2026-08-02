---
title: Derived Media Handler Components Update
apple_id: DTS10001951
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1996-08-21'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc08.html
archived_at: '2026-07-18T02:38:46.816784Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime Component Creation](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeComponentCreation-date.html)

|  |
| --- |
| Technical Q&A QTMCC08Derived Media Handler Components Update |

|  |
| --- |
| Q What is a practical limit on data transfer rates for the base media handler on Power Macintoshes with PCI and QuickTime 2.5? Also, is the MPEG media handler derived from the base one?   A The practical limit on data transfer rates depends on your drive and SCSI bus. With a high performance hard drive connected to a PCI SCSI card, I've seen video data transfer rates up to 15 MB/sec. All media handlers, except for Sound and Video, are derived from the base media handler. This includes MPEG, text, tween, 3d, timecode, music, and sprites. You should also be aware of the fact that as of QuickTime 2.0, the statement in _Inside Macintosh_ regarding performance limitations of Derived Media Handlers is no longer accurate, because you now have access to everything we use inside QuickTime's sound and video media handlers. _Inside Macintosh_ was referring to the fact that the Data Handler API wasn't yet publicly available for versions of QuickTime earlier than 2.0. [Aug 21 1996] |

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
