---
title: FWSendSoftwareInterrupt vs. SendSoftwareInterrupt
apple_id: DTS10001558
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-02-13'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1002.html
archived_at: '2026-07-18T02:38:01.173664Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A QA1002FWSendSoftwareInterrupt vs. SendSoftwareInterrupt |

|  |
| --- |
| ---   Q: What is the difference between `SendSoftwareInterrupt` and `FWSendSoftwareInterrupt`?  A: A: `SendSoftwareInterrupt` in `DriverServicesLib` doesn't actually do anything except immediately call the associated interrupt handler.  `FWSendSoftwareInterrupt` depends on a patch to `WaitNextEvent` for it's behavior. In general when you call `FWSendSoftwareInterrupt`, the handler installed using `FWCreateSoftwareInterrupt` gets run the next time `WaitNextEvent` is called. When you call `FWCreateSoftwareInterrupt` one of the parameters is a `TaskID`. `FWSendSoftwareInterrupt` tries to make sure that the `TaskID` of the software interrupt matches the TaskID of the current process according to the Process Manager. If you don't care what the current process is when you get called (as would likely be the case for a driver) pass in `kInvalidID` instead of `FWCurrentTaskID` when you call `FWCreateSoftwareInterrupt`. This way the software interrupt will get called the next time `WaitNextEvent` gets called after you call `FWSendSoftwareInterrupt`.   ---  [Feb 13 2002] |

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
