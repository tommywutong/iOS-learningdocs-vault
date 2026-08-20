---
title: MacTCP I/O
apple_id: DTS10001514
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat04.html
archived_at: '2026-07-18T02:29:51.112635Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A PLAT04MacTCP I/O |

|  |
| --- |
| ---   Q: I am having a problem killing MacTCP I/O: I issue asynchronous MacTCP reads and writes during the operation of my application, and I occasionally need to kill any outstanding I/O. I'm trying to use the `PBKillIO` call, giving it the reference number of the MacTCP driver. According to _Inside Macintosh_, `PBKillIO` should cause all I/O on that driver to complete with an error (cause any completion routines to fire). Unfortunately, this doesn't seem to work -- my completion routines aren't getting called. To make this happen, I have to abort the connection instead of calling `KillIO`, which isn't what I want -- I need the connection to stay up.  Is there a known problem with `PBKillIO` and MacTCP?  A: `KillIO` is not supported by MacTCP, since it only affects `PBReads` and `PBWrites`, where MacTCP reads and writes are `PBControl` calls. MacTCP ignores `KillIO` calls to the driver (an `ioResult` of 0 is returned every time). The only way to kill an outstanding read/write in MacTCP is with `TCPAbort`. Unfortunately, this means that you do lose the connection. |

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
