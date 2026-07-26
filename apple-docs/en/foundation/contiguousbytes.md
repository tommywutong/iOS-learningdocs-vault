---
title: ContiguousBytes
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/contiguousbytes
source_url: 'https://developer.apple.com/documentation/foundation/contiguousbytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/contiguousbytes.json'
content_hash: 'sha256:5e9974f9a8f3000a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ContiguousBytes

<sub>Protocol</sub>

A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ContiguousBytes : ~Copyable, ~Escapable
```

## Relationships

- **Conforming Types**: [Data](data.md)

## Topics

### Accessing Underlying Storage

- [withUnsafeBytes(_:)](<contiguousbytes/withunsafebytes(__).md>) — Calls the given closure with a pointer to the underlying bytes of the type’s contiguous storage.

### Instance Methods

- [withBytes(_:)](<contiguousbytes/withbytes(__).md>) — Calls the given closure with the contents of underlying storage. _(beta)_

## See Also

### Binary Data

- [Data](data.md) — A byte buffer in memory.
- [DataProtocol](dataprotocol.md) — A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.
- [MutableDataProtocol](mutabledataprotocol.md) — A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.
