---
title: Composite Class Driver loads via both Driver/InterfaceInitialize entry point
apple_id: DTS10002270
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-09-28'
source_url: https://developer.apple.com/library/archive/qa/usb/usb04.html
archived_at: '2026-07-18T02:38:59.509863Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > USB](https://developer.apple.com/referencelibrary/HardwareDrivers/idxUSB-date.html)

|  |
| --- |
| Technical Q&A USB04Composite Class Driver loads via both Driver/InterfaceInitialize entry point |

|  |
| --- |
| ---   Q: I've written a USB class driver to support my composite class USB device. I have found that my class driver is called through both the `DriverInitialize` and `InterfaceInitialize` entry points. What is happening here?  A: You've encountered a unique situation with how Mac OS USB loads USB composite class drivers, depending on whether the device is detected at system startup or is "hot-plugged."  Developers of USB Class Drivers for USB devices which return a composite class description are warned that their class driver may be called via the `DriverInitialize` OR the `InterfaceInitialize` entry point. If you set the `ProductID` and `VendorID` fields of the `DriverDescription` record to match the values that the device returns in the device configuration string, you would expect the driver to be sensed with a higher match value as compared to the generic composite driver supplied by Apple. It turns out that the driver loading mechanism at start up is different from the case when the device is hot-plugged.  Apple provides a Composite class driver that is used to support USB Composite class devices. At startup, the USB driver detection mechanism matches devices directly from the drivers in ROM. This includes the Composite driver, but not a vendor-specific class drivers. When a composite class device is detected, the Apple generic composite class driver is used, even though a better matching driver exists in the extension folder. If this happens, then the Composite driver loads, which is followed by the vendor class driver being called through the `InterfaceInitialize` procedure.  Contrast the startup case above with the hot-plug case. Given the same drivers, at hot-plug, USB finds that the developer's class driver matches better (since a match by `VendorID` and `ProductID` is higher) than the composite class driver. In this case, the developers class driver is called through the `driverInitialize` procedure.  Note that this problem only exists with composite class devices and developer class drivers, which specify both the `VendorID` AND the `ProductID`. If either of these values are missing from the `DriverDescription` record, then USB will not match the developer's class driver as a device (not interface) driver.  This is a known issue with USB prior to v1.0.1. For a future version of USB, the driver loading for composite class drivers will be the same whether the device is present at startup or is hot-plugged. In the meantime, a class driver for a composite device should expect to be called through either the `DeviceInitialize` or `InterfaceInitialize` entry point. The difference between the two entry points is that for the `DriverInitialize` call, the driver must issue the `kUSBRqSetConfig` request using the `USBDeviceRequest` call. A sample of this call is presented in the Composite Class Driver example code that is present on the Mac OS USB DDK.  Note that in order for a driver to be called as an `interfaceDriver`, ensure that the `kUSBDoNotMatchInterface` is not set in the `USBDriverLoadingOptions` field.  To learn more about the how USB class drivers are matched, refer to the USB TechNote which is available from the [Mac OS USB Developer Web Page](https://developer.apple.com/dev/usb/devinfo.htm). [Sep 28 1998] |

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
