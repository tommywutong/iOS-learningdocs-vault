---
title: span
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/span
source_url: 'https://developer.apple.com/documentation/swift/array/span'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/span.json'
content_hash: 'sha256:20d55e03610b9b08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# span

<sub>Instance Property</sub>

A span over the elements of this array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var span: Span<Element> { get }
```

## Return Value

A `Span` over the elements of this array.

## Discussion

> [!note] Note
> On Apple platforms, this property copies bridged `NSArray` instances into contiguous storage on first access and caches the result. Subsequent calls can reuse the cached copy.

> [!abstract] Complexity
> O(1) for native arrays, amortized O(1) for bridged arrays.
