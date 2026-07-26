---
title: SCSIPeripheralsDriverKit
framework: SCSIPeripheralsDriverKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [DriverKit 22.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/scsiperipheralsdriverkit
source_url: 'https://developer.apple.com/documentation/scsiperipheralsdriverkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/scsiperipheralsdriverkit.json'
content_hash: 'sha256:3db49aaa8d00897c'
translated: false
---

> Navigation: [Technologies](technologies.md)

# SCSIPeripheralsDriverKit

<sub>Framework</sub>

Develop drivers for peripherals that use SCSI Block Command and Multimedia Command protocols.

## Overview

The SCSIPeripheralsDriverKit framework supports the development of drivers for external devices that communicate using SCSI protocols. This framework operates at the logical unit level. For block-level driver development, use [BlockStorageDeviceDriverKit](blockstoragedevicedriverkit.md). For protocol-level driver development, use [SCSIControllerDriverKit](scsicontrollerdriverkit.md).

Develop your driver by subclassing [IOUserSCSIPeripheralDeviceType00](scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00.md) or [IOUserSCSIPeripheralDeviceType05](scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05.md), depending on whether your device works with SCSI Block Commands (SBC) or SCSI Multimedia Commands (SMC), respectively. In your subclass, override all methods the framework declares as pure virtual. Then package your driver in an app that uses the [System Extensions](systemextensions.md) framework to install and upgrade the driver on the user’s Mac.

> [!note] Note
> SCSIPeripheralsDriverKit is available on macOS.

## Topics

### Driver interfaces

- [IOUserSCSIPeripheralDeviceType00](scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00.md) — A DriverKit provider object that works with type 00 devices, those that use SCSI Block Commands (SBC).
- [IOUserSCSIPeripheralDeviceType05](scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05.md) — A DriverKit provider object that works with type 05 devices, those that use SCSI Multimedia Commands (SMC).

### Device commands

- [SCSI commands](scsiperipheralsdriverkit/scsi-commands.md) — Call the framework’s free functions to populate Command Descriptor Blocks (CDBs) to send to your peripheral.

### Classes

- [IOUserSCSIPeripheralDeviceType07](scsiperipheralsdriverkit/iouserscsiperipheraldevicetype07.md)

### Reference

- [SCSIPeripheralsDriverKit Enumerations](scsiperipheralsdriverkit/scsiperipheralsdriverkit-enumerations.md)
- [SCSIPeripheralsDriverKit Data Types](scsiperipheralsdriverkit/scsiperipheralsdriverkit-data-types.md)
