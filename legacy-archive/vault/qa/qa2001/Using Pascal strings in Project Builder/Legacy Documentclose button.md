---
title: Using Pascal strings in Project Builder
apple_id: DTS10001605
resource_type: QA
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2001-06-28'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1053.html
archived_at: '2026-07-18T02:38:05.953690Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTools-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Tools > Compiling & Debugging](https://developer.apple.com/referencelibrary/DeveloperTools/idxCompilersDebuggers-date.html)

|  |
| --- |
| Technical Q&A QA1053Using Pascal strings in Project Builder |

|  |
| --- |
| ---   Q: I'm getting warnings from the compiler (gcc) about my Pascal strings. How can I get them to be recognized in Project Builder?  A: Usually Pascal strings work just fine when doing Carbon development in Project Builder, but under some situations when building your project or checking syntax on a source file, you may run into the "unknown escape sequence '\p'" warning. This means that the compiler has not been told how to handle your Pascal strings. To fix this, go to your target's Build Settings tab and under Build Settings -> OTHER_CFLAGS add "-fpascal-strings". This tells the compiler to replace the '\p' with a byte containing the length of the string.     ---  [Jun 27 2001] |

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
