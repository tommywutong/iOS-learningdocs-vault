---
title: 'storeBytes(of:toByteOffset:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablerawspan/storebytes(of:tobyteoffset:as:)-1afju'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/storebytes(of:tobyteoffset:as:)-1afju'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/storebytes%28of%3Atobyteoffset%3Aas%3A%29-1afju.json'
content_hash: 'sha256:85513bb836323f25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# storeBytes(of:toByteOffset:as:)

<sub>Instance Method</sub>

Stores the given value’s bytes to the specified offset into the span’s memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func storeBytes<T>(of value: T, toByteOffset offset: Int, as type: T.Type) where T : BitwiseCopyable, T : ConvertibleToBytes
```

## Parameters

- `value` — The value to store as raw bytes.

- `offset` — The offset in bytes into the span’s memory at which to begin writing the bytes from the value.

- `type` — The type of the instance to store.

## Discussion

The range of bytes required to store a value of type `T` starting at byte offset `offset` must be completely within the span.
