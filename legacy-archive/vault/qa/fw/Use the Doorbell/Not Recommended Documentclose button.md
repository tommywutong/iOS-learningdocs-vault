---
title: Use the Doorbell
apple_id: DTS10001201
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/fw/fw01.html
archived_at: '2026-07-18T02:29:29.212082Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/index.html) > [FireWire](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/idxFireWire-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > FireWire](https://developer.apple.com/referencelibrary/HardwareDrivers/idxFireWire-date.html)

|  |
| --- |
| Technical Q&A FW01Use the Doorbell |

|  |
| --- |
| ---   Q: What is the proper use of a FireWire SBP2 (Serial Bus Protocol 2) device's Doorbell?  A: The Doorbell is used to signal the waiting SBP2 device to reexamine the current ORB (Object Request Block) pointer. If the SBP2 device is currently executing an ORB, then ringing the Doorbell will have no effect (other than a little traffic on the FireWire bus).  Since some drivers will be creating ORB chains that do not have status notifications, the driver may not know whether the SPB2 device is processing an ORB or it is idle when it appends a new ORB to the chain. For this reason, it is acceptable to always ring the Doorbell. If the SPB2 device is still executing the previous ORB(s) sent to it, the Doorbell will not affect anything, and the new ORB that was just appended will be executed as if it had been part of the previously sent ORB chain. If the SPB2 device has finished processing the previous ORB chain, then ringing the Doorbell will cause it to fetch the newly appended ORB and begin executing it.  If, however, you set the immediate flag for `FWSBP2Append`, there is no point in then ringing the Doorbell (unless you later append more ORBs). Ringing the Doorbell only makes sense after calling `FWSBP2Append` with an ORB that does not have the immediate flag set.  Since always ringing the Doorbell is a much simpler algorithm than trying to determine if you need to ring the Doorbell or not, and has no penalty other than a four-byte write on the FireWire bus, we recommend that you not bother to avoid ringing the Doorbell. |

#### [May 17 1999]

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
