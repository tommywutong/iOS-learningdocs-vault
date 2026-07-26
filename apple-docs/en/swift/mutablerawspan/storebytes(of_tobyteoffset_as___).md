---
title: 'storeBytes(of:toByteOffset:as:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/mutablerawspan/storebytes(of:tobyteoffset:as:_:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/storebytes(of:tobyteoffset:as:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/storebytes%28of%3Atobyteoffset%3Aas%3A_%3A%29.json'
content_hash: 'sha256:e762133d37596113'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# storeBytes(of:toByteOffset:as:_:)

<sub>Instance Method</sub>

Stores the given value’s bytes to the specified offset into the span’s memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func storeBytes<T>(of value: T, toByteOffset offset: Int, as type: T.Type, _ byteOrder: ByteOrder) where T : BitwiseCopyable, T : ConvertibleToBytes, T : FixedWidthInteger
```

## Parameters

- `value` — The value to store as raw bytes.

- `offset` — The offset in bytes into the span’s memory at which to begin writing the bytes from the value.

- `type` — The type of the instance to store.

- `byteOrder` — The order in which the bytes will be encoded to the span.

## Discussion

The range of bytes required to store a value of type `T` starting at byte offset `offset` must be completely within the span. `offset` is not required to be aligned for `T`.
