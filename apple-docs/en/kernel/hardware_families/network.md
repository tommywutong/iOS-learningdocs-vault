---
title: Network
framework: Kernel
symbol_kind: symbol
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel/hardware_families/network
source_url: 'https://developer.apple.com/documentation/kernel/hardware_families/network'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel/hardware_families/network.json'
content_hash: 'sha256:cfc1b7821b09f69d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Kernel](../../kernel.md) · [Hardware Families](../hardware_families.md)

# Network

<sub>API Collection</sub>

Implement a driver that interacts with network interfaces such as Ethernet adaptors. 

## Overview

For most types of network interfaces, the use of kernel extensions is deprecated. Instead, create a DriverKit extension using [NetworkingDriverKit](../../networkingdriverkit.md).

## Topics

### Interfaces

- [IONetworkInterface](../ionetworkinterface.md) — Abstract class that manages the connection between an IONetworkController and the data link interface layer.
- [IONetworkController](../ionetworkcontroller.md) — Implements the framework for a generic network controller.

### Network Data

- [IONetworkData](../ionetworkdata.md) — An object that manages a fixed-size named buffer.
- [IONetworkMedium](../ionetworkmedium.md) — An object that encapsulates information about a network medium (i.e. 10Base-T, or 100Base-T Full Duplex).
- [IOPacketQueue](../iopacketqueue.md) — Implements a bounded FIFO queue of mbuf packets.
- [IOPacketBufferConstraints](../iopacketbufferconstraints.md)

## See Also

### Interfaces

- [Audio](audio.md) — Implement a driver that interacts with audio hardware. 
- [Graphics and Displays](graphics_and_displays.md) — Implement a driver that interacts with graphics and video hardware. 
- [HID](hid.md) — Implement a driver that interacts with human interface devices, such as mice and keyboards.
- [SCSI](scsi.md) — Implement a driver that supports Small Computer System Interface (SCSI) protocols.
- [Mass Storage](mass_storage.md) — Implement a driver that communicates with CD, DVD, or other mass storage devices.
