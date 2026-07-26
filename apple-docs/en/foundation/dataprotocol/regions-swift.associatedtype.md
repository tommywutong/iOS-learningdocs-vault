---
title: Regions
framework: Foundation
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/dataprotocol/regions-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol/regions-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol/regions-swift.associatedtype.json'
content_hash: 'sha256:840a040c29ff3eb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DataProtocol](../dataprotocol.md)

# Regions

<sub>Associated Type</sub>

A type that represents a collection of contiguous parts that make up the type conforming to a data protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Regions : BidirectionalCollection where Self.Regions.Element : ContiguousBytes, Self.Regions.Element : DataProtocol, Self.Regions.Element.SubSequence : ContiguousBytes
```

## See Also

### Accessing Backing Storage

- [regions](regions-swift.property.md) — A collection of buffers that make up the whole of the type conforming to a data protocol.
