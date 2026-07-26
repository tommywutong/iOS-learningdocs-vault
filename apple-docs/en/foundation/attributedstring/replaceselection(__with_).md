---
title: 'replaceSelection(_:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/replaceselection(_:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/replaceselection(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/replaceselection%28_%3Awith%3A%29.json'
content_hash: 'sha256:cd94cda1bca90731'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# replaceSelection(_:with:)

<sub>Instance Method</sub>

Replace the selection with new attributed content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceSelection(_ selection: inout AttributedTextSelection, with newContent: some AttributedStringProtocol)
```

## Discussion

In the case the selection is an insertion point, the `newContent` gets inserted at the caret location and the caret is moved to after the new content.

In the case where the selection spans one or multiple characters, those characters are removed and the new content is inserted at location of the first selected character.
