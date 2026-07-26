---
title: 'extracting(last:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/span/extracting(last:)'
source_url: 'https://developer.apple.com/documentation/swift/span/extracting(last:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/span/extracting%28last%3A%29.json'
content_hash: 'sha256:9c6e9086cd8dfbbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Span](../span.md)

# extracting(last:)

<sub>Instance Method</sub>

Returns a span containing the trailing elements of the span, up to the given maximum length.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func extracting(last maxLength: Int) -> Span<Element>
```

## Parameters

- `maxLength` — The maximum number of elements to return. `maxLength` must be greater than or equal to zero.

## Return Value

A span with at most `maxLength` elements.

## Discussion

If the maximum length exceeds the length of this span, the result contains all the elements.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> [!abstract] Complexity
> O(1)
