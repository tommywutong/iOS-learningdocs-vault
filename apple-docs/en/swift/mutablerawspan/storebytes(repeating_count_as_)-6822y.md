---
title: 'storeBytes(repeating:count:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablerawspan/storebytes(repeating:count:as:)-6822y'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/storebytes(repeating:count:as:)-6822y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/storebytes%28repeating%3Acount%3Aas%3A%29-6822y.json'
content_hash: 'sha256:e740f3bd40ee412b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# storeBytes(repeating:count:as:)

<sub>Instance Method</sub>

Stores the given value’s bytes repeatedly into this span’s memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func storeBytes<T>(repeating repeatedValue: T, count: Int, as type: T.Type) where T : BitwiseCopyable
```

## Parameters

- `repeatedValue` — The value to store as raw bytes.

- `count` — The number of copies of `repeatedValue` to store into this span.

- `type` — The type of the instance to store repeatedly.

## Discussion

There must be at least `count * MemoryLayout<T>.stride` bytes available in the span.
