---
title: Static Socket Numbers
apple_id: DTS10001424
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw12.html
archived_at: '2026-07-18T02:29:44.500650Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW12Static Socket Numbers |

|  |
| --- |
| ---   Q: We created an application that allows many users to communicate and send files on a common socket number. ___Inside Macintosh: Networking_____states on page 7-6__that 64-127 socket numbers are available for program development, but not for a released product. We want to use a static socket number, since opening a different dynamic socket for each machine to send duplicate information is pointless, and it would have excessive overhead.  We want to apply for a socket number within the range of 1-63 (_Inside Macintosh: Networking_ states these are reserved for use by Apple) so that there is no chance that Apple or another developer could create a product that tries to use the same socket. If we can obtain an assigned socket number, all future applications that we create will use the same socket number.  A: We understand your need for a well-known, static DDP socket number, since your application multicasts/broadcasts to a well-known number. Unfortunately, however, Apple does not assign static socket numbers.  Your best bet would be to pick an arbitrary number (in whatever range you feel safest) and use it, but allow the user (or the network administrator) to modify that number via a control panel (possibly an administrative panel that uses a preference file that the administrator distributes, or an administrative server that provides this number).  While this method doesn't guarantee that you'll have sole use of a socket number, it does allows you to have some centrally administered options. |

#### [June 01 1995]

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
