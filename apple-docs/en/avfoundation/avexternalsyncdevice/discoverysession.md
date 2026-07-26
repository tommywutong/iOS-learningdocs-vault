---
title: AVExternalSyncDevice.DiscoverySession
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice/discoverysession
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/discoverysession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice/discoverysession.json'
content_hash: 'sha256:4ce08c56e3dba594'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalSyncDevice](../avexternalsyncdevice.md)

# AVExternalSyncDevice.DiscoverySession

<sub>Class</sub>

A means of discovering and monitoring connection / disconnection of external sync devices to the host.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class DiscoverySession
```

## Overview

[DiscoverySession](discoverysession.md) is a singleton that lists the external sync devices connected to the host. The client is expected to key-value observe the [devices](discoverysession/devices.md) property for changes to the external sync devices list.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the shared instance

- [sharedSession](discoverysession/shared.md) — The singleton instance of the external sync source device discovery session.
- [supported](discoverysession/issupported.md) — Whether external sync devices are supported by this device.

### Finding devices

- [devices](discoverysession/devices.md) — An array of external sync devices connected to this host.

## See Also

### External synchronization

- [AVExternalSyncDevice](../avexternalsyncdevice.md) — An external sync device connected to a host device that can be used to drive the timing of an internal component, such as a camera sensor.
- [AVExternalSyncDeviceDelegate](../avexternalsyncdevicedelegate.md) — Defines an interface for delegates of [AVCaptureDeviceInput](../avcapturedeviceinput.md) to respond to events that occur when connecting, calibrating, and disconnecting external sync devices.
- [AVExternalSyncDeviceStatus](../avexternalsyncdevicestatus.md) — Connection state of an external sync device
