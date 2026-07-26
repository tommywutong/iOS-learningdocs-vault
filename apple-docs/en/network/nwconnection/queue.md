---
title: queue
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/queue
source_url: 'https://developer.apple.com/documentation/network/nwconnection/queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/queue.json'
content_hash: 'sha256:5db5a00e8eb7d72e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# queue

<sub>Instance Property</sub>

The queue on which connection events are delivered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var queue: DispatchQueue? { get }
```

## See Also

### Inspecting Connections

- [metadata(definition:)](<metadata(definition_).md>) — Retrieves the connection-wide metadata for a specific protocol.
- [NWProtocolMetadata](../nwprotocolmetadata.md) — The abstract superclass for specifying metadata about a network protocol.
- [endpoint](endpoint.md) — The remote endpoint with which the connection was initialized.
- [parameters](parameters.md) — The parameters with which the connection was initialized.
