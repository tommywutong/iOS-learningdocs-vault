---
title: identifier
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/contentcontext/identifier
source_url: 'https://developer.apple.com/documentation/network/nwconnection/contentcontext/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/contentcontext/identifier.json'
content_hash: 'sha256:b7b425c245e9331c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [ContentContext](../contentcontext.md)

# identifier

<sub>Instance Property</sub>

The identifier of the message, used for debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final let identifier: String
```

## See Also

### Creating Custom Send Contexts

- [init(identifier:expiration:priority:isFinal:antecedent:metadata:)](<init(identifier_expiration_priority_isfinal_antecedent_metadata_).md>) — Initializes a custom message context.
- [protocolMetadata](protocolmetadata.md) — An array of protocol metadata used to configure per-message or per-packet properties.
- [NWProtocolMetadata](../../nwprotocolmetadata.md) — The abstract superclass for specifying metadata about a network protocol.
- [antecedent](antecedent.md) — An optional message context that must be sent before the context you are sending.
- [expirationMilliseconds](expirationmilliseconds.md) — A number of milliseconds after which sending the data associated with this context must begin, otherwise the data is discarded.
- [relativePriority](relativepriority.md) — A relative value of priority used to reorder contexts when sending.
