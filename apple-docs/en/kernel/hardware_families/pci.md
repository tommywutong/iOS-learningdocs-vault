---
title: PCI
framework: Kernel
symbol_kind: symbol
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel/hardware_families/pci
source_url: 'https://developer.apple.com/documentation/kernel/hardware_families/pci'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel/hardware_families/pci.json'
content_hash: 'sha256:04c35f829582e98a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Kernel](../../kernel.md) · [Hardware Families](../hardware_families.md)

# PCI

<sub>API Collection</sub>

Implement a driver that supports Thunderbolt devices or PCI cards.

## Overview

For many types of PCI drivers, the use of kernel extensions is deprecated. Instead, create a DriverKit extension using [PCIDriverKit](../../pcidriverkit.md).

## Topics

### Devices

- [Implementing a PCIe Kext for a Thunderbolt Device](pci/implementing_a_pcie_kext_for_a_thunderbolt_device.md) — Create an IOKit driver to support Thunderbolt devices that implement features not supported in PCIDriverKit, such as wireless networking or audio. 
- [IOPCIDevice](../iopcidevice.md) — An IOService class representing a PCI device. _(deprecated)_
- [IOAGPDevice](../ioagpdevice.md) — An IOService class representing an AGP primary device. _(deprecated)_

### Event Source

- [IOPCIEventSource](../iopcieventsource.md) _(deprecated)_

## See Also

### Hardware Interconnects

- [ATA](ata.md) — Implement a driver that supports Advanced Technology Attachment (ATA) devices.
- [Bluetooth](bluetooth.md) — Implement a driver that supports Bluetooth devices.
- [FireWire](firewire.md) — Implement a driver that supports FireWire devices. 
- [USB](usb.md) — Implement a driver that supports Universal Serial Bus (USB) devices.
