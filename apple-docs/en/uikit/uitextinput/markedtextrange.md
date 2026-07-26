---
title: markedTextRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/markedtextrange
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/markedtextrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/markedtextrange.json'
content_hash: 'sha256:11c02f43c0c25447'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# markedTextRange

<sub>Instance Property</sub>

The range of currently marked text in a document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var markedTextRange: UITextRange? { get }
```

## Discussion

If there is no marked text, the value of the property is `nil`. Marked text is provisionally inserted text that requires user confirmation; it occurs in multistage text input. The current selection, which can be a caret or an extended range, always occurs within the marked text.

## See Also

### Working with marked and selected text

- [selectedTextRange](selectedtextrange.md) — The range of selected text in a document.
- [markedTextStyle](markedtextstyle.md) — A dictionary of attributes that describes how to draw marked text.
- [- setMarkedText:selectedRange:](<setmarkedtext(__selectedrange_).md>) — Inserts the provided text and marks it to indicate that it is part of an active input session.
- [- setAttributedMarkedText:selectedRange:](<setattributedmarkedtext(__selectedrange_).md>) — Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [- unmarkText](<unmarktext().md>) — Unmarks the currently marked text.
- [selectionAffinity](selectionaffinity.md) — The desired location for the insertion point.
