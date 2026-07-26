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
doc_path: '/documentation/swift/mutablespan/extracting(_:)-bphj'
source_url: 'https://developer.apple.com/documentation/swift/mutablespan/extracting(_:)-bphj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablespan/extracting%28_%3A%29-bphj.json'
content_hash: 'sha256:99321e78e23e4b85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableSpan](../mutablespan.md)

# extracting(_:)

<sub>Instance Method</sub>

Constructs a new span over the items within the supplied range of indices within this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func extracting(_ bounds: Range<MutableSpan<Element>.Index>) -> MutableSpan<Element>
```

## Parameters

- `bounds` — A valid range of indices. Every index in this range must be within the bounds of this `MutableSpan`.

## Return Value

A `MutableSpan` over the items within `bounds`.

## Discussion

The returned span represents a mutation of this span.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> [!abstract] Complexity
> O(1)
