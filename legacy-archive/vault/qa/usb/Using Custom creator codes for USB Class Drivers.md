---
title: Using Custom creator codes for USB Class Drivers
apple_id: DTS10002267
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-09-28'
source_url: https://developer.apple.com/library/archive/qa/usb/usb01.html
archived_at: '2026-07-18T02:38:59.416865Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > USB](https://developer.apple.com/referencelibrary/HardwareDrivers/idxUSB-date.html)

|  |
| --- |
| Technical Q&A USB01Using Custom creator codes for USB Class Drivers |

|  |
| --- |
| Q Can I use my own creator code for my USB class driver so that I can associate custom icons with the file?   A For the current releases of Mac OS USB to v1.0.1, you must set the creator code of a USB class driver file, to `'usbd'`; otherwise, the driver will not be detected. We are investigating a modification to the driver detection mechanism. When this change occurs, this Q&A will be updated and notice will be posted to subscribers on the USB mailing list. For information on the USB mailing list, go to the [Mac OS USB Developers web site](https://developer.apple.com/dev/usb/devinfo.htm).   [Sep 28 1998] |

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
