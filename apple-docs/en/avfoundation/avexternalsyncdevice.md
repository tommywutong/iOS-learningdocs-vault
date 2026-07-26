---
title: AVExternalSyncDevice
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice.json'
content_hash: 'sha256:0a4f7415ef2268ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVExternalSyncDevice

<sub>Class</sub>

An external sync device connected to a host device that can be used to drive the timing of an internal component, such as a camera sensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVExternalSyncDevice
```

## Overview

Each instance of [AVExternalSyncDevice](avexternalsyncdevice.md) corresponds to a physical external device that can drive an internal component, like a camera readout. You cannot create instances of [AVExternalSyncDevice](avexternalsyncdevice.md). Instead, you obtain an array of all currently available external sync devices using [DiscoverySession](avexternalsyncdevice/discoverysession.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Finding and monitoring devices

- [DiscoverySession](avexternalsyncdevice/discoverysession.md) — A means of discovering and monitoring connection / disconnection of external sync devices to the host.

### Inspecting a device

- [clock](avexternalsyncdevice/clock.md) — A clock representing the source of time from the external sync device.
- [productID](avexternalsyncdevice/productid.md) — The USB product identifier associated with the external sync device.
- [signalCompensationDelay](avexternalsyncdevice/signalcompensationdelay.md) — Delay to wait before starting the frame capture.
- [status](avexternalsyncdevice/status.md) — The status of the externally connected device.
- [uuid](avexternalsyncdevice/uuid.md) — A unique identifier for an external sync device.
- [vendorID](avexternalsyncdevice/vendorid.md) — The USB vendor identifier associated with the external sync device.

### Instance Properties

- [signalCompensationDelaySupported](avexternalsyncdevice/issignalcompensationdelaysupported.md) — Whether adjusting the signal compensation delay property is currently supported. _(beta)_

## See Also

### External synchronization

- [AVExternalSyncDeviceDelegate](avexternalsyncdevicedelegate.md) — Defines an interface for delegates of [AVCaptureDeviceInput](avcapturedeviceinput.md) to respond to events that occur when connecting, calibrating, and disconnecting external sync devices.
- [AVExternalSyncDeviceStatus](avexternalsyncdevicestatus.md) — Connection state of an external sync device
- [DiscoverySession](avexternalsyncdevice/discoverysession.md) — A means of discovering and monitoring connection / disconnection of external sync devices to the host.
