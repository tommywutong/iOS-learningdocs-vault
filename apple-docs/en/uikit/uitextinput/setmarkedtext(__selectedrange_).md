---
title: 'setMarkedText(_:selectedRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/setmarkedtext(_:selectedrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/setmarkedtext(_:selectedrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/setmarkedtext%28_%3Aselectedrange%3A%29.json'
content_hash: 'sha256:3294ba2f30d6838c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# setMarkedText(_:selectedRange:)

<sub>Instance Method</sub>

Inserts the provided text and marks it to indicate that it is part of an active input session.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setMarkedText(_ markedText: String?, selectedRange: NSRange)
```

## Parameters

- `markedText` — The text to be marked.

- `selectedRange` — A range within `markedText` that indicates the current selection. This range is always relative to `markedText`.

## Discussion

Setting marked text either replaces the existing marked text or, if none is present, inserts it in place of the current selection.

## See Also

### Working with marked and selected text

- [selectedTextRange](selectedtextrange.md) — The range of selected text in a document.
- [markedTextRange](markedtextrange.md) — The range of currently marked text in a document.
- [markedTextStyle](markedtextstyle.md) — A dictionary of attributes that describes how to draw marked text.
- [- setAttributedMarkedText:selectedRange:](<setattributedmarkedtext(__selectedrange_).md>) — Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [- unmarkText](<unmarktext().md>) — Unmarks the currently marked text.
- [selectionAffinity](selectionaffinity.md) — The desired location for the insertion point.
