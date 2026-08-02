---
title: Inputting characters using InputMethod
apple_id: DTS10001393
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-10-18'
source_url: https://developer.apple.com/library/archive/qa/java/java18.html
archived_at: '2026-07-18T02:29:41.884230Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA18Inputting characters using InputMethod |

|  |
| --- |
| ---   Q:I cannot input Japanese characters using `InputMethod` into a text field. Why not?  A: There are several issues to consider when using the `InputMethod` into a text field. If you are using an applet, you may encounter difficulty under MRJ 2.0. No matter which input mode of the `InputMethod`, Roman alphabetic characters will be sent to the text field. This problem is fixed in MRJ 2.1 (and later).  This problem also affects applets running in Netscape Navigator with the MRJ plugin (Communicator 4.7 is OK). Applications are not affected by this problem. [Oct 18 1999] |

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
