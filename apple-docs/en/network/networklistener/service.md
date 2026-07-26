---
title: service
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networklistener/service
source_url: 'https://developer.apple.com/documentation/network/networklistener/service'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/service.json'
content_hash: 'sha256:8d08e8e8ad8c5f25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# service

<sub>Instance Property</sub>

An optional service to advertise with the listener.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var service: NWListener.Service? { get set }
```

## Discussion

May be modified after the listener becomes ready to update the TXT record or change the advertised service.
