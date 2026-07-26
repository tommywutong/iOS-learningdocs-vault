---
title: 'storeBytes(repeating:count:as:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/mutablerawspan/storebytes(repeating:count:as:_:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/storebytes(repeating:count:as:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/storebytes%28repeating%3Acount%3Aas%3A_%3A%29.json'
content_hash: 'sha256:6995102bdac23990'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# storeBytes(repeating:count:as:_:)

<sub>Instance Method</sub>

Stores the given value’s bytes repeatedly into this span’s memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func storeBytes<T>(repeating repeatedValue: T, count: Int, as type: T.Type, _ byteOrder: ByteOrder) where T : BitwiseCopyable, T : ConvertibleToBytes, T : FixedWidthInteger
```

## Parameters

- `repeatedValue` — The value to store as raw bytes.

- `count` — The number of copies of `repeatedValue` to store into this span.

- `type` — The type of the instance to store repeatedly.

- `byteOrder` — The order in which the bytes will be encoded to the span.

## Discussion

There must be at least `count * MemoryLayout<T>.stride` bytes available in the span.
