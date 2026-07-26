---
title: 'metadata(definition:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/metadata(definition:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/metadata(definition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/metadata%28definition%3A%29.json'
content_hash: 'sha256:25cd55a3740e5c20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# metadata(definition:)

<sub>Instance Method</sub>

Retrieves the connection-wide metadata for a specific protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func metadata(definition: NWProtocolDefinition) -> NWProtocolMetadata?
```

## See Also

### Inspecting Connections

- [NWProtocolMetadata](../nwprotocolmetadata.md) — The abstract superclass for specifying metadata about a network protocol.
- [endpoint](endpoint.md) — The remote endpoint with which the connection was initialized.
- [parameters](parameters.md) — The parameters with which the connection was initialized.
- [queue](queue.md) — The queue on which connection events are delivered.
