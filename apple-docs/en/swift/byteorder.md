---
title: ByteOrder
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/byteorder
source_url: 'https://developer.apple.com/documentation/swift/byteorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/byteorder.json'
content_hash: 'sha256:7607dc8b1b52f5a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ByteOrder

<sub>Enumeration</sub>

A byte ordering in memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum ByteOrder
```

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [Equatable](equatable.md), [Hashable](hashable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<byteorder/==(____).md>) — Returns a Boolean value indicating whether two values are equal. _(beta)_

### Enumeration Cases

- [ByteOrder.bigEndian](byteorder/bigendian.md) — Bytes are ordered with the most significant bits starting at the lowest memory address. _(beta)_
- [ByteOrder.littleEndian](byteorder/littleendian.md) — Bytes are ordered with the least significant bits starting at the lowest memory address. _(beta)_

### Instance Properties

- [hashValue](byteorder/hashvalue.md) — The hash value. _(beta)_

### Instance Methods

- [hash(into:)](<byteorder/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher. _(beta)_

### Type Properties

- [native](byteorder/native.md) — The native byte ordering for the runtime target. _(beta)_

### Default Implementations

- [Equatable Implementations](byteorder/equatable-implementations.md)

## See Also

### Safe Access to Raw Bytes

- [FullyInhabited](fullyinhabited.md) — A protocol for types whose memory can safely be written as or read from raw bytes.
- [ConvertibleFromBytes](convertiblefrombytes.md) — A protocol for types whose memory can safely be populated from raw bytes, resulting in a valid instance.
- [ConvertibleToBytes](convertibletobytes.md) — A protocol for types whose memory can safely be read as individual raw bytes.
- [bitCast(_:to:)](<bitcast(__to_).md>) — Returns the bits of the given instance, interpreted as having the specified type.
