---
title: Workaround for PLookupName Bug
apple_id: DTS10001467
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-07-20'
source_url: https://developer.apple.com/library/archive/qa/nw/nw55.html
archived_at: '2026-07-18T02:29:47.241338Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW55Workaround for PLookupName Bug |

|  |  |
| --- | --- |
| ---   Q: I've found that there is a bug with how Open Transport handles the NBP `PLookupName` call? How can I work around this problem?  A: To expound, there is a bug with how OpenTransport (up to and including v 1.3) handles the NBP `PLookupName` call, such that Open Transport can write past the end of the lookup buffer by up to 2 bytes. The problem only applies to the `PLookupName` call and does not occur with the Open Transport equivalent - `OTLookupName`.  The preferred solution to this bug is to upgrade your networking code to use the Open Transport `OTLookupName` call rather than the outdated `PLookupName` call. `OTLookupName` will be supported under [Mac OS X](https://developer.apple.com/macosx/). The `PLookupName` as well as the other [AppleTalk Manager](https://developer.apple.com/documentation/carbon/Carbon_Specification/CarbSpecWebIntro.html) calls will not be supported under [Mac OS X](https://developer.apple.com/macosx/).  The alternate solution is to set the `NBPretBuffSize` parameter to be 2 bytes less than the actual size of the buffer pointed to by `NBPretBuffPtr` as shown in the code below. This solution will work for all releases of Open Transport and will not be affected if the problem is fixed by Open Transport.   |  | | --- | | ``` char buffer[1024]; ... gPBLkUP->myMPP.NBPretBuffSize = sizeof(buffer) - 2; gPBLkUP->myMPP.NBPretBuffPtr = &buffer; result = PLookupName((MPPParamBlock *) &myMPP, ...); ``` | |

#### [Jul 20 1998]

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
