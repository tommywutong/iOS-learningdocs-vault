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
doc_path: '/documentation/swift/mutablespan/extracting(_:)-80srp'
source_url: 'https://developer.apple.com/documentation/swift/mutablespan/extracting(_:)-80srp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablespan/extracting%28_%3A%29-80srp.json'
content_hash: 'sha256:6ead4b01d8faa5fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableSpan](../mutablespan.md)

# extracting(_:)

<sub>Instance Method</sub>

Constructs a new span over all the items of this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func extracting(_: UnboundedRange) -> MutableSpan<Element>
```

## Return Value

A `MutableSpan` over all the items of this span.

## Discussion

The returned span represents a mutation of this span.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> [!abstract] Complexity
> O(1)
