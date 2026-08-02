---
title: Detecting the Microseconds Trap
apple_id: DTS10002202
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb16.html
archived_at: '2026-07-18T02:38:56.102459Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB16Detecting the Microseconds Trap |

|  |
| --- |
| Q I am creating FAT applications, and I'm using the Microseconds trap. This helps to keep my common source code simple, because I don't have to use the Time Manager to do timings on 68K machines and Microseconds on PPC machines. Which versions of the System software include the Microseconds trap, and on which models is this included?   A You have to detect the availability of the Micrososeconds trap with the TrapAvailable routine, because its availability varies with the software that is installed and on the version of the System software that is used. Microseconds was first implemented in QuickTime, which could optionally be installed as far back as System 6.0.7. Microseconds wasn't officially documented until the release of _Inside Macintosh: Operating System Utilities_. The following code can be used to detect the Microseconds trap:   ``` #define _Microseconds 0xa193 // from traps.h  if (GetToolTrapAddress(_Microseconds) == GetToolTrapAddres(_Unimplemented))  // use extended time manager else  // use Microseconds ```  [Jun 01 1995] |

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
