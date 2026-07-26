---
title: 'append(_:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/outputrawspan/append(_:as:)-89j87'
source_url: 'https://developer.apple.com/documentation/swift/outputrawspan/append(_:as:)-89j87'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputrawspan/append%28_%3Aas%3A%29-89j87.json'
content_hash: 'sha256:d55600a3f9ed963f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputRawSpan](../outputrawspan.md)

# append(_:as:)

<sub>Instance Method</sub>

Appends the given value’s bytes to this span’s bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append<T>(_ value: T, as type: T.Type) where T : BitwiseCopyable, T : ConvertibleToBytes
```

## Parameters

- `value` — The value to store as raw bytes.

- `type` — The type of the instance to store.

## Discussion

There must be at least `MemoryLayout<T>.size` bytes available in the span.
