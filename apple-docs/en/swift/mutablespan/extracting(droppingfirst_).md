---
title: 'extracting(droppingFirst:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablespan/extracting(droppingfirst:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablespan/extracting(droppingfirst:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablespan/extracting%28droppingfirst%3A%29.json'
content_hash: 'sha256:87c1febb82668f7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableSpan](../mutablespan.md)

# extracting(droppingFirst:)

<sub>Instance Method</sub>

Returns a span over all but the given number of initial elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func extracting(droppingFirst k: Int) -> MutableSpan<Element>
```

## Parameters

- `k` — The number of elements to drop from the beginning of the span. `k` must be greater than or equal to zero.

## Return Value

A span starting after the specified number of elements.

## Discussion

If the number of elements to drop exceeds the number of elements in the span, the result is an empty span.

The returned span represents a mutation of this span.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> [!abstract] Complexity
> O(1)
