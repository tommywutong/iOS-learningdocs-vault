---
title: 'AttributedTextSelection.Indices.insertionPoint(_:)'
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextselection/indices/insertionpoint(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextselection/indices/insertionpoint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextselection/indices/insertionpoint%28_%3A%29.json'
content_hash: 'sha256:dac936508916a3e8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [AttributedTextSelection](../../attributedtextselection.md) · [Indices](../indices.md)

# AttributedTextSelection.Indices.insertionPoint(_:)

<sub>Case</sub>

The index of a single insertion point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case insertionPoint(AttributedString.Index)
```

## Discussion

The an insertion point at the `startIndex` of an attributed string is equivalent to a caret preceding the first character. An insertion point using `endIndex` is valid. It is equivalent to a caret located after the last character in the attributed string.
