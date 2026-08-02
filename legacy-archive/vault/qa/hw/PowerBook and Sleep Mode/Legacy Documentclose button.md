---
title: PowerBook and Sleep Mode
apple_id: DTS10001274
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/hw/hw04.html
archived_at: '2026-07-18T02:29:35.336825Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A HW04PowerBook and Sleep Mode |

|  |
| --- |
| ---   Q: Our multimedia presentation software does not awaken properly on a PowerBook that has come out of sleep mode. Are there any special handling requirements to recover from sleep mode? What event should we be watching for?  A: These are some of the changes to the system state when a PowerBook goes to sleep:   - All AppleTalk connections are lost, as the AppleTalk driver is turned off. - The serial ports are entirely shut down to conserve power.   It is not clear why these two changes would affect your multimedia presentation software. However, there are two Macintosh Technotes available that relate to your situation: ["HW 24, Little PowerBook in Slumberland,"](https://developer.apple.com/library/archive/technotes/hw/hw_24.html) which provides a brief overview of the sleep process, and ["HW 31, Sleep Queue Tasks,"](https://developer.apple.com/library/archive/technotes/hw/hw_31.html) which presents additional material regarding the sleep process. The second Technote includes sample code that demonstrates a sleep-queue task implementation. The sleep-queue task provides a means by which your program can save state information that otherwise might be lost. Typically, this is important for a networked process, but it's not clear why your application would have to monitor this type of information.  You might want to implement a sleep-queue handler so you can drop to the debugger when the handler is notified that the unit is waking up. This would allow you to take debugging steps before a crash occurs. |

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
