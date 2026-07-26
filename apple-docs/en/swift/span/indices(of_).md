---
title: 'indices(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/span/indices(of:)'
source_url: 'https://developer.apple.com/documentation/swift/span/indices(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/span/indices%28of%3A%29.json'
content_hash: 'sha256:b6ab646a7e6e2a30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Span](../span.md)

# indices(of:)

<sub>Instance Method</sub>

Returns the indices within this span where the memory represented by other is located, or nil if other is not located within this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func indices(of other: borrowing Span<Element>) -> Range<Span<Element>.Index>?
```

## Parameters

- `other` — A span that may be a subrange of `self`

## Return Value

A range of indices within `self`, or `nil`.
