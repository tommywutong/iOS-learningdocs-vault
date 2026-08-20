---
title: Understanding USB Error -6911 - (kUSBNotResponding)
apple_id: DTS10002271
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-11-16'
source_url: https://developer.apple.com/library/archive/qa/usb/usb05.html
archived_at: '2026-07-18T02:38:59.549313Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > USB](https://developer.apple.com/referencelibrary/HardwareDrivers/idxUSB-date.html)

|  |
| --- |
| Technical Q&A USB05Understanding USB Error -6911 - (kUSBNotResponding) |

|  |  |  |
| --- | --- | --- |
| ---   Q: I'm getting an occasional USB error -6911 (`kUSBNotResponding`). According to the documentation, this means that the device is hung. What does this mean in terms of what happened on the bus, and how do I handle this error in my class driver?  A: The `kUSBNotRespondingErr` results because the host controller on the Macintosh tried three times to transfer data and did not receive an `ACK` or `NAK` packet in return. The host internally tries three times before returning this error, which the USB returns to the caller as documented in the USB Specification (revision 1.0, section 4.5.2). From a packet-level perspective, the host controller issued 3 `IN` or `OUT` PIDs (Packet ID), and did not receive a response from the USB function.  Usually this happens because the device is hung. Sometimes, transient errors can cause this problem on a request which takes a long time. (Lots of `NAK`s give lots of opportunity for things to go wrong.)  If this is happening, you can recover from the problem. You first need to clear the stall on the pipe using the `USBClearPipeStallByReference` function. Second, you need to resynchronize the host and the device (which is usually a `Clear_Feature` or `Endpoint_Stall`).  An example of sending the `Clear_Feature` request is shown below. Note that this code assumes the use of the USB v1.1 USB.h header file.   |  | | --- | | ```     pb.pbLength = sizeof(pb);     pb.usbReference = deviceRef;     pb.usbCompletion = yourAsnchHandlerRoutine;     pb.usbStatus = noErr;     pb.pbVersion = kUSBCurrentPBVersion;     pb.usb.cntl.BMRequestType = USBMakeBMRequestType(kUSBOut,          kUSBStandard, kUSBEndpoint);     pb.usb.cntl.BRequest = kUSBRqClearFeature;     pb.usb.cntl.WValue = 0;                   // feature selector - Endpoint stall     pb.usb.cntl.WIndex = endpointNumber;     pb.usbReqCount = 0;     pb.usbBuffer = nil;     pb.usbFlags = 0;     err = USBDeviceRequest(pb);    Example 1. Clear_Feature request example ``` |    When making the `Clear_Feature` request using `USBDeviceRequest`, the `usbWIndex` field must be set to the `endpointNumber`. The `endpointNumber` is typically obtained during device configuration. Alternatively, you could obtain the `endpointNumber` using the `USBFindNextAssociatedDescriptor` call. Example values are `0x01` for an output endpoint, or `0x81` for an input endpoint.  For USB v1.1 and greater, a minor change was implemented to simplify the requirement that the `usbWIndex` field be set the to the `endpointNumber`. Instead of setting the `usbWIndex` field, set the `usbFlags` field with the `kUSBAddressRequest` bit set. The USB Manager v1.1 and greater will check the `usbFlags` field to see if the `kUSBAddressRequest` bit is set, and check if the "usb.cntl.BMRequestType" field is for an endpoint, then fill in the `endpointNumber` into the `usbWIndex` field corresponding to the endpoint reference passed in the `usbReference` field. The following code sample demonstrates this modification for USB v1.1 and later. Note that the code in Example 1 also works with USB v1.1 and later. Use the `gestalt` selector `'usbv'` to determine the version of Mac OS USB present.   |  | | --- | | ```     pb.pbLength = sizeof(pb);     pb.usbReference = endpointRef;     pb.usbCompletion = yourAsnchHandlerRoutine;     pb.usbStatus = noErr;     pb.pbVersion = kUSBCurrentPBVersion;     pb.usb.cntl.BMRequestType =          USBMakeBMRequestType(kUSBOut, kUSBStandard, kUSBEndpoint);     pb.usb.cntl.BRequest = kUSBRqClearFeature;     pb.usb.cntl.WValue = 0;         // feature selector - Endpoint stall     pb.usbReqCount = 0;     pb.usbBuffer = nil;     pb.usbFlags = kUSBAddressRequest;     err = USBDeviceRequest(pb);    Example 2. Alternate Clear_Feature request for USB 1.1 and later ``` |   Note that the `kUSBNotRespondingErr` can also occur if the USB cable is unplugged while the host is communicating with the device. When this error occurs, make the `Clear_Feature` request. If the device has been unplugged, the `USBDeviceRequest` will complete with another -6911 error. [Nov 16 1998] |

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
