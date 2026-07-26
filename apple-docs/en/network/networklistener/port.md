---
title: port
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networklistener/port
source_url: 'https://developer.apple.com/documentation/network/networklistener/port'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/port.json'
content_hash: 'sha256:a6e68338c8bd81d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# port

<sub>Instance Property</sub>

The port that the listener is listening on.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var port: NWEndpoint.Port? { get }
```

## Discussion

Present once the listener becomes ready.
