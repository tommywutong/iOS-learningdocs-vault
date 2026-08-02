---
title: Apple Mass Storage Class Driver always matches to my device at startup
apple_id: DTS10001678
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-05-23'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1131.html
archived_at: '2026-07-18T02:38:15.042759Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Storage](https://developer.apple.com/referencelibrary/HardwareDrivers/idxMassStorageDevices-date.html)

|  |
| --- |
| Technical Q&A QA1131Apple Mass Storage Class Driver always matches to my device at startup |

|  |
| --- |
| ---   Q: I have a mass storage device for which I've written a vendor specific driver. For MacOS 9.x, if I have the device attached and restart the system, the Apple Mass Storage Class driver always gets matched to my device. Why is this happening and can anything be done to force my driver to be used instead?  A: This is a known issue which results in trying to support booting the Macintosh from a USB mass storage device. At boot time, only drivers from the ROM are available to the system. The Apple Mass Storage class driver is implemented in ROM and is the only driver available to support USB Mass Storage class devices. At system start time, the Apple driver is used to support each USB mass storage device with media, that is present. If the mass storage device with media, is not present at system start time, but is attached anytime afterwards or the media is inserted later on, then the standard device driver arbitration mechanism is used which will match the device to a vendor specific driver, if present.  Note that this problem is only with Power Macintosh Systems with USB built-in running Mac OS 9.0 or greater. Beige G3's with a PCI USB card or PowerBook G3's (without USB built-in) using a CardBus USB card, will not have this problem.  During the development of the Apple Mass Storage class driver for Mac OS 9, it was understood that if the USB mass storage device was not the boot device, that there should be a way to allow the Apple driver to be replaced by a vendor specific driver later on, if one was present. Similar support was already in place for non-Apple USB keyboards and mice. Due to time constraints, this support could not be implemented and was deferred as an enhancement for a future release of the Apple Mass Storage class driver. Unfortunately, this enhancement has not been implemented. With the engineering focus on Mac OS X, there are no plans at this time to change the loading behavior of the Apple Mass Storage class driver.  The problem described here primarily affects mass storage class devices with multi-LUN support. Hardware vendors for USB multi-LUN mass storage devices know that the Apple driver does not support multiple LUNS and thus provide vendor specific drivers to support their devices. The Apple Mass Storage class driver only supports LUN 0 on the USB mass storage device. As a result, when the multi-LUN mass storage class device is attached at system start, only the LUN 0 storage device is visible. As such, hardware vendors should ensure that the device works properly with the Apple driver to support LUN 0.  Developers may note that the USB API provides the USBAddDriverForFSSpec call. This call is used to force USB to quit using the current driver and use a different driver for the device. One might think that an INIT could be implemented to force their vendor specific driver to be used instead of the Apple driver. The problem with this option is that the USBAddDriverForFSSpec call results in yanking a drive from the system without ensuring that that system is not accessing a file on the drive. This is not a trivial problem to resolve.  Your options for this situation, are limited. The first option is to inform users as to the limitation of the Apple Mass Storage class driver when the USB device is attached at system start, and to advise them to un-mount USB device volumes, unplug the device and reconnect the device. In this way, the vendor specific driver will be matched to the device.  The alternative and attractive option, is to alter the firmware so that the device has a vendor specific class and subclass. By doing this, the Apple Mass Storage class driver will never match to the device.   ---  [May 23 2002] |

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
