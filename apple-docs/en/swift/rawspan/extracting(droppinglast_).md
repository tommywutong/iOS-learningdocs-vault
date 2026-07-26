---
title: 'extracting(droppingLast:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawspan/extracting(droppinglast:)'
source_url: 'https://developer.apple.com/documentation/swift/rawspan/extracting(droppinglast:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan/extracting%28droppinglast%3A%29.json'
content_hash: 'sha256:2f59616640331db7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawSpan](../rawspan.md)

# extracting(droppingLast:)

<sub>Instance Method</sub>

Returns a span over all but the given number of trailing bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extracting(droppingLast k: Int) -> RawSpan
```

## Parameters

- `k` — The number of bytes to drop off the end of the span. `k` must be greater than or equal to zero.

## Return Value

A span leaving off the specified number of bytes at the end.

## Discussion

If the number of bytes to drop exceeds the number of bytes in the span, the result is an empty span.

The returned span’s first byte is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> [!abstract] Complexity
> O(1)
