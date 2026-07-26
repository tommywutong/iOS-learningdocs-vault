---
title: 'init(identifier:expiration:priority:isFinal:antecedent:metadata:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/contentcontext/init(identifier:expiration:priority:isfinal:antecedent:metadata:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/contentcontext/init(identifier:expiration:priority:isfinal:antecedent:metadata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/contentcontext/init%28identifier%3Aexpiration%3Apriority%3Aisfinal%3Aantecedent%3Ametadata%3A%29.json'
content_hash: 'sha256:4dfa3f788a1dbe08'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [ContentContext](../contentcontext.md)

# init(identifier:expiration:priority:isFinal:antecedent:metadata:)

<sub>Initializer</sub>

Initializes a custom message context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(identifier: String, expiration: UInt64 = 0, priority: Double = 0.5, isFinal: Bool = false, antecedent: NWConnection.ContentContext? = nil, metadata: [NWProtocolMetadata]? = [])
```

## See Also

### Creating Custom Send Contexts

- [identifier](identifier.md) — The identifier of the message, used for debugging.
- [protocolMetadata](protocolmetadata.md) — An array of protocol metadata used to configure per-message or per-packet properties.
- [NWProtocolMetadata](../../nwprotocolmetadata.md) — The abstract superclass for specifying metadata about a network protocol.
- [antecedent](antecedent.md) — An optional message context that must be sent before the context you are sending.
- [expirationMilliseconds](expirationmilliseconds.md) — A number of milliseconds after which sending the data associated with this context must begin, otherwise the data is discarded.
- [relativePriority](relativepriority.md) — A relative value of priority used to reorder contexts when sending.
