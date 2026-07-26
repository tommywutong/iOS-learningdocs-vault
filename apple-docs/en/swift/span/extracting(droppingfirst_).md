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
doc_path: '/documentation/swift/span/extracting(droppingfirst:)'
source_url: 'https://developer.apple.com/documentation/swift/span/extracting(droppingfirst:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/span/extracting%28droppingfirst%3A%29.json'
content_hash: 'sha256:21e1988fc018e4c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Span](../span.md)

# extracting(droppingFirst:)

<sub>Instance Method</sub>

Returns a span over all but the given number of initial elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extracting(droppingFirst k: Int) -> Span<Element>
```

## Parameters

- `k` — The number of elements to drop from the beginning of the span. `k` must be greater than or equal to zero.

## Return Value

A span starting after the specified number of elements.

## Discussion

If the number of elements to drop exceeds the number of elements in the span, the result is an empty span.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> [!abstract] Complexity
> O(1)
