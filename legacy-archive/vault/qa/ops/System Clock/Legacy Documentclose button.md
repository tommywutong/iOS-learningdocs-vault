---
title: System Clock
apple_id: DTS10001482
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/ops/ops01.html
archived_at: '2026-07-18T02:29:48.255918Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS01System Clock |

|  |
| --- |
| Q Has the manner in which the system clock keeps time changed? The Date & Time control panel in System 7.5 only allows a range of years from 1920 through 2019, and I thought that all clock ticks counted up from 1904.   A The date and time information in the Date & Time control panel is obtained from the system global variable 'Time', which is a four-byte value that stores the number of seconds elapsed since midnight, January 1, 1904. The System 7.5 Date & Time Control Panel allows you to access the range of dates from 1 January 1920 through 31 December 2019 (the System 7.1 Date & Time Control Panel did also), but this is not the result of any changes in the global variable 'Time' -- it is merely an interface change. The 'Ticks' global variable, which you can access with the function 'TickCount', returns the number of ticks elapsed since you last started up your system. This has not changed either. Developer CD, March 1995: Technical Documentation: _Inside Macintosh: Operating System Utils_: Chapter 4 - Date, Time and Measurement Utilities: page 4-4.  Developer CD, March 1995: Documentation: _Inside Macintosh: Macintosh TB Essentials_: Chapter 2 - Event Manager: page 2-112. Updated: 1-May-95 |

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
