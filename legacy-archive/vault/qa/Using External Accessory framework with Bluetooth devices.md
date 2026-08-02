---
title: Using External Accessory framework with Bluetooth devices.
apple_id: DTS40010232
resource_type: QA
platform: iOS
topic: Data Management
technology: null
published: '2012-10-23'
source_url: https://developer.apple.com/library/archive/qa/qa1657/_index.html
archived_at: '2026-07-18T02:33:17.526560Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1657

# Using External Accessory framework with Bluetooth devices.

## Q:  I understand that the External Accessory framework in iOS 3.0 and later will allow my application to communicate with Bluetooth devices. So why doesn't my application see the Bluetooth accessory sitting next to my iPhone?

A: The External Accessory framework is designed to allow iOS applications to communicate only with hardware accessories that are developed under Apple's MFi licensee program. MFi compliant accessories can be implemented as wired devices, meaning they plug in to the Apple device's 30-pin or Lightning connector, or as wireless devices, whereby they use Bluetooth as the communication channel. Either way, an application that uses the External Accessory framework will not be notified of an accessory's presence unless the accessory identifies itself as being MFi compliant, i.e., it was specifically designed to interface with an iOS application.

More information about developing MFi accessories can be found [here](https://developer.apple.com/programs/mfi/).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-10-23 | Added references to Lightning connector and Bluetooth low energy. |
| 2010-10-14 | Updated terminology. |
| 2010-08-06 | New document that attempts to clarify how Bluetooth devices can be used with External Accessory framework. |

