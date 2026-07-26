---
title: 'storeBytes(of:toUncheckedByteOffset:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablerawspan/storebytes(of:touncheckedbyteoffset:as:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/storebytes(of:touncheckedbyteoffset:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/storebytes%28of%3Atouncheckedbyteoffset%3Aas%3A%29.json'
content_hash: 'sha256:db571a0ce490658a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# storeBytes(of:toUncheckedByteOffset:as:)

<sub>Instance Method</sub>

Stores the given value’s bytes into the span’s raw memory at the specified byte offset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func storeBytes<T>(of value: T, toUncheckedByteOffset offset: Int, as type: T.Type) where T : BitwiseCopyable
```

## Parameters

- `value` — The value to store as raw bytes.

- `offset` — The offset from the start of the span, in bytes. `offset` must be nonnegative.

- `type` — The type of `value`.

## Discussion

This function does not validate `offset`; this is an unsafe operation.
