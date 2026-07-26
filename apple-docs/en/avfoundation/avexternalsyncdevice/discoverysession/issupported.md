---
title: isSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice/discoverysession/issupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/discoverysession/issupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice/discoverysession/issupported.json'
content_hash: 'sha256:0ab69f6c90f62b1f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVExternalSyncDevice](../../avexternalsyncdevice.md) · [DiscoverySession](../discoverysession.md)

# isSupported

<sub>Type Property</sub>

Whether external sync devices are supported by this device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var isSupported: Bool { get }
```

## Discussion

A value of `true` indicates that external sync devices are supported while `false` indicates they are not.

## See Also

### Accessing the shared instance

- [sharedSession](shared.md) — The singleton instance of the external sync source device discovery session.
