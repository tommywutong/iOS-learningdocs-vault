---
title: WebObjects applications crashing on NT using IIS
apple_id: DTS10002273
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-10-30'
source_url: https://developer.apple.com/library/archive/qa/wov/wov01.html
archived_at: '2026-07-18T02:38:59.722892Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/DeveloperTools/index.html) > [WebObjects](https://developer.apple.com/library/archive/technicalqas/DeveloperTools/idxWebObjects-date.html) >

|  |
| --- |
| Technical Q&A WOV01WebObjects applications crashing on NT using IIS |

|  |
| --- |
| ---   Q: Why is my WebObjects application crashing on Windows NT? It worked fine before, but I just upgraded to patch 2, and now the applications crash consistently. I'm using IIS for my WebServer, and WebObjects 4.5.  A: There is a known bug that arises between IIS and patch 2 of WebObjects on Windows NT using IIS. The problem is the adaptor sends out empty headers. A patch (patch 3) is imminent, and a workaround is to subclass and extend the functionality of the adaptor to filter out (i.e., not send) empty packets across the wire.  Updated 30-October-2000 |

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
