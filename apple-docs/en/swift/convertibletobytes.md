---
title: ConvertibleToBytes
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/convertibletobytes
source_url: 'https://developer.apple.com/documentation/swift/convertibletobytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/convertibletobytes.json'
content_hash: 'sha256:2114265ed9493632'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ConvertibleToBytes

<sub>Protocol</sub>

A protocol for types whose memory can safely be read as individual raw bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ConvertibleToBytes
```

## Overview

A type can conform to ConvertibleToBytes if its memory representation includes no padding. The sum of the size of its stored properties must be equal to its stride.

A type that conforms to ConvertibleToBytes must have:

- one or more stored properties,
- all of its stored properties have a type which conforms to `ConvertibleToBytes`,
- its stored properties are stored contiguously in memory, with no padding,
- none of its values disregards a subset of its bytes, making most enums ineligible.

## Relationships

- **Conforming Types**: [Bool](bool.md), [ClosedRange](closedrange.md), [CollectionOfOne](collectionofone.md), [Double](double.md), [Duration](duration.md), [Float](float.md), [Float16](float16.md), [InlineArray](inlinearray.md), [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [ObjectIdentifier](objectidentifier.md), [OpaquePointer](opaquepointer.md), [PartialRangeFrom](partialrangefrom.md), [Iterator](partialrangefrom/iterator.md), [PartialRangeThrough](partialrangethrough.md), [PartialRangeUpTo](partialrangeupto.md), [Range](range.md), [UInt](uint.md), [UInt128](uint128.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md), [UnsafeBufferPointer](unsafebufferpointer.md), [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md), [UnsafeMutablePointer](unsafemutablepointer.md), [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md), [UnsafeMutableRawPointer](unsafemutablerawpointer.md), [UnsafePointer](unsafepointer.md), [UnsafeRawBufferPointer](unsaferawbufferpointer.md), [UnsafeRawPointer](unsaferawpointer.md)

## See Also

### Safe Access to Raw Bytes

- [FullyInhabited](fullyinhabited.md) — A protocol for types whose memory can safely be written as or read from raw bytes.
- [ConvertibleFromBytes](convertiblefrombytes.md) — A protocol for types whose memory can safely be populated from raw bytes, resulting in a valid instance.
- [ByteOrder](byteorder.md) — A byte ordering in memory. _(beta)_
- [bitCast(_:to:)](<bitcast(__to_).md>) — Returns the bits of the given instance, interpreted as having the specified type.
