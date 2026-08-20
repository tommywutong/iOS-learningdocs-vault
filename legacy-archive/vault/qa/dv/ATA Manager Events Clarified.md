---
title: ATA Manager Events Clarified
apple_id: DTS10001165
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-12-07'
source_url: https://developer.apple.com/library/archive/qa/dv/dv24.html
archived_at: '2026-07-18T02:29:26.544739Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > ATA](https://developer.apple.com/referencelibrary/HardwareDrivers/idxATA-date.html)

|  |
| --- |
| Technical Q&A DV24ATA Manager Events Clarified |

|  |
| --- |
| ---   Q: The `kATAOfflineEvent` and `kATARemovedEvent` documentation is incomplete in the Reference Library CD Developer's Notes. The documentation is clarified here.  A: `kATAOnlineEvent` (code 1)  This event notifies clients when an ATA or ATAPI device becomes available for use. The event occurs either when a new device is connected to the bus or when a previously unavailable device becomes available again (as in system wakeup when power is restored to the device).  If the device has a registered driver, only that driver will be notified of the event; otherwise, each registered default driver will be notified until a driver responds favorably (a `noErr` response to the event). Note that for newly connected devices a driver loaded from the media is given priority.  Drivers should keep track of whether the device coming online is a newly connected device or one which is currently offline (connected but not unavailable). A device should be considered connected until a kATARemovedEvent for the device occurs.  `kATAOfflineEvent` (code 2)  This event notifies the registered driver of an ATA or ATAPI device that the device is now unavailable for use (offline). The device, however, is still connected to the bus and the offline state is assumed to be temporary. This event will occur at system sleep when power is removed.  Currently, this event is generated only when the ATA Manager receives a `PMSuspend` event (essentially the same as a Power Manager sleep demand event) from the PC Card Manager. Drivers receiving `kATAOfflineEvent` events most likely will want to maintain control of the device, but deny access to the device from its clients. In addition, the driver should note the device may need to be reconfigured when the device becomes online again (a `kATAOnlineEvent` will be generated when this happens).  `kATARemovedEvent` (code 3)  This event notifies the registered driver of an ATA or ATAPI device that the device has been removed. The removal may be either controlled (e.g., a software eject command to the ATA Manager) or uncontrolled (e.g., a forced removal by the user). Note the device may have been in either an online or offline state prior to the removal. If the device state was online prior to the removal a `kATAOfflineEvent` is not generated since the removal implies an offline condition had to occur.  `kATAResetEvent` (code 4)  This event notifies the registered driver of an ATA or ATAPI device that the device has been reset. The device may need to be reconfigured by the driver before it can be used again.  This event was created for use with multiple devices per bus (ATA Master/Slave mode), since reset applies to all devices on the bus and not a specific device. At this time Apple does not implement multiple devices per bus with ATA and this event has not been implemented. It is advised, however, that drivers support this event now to prevent problems later on when the event is implemented.  `kATAOfflineRequest` (code 5)  This event is obsolete. It was defined for the early stages of the PC Card Manager which would echo the Power Manager Sleep events to its clients. The ATA Manager would in turn echo the request to its clients. This event was akin to the `sleepRequest` event. The current PC Card Manager now allows only for an event akin to a `sleepDemand`, which does not permit rejection by the client.  `kATAEjectRequest` (code 6)  This event notifies the registered driver of an ATA or ATAPI device that a request has been made to eject the device. If the response to the request is 0 the device will be ejected and a subsequent `kATARemovedEvent` will be generated when the eject is successful.  The event is defined as a protection mechanism to alert drivers of a pending ejection. Drivers will most likely want to reject the request unless it initiated the request since ejection will remove the device from the bus.  Note also that the `kATAResetEvent`, `kATAOfflineRequest`, and `kATAEjectRequest` events are not implemented in the ATA Manager at this time. |

#### [Dec 07 1995]

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
