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
translated: true
---

> 导航：[Technologies](technologies.md)

# SCSIPeripheralsDriverKit

<sub>框架</sub>

为使用 SCSI Block Command 和 Multimedia Command 协议的外围设备开发驱动程序。

## 概述

SCSIPeripheralsDriverKit 框架支持为使用 SCSI 协议通信的外部设备开发驱动程序。此框架在逻辑单元级别运行。如需进行块级驱动程序开发，请使用 [BlockStorageDeviceDriverKit](blockstoragedevicedriverkit.md)。如需进行协议级驱动程序开发，请使用 [SCSIControllerDriverKit](scsicontrollerdriverkit.md)。

通过子类化 [IOUserSCSIPeripheralDeviceType00](scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00.md) 或 [IOUserSCSIPeripheralDeviceType05](scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05.md) 来开发你的驱动程序，具体取决于你的设备使用的是 SCSI Block Commands (SBC) 还是 SCSI Multimedia Commands (SMC)。在你的子类中，重写框架声明为纯虚方法的所有方法。然后将你的驱动程序打包进一个使用 [System Extensions](systemextensions.md) 框架的 App 中，以便在用户的 Mac 上安装和升级该驱动程序。

> [!note] 注意
> SCSIPeripheralsDriverKit 可在 macOS 上使用。

## 主题

### 驱动程序接口

- [IOUserSCSIPeripheralDeviceType00](scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00.md) — 一个与 00 类型设备（使用 SCSI Block Commands (SBC) 的设备）配合使用的 DriverKit 提供程序对象。
- [IOUserSCSIPeripheralDeviceType05](scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05.md) — 一个与 05 类型设备（使用 SCSI Multimedia Commands (SMC) 的设备）配合使用的 DriverKit 提供程序对象。

### 设备命令

- [SCSI commands](scsiperipheralsdriverkit/scsi-commands.md) — 调用框架的自由函数来填充要发送给外围设备的命令描述符块（Command Descriptor Blocks，CDB）。

### 类

- [IOUserSCSIPeripheralDeviceType07](scsiperipheralsdriverkit/iouserscsiperipheraldevicetype07.md)

### 参考

- [SCSIPeripheralsDriverKit Enumerations](scsiperipheralsdriverkit/scsiperipheralsdriverkit-enumerations.md)
- [SCSIPeripheralsDriverKit Data Types](scsiperipheralsdriverkit/scsiperipheralsdriverkit-data-types.md)
