---
title: MutableDataProtocol
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/mutabledataprotocol
source_url: 'https://developer.apple.com/documentation/foundation/mutabledataprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/mutabledataprotocol.json'
content_hash: 'sha256:8e63dac9aaf2eee9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# MutableDataProtocol

<sub>Protocol</sub>

A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MutableDataProtocol : DataProtocol, MutableCollection, RangeReplaceableCollection
```

## Relationships

- **Inherits From**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [DataProtocol](dataprotocol.md), [MutableCollection](../swift/mutablecollection.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [RangeReplaceableCollection](../swift/rangereplaceablecollection.md), [Sequence](../swift/sequence.md)

- **Conforming Types**: [Data](data.md)

## Topics

### Resetting Backing Storage

- [resetBytes(in:)](<mutabledataprotocol/resetbytes(in_).md>) — Replaces the contents of the data buffer with zeros for the provided range.

## See Also

### Binary Data

- [Data](data.md) — A byte buffer in memory.
- [DataProtocol](dataprotocol.md) — A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.
- [ContiguousBytes](contiguousbytes.md) — A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.
