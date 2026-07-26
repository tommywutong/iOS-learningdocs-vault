---
title: AVExternalSyncDeviceDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevicedelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevicedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevicedelegate.json'
content_hash: 'sha256:0f471d6688b3e71f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVExternalSyncDeviceDelegate

<sub>Protocol</sub>

Defines an interface for delegates of [AVCaptureDeviceInput](avcapturedeviceinput.md) to respond to events that occur when connecting, calibrating, and disconnecting external sync devices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVExternalSyncDeviceDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to device events

- [- externalSyncDevice:failedWithError:](<avexternalsyncdevicedelegate/externalsyncdevice(__failedwitherror_).md>)
- [- externalSyncDeviceStatusDidChange:](<avexternalsyncdevicedelegate/externalsyncdevicestatusdidchange(__).md>) — Informs your delegate when the external sync device status has changed.

## See Also

### External synchronization

- [AVExternalSyncDevice](avexternalsyncdevice.md) — An external sync device connected to a host device that can be used to drive the timing of an internal component, such as a camera sensor.
- [AVExternalSyncDeviceStatus](avexternalsyncdevicestatus.md) — Connection state of an external sync device
- [DiscoverySession](avexternalsyncdevice/discoverysession.md) — A means of discovering and monitoring connection / disconnection of external sync devices to the host.
