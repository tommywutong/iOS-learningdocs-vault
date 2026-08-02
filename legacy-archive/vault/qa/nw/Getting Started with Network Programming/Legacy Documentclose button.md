---
title: Getting Started with Network Programming
apple_id: DTS10001444
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/nw/nw32.html
archived_at: '2026-07-18T02:29:45.912578Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Networking](https://developer.apple.com/referencelibrary/Carbon/idxNetworking-date.html)

|  |
| --- |
| Technical Q&A NW32Getting Started with Network Programming |

|  |
| --- |
| ---   Q: I am interested in network programming on the Macintosh, can you give me any hints?  A: There are a variety of network programming strategies and API's available on the Mac OS. The choice of API will depend upon your background, experience, and goals.  For developers with a background in UNIX, a need for POSIX compliance, or a need to deploy an application across MacOS and UNIX systems, OpenTransport is a logical choice.  OpenTransport is also the preferred choice for a Mac-only application. It provides the highest performance of all network methods. The older MacTCP API's interface is being phased out, and Apple encourages all developers to move to the Open Transport XTI API.  The OpenTransport API's do not implement the higher layer internet protocols such as HTTP, FTP, gopher, etc. OpenTransport is, however, a building block with which these protocols are typically implemented.  Although Apple does not provide one yet, there are a few internet access libraries being developed by various third parties.  For the CodeWarrior environment, there is a certain amount of network access available in the Powerplant framework.  Finally, for developers with a background in Microsoft Windows, or a need to implement a cross-platform application, WinSock compatibility services are provided through third-party software available from NetManage (408 973-7171).  A good place to start is to investigate the [Open Transport](https://developer.apple.com/macos/opentransport/) web pages. |

#### [May 14 1996]

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
