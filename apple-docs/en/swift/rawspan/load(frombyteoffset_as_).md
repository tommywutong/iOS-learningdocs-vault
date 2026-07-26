---
title: 'load(fromByteOffset:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawspan/load(frombyteoffset:as:)'
source_url: 'https://developer.apple.com/documentation/swift/rawspan/load(frombyteoffset:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan/load%28frombyteoffset%3Aas%3A%29.json'
content_hash: 'sha256:51998c6cdf665c97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawSpan](../rawspan.md)

# load(fromByteOffset:as:)

<sub>Instance Method</sub>

Returns a value constructed from the raw memory at the specified offset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func load<T>(fromByteOffset offset: Int, as type: T.Type) -> T where T : ConvertibleFromBytes
```

## Parameters

- `offset` — The offset from the beginning of this span, in bytes. `offset` must be nonnegative.

- `type` — The type of the instance to create.

## Return Value

A new value of type `T`, read from `offset`.

## Discussion

The range of bytes required to construct a value of type `T` starting at `offset` must be completely within the span. `offset` is not required to be aligned for `T`.
