---
title: 68K Open Transport Code on Power Macintoshes
apple_id: DTS10001460
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-03-14'
source_url: https://developer.apple.com/library/archive/qa/nw/nw48.html
archived_at: '2026-07-18T02:29:46.888892Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW4868K Open Transport Code on Power Macintoshes |

|  |
| --- |
| ---   Q: I'm writing some test code using `OTStreamOpen`. When I compile this code for PowerPC and run it on a Power Macintosh, it works just fine. When I compile this code for 68K and run it on a 68K, it also works fine. When I compile it for 68K and run it on a PPC, my application quits immediately. What's going on?  A: Open Transport has special Mixed Mode glue that allows 68K clients to run successfully on Power Macintosh computers. This glue is only available for a subset of the Open Transport API routines. This has caused some confusion, which the OT 1.1.1 SDK attempts to correct by placing the routines in distinct header files.  The only routines that are callable by 68K clients running emulated on PPC machines are those defined in "OpenTransport.h", "OpenTptAppleTalk.h" and "OpenTptInternet.h". All routines defined in all other header files (specifically those in "OpenTptClient.h" and "OpenTptCommon.h") are available only to PPC-native clients on PPC machines, or 68K clients on 68K machines.  In addition, non-application code (such as OT modules, drivers, port scanner and configurators) will only run under the native architecture. For example, it's not possible to compile an OT driver as 68K code and have it run on a PPC.  In general, we recommend that you build all your Open Transport application code fat, both to run as quickly as possible and to guarantee future compatibility (see [Technical Q&A NW 40](Legacy%20Documentclose%20button.md)). |

#### [Mar 14 1997]

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
