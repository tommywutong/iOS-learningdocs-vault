---
title: MacTCP and UDP Performance
apple_id: DTS10001419
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw07.html
archived_at: '2026-07-18T02:29:44.274117Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Internet & Web](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxInternetWeb-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Internet & Web](https://developer.apple.com/referencelibrary/InternetWeb/index.html)

|  |
| --- |
| Technical Q&A NW07MacTCP and UDP Performance |

|  |
| --- |
| ---   Q: We are trying to tunnel IPX through MacTCP (version 2.0.X), and we are experiencing a performance slowdown. We ran some timing tests on our routines and noticed that it takes approximately 10 milliseconds between when we post the read to UDP and when our completion routine is called. It also takes approximately 10 milliseconds for our send completion routine to be called after we post a send to UDP. How does MacTCP implement the completion-routine calling mechanism to its clients? Is there some sort of timer involved? Is there anything that we can do to speed up this process?  A: The sluggish performance you are experiencing with UDP stems from MacTCP's use of a Time Manager task (scheduled every 10 milliseconds) to process UDP commands. Since this portion of MacTCP would have to be rewritten to eliminate the Time Manager tasks, there doesn't appear to be anything you can do to improve the UDP performance. |

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
