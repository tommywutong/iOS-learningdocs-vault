---
title: 'attributes(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextselection/attributes(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextselection/attributes(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextselection/attributes%28in%3A%29.json'
content_hash: 'sha256:08505927d8493c37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextSelection](../attributedtextselection.md)

# attributes(in:)

<sub>Instance Method</sub>

Obtain a lazy sequence of all attribute values the selection has in a given text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attributes(in text: AttributedString) -> AttributedTextSelection.Attributes<AttributedString>
```

## Discussion

The attribute values of a selection are the attribute values of each run that is fully or partially selected, or the typing attributes in the case the selection is an insertion point.

By default, the sequence contains the attribute container for every run or the typing attributes. Use the [Attributes](attributes.md)’ subscript to obtain only the values for a single attribute:

```swift
selection.attributes(in: text)[\.foregroundColor].contains(.red)
```
