---
title: Cocoa-Java quit/cancel-quit header bug in Mac OS X 10.0
apple_id: DTS10001574
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-04-09'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1021.html
archived_at: '2026-07-18T02:38:02.055080Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Cocoa](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCocoa-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Cocoa > Java](https://developer.apple.com/referencelibrary/Cocoa/idxJava-date.html)

|  |
| --- |
| Technical Q&A QA1021Cocoa-Java quit/cancel-quit header bug in Mac OS X 10.0 |

|  |
| --- |
| ---   Q: Why does my new/modified Cocoa Java application quit when the user cancels quitting, and cancel quitting when it should really quit?  A: Mac OS X 10.0 contains a bug in the headers for Cocoa Java's NSApplication class. Cocoa Java programs that rely on using the constants NSApplication.TerminateNow or NSApplication.TerminateCancel and have been compiled with the headers in Mac OS X 10.0 will find that they are backwards; the integer values of those constants were reversed by mistake. Thus, developers should use the correct (reverse) integer values when developing their programs, to get the desired behavior. Existing, not-recompiled apps should not be affected by this bug.   ---  [Apr 09 2001] |

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
