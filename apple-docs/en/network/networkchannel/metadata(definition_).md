---
title: 'metadata(definition:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkchannel/metadata(definition:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/metadata(definition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/metadata%28definition%3A%29.json'
content_hash: 'sha256:8af0afe1f1197476'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# metadata(definition:)

<sub>Instance Method</sub>

Access connection-wide protocol metadata on the connection. This allows access to state for protocols like TCP and TLS that have long-term state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?
```
