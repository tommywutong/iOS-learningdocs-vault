---
title: AVExternalSyncDeviceStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevicestatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevicestatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevicestatus.json'
content_hash: 'sha256:1b75b167a3a1c69d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVExternalSyncDeviceStatus

<sub>Enumeration</sub>

Connection state of an external sync device

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum AVExternalSyncDeviceStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Status values

- [AVExternalSyncDeviceStatusActiveSync](avexternalsyncdevicestatus/activesync.md) — Indicates that the [AVExternalSyncDevice](avexternalsyncdevice.md) object is running and that the clock property on [AVExternalSyncDevice](avexternalsyncdevice.md) is calibrated to the external sync signal.
- [AVExternalSyncDeviceStatusCalibrating](avexternalsyncdevicestatus/calibrating.md) — Indicates that the external sync signal is connected and that the AVExternalSyncDevice object is calibrating to follow.
- [AVExternalSyncDeviceStatusFreeRunSync](avexternalsyncdevicestatus/freerunsync.md) — Indicates that the AVExternalSyncDevice was calibrated to follow the external sync, but the sync signal has been lost. The camera will continue to match the last signal it received, but sync is not guaranteed.
- [AVExternalSyncDeviceStatusReady](avexternalsyncdevicestatus/ready.md) — Indicates that a device supporting external sync is connected, but calibration has not started.
- [AVExternalSyncDeviceStatusUnavailable](avexternalsyncdevicestatus/unavailable.md) — Indicates that external sync signal is not connected, or has transitioned to a state that is not recoverable.

### Initializers

- [init(rawValue:)](<avexternalsyncdevicestatus/init(rawvalue_).md>)

## See Also

### External synchronization

- [AVExternalSyncDevice](avexternalsyncdevice.md) — An external sync device connected to a host device that can be used to drive the timing of an internal component, such as a camera sensor.
- [AVExternalSyncDeviceDelegate](avexternalsyncdevicedelegate.md) — Defines an interface for delegates of [AVCaptureDeviceInput](avcapturedeviceinput.md) to respond to events that occur when connecting, calibrating, and disconnecting external sync devices.
- [DiscoverySession](avexternalsyncdevice/discoverysession.md) — A means of discovering and monitoring connection / disconnection of external sync devices to the host.
