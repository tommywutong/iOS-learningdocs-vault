---
title: 'extracting(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablerawspan/extracting(_:)-7d5f1'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/extracting(_:)-7d5f1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/extracting%28_%3A%29-7d5f1.json'
content_hash: 'sha256:22735080c67bf8c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# extracting(_:)

<sub>Instance Method</sub>

Constructs a new span over all the bytes of this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func extracting(_: UnboundedRange) -> MutableRawSpan
```

## Return Value

A `MutableRawSpan` over all the bytes of this span.

## Discussion

The returned span represents a mutation of this span.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> [!abstract] Complexity
> O(1)
