---
title: 'append(_:as:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/outputrawspan/append(_:as:_:)'
source_url: 'https://developer.apple.com/documentation/swift/outputrawspan/append(_:as:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputrawspan/append%28_%3Aas%3A_%3A%29.json'
content_hash: 'sha256:2c48d74152306932'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputRawSpan](../outputrawspan.md)

# append(_:as:_:)

<sub>Instance Method</sub>

Appends the given value’s bytes to this span’s bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append<T>(_ value: T, as type: T.Type, _ byteOrder: ByteOrder) where T : BitwiseCopyable, T : ConvertibleToBytes, T : FixedWidthInteger
```

## Parameters

- `value` — The value to store as raw bytes.

- `type` — The type of the instance to store.

- `byteOrder` — The order in which the bytes will be encoded to the span.

## Discussion

There must be at least `MemoryLayout<T>.size` bytes available in the span.
