---
title: 'setAttributedMarkedText(_:selectedRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/setattributedmarkedtext(_:selectedrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/setattributedmarkedtext(_:selectedrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/setattributedmarkedtext%28_%3Aselectedrange%3A%29.json'
content_hash: 'sha256:7460657796ef5b40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# setAttributedMarkedText(_:selectedRange:)

<sub>Instance Method</sub>

Inserts the provided styled text and marks it to indicate that it is part of an active input session.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func setAttributedMarkedText(_ markedText: NSAttributedString?, selectedRange: NSRange)
```

## See Also

### Working with marked and selected text

- [selectedTextRange](selectedtextrange.md) — The range of selected text in a document.
- [markedTextRange](markedtextrange.md) — The range of currently marked text in a document.
- [markedTextStyle](markedtextstyle.md) — A dictionary of attributes that describes how to draw marked text.
- [- setMarkedText:selectedRange:](<setmarkedtext(__selectedrange_).md>) — Inserts the provided text and marks it to indicate that it is part of an active input session.
- [- unmarkText](<unmarktext().md>) — Unmarks the currently marked text.
- [selectionAffinity](selectionaffinity.md) — The desired location for the insertion point.
