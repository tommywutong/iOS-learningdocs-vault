---
title: IODeviceTree and the I/O Registry
apple_id: DTS10001668
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2008-09-18'
source_url: https://developer.apple.com/library/archive/qa/qa1120/_index.html
archived_at: '2026-07-18T02:29:55.971078Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1120

# IODeviceTree and the I/O Registry

## Q:  What is the IODeviceTree plane in the Mac OS X I/O Registry?

A: What is the IODeviceTree plane in the Mac OS X I/O Registry?

The I/O Registry has multiple planes which serve to organize groups of I/O Registry nodes and their properties according to I/O function. At present the default plane is the IOService plane with other planes being IOUSB, IOPower, and IODeviceTree. A plane can be the entire I/O Registry like the IOService plane or a subset of the I/O Registry for certain I/O functions such as USB.

Some of these planes are dynamic. A dynamic plane is one that is updated when an I/O device is attached or removed. For example, when a USB device is attached or removed, the IOService plane is updated by adding or removing the I/O Registry entry representing that device.

On the other hand, the IODeviceTree plane is static. On PowerPC-based Macs, the IODeviceTree plane is a direct copy of the device tree created by Open Firmware during boot. On Intel-based Macs, the IODeviceTree plane is created by the secondary booter from device information it receives from EFI.

Once it is copied into the I/O Registry, the IODeviceTree plane is never updated even if devices come and go. If you are working with I/O Kit and you need to see your device being attached and/or removed, use the IOService plane instead of the IODeviceTree plane.

Note that not all possible planes will be on every Macintosh computer. For instance, the IOFireWire plane would only be on computers with FireWire.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-18 | Modernized and made minor editorial changes. |
| 2002-02-13 | New document that describes the IODeviceTree plane in the Mac OS X I/O Registry. |

