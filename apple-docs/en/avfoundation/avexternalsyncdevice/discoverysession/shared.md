---
title: shared
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice/discoverysession/shared
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/discoverysession/shared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice/discoverysession/shared.json'
content_hash: 'sha256:ad81520ae34937db'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVExternalSyncDevice](../../avexternalsyncdevice.md) · [DiscoverySession](../discoverysession.md)

# shared

<sub>Type Property</sub>

The singleton instance of the external sync source device discovery session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var shared: AVExternalSyncDevice.DiscoverySession? { get }
```

## Discussion

Access the one and only external sync device discovery session on this host device using this method. `sharedSession` returns `nil` if the host device doesn’t support external sync devices.

## See Also

### Accessing the shared instance

- [supported](issupported.md) — Whether external sync devices are supported by this device.
