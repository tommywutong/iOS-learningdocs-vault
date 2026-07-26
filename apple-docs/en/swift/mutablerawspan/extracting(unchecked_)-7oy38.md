---
title: 'extracting(unchecked:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablerawspan/extracting(unchecked:)-7oy38'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/extracting(unchecked:)-7oy38'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/extracting%28unchecked%3A%29-7oy38.json'
content_hash: 'sha256:9e00926d34edd67d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# extracting(unchecked:)

<sub>Instance Method</sub>

Constructs a new span over the bytes within the supplied range of positions within this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func extracting(unchecked bounds: Range<Int>) -> MutableRawSpan
```

## Parameters

- `bounds` — A valid range of positions. Every position in this range must be within the bounds of this `MutableRawSpan`.

## Return Value

A `MutableRawSpan` over the bytes within `bounds`.

## Discussion

The returned span represents a mutation of this span.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

This function does not validate `bounds`; this is an unsafe operation.

> [!abstract] Complexity
> O(1)
