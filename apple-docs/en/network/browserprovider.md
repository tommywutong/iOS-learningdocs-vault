---
title: BrowserProvider
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/browserprovider
source_url: 'https://developer.apple.com/documentation/network/browserprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/browserprovider.json'
content_hash: 'sha256:79a88522dc24a4a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# BrowserProvider

<sub>Protocol</sub>

BrowserProviders can be used when creating NetworkBrowsers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol BrowserProvider : Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [Bonjour](bonjour.md)

## Topics

### Associated Types

- [Endpoint](browserprovider/endpoint.md)

### Type Methods

- [bonjour(_:domain:includeTxtRecord:)](<browserprovider/bonjour(__domain_includetxtrecord_).md>) — Create a Bonjour browser provider used to browse for Bonjour services.
- [wifiAware(_:active:)](<browserprovider/wifiaware(__active_).md>) — Setup a `NetworkBrowser` to subscribe to Wi-Fi Aware services on selected, paired devices.
