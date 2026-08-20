---
title: Open Transport's Limited Compatibility with 680x0
apple_id: DTS10001452
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-09-27'
source_url: https://developer.apple.com/library/archive/qa/nw/nw40.html
archived_at: '2026-07-18T02:29:46.361660Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [68K Open Transport Code on Power Macintoshes](Not%20Recommended%20Documentclose%20button.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW40Open Transport's Limited Compatibility with 680x0 |

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: I'm writing an application using the Open Transport native APIs. My original intention was to ship only a 68K version of the application, but I've heard that this will not be compatible with future versions of OT. Is this true?  A: Yes. We strongly recommend that you ship all OT native applications as fat applications. This will give your applications the maximum speed and compatibility.  Under System 7, OT provides OT native APIs for both 68K and PPC clients. This allows 68K OT clients to operate under emulation on PPC Macintoshes. This will not be supported under Copland, because Copland will not support the Apple Shared Library Manager, the dynamic linking technology used by 68K OT clients. Table 1 summarizes this information.   |  |  |  |  | | --- | --- | --- | --- | | __OT Version__ | __68K Client on 68K__ | __68K Client on PPC__ | __PPC Client on PPC__ | | OT 1.0.x | na (1) | Yes (2,3,4) | Yes | | OT 1.1 Sys 7 | Yes | Yes | Yes | | OT 1.5 Sys 7 | Yes | Yes | Yes | | OT Copland | na (5) | No (6) | Yes |   __Notes:__   1. OT 1.0.x was never shipped or supported on any 68K    Macintoshes. 2. You must link with the OT 1.1b6 or later libraries for this to    work. 3. Obviously you must not call routines that were introduced with    OT 1.1 4. Support for 68K clients on PPC is not well tested under OT    1.0.x. For this and many other reasons, you should emplore your    users to upgrade to 1.1. 5. Copland is a PPC product only. 6. Copland does not support ASLM, so it is not possible for it    to support OT 68K clients. |

#### [Jul 15 1997]

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
