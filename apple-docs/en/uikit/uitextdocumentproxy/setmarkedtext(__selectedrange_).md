---
title: 'setMarkedText(_:selectedRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdocumentproxy/setmarkedtext(_:selectedrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdocumentproxy/setmarkedtext(_:selectedrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdocumentproxy/setmarkedtext%28_%3Aselectedrange%3A%29.json'
content_hash: 'sha256:69a2f03435eb28e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDocumentProxy](../uitextdocumentproxy.md)

# setMarkedText(_:selectedRange:)

<sub>Instance Method</sub>

Inserts the provided text and marks it to indicate that it’s part of an active input session.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setMarkedText(_ markedText: String, selectedRange: NSRange)
```

## Discussion

Setting marked text either replaces the existing marked text or, if none is present, inserts it in place of the current selection.

## See Also

### Managing marked text

- [- unmarkText](<unmarktext().md>) — Unmarks the currently marked text.
