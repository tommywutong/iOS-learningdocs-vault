---
title: Bonjour over Bluetooth on iOS 5 and Later
apple_id: DTS40011315
resource_type: QA
platform: iOS
topic: null
technology: Foundation
published: '2013-11-14'
source_url: https://developer.apple.com/library/archive/qa/qa1753/_index.html
archived_at: '2026-07-18T02:34:35.670278Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1753

# Bonjour over Bluetooth on iOS 5 and Later

## Q:  After adopting the iOS 5 SDK my app no longer sees Bonjour services over Bluetooth. What's going on here?

A: When Bonjour over Bluetooth support was added in iOS 3.0, the default policy was that it should be enabled for all apps. That is, a Bonjour app would operate over Bluetooth unless it explicitly opted out of that behaviour.

This policy changed in iOS 5.0. The new policy is that a Bonjour app must explicitly opt in to Bluetooth support. This change was made to reduce interference with Wi-Fi. To ensure binary compatibility, this change is only enabled for apps that link with the iOS 5.0 SDK (or later). This explains why your previous app binary continues to see Bonjour services over Bluetooth, but your latest binary, built with a modern SDK, does not.

iOS 7 introduced a new NSNetService property, `includesPeerToPeer`, that you can set to explicitly enable registration and discovery over Bluetooth. If your app runs on iOS 7 and later, you can simply set that property and you're done.

If your app runs on iOS 5 or 6 and you want to reenable Bonjour over Bluetooth, you must switch to using the low-level DNS-SD API (`<dns_sd.h>`). For an example of how to integrate the DNS-SD API into a Cocoa application, take a look at [Sample Code 'DNSSDObjects'](https://developer.apple.com/samplecode/DNSSDObjects/index.html).

Once you've adopted the DNS-SD API, you can set the `interfaceIndex` parameter to explicitly control the interfaces over which it operates. The standard value for this parameter, `kDNSServiceInterfaceIndexAny`, yields the default policy as explained above. You can modify this by passing in the `kDNSServiceFlagsIncludeP2P` flag, as shown in Table 1. Alternatively, you can browse for services over Bluetooth, and only over Bluetooth, by passing `kDNSServiceInterfaceIndexP2P` to the `interfaceIndex` parameter.

__Table 1__  DNS-SD kDNSServiceInterfaceIndexAny behavior

| OS Version | SDK Version | kDNSServiceFlagsIncludeP2P | Behavior |
| < 5.0 | any | any value | all interfaces, including Bluetooth |
| ≥ 5.0 | ≥ 5.0 | clear | all interfaces, excluding Bluetooth |
| ≥ 5.0 | any | set | all interfaces, including Bluetooth |

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-11-14 | Updated to reflect changes in iOS 7 (r. 10264938). |
| 2012-01-05 | Updated to reference the new DNSSDObjects sample code. |
| 2011-10-19 | New document that describes how Bonjour over Bluetooth has changed in iOS 5 and later. |

