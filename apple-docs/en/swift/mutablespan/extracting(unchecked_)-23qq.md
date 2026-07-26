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
doc_path: '/documentation/swift/mutablespan/extracting(unchecked:)-23qq'
source_url: 'https://developer.apple.com/documentation/swift/mutablespan/extracting(unchecked:)-23qq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablespan/extracting%28unchecked%3A%29-23qq.json'
content_hash: 'sha256:839cd706543d43b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableSpan](../mutablespan.md)

# extracting(unchecked:)

<sub>Instance Method</sub>

Constructs a new span over the items within the supplied range of indices within this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func extracting(unchecked bounds: Range<MutableSpan<Element>.Index>) -> MutableSpan<Element>
```

## Parameters

- `bounds` — A valid range of indices. Every index in this range must be within the bounds of this `MutableSpan`.

## Return Value

A `MutableSpan` over the items within `bounds`.

## Discussion

The returned span represents a mutation of this span.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

This function does not validate `bounds`; this is an unsafe operation.

> [!abstract] Complexity
> O(1)
