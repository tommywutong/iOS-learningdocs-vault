---
title: Issues with boot time KEXT loading
apple_id: DTS10001636
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2011-07-18'
source_url: https://developer.apple.com/library/archive/qa/qa1087/_index.html
archived_at: '2026-07-18T02:29:55.720528Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1087

# Issues with boot time KEXT loading

## Q:  My KEXT loads when I hot-plug my device, so why won't it load at boot time?

A: A boot time KEXT other than your own may be matching to your device, namely a KEXT with its `OSBundleRequired` property set. Once a driver has been matched to a device, it will stay loaded until the device is removed or the system is rebooted.

A common example of this is a composite USB device with a vendor-specific driver. The Apple composite class driver will match at boot time. (The composite class driver has to be a boot time KEXT because it is needed to boot from Mass Storage class devices.) As a result, the vendor-specific driver will not load. But, if the device is hot-plugged, all eligible drivers will then compete for the device and the vendor-specific driver will be a better match than the composite class driver.

The solution is to set the `OSBundleRequired` property in your `Info.plist` to the same value as that in the competing boot time driver.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-18 | Reformatted and removed content that was obsoleted in Mac OS X v10.2 Jaguar. |
| 2004-01-15 | New document that explains how to solve problems with loading KEXTs at boot time. |

