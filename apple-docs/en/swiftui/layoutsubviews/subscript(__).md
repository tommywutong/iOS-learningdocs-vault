---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layoutsubviews/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/layoutsubviews/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutsubviews/subscript%28_%3A%29.json'
content_hash: 'sha256:1d0f1a3a58d6a80f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutSubviews](../layoutsubviews.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Gets the subview proxies in the specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(bounds: Range<Int>) -> LayoutSubviews { get }
```

## See Also

### Accessing subviews

- [startIndex](startindex.md) — The index of the first subview.
- [endIndex](endindex.md) — An index that’s one higher than the last subview.
- [Element](element.md) — A type that contains a proxy value.
- [Index](index.md) — A type that you can use to index proxy values.
- [SubSequence](subsequence.md) — A type that contains a subsequence of proxy values.
