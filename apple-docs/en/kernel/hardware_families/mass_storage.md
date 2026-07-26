---
title: Mass Storage
framework: Kernel
symbol_kind: symbol
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel/hardware_families/mass_storage
source_url: 'https://developer.apple.com/documentation/kernel/hardware_families/mass_storage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel/hardware_families/mass_storage.json'
content_hash: 'sha256:72e3b993ffb5795e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Kernel](../../kernel.md) · [Hardware Families](../hardware_families.md)

# Mass Storage

<sub>API Collection</sub>

Implement a driver that communicates with CD, DVD, or other mass storage devices.

## Topics

### Drivers

- [IOBDBlockStorageDriver](../iobdblockstoragedriver.md)
- [IODVDBlockStorageDriver](../iodvdblockstoragedriver.md)
- [IOCDBlockStorageDriver](../iocdblockstoragedriver.md)
- [IOBlockStorageDriver](../ioblockstoragedriver.md) — The common base class for generic block storage drivers.
- [IOStorage](../iostorage.md) — The common base class for mass storage objects.

### Interfaces

- [IODVDServices](../iodvdservices.md)
- [IOBDBlockStorageDevice](../iobdblockstoragedevice.md) — The IOBDBlockStorageDevice class is a generic BD block storage device abstraction.
- [IODVDBlockStorageDevice](../iodvdblockstoragedevice.md) — The IODVDBlockStorageDevice class is a generic DVD block storage device abstraction.
- [IOCompactDiscServices](../iocompactdiscservices.md)
- [IOBDMediaBSDClient](../iobdmediabsdclient.md)
- [IOMediaBSDClient](../iomediabsdclient.md)

### Devices

- [IOBlockStorageServices](../ioblockstorageservices.md)
- [IOCDBlockStorageDevice](../iocdblockstoragedevice.md) — The IOCDBlockStorageDevice class is a generic CD block storage device abstraction.
- [IOBDServices](../iobdservices.md)
- [IOBlockStorageDevice](../ioblockstoragedevice.md) — A generic block storage device abstraction.

### Data Storage

- [IOCDMedia](../iocdmedia.md) — The IOCDMedia class is a random-access disk device abstraction for CDs.
- [IOBDMedia](../iobdmedia.md) — The IOBDMedia class is a random-access disk device abstraction for BDs.
- [IOMedia](../iomedia.md) — A random-access disk device abstraction.
- [IOCDMediaBSDClient](../iocdmediabsdclient.md)
- [IOCDPartitionScheme](../iocdpartitionscheme.md)
- [IODVDMedia](../iodvdmedia.md) — The IODVDMedia class is a random-access disk device abstraction for DVDs.
- [IODVDMediaBSDClient](../iodvdmediabsdclient.md)

### Schemes

- [IOAppleLabelScheme](../ioapplelabelscheme.md)
- [IOApplePartitionScheme](../ioapplepartitionscheme.md)
- [IOFDiskPartitionScheme](../iofdiskpartitionscheme.md)
- [IOGUIDPartitionScheme](../ioguidpartitionscheme.md)
- [IOPartitionScheme](../iopartitionscheme.md) — The common base class for all partition scheme objects.
- [IOFilterScheme](../iofilterscheme.md) — The common base class for all filter scheme objects.

### Data

- [CD Data Structures](mass_storage/cd_data_structures.md)
- [DVD Data Structures](mass_storage/dvd_data_structures.md)

## See Also

### Interfaces

- [Audio](audio.md) — Implement a driver that interacts with audio hardware. 
- [Graphics and Displays](graphics_and_displays.md) — Implement a driver that interacts with graphics and video hardware. 
- [HID](hid.md) — Implement a driver that interacts with human interface devices, such as mice and keyboards.
- [Network](network.md) — Implement a driver that interacts with network interfaces such as Ethernet adaptors. 
- [SCSI](scsi.md) — Implement a driver that supports Small Computer System Interface (SCSI) protocols.
