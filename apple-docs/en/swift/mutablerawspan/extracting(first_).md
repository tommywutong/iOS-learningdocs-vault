---
title: 'extracting(first:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablerawspan/extracting(first:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan/extracting(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan/extracting%28first%3A%29.json'
content_hash: 'sha256:7b66d29cdcf05b64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRawSpan](../mutablerawspan.md)

# extracting(first:)

<sub>Instance Method</sub>

Returns a span containing the initial bytes of this span, up to the specified maximum length.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func extracting(first maxLength: Int) -> MutableRawSpan
```

## Parameters

- `maxLength` — The maximum number of bytes to return. `maxLength` must be greater than or equal to zero.

## Return Value

A span with at most `maxLength` bytes.

## Discussion

If the maximum length exceeds the length of this span, the result contains all the bytes.

The returned span represents a mutation of this span.

The returned span’s first item is always at offset 0; unlike buffer slices, extracted spans do not share their indices with the span from which they are extracted.

> [!abstract] Complexity
> O(1)
