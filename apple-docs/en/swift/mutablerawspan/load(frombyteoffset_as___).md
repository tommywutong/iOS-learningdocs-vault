---
title: 'load(fromByteOffset:as:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/mutablerawspan/load(frombyteoffset:as:_:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/load(frombyteoffset:as:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/load%28frombyteoffset%3Aas%3A_%3A%29.json'
content_hash: 'sha256:9e35137a83fd5a0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# load(fromByteOffset:as:_:)

<sub>Instance Method</sub>

Returns a value constructed from the raw memory at the specified offset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func load<T>(fromByteOffset offset: Int, as type: T.Type, _ byteOrder: ByteOrder) -> T where T : ConvertibleFromBytes, T : FixedWidthInteger
```

## Parameters

- `offset` — The offset from the beginning of this span, in bytes. `offset` must be nonnegative.

- `type` — The type of the instance to create.

- `byteOrder` — The order in which the bytes will be decoded.

## Return Value

A new value of type `T`, read from `offset`.

## Discussion

The range of bytes required to construct a value of type `T` starting at `offset` must be completely within the span. `offset` is not required to be aligned for `T`.
