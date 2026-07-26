---
title: selectedTextRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearching-3wkjv/selectedtextrange
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/selectedtextrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/selectedtextrange.json'
content_hash: 'sha256:05632d2e1a3634a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# selectedTextRange

<sub>Instance Property</sub>

The range of selected text in a document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var selectedTextRange: UITextRange? { get }
```

## Discussion

If the text range has a length, it indicates the currently selected text. If it has zero length, it indicates the caret (insertion point). If the text-range object is `nil`, it indicates that there’s no current selection.

## See Also

### Identifying selected text

- [selectedTextSearchDocument](selectedtextsearchdocument.md) — The object that uniquely identifies the specific document with selected text.
