---
title: Problems with Caching Drivers on PowerMac 9500
apple_id: DTS10001160
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/dv/dv19.html
archived_at: '2026-07-18T02:29:26.252937Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A DV19Problems with Caching Drivers on PowerMac 9500 |

|  |
| --- |
| ---   Q: I'm having problems with our caching drivers on the PowerMac 9500. Our drivers allocate a large (up to 4 MB) amount of RAM early in the boot process. If I set the driver's cache size to 4 MB, the computer locks up as soon as the driver is executed. If I set the cache size to 2 MB, the driver loads, and executes properly, but the computer gets a bus error much later in the boot process (after MacsBug loads, and after the MacOS screen is displayed, but before Finder executes). If I set the cache size to 1 MB, everything runs properly. What's going on here?  A: Because of `OpenFirmware` requirements, the boot stack on the new PowerMac 9500 CPUs was moved to 4MB. As a result, you can't grow the system heap past 4 MB or a system crash will occur.  If possible, try to defer allocating memory until INIT time. The `'sysz'` mechanism is supported by the enabler (`'boot'` 3) when loading INITs. |

#### [Sep 15 1995]

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
