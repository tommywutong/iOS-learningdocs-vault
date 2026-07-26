---
title: DataProtocol
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/dataprotocol
source_url: 'https://developer.apple.com/documentation/foundation/dataprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dataprotocol.json'
content_hash: 'sha256:e5b24452e87a5087'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# DataProtocol

<sub>Protocol</sub>

A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DataProtocol : RandomAccessCollection where Self.Element == UInt8, Self.SubSequence : DataProtocol
```

## Relationships

- **Inherits From**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sequence](../swift/sequence.md)

- **Inherited By**: [MutableDataProtocol](mutabledataprotocol.md)

- **Conforming Types**: [Data](data.md), [NSData](nsdata.md), [NSMutableData](nsmutabledata.md), [NSPurgeableData](nspurgeabledata.md)

## Topics

### Accessing Backing Storage

- [regions](dataprotocol/regions-swift.property.md) — A collection of buffers that make up the whole of the type conforming to a data protocol.
- [Regions](dataprotocol/regions-swift.associatedtype.md) — A type that represents a collection of contiguous parts that make up the type conforming to a data protocol.

### Copying Underlying Bytes

- [copyBytes(to:)](<dataprotocol/copybytes(to_)-52wps.md>) — Copies the bytes of data from the type into a typed memory buffer.
- [copyBytes(to:)](<dataprotocol/copybytes(to_)-3mk27.md>) — Copies the bytes of data from the type into a raw memory buffer.
- [copyBytes(to:count:)](<dataprotocol/copybytes(to_count_)-6krsm.md>) — Copies the provided number of bytes from the start of the type into  a typed memory buffer.
- [copyBytes(to:count:)](<dataprotocol/copybytes(to_count_)-29t5.md>) — Copies the provided number of bytes from the start of the type into a raw memory buffer.
- [copyBytes(to:from:)](<dataprotocol/copybytes(to_from_)-1ol47.md>) — Copies a range of the bytes from the type into a typed memory buffer.
- [copyBytes(to:from:)](<dataprotocol/copybytes(to_from_)-1y839.md>) — Copies a range of the bytes from the type into a raw memory buffer.

### Searching Within Data

- [firstRange(of:)](<dataprotocol/firstrange(of_).md>) — Returns the first found range of the type’s data buffer.
- [firstRange(of:in:)](<dataprotocol/firstrange(of_in_).md>) — Returns the first found range of the type’s data buffer.
- [lastRange(of:)](<dataprotocol/lastrange(of_).md>) — Returns the last found range of the type’s data buffer.
- [lastRange(of:in:)](<dataprotocol/lastrange(of_in_).md>) — Returns the last found range of the type’s data buffer.

## See Also

### Binary Data

- [Data](data.md) — A byte buffer in memory.
- [MutableDataProtocol](mutabledataprotocol.md) — A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.
- [ContiguousBytes](contiguousbytes.md) — A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.
