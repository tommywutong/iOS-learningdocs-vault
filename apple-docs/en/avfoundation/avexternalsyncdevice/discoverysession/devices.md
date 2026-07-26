---
title: devices
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice/discoverysession/devices
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/discoverysession/devices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice/discoverysession/devices.json'
content_hash: 'sha256:dc30278856fe0246'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVExternalSyncDevice](../../avexternalsyncdevice.md) · [DiscoverySession](../discoverysession.md)

# devices

<sub>Instance Property</sub>

An array of external sync devices connected to this host.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var devices: [AVExternalSyncDevice] { get }
```

## Discussion

The list is updated when external sync devices are connected to the host and they remain in the list until they become unavailable. This property is key-value observable.
