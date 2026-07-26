---
title: markedTextStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/markedtextstyle
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/markedtextstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/markedtextstyle.json'
content_hash: 'sha256:571e63e86af3e149'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# markedTextStyle

<sub>Instance Property</sub>

A dictionary of attributes that describes how to draw marked text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var markedTextStyle: [NSAttributedString.Key : Any]? { get set }
```

## Discussion

Marked text requires a unique visual treatment when displayed to users. See [Style dictionary keys](../style-dictionary-keys.md) for descriptions of the valid keys and values for this dictionary.

## See Also

### Working with marked and selected text

- [selectedTextRange](selectedtextrange.md) — The range of selected text in a document.
- [markedTextRange](markedtextrange.md) — The range of currently marked text in a document.
- [- setMarkedText:selectedRange:](<setmarkedtext(__selectedrange_).md>) — Inserts the provided text and marks it to indicate that it is part of an active input session.
- [- setAttributedMarkedText:selectedRange:](<setattributedmarkedtext(__selectedrange_).md>) — Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [- unmarkText](<unmarktext().md>) — Unmarks the currently marked text.
- [selectionAffinity](selectionaffinity.md) — The desired location for the insertion point.
