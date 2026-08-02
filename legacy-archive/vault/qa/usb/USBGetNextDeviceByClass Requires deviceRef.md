---
title: USBGetNextDeviceByClass Requires deviceRef
apple_id: DTS10002269
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-09-28'
source_url: https://developer.apple.com/library/archive/qa/usb/usb03.html
archived_at: '2026-07-18T02:38:59.462874Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > USB](https://developer.apple.com/referencelibrary/HardwareDrivers/idxUSB-date.html)

|  |
| --- |
| Technical Q&A USB03USBGetNextDeviceByClass Requires deviceRef |

|  |
| --- |
| Q When I make the `USBGetNextDeviceByClass` call, error -43 (file not found) error is returned. My device is attached, and is displayed by USB Prober. The call used to work, but no longer. Why?  A If you make the `USBGetNextDeviceByClass` call, you must set the input `deviceRef` parameter to a valid device `ref` or to the predefined constant `kNoDeviceRef`. If the deviceRef parameter is a different value, then error -43 results. If you set the input `deviceRef` value to a valid `deviceRef`, then `USBGetNextDeviceByClass` returns the next device that is found in the "USB device list", which matches the specified criteria. The key point here is that the input `deviceRef` value must be valid or -1. Note that error -43 might still be returned, if there are no more devices in the device list. [Sep 28 1998] |

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
