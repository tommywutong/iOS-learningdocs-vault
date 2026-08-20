---
title: Thunderbolt Device Driver Programming Guide
apple_id: TP40011138
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/ThunderboltDevGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:41:11.946298Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Thunderbolt%20Technology%20Overview.md)

# About the Thunderbolt Technology

The Thunderbolt interface is a new I/O technology that supports high-resolution displays and high-performance data devices through a single expansion interface.

The Thunderbolt interface is made up of an Intel controller chip designed to tunnel DisplayPort (DP) version 1.1 and PCI Express (PCIe) information. Its dual-link cables are designed to carry 10 gigabits per second (Gbps) of data bidirectionally on each link, for a total of 40 Gbps per cable. Thunderbolt ports may be hot-plugged, daisy chained with up to six devices in depth, and can be connected host-to-host.

Thunderbolt ports use a Mini DisplayPort (mDP) connector and provide 10 W of power to downstream devices. Thunderbolt cables may be connected by either end (both ends are exactly the same). Thunderbolt technology is a host-centered and host-managed system (like USB), but also allows for host-to-host connections.

A Thunderbolt port or cable provides two 10 Gbps bidirectional links, but these two links cannot be bonded into a single channel. Host software must assign specific paths (for example, DP, PCIe, native) to each link to balance the load. This functionality is included in EFI and in OS X. For example, if there are two Thunderbolt enabled displays attached, it can choose to route the DisplayPort (DP) over each link and use the remaining bandwidth for PCI. If there is only one Thunderbolt display, software can route the DisplayPort traffic over the optimal link. The Thunderbolt interface has no requirement for fixed routing.

It is possible to boot directly from Thunderbolt devices. Apple provides a Unified Target Disk Mode (UTDM), which supports FireWire and Thunderbolt connections. Users may boot from UTDM over FireWire or Thunderbolt connections as well.

Drivers must be built as Universal and be able to support systems with greater than 2 GB of RAM. Refer to the section entitled “Kernel Extensions and Drivers” in the _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_ for more details. In particular, all drivers must use [IODMACommand](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/KernelIOKitFramework/IODMACommand_h/Classes/IODMACommand/index.html) for scatter-gather list support.

Apple provides the following reference material. For more information please refer to these documents.

### Reference Material

- _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_

  This document provides a broad, conceptual description of the I/O Kit and device-driver development on OS X. This document is useful for both the developer who is creating a device driver that is resident in the kernel and the developer who is using an I/O Kit device interface to communicate with the hardware.
- _[64-Bit Transition Guide](../../Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru)_

  This document assists you in the transition to Snow Leopard and Lion where the kernel is using a 64-bit environment on some hardware.

[Next](Thunderbolt%20Technology%20Overview.md)

