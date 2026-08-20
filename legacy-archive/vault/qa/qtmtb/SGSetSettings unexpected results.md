---
title: SGSetSettings unexpected results
apple_id: DTS10002025
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1999-10-11'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb55.html
archived_at: '2026-07-18T02:38:49.444724Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Creation](https://developer.apple.com/referencelibrary/QuickTime/idxMovieCreation-date.html)

|  |
| --- |
| Technical Q&A QTMTB55SGSetSettings unexpected results |

|  |
| --- |
| ---   Q: I'm calling the QuickTime `SGSetSettings` function to configure the sequence grabber and its channels. The problem is, after I call this function once, subsequent calls to the function always return an error code, and the settings dialog box no longer appears. What's going on?  A: When you call the `SGSetSettings` function (described in [Inside Macintosh: QuickTime Components](https://developer.apple.com/documentation/quicktime/qtdevdocs/RM/frameset.htm), page 5-50) the sequence grabber will dispose of any of its current channels before applying this configuration information. It then opens connections to new channels as appropriate.  What this means is if you've created sequence grabber channels yourself (for example, with the `SGNewChannel` function) prior to calling `SGSetSettings`, the old references to these channels are no longer valid, and you must query the sequence grabber using the `SGGetIndChannel` function (described in Inside Macintosh: QuickTime Components, page 5-33) to re-acquire the channel references. [Oct 11 1999] |

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
