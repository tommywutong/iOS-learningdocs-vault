---
title: fBroadCastAddr Always Zero
apple_id: DTS10001470
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-03-08'
source_url: https://developer.apple.com/library/archive/qa/nw/nw58.html
archived_at: '2026-07-18T02:29:47.418790Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW58fBroadCastAddr Always Zero |

|  |  |
| --- | --- |
| ---    ---   __Q:__When I call `OTInetGetInterfaceInfo`, the `fBroadcastAddr` field always comes back as zero. Is this a bug?  A: Not really. The field describes how the broadcast address was configured. If it is zero, the broadcast address has not been explicitly configured. In this case, IP will synthesize a broadcast address based on the IP address and subnet mask.  If the broadcast address was explicitly configured, `fBroadcastAddr` will be the configured address. On current systems, the only time `fBroadcastAddr` is non-zero is when a DHCP server supplies it via DHCP option 28.  You can calculate the actual broadcast address being used with the following code.   |  | | --- | | ``` broadcastAddr = info.fBroadcastAddr; if (broadcastAddr == 0) {     broadcastAddr = info.fAddress | ~info.fNetmask; } ``` | |

#### [Mar 08 1999]

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
