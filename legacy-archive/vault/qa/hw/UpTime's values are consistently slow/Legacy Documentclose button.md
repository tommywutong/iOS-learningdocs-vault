---
title: UpTime's values are consistently slow?
apple_id: DTS10001303
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-10-19'
source_url: https://developer.apple.com/library/archive/qa/hw/hw31.html
archived_at: '2026-07-18T02:29:36.647725Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A HW31UpTime's values are consistently slow? |

|  |
| --- |
| ---   Q: We're using `UpTime` and finding the values are consistently slow when running on certain accelerator cards. How can we get the correct timing values?  A: 8500/9500/8600/9600 machines measure the computer's bus speed against the VIA timer, and use this value to look up the timing information from a table in the ROM. This table has data for all integral values between 25 and 66 mhz, as well as 33.333 mhz. Some later machines also support integral speeds between 67 and 125 mhz. The timing information is used to set the time base, which converts from absolute time to nanoseconds.  If the bus timing is incorrect, or does not exactly match one of the values specified in the ROM table, then the time base will be set incorrectly, and `UpTime` will be consistently off. For example, if the actual bus speed is 44.5 mhz, then `UpTime` will actually run at 44.5/45, or about 99% of the correct value. This causes `UpTime` to drift from other clocks on the Mac.  Accelerator card vendors should choose timings that are in the list described above. Apple is investigating options that may fix this in future OS releases, but no plans or decisions have been announced. |

#### [Oct 19 1998]

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
